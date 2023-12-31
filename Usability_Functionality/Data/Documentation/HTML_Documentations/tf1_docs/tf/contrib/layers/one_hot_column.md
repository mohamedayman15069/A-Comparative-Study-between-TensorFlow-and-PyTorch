<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.layers.one_hot_column" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.layers.one_hot_column

Creates an `_OneHotColumn` for a one-hot or multi-hot repr in a DNN.

``` python
tf.contrib.layers.one_hot_column(sparse_id_column)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sparse_id_column`</b>: A _SparseColumn which is created by
  `sparse_column_with_*` or crossed_column functions. Note that `combiner`
  defined in `sparse_id_column` is ignored.


#### Returns:

An _OneHotColumn.
