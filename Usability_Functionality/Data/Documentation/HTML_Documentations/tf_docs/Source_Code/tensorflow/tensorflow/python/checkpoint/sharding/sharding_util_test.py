# Copyright 2023 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================
"""Tests for checkpoint sharding structures and utilities."""


from typing import Sequence

from tensorflow.python.checkpoint import checkpoint
from tensorflow.python.checkpoint import graph_view
from tensorflow.python.checkpoint.sharding import sharding_policies
from tensorflow.python.checkpoint.sharding import sharding_util
from tensorflow.python.eager import remote
from tensorflow.python.eager import test
from tensorflow.python.framework import dtypes
from tensorflow.python.framework import ops
from tensorflow.python.framework import tensor as tensor_lib
from tensorflow.python.module import module
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import resource_variable_ops
from tensorflow.python.ops import variables
from tensorflow.python.training import server_lib
from tensorflow.python.training.saving import saveable_object


class ShardingUtilTest(test.TestCase):

  def _get_shardable_tensors(self, root):
    serialized_tensors, _, _, _ = (
        checkpoint.TrackableSaver(graph_view.ObjectGraphView(root))
        ._gather_serialized_tensors(None))

    shardable_tensors = []
    for obj, tensor_dict in serialized_tensors.items():
      # Divide tensor_dict by device.
      for checkpoint_key, tensor_slice_dict in tensor_dict.items():
        if not isinstance(tensor_slice_dict, dict):
          # Make sure that maybe_tensor is structured as {slice_spec -> tensor}.
          tensor_slice_dict = {"": tensor_slice_dict}
        for slice_spec, tensor_save_spec in tensor_slice_dict.items():
          if not isinstance(tensor_save_spec, saveable_object.SaveSpec):
            tensor_save_spec = saveable_object.SaveSpec(
                tensor=tensor_save_spec,
                slice_spec=slice_spec,
                name=checkpoint_key,
                dtype=tensor_save_spec.dtype,
                device=tensor_save_spec.device)
          save_spec_tensor = tensor_save_spec.tensor
          shardable_tensors.append(
              sharding_util.ShardableTensor(
                  _tensor_save_spec=tensor_save_spec,
                  tensor=save_spec_tensor,
                  dtype=tensor_save_spec.dtype,
                  device=tensor_save_spec.device,
                  name=tensor_save_spec.name,
                  shape=save_spec_tensor.shape,
                  slice_spec=slice_spec,
                  checkpoint_key=checkpoint_key,
                  trackable=obj))
    return shardable_tensors

  def test_validate_shards_correct(self):
    root = module.Module()
    with ops.device("cpu:0"):
      v0 = resource_variable_ops.ResourceVariable(0.0, name="v0")
    with ops.device("cpu:1"):
      v1 = resource_variable_ops.ResourceVariable(1.0, name="v1")
    with ops.device("cpu:2"):
      v2 = resource_variable_ops.ResourceVariable(2.0, name="v2")
    root.v0 = v0
    root.v1 = v1
    root.v2 = v2

    shardable_tensors = self._get_shardable_tensors(root)
    sharding_callback = sharding_policies.ShardByDevicePolicy()
    shards = sharding_callback(shardable_tensors)

    sharding_util.validate_shards(
        shards, shardable_tensors, sharding_callback.description)

    self.assertEqual(
        [list(shard.keys()) for shard in shards],
        [[
            "v0/.ATTRIBUTES/VARIABLE_VALUE",
            "v1/.ATTRIBUTES/VARIABLE_VALUE",
            "v2/.ATTRIBUTES/VARIABLE_VALUE",
            "_CHECKPOINTABLE_OBJECT_GRAPH"
        ]])

    self.assertEqual(
        shards[0]["v0/.ATTRIBUTES/VARIABLE_VALUE"][""].numpy(),
        v0.numpy())
    self.assertEqual(
        shards[0]["v1/.ATTRIBUTES/VARIABLE_VALUE"][""].numpy(),
        v1.numpy())
    self.assertEqual(
        shards[0]["v2/.ATTRIBUTES/VARIABLE_VALUE"][""].numpy(),
        v2.numpy())

  def test_validate_shards_duplicate_tensor(self):
    root = module.Module()
    with ops.device("cpu:0"):
      v0 = resource_variable_ops.ResourceVariable(0.0, name="v0")
    with ops.device("cpu:1"):
      v1 = resource_variable_ops.ResourceVariable(1.0, name="v1")
    root.v0 = v0
    root.v1 = v1

    class DuplicateTensorCallback(sharding_util.ShardingCallback):
      def __init__(self):
        def sharding_callback_impl(shardable_tensors):
          tensor = shardable_tensors[0].tensor
          checkpoint_key = shardable_tensors[0].checkpoint_key
          slice_spec = shardable_tensors[0].slice_spec
          shards = [
              {checkpoint_key: {slice_spec: tensor}},
              {checkpoint_key: {slice_spec: tensor}}
          ]
          return shards
        super().__init__(sharding_callback_impl, "duplicate tensor callback")

      def __call__(
          self,
          shardable_tensors: Sequence[sharding_util.ShardableTensor]
      ) -> Sequence[sharding_util.TensorSlice]:
        return self.callback(shardable_tensors)  # pylint: disable=no-value-for-parameter

    sharding_callback = DuplicateTensorCallback()
    shardable_tensors = self._get_shardable_tensors(root)
    shards = sharding_callback(shardable_tensors)

    with self.assertRaisesRegex(RuntimeError,
                                "multiple tensors with the same checkpoint "
                                "key and slice spec were found"):
      sharding_util.validate_shards(
          shards, shardable_tensors, sharding_callback.description)

  def test_validate_shards_added_tensor(self):
    root = module.Module()
    with ops.device("cpu:0"):
      v0 = resource_variable_ops.ResourceVariable(0.0, name="v0")
    root.v0 = v0

    class AddedTensorCallback(sharding_util.ShardingCallback):
      def __init__(self):
        def sharding_callback_impl(_):
          checkpoint_key = "ADDED_TENSOR_ABC123"
          slice_spec = variables.Variable.SaveSliceInfo()
          tensor = tensor_lib.Tensor()
          return [{checkpoint_key: {slice_spec: tensor}}]
        super().__init__(sharding_callback_impl, "added tensor callback")

      def __call__(
          self,
          shardable_tensors: Sequence[sharding_util.ShardableTensor]
      ) -> Sequence[sharding_util.TensorSlice]:
        return self.callback(shardable_tensors)  # pylint: disable=no-value-for-parameter

    sharding_callback = AddedTensorCallback()
    shardable_tensors = self._get_shardable_tensors(root)
    shards = sharding_callback(shardable_tensors)

    with self.assertRaisesRegex(RuntimeError,
                                "a tensor not originally in the object graph"):
      sharding_util.validate_shards(
          shards, shardable_tensors, sharding_callback.description)

  def test_validate_shards_shape_change(self):
    root = module.Module()
    with ops.device("cpu:0"):
      v0 = resource_variable_ops.ResourceVariable([[0.0, 1.0]], name="v0")
    root.v0 = v0

    class ShapeChangeCallback(sharding_util.ShardingCallback):
      def __init__(self):
        def sharding_callback_impl(shardable_tensors):
          shards = []
          for shardable_tensor in shardable_tensors:
            tensor = shardable_tensor.tensor
            checkpoint_key = shardable_tensor.checkpoint_key
            slice_spec = shardable_tensor.slice_spec
            if checkpoint_key == "v0/.ATTRIBUTES/VARIABLE_VALUE":
              tensor = array_ops.transpose(tensor)
            shards.append({checkpoint_key: {slice_spec: tensor}})
          return shards
        super().__init__(sharding_callback_impl, "shape change callback")

      def __call__(
          self,
          shardable_tensors: Sequence[sharding_util.ShardableTensor]
      ) -> Sequence[sharding_util.TensorSlice]:
        return self.callback(shardable_tensors)  # pylint: disable=no-value-for-parameter

    sharding_callback = ShapeChangeCallback()
    shardable_tensors = self._get_shardable_tensors(root)
    shards = sharding_callback(shardable_tensors)

    with self.assertRaisesRegex(RuntimeError,
                                "a tensor was found with an altered shape"):
      sharding_util.validate_shards(
          shards, shardable_tensors, sharding_callback.description)

  def test_validate_shards_dtype_change(self):
    root = module.Module()
    with ops.device("cpu:0"):
      v0 = resource_variable_ops.ResourceVariable(0.0, name="v0")
    root.v0 = v0

    class DtypeChangeCallback(sharding_util.ShardingCallback):
      def __init__(self):
        def sharding_callback_impl(shardable_tensors):
          shards = []
          for shardable_tensor in shardable_tensors:
            tensor = shardable_tensor.tensor
            checkpoint_key = shardable_tensor.checkpoint_key
            slice_spec = shardable_tensor.slice_spec
            if checkpoint_key == "v0/.ATTRIBUTES/VARIABLE_VALUE":
              tensor = math_ops.cast(tensor, dtype=dtypes.int32)
            shards.append({checkpoint_key: {slice_spec: tensor}})
          return shards
        super().__init__(sharding_callback_impl, "dtype change callback")

      def __call__(
          self,
          shardable_tensors: Sequence[sharding_util.ShardableTensor]
      ) -> Sequence[sharding_util.TensorSlice]:
        return self.callback(shardable_tensors)  # pylint: disable=no-value-for-parameter

    sharding_callback = DtypeChangeCallback()
    shardable_tensors = self._get_shardable_tensors(root)
    shards = sharding_callback(shardable_tensors)

    with self.assertRaisesRegex(RuntimeError,
                                "a tensor was found with an altered dtype"):
      sharding_util.validate_shards(
          shards, shardable_tensors, sharding_callback.description)

  def test_validate_shards_different_tasks(self):
    servers = [server_lib.Server.create_local_server() for _ in range(3)]
    cluster_spec = server_lib.ClusterSpec({
        "worker": [s.target[len("grpc://"):] for s in servers]})
    remote.connect_to_cluster(cluster_spec)

    root = module.Module()
    with ops.device("/job:worker/task:0/cpu:0"):
      v0 = resource_variable_ops.ResourceVariable(0.0, name="v0")
    with ops.device("/job:worker/task:1/cpu:0"):
      v1 = resource_variable_ops.ResourceVariable(0.0, name="v1")
    root.v0 = v0
    root.v1 = v1

    class DifferentTasksCallback(sharding_util.ShardingCallback):
      def __init__(self):
        def sharding_callback_impl(shardable_tensors):
          shard = {}
          for shardable_tensor in shardable_tensors:
            tensor = shardable_tensor.tensor
            checkpoint_key = shardable_tensor.checkpoint_key
            slice_spec = shardable_tensor.slice_spec
            shard.setdefault(checkpoint_key, {})[slice_spec] = tensor
          return [shard]
        super().__init__(sharding_callback_impl, "different tasks callback")

      def __call__(
          self,
          shardable_tensors: Sequence[sharding_util.ShardableTensor]
      ) -> Sequence[sharding_util.TensorSlice]:
        return self.callback(shardable_tensors)  # pylint: disable=no-value-for-parameter

    sharding_callback = DifferentTasksCallback()
    shardable_tensors = self._get_shardable_tensors(root)
    shards = sharding_callback(shardable_tensors)

    with self.assertRaisesRegex(RuntimeError,
                                "tensors with different tasks were found"):
      sharding_util.validate_shards(
          shards, shardable_tensors, sharding_callback.description)

  def test_validate_shards_tensor_removal(self):
    root = module.Module()
    with ops.device("cpu:0"):
      v0 = resource_variable_ops.ResourceVariable(0.0, name="v0")
    root.v0 = v0

    class TensorRemovalCallback(sharding_util.ShardingCallback):
      def __init__(self):
        def sharding_callback_impl(_):
          return []
        super().__init__(sharding_callback_impl, "tensor removal callback")

      def __call__(
          self,
          shardable_tensors: Sequence[sharding_util.ShardableTensor]
      ) -> Sequence[sharding_util.TensorSlice]:
        return self.callback(shardable_tensors)  # pylint: disable=no-value-for-parameter

    sharding_callback = TensorRemovalCallback()
    shardable_tensors = self._get_shardable_tensors(root)
    shards = sharding_callback(shardable_tensors)

    with self.assertRaisesRegex(RuntimeError,
                                "tensors in the object graph were not found"):
      sharding_util.validate_shards(
          shards, shardable_tensors, sharding_callback.description)


if __name__ == "__main__":
  test.main()
