<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.feature_column.make_parse_example_spec" />
<meta itemprop="path" content="Stable" />
</div>

# tf.feature_column.make_parse_example_spec

Creates parsing spec dictionary from input feature_columns.

### Aliases:

* `tf.compat.v1.feature_column.make_parse_example_spec`
* `tf.compat.v2.compat.v1.feature_column.make_parse_example_spec`
* `tf.feature_column.make_parse_example_spec`

``` python
tf.feature_column.make_parse_example_spec(feature_columns)
```

<!-- Placeholder for "Used in" -->

The returned dictionary can be used as arg 'features' in
<a href="../../tf/io/parse_example.md"><code>tf.io.parse_example</code></a>.

#### Typical usage example:



```python
# Define features and transformations
feature_a = categorical_column_with_vocabulary_file(...)
feature_b = numeric_column(...)
feature_c_bucketized = bucketized_column(numeric_column("feature_c"), ...)
feature_a_x_feature_c = crossed_column(
    columns=["feature_a", feature_c_bucketized], ...)

feature_columns = set(
    [feature_b, feature_c_bucketized, feature_a_x_feature_c])
features = tf.io.parse_example(
    serialized=serialized_examples,
    features=make_parse_example_spec(feature_columns))
```

For the above example, make_parse_example_spec would return the dict:

```python
{
    "feature_a": parsing_ops.VarLenFeature(tf.string),
    "feature_b": parsing_ops.FixedLenFeature([1], dtype=tf.float32),
    "feature_c": parsing_ops.FixedLenFeature([1], dtype=tf.float32)
}
```

#### Args:


* <b>`feature_columns`</b>: An iterable containing all feature columns. All items
  should be instances of classes derived from `_FeatureColumn`.


#### Returns:

A dict mapping each feature key to a `FixedLenFeature` or `VarLenFeature`
value.



#### Raises:


* <b>`ValueError`</b>: If any of the given `feature_columns` is not a `_FeatureColumn`
  instance.