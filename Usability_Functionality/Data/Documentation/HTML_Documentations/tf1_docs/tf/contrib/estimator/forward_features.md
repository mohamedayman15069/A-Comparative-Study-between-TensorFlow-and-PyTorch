<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.estimator.forward_features" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.estimator.forward_features

Forward features to predictions dictionary.

``` python
tf.contrib.estimator.forward_features(
    estimator,
    keys=None,
    sparse_default_values=None
)
```



Defined in [`contrib/estimator/python/estimator/extenders.py`](https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/contrib/estimator/python/estimator/extenders.py).

<!-- Placeholder for "Used in" -->

In some cases, user wants to see some of the features in estimators prediction
output. As an example, consider a batch prediction service: The service simply
runs inference on the users graph and returns the results. Keys are essential
because there is no order guarantee on the outputs so they need to be rejoined
to the inputs via keys or transclusion of the inputs in the outputs.
Example:
```python
  def input_fn():
    features, labels = ...
    features['unique_example_id'] = ...
    features, labels
  estimator = tf.estimator.LinearClassifier(...)
  estimator = tf.contrib.estimator.forward_features(
      estimator, 'unique_example_id')
  estimator.train(...)
  assert 'unique_example_id' in estimator.predict(...)
```
Args:
  estimator: A <a href="../../../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a> object.
  keys: A `string` or a `list` of `string`. If it is `None`, all of the
    `features` in `dict` is forwarded to the `predictions`. If it is a
    `string`, only given key is forwarded. If it is a `list` of strings, all
    the given `keys` are forwarded.
  sparse_default_values: A dict of `str` keys mapping the name of the sparse
    features to be converted to dense, to the default value to use. Only
    sparse features indicated in the dictionary are converted to dense and the
    provided default value is used.

#### Returns:

A new <a href="../../../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a> which forwards features to predictions.


#### Raises:


* <b>`ValueError`</b>:   * if `keys` is already part of `predictions`. We don't allow
    override.
  * if 'keys' does not exist in `features`.
* <b>`TypeError`</b>: if `keys` type is not one of `string` or list/tuple of `string`.