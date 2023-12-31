<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.layers.flatten" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.layers.flatten

Flattens the input while maintaining the batch_size.

``` python
tf.contrib.layers.flatten(
    inputs,
    outputs_collections=None,
    scope=None
)
```

<!-- Placeholder for "Used in" -->

  Assumes that the first dimension represents the batch.

#### Args:


* <b>`inputs`</b>: A tensor of size [batch_size, ...].
* <b>`outputs_collections`</b>: Collection to add the outputs.
* <b>`scope`</b>: Optional scope for name_scope.


#### Returns:

A flattened tensor with shape [batch_size, k].


#### Raises:


* <b>`ValueError`</b>: If inputs rank is unknown or less than 2.