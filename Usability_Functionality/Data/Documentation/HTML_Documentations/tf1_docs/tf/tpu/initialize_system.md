<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tpu.initialize_system" />
<meta itemprop="path" content="Stable" />
</div>

# tf.tpu.initialize_system

Initializes a distributed TPU system for use with TensorFlow.

### Aliases:

* `tf.compat.v1.tpu.initialize_system`
* `tf.compat.v2.compat.v1.tpu.initialize_system`
* `tf.contrib.tpu.initialize_system`
* `tf.tpu.initialize_system`

``` python
tf.tpu.initialize_system(
    embedding_config=None,
    job=None
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`embedding_config`</b>: If not None, a `TPUEmbeddingConfiguration` proto
  describing the desired configuration of the hardware embedding lookup
  tables. If embedding_config is None, no hardware embeddings can be used.
* <b>`job`</b>: The job (the XXX in TensorFlow device specification /job:XXX) that
  contains the TPU devices that will be initialized. If job=None it is
  assumed there is only one job in the TensorFlow flock, and an error will
  be returned if this assumption does not hold.

#### Returns:

A serialized `TopologyProto` that describes the TPU system. Note:
  the topology must be evaluated using <a href="../../tf/InteractiveSession.md#run"><code>Session.run</code></a> before it can be used.
