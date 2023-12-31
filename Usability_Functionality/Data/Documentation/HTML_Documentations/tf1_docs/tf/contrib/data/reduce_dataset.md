<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.data.reduce_dataset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.data.reduce_dataset

Returns the result of reducing the `dataset` using `reducer`. (deprecated)

``` python
tf.contrib.data.reduce_dataset(
    dataset,
    reducer
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/Dataset.md#reduce"><code>tf.data.Dataset.reduce(...)</code></a>.

#### Args:


* <b>`dataset`</b>: A <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object.
* <b>`reducer`</b>: A <a href="../../../tf/data/experimental/Reducer.md"><code>tf.data.experimental.Reducer</code></a> object representing the reduce
  logic.


#### Returns:

A nested structure of <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a> objects, corresponding to the result
of reducing `dataset` using `reducer`.



#### Raises:


* <b>`TypeError`</b>: if `dataset` is not a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object.