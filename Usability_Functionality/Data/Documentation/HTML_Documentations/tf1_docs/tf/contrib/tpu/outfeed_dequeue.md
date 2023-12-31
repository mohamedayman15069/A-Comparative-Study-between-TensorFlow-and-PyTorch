<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.tpu.outfeed_dequeue" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.tpu.outfeed_dequeue

Retrieves a single tensor from the computation outfeed.

``` python
tf.contrib.tpu.outfeed_dequeue(
    dtype,
    shape,
    device_ordinal=-1,
    name=None
)
```

<!-- Placeholder for "Used in" -->

This operation will block indefinitely until data is available.

#### Args:


* <b>`dtype`</b>: A <a href="../../../tf/dtypes/DType.md"><code>tf.DType</code></a>. The type of elements in the tensor.
* <b>`shape`</b>: A <a href="../../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`. The shape of the tensor.
* <b>`device_ordinal`</b>: An optional `int`. Defaults to `-1`.
  The TPU device to use. This should be -1 when the Op
  is running on a TPU device, and >= 0 when the Op is running on the CPU
  device.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `dtype`.
