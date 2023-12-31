<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.dense_to_sparse_batch" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.dense_to_sparse_batch

A transformation that batches ragged elements into <a href="../../../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a>s.

### Aliases:

* `tf.compat.v1.data.experimental.dense_to_sparse_batch`
* `tf.compat.v2.compat.v1.data.experimental.dense_to_sparse_batch`
* `tf.compat.v2.data.experimental.dense_to_sparse_batch`
* `tf.data.experimental.dense_to_sparse_batch`

``` python
tf.data.experimental.dense_to_sparse_batch(
    batch_size,
    row_shape
)
```

<!-- Placeholder for "Used in" -->

Like <a href="../../../tf/data/Dataset.md#padded_batch"><code>Dataset.padded_batch()</code></a>, this transformation combines multiple
consecutive elements of the dataset, which might have different
shapes, into a single element. The resulting element has three
components (`indices`, `values`, and `dense_shape`), which
comprise a <a href="../../../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a> that represents the same data. The
`row_shape` represents the dense shape of each row in the
resulting <a href="../../../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a>, to which the effective batch size is
prepended. For example:

```python
# NOTE: The following examples use `{ ... }` to represent the
# contents of a dataset.
a = { ['a', 'b', 'c'], ['a', 'b'], ['a', 'b', 'c', 'd'] }

a.apply(tf.data.experimental.dense_to_sparse_batch(
    batch_size=2, row_shape=[6])) ==
{
    ([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1]],  # indices
     ['a', 'b', 'c', 'a', 'b'],                 # values
     [2, 6]),                                   # dense_shape
    ([[0, 0], [0, 1], [0, 2], [0, 3]],
     ['a', 'b', 'c', 'd'],
     [1, 6])
}
```

#### Args:


* <b>`batch_size`</b>: A <a href="../../../tf.md#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing the number of
  consecutive elements of this dataset to combine in a single batch.
* <b>`row_shape`</b>: A <a href="../../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or <a href="../../../tf.md#int64"><code>tf.int64</code></a> vector tensor-like object
  representing the equivalent dense shape of a row in the resulting
  <a href="../../../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a>. Each element of this dataset must have the same rank as
  `row_shape`, and must have size less than or equal to `row_shape` in each
  dimension.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset.md#apply"><code>tf.data.Dataset.apply</code></a>.
