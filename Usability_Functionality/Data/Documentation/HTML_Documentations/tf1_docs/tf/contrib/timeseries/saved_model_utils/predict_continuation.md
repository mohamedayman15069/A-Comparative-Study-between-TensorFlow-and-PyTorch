<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.timeseries.saved_model_utils.predict_continuation" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.timeseries.saved_model_utils.predict_continuation

Perform prediction using an exported saved model.

``` python
tf.contrib.timeseries.saved_model_utils.predict_continuation(
    continue_from,
    signatures,
    session,
    steps=None,
    times=None,
    exogenous_features=None
)
```

<!-- Placeholder for "Used in" -->

Analogous to _input_pipeline.predict_continuation_input_fn, but operates on a
saved model rather than feeding into Estimator's predict method.

#### Args:


* <b>`continue_from`</b>: A dictionary containing the results of either an Estimator's
  evaluate method or filter_continuation. Used to determine the model state
  to make predictions starting from.
* <b>`signatures`</b>: The `MetaGraphDef` protocol buffer returned from
  <a href="../../../../tf/saved_model/load.md"><code>tf.compat.v1.saved_model.loader.load</code></a>. Used to determine the names of
  Tensors to feed and fetch. Must be from the same model as `continue_from`.
* <b>`session`</b>: The session to use. The session's graph must be the one into which
  <a href="../../../../tf/saved_model/load.md"><code>tf.compat.v1.saved_model.loader.load</code></a> loaded the model.
* <b>`steps`</b>: The number of steps to predict (scalar), starting after the
  evaluation or filtering. If `times` is specified, `steps` must not be; one
  is required.
* <b>`times`</b>: A [batch_size x window_size] array of integers (not a Tensor)
  indicating times to make predictions for. These times must be after the
  corresponding evaluation or filtering. If `steps` is specified, `times`
  must not be; one is required. If the batch dimension is omitted, it is
  assumed to be 1.
* <b>`exogenous_features`</b>: Optional dictionary. If specified, indicates exogenous
  features for the model to use while making the predictions. Values must
  have shape [batch_size x window_size x ...], where `batch_size` matches
  the batch dimension used when creating `continue_from`, and `window_size`
  is either the `steps` argument or the `window_size` of the `times`
  argument (depending on which was specified).


#### Returns:

A dictionary with model-specific predictions (typically having keys "mean"
and "covariance") and a feature_keys.PredictionResults.TIMES key indicating
the times for which the predictions were computed.


#### Raises:


* <b>`ValueError`</b>: If `times` or `steps` are misspecified.