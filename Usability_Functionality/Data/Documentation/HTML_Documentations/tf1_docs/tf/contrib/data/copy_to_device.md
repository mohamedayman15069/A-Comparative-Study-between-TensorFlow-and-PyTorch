<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.data.copy_to_device" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.data.copy_to_device

A transformation that copies dataset elements to the given `target_device`. (deprecated)

``` python
tf.contrib.data.copy_to_device(
    target_device,
    source_device='/cpu:0'
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/experimental/copy_to_device.md"><code>tf.data.experimental.copy_to_device(...)</code></a>.

#### Args:


* <b>`target_device`</b>: The name of a device to which elements will be copied.
* <b>`source_device`</b>: The original device on which `input_dataset` will be placed.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset.md#apply"><code>tf.data.Dataset.apply</code></a>.
