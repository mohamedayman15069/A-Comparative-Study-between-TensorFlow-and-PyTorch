<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.data.padded_batch_and_drop_remainder" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.data.padded_batch_and_drop_remainder

A batching and padding transformation that omits the final small batch. (deprecated)

``` python
tf.contrib.data.padded_batch_and_drop_remainder(
    batch_size,
    padded_shapes,
    padding_values=None
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/Dataset.md#padded_batch"><code>tf.data.Dataset.padded_batch(..., drop_remainder=True)</code></a>.

Like <a href="../../../tf/data/Dataset.md#padded_batch"><code>tf.data.Dataset.padded_batch</code></a>, this transformation combines
consecutive elements of this dataset into batches. However, if the batch
size does not evenly divide the input dataset size, this transformation will
drop the final smaller element.

See <a href="../../../tf/contrib/data/batch_and_drop_remainder.md"><code>tf.contrib.data.batch_and_drop_remainder</code></a> for more details.

#### Args:


* <b>`batch_size`</b>: A <a href="../../../tf.md#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing the number of
  consecutive elements of this dataset to combine in a single batch.
* <b>`padded_shapes`</b>: A nested structure of <a href="../../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or <a href="../../../tf.md#int64"><code>tf.int64</code></a> vector
  tensor-like objects. See <a href="../../../tf/data/Dataset.md#padded_batch"><code>tf.data.Dataset.padded_batch</code></a> for details.
* <b>`padding_values`</b>: (Optional.) A nested structure of scalar-shaped <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>.
  See <a href="../../../tf/data/Dataset.md#padded_batch"><code>tf.data.Dataset.padded_batch</code></a> for details.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset.md#apply"><code>tf.data.Dataset.apply</code></a>
