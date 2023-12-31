<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.eye" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.eye

Creates a two-dimensional sparse tensor with ones along the diagonal.

### Aliases:

* `tf.compat.v1.sparse.eye`
* `tf.compat.v2.compat.v1.sparse.eye`
* `tf.compat.v2.sparse.eye`
* `tf.sparse.eye`

``` python
tf.sparse.eye(
    num_rows,
    num_columns=None,
    dtype=tf.dtypes.float32,
    name=None
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`num_rows`</b>: Non-negative integer or `int32` scalar `tensor` giving the number
  of rows in the resulting matrix.
* <b>`num_columns`</b>: Optional non-negative integer or `int32` scalar `tensor` giving
  the number of columns in the resulting matrix. Defaults to `num_rows`.
* <b>`dtype`</b>: The type of element in the resulting `Tensor`.
* <b>`name`</b>: A name for this `Op`. Defaults to "eye".


#### Returns:

A `SparseTensor` of shape [num_rows, num_columns] with ones along the
diagonal.
