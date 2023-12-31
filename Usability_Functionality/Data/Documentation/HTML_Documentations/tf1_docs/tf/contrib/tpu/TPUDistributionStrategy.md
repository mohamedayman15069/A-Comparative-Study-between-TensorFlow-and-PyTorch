<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.tpu.TPUDistributionStrategy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.contrib.tpu.TPUDistributionStrategy

## Class `TPUDistributionStrategy`

The strategy to run Keras model on TPU.



<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    tpu_cluster_resolver=None,
    using_single_core=False
)
```

Construct a TPUDistributionStrategy.


#### Args:


* <b>`tpu_cluster_resolver`</b>: Any instance of `TPUClusterResolver`. If None, will
  create one with '' as master address.
* <b>`using_single_core`</b>: Bool. This is the debugging option, which might be
  removed in future once the model replication functionality is mature
  enough. If `False` (default behavior), the system automatically finds
  the best configuration, in terms of number of TPU cores, for the model
  replication, typically using all available TPU cores. If overwrites as
  `True`, force the model replication using single core, i.e., no
  replication.

#### Raises:


* <b>`Exception`</b>: No TPU Found on the given worker.



