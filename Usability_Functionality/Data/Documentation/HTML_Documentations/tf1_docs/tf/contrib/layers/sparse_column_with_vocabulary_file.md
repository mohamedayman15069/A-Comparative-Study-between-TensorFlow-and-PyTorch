<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.layers.sparse_column_with_vocabulary_file" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.layers.sparse_column_with_vocabulary_file

Creates a _SparseColumn with vocabulary file configuration.

``` python
tf.contrib.layers.sparse_column_with_vocabulary_file(
    column_name,
    vocabulary_file,
    num_oov_buckets=0,
    vocab_size=None,
    default_value=-1,
    combiner='sum',
    dtype=tf.dtypes.string
)
```

<!-- Placeholder for "Used in" -->

Use this when your sparse features are in string or integer format, and you
have a vocab file that maps each value to an integer ID.
output_id = LookupIdFromVocab(input_feature_string)

#### Args:


* <b>`column_name`</b>: A string defining sparse column name.
* <b>`vocabulary_file`</b>: The vocabulary filename.
* <b>`num_oov_buckets`</b>: The number of out-of-vocabulary buckets. If zero all out of
  vocabulary features will be ignored.
* <b>`vocab_size`</b>: Number of the elements in the vocabulary.
* <b>`default_value`</b>: The value to use for out-of-vocabulary feature values.
  Defaults to -1.
* <b>`combiner`</b>: A string specifying how to reduce if the sparse column is
  multivalent. Currently "mean", "sqrtn" and "sum" are supported, with "sum"
  the default. "sqrtn" often achieves good accuracy, in particular with
  bag-of-words columns.
    * "sum": do not normalize features in the column
    * "mean": do l1 normalization on features in the column
    * "sqrtn": do l2 normalization on features in the column
  For more information: `tf.embedding_lookup_sparse`.
* <b>`dtype`</b>: The type of features. Only string and integer types are supported.


#### Returns:

A _SparseColumn with vocabulary file configuration.



#### Raises:


* <b>`ValueError`</b>: vocab_size is not defined.
* <b>`ValueError`</b>: dtype is neither string nor integer.