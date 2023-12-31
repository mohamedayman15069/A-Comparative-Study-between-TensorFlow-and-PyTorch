<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.layers.one_hot_encoding" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.layers.one_hot_encoding

Transform numeric labels into onehot_labels using <a href="../../../tf/one_hot.md"><code>tf.one_hot</code></a>.

``` python
tf.contrib.layers.one_hot_encoding(
    labels,
    num_classes,
    on_value=1.0,
    off_value=0.0,
    outputs_collections=None,
    scope=None
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`labels`</b>: [batch_size] target labels.
* <b>`num_classes`</b>: Total number of classes.
* <b>`on_value`</b>: A scalar defining the on-value.
* <b>`off_value`</b>: A scalar defining the off-value.
* <b>`outputs_collections`</b>: Collection to add the outputs.
* <b>`scope`</b>: Optional scope for name_scope.


#### Returns:

One-hot encoding of the labels.
