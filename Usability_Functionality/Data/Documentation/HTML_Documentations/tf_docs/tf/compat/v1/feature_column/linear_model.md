description: Returns a linear prediction Tensor based on given feature_columns. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.feature_column.linear_model" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.feature_column.linear_model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/feature_column/feature_column.py">View source</a>



Returns a linear prediction `Tensor` based on given `feature_columns`. (deprecated)



Warning: tf.feature_column is not recommended for new code. Instead,
feature preprocessing can be done directly using either [Keras preprocessing
layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns)
or through the one-stop utility [`tf.keras.utils.FeatureSpace`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace)
built on top of them. See the [migration guide](https://tensorflow.org/guide/migrate)
for details.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.feature_column.linear_model(
    features,
    feature_columns,
    units=1,
    sparse_combiner=&#x27;sum&#x27;,
    weight_collections=None,
    trainable=True,
    cols_to_vars=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use Keras preprocessing layers instead, either directly or via the <a href="../../../../tf/keras/utils/FeatureSpace.md"><code>tf.keras.utils.FeatureSpace</code></a> utility. Each of `tf.feature_column.*` has a functional equivalent in `tf.keras.layers` for feature preprocessing when training a Keras model.

This function generates a weighted sum based on output dimension `units`.
Weighted sum refers to logits in classification problems. It refers to the
prediction itself for linear regression problems.

Note on supported columns: `linear_model` treats categorical columns as
`indicator_column`s. To be specific, assume the input as `SparseTensor` looks
like:

```python
  shape = [2, 2]
  {
      [0, 0]: "a"
      [1, 0]: "b"
      [1, 1]: "c"
  }
```
`linear_model` assigns weights for the presence of "a", "b", "c' implicitly,
just like `indicator_column`, while `input_layer` explicitly requires wrapping
each of categorical columns with an `embedding_column` or an
`indicator_column`.

#### Example of usage:



```python
price = numeric_column('price')
price_buckets = bucketized_column(price, boundaries=[0., 10., 100., 1000.])
keywords = categorical_column_with_hash_bucket("keywords", 10K)
keywords_price = crossed_column('keywords', price_buckets, ...)
columns = [price_buckets, keywords, keywords_price ...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
prediction = linear_model(features, columns)
```

The `sparse_combiner` argument works as follows
For example, for two features represented as the categorical columns:

```python
  # Feature 1

  shape = [2, 2]
  {
      [0, 0]: "a"
      [0, 1]: "b"
      [1, 0]: "c"
  }

  # Feature 2

  shape = [2, 3]
  {
      [0, 0]: "d"
      [1, 0]: "e"
      [1, 1]: "f"
      [1, 2]: "f"
  }
```

with `sparse_combiner` as "mean", the linear model outputs consequently
are:

```
  y_0 = 1.0 / 2.0 * ( w_a + w_b ) + w_d + b
  y_1 = w_c + 1.0 / 3.0 * ( w_e + 2.0 * w_f ) + b
```

where `y_i` is the output, `b` is the bias, and `w_x` is the weight
assigned to the presence of `x` in the input features.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`features`<a id="features"></a>
</td>
<td>
A mapping from key to tensors. `_FeatureColumn`s look up via these
keys. For example `numeric_column('price')` will look at 'price' key in
this dict. Values are `Tensor` or `SparseTensor` depending on
corresponding `_FeatureColumn`.
</td>
</tr><tr>
<td>
`feature_columns`<a id="feature_columns"></a>
</td>
<td>
An iterable containing the FeatureColumns to use as inputs
to your model. All items should be instances of classes derived from
`_FeatureColumn`s.
</td>
</tr><tr>
<td>
`units`<a id="units"></a>
</td>
<td>
An integer, dimensionality of the output space. Default value is 1.
</td>
</tr><tr>
<td>
`sparse_combiner`<a id="sparse_combiner"></a>
</td>
<td>
A string specifying how to reduce if a categorical column
is multivalent. Except `numeric_column`, almost all columns passed to
`linear_model` are considered as categorical columns.  It combines each
categorical column independently. Currently "mean", "sqrtn" and "sum" are
supported, with "sum" the default for linear model. "sqrtn" often achieves
good accuracy, in particular with bag-of-words columns.
  * "sum": do not
  normalize features in the column
  * "mean": do l1 normalization on features
  in the column
  * "sqrtn": do l2 normalization on features in the column
</td>
</tr><tr>
<td>
`weight_collections`<a id="weight_collections"></a>
</td>
<td>
A list of collection names to which the Variable will be
added. Note that, variables will also be added to collections
`tf.GraphKeys.GLOBAL_VARIABLES` and `ops.GraphKeys.MODEL_VARIABLES`.
</td>
</tr><tr>
<td>
`trainable`<a id="trainable"></a>
</td>
<td>
If `True` also add the variable to the graph collection
`GraphKeys.TRAINABLE_VARIABLES` (see <a href="../../../../tf/Variable.md"><code>tf.Variable</code></a>).
</td>
</tr><tr>
<td>
`cols_to_vars`<a id="cols_to_vars"></a>
</td>
<td>
If not `None`, must be a dictionary that will be filled with a
mapping from `_FeatureColumn` to associated list of `Variable`s.  For
example, after the call, we might have cols_to_vars = { _NumericColumn(
key='numeric_feature1', shape=(1,): [<tf.Variable
'linear_model/price2/weights:0' shape=(1, 1)>], 'bias': [<tf.Variable
'linear_model/bias_weights:0' shape=(1,)>], _NumericColumn(
key='numeric_feature2', shape=(2,)): [<tf.Variable
'linear_model/price1/weights:0' shape=(2, 1)>]} If a column creates no
variables, its value will be an empty list. Note that cols_to_vars will
also contain a string key 'bias' that maps to a list of Variables.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` which represents predictions/logits of a linear model. Its shape
is (batch_size, units) and its dtype is `float32`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
if an item in `feature_columns` is neither a `_DenseColumn`
nor `_CategoricalColumn`.
</td>
</tr>
</table>

