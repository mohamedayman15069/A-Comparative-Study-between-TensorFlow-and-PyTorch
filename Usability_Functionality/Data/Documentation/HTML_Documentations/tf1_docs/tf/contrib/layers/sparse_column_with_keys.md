<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.layers.sparse_column_with_keys" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.layers.sparse_column_with_keys

Creates a _SparseColumn with keys.

``` python
tf.contrib.layers.sparse_column_with_keys(
    column_name,
    keys,
    default_value=-1,
    combiner='sum',
    dtype=tf.dtypes.string
)
```

<!-- Placeholder for "Used in" -->

Look up logic is as follows:
lookup_id = index_of_feature_in_keys if feature in keys else default_value

#### Args:


* <b>`column_name`</b>: A string defining sparse column name.
* <b>`keys`</b>: A list or tuple defining vocabulary. Must be castable to `dtype`.
* <b>`default_value`</b>: The value to use for out-of-vocabulary feature values.
  Default is -1.
* <b>`combiner`</b>: A string specifying how to reduce if the sparse column is
  multivalent. Currently "mean", "sqrtn" and "sum" are supported, with "sum"
  the default. "sqrtn" often achieves good accuracy, in particular with
  bag-of-words columns.
    * "sum": do not normalize features in the column
    * "mean": do l1 normalization on features in the column
    * "sqrtn": do l2 normalization on features in the column
  For more information: `tf.embedding_lookup_sparse`.
* <b>`dtype`</b>: Type of features. Only integer and string are supported.


#### Returns:

A _SparseColumnKeys with keys configuration.
