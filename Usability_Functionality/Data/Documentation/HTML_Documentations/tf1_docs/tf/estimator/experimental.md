<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.experimental" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.estimator.experimental

Public API for tf.estimator.experimental namespace.

### Aliases:

* Module `tf.compat.v1.estimator.experimental`
* Module `tf.compat.v2.compat.v1.estimator.experimental`
* Module `tf.estimator.experimental`



Defined in [`python/estimator/api/_v1/estimator/experimental/__init__.py`](https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/api/_v1/estimator/experimental/__init__.py).

<!-- Placeholder for "Used in" -->


## Classes

[`class InMemoryEvaluatorHook`](../../tf/estimator/experimental/InMemoryEvaluatorHook.md): Hook to run evaluation in training without a checkpoint.

[`class KMeans`](../../tf/estimator/experimental/KMeans.md): An Estimator for K-Means clustering.

[`class LinearSDCA`](../../tf/estimator/experimental/LinearSDCA.md): Stochastic Dual Coordinate Ascent helper for linear estimators.

## Functions

[`build_raw_supervised_input_receiver_fn(...)`](../../tf/contrib/estimator/build_raw_supervised_input_receiver_fn.md): Build a supervised_input_receiver_fn for raw features and labels.

[`call_logit_fn(...)`](../../tf/estimator/experimental/call_logit_fn.md): Calls logit_fn (experimental).

[`dnn_logit_fn_builder(...)`](../../tf/contrib/estimator/dnn_logit_fn_builder.md): Function builder for a dnn logit_fn.

[`linear_logit_fn_builder(...)`](../../tf/contrib/estimator/linear_logit_fn_builder.md): Function builder for a linear logit_fn.

[`make_early_stopping_hook(...)`](../../tf/estimator/experimental/make_early_stopping_hook.md): Creates early-stopping hook.

[`make_stop_at_checkpoint_step_hook(...)`](../../tf/estimator/experimental/make_stop_at_checkpoint_step_hook.md): Creates a proper StopAtCheckpointStepHook based on chief status.

[`stop_if_higher_hook(...)`](../../tf/estimator/experimental/stop_if_higher_hook.md): Creates hook to stop if the given metric is higher than the threshold.

[`stop_if_lower_hook(...)`](../../tf/estimator/experimental/stop_if_lower_hook.md): Creates hook to stop if the given metric is lower than the threshold.

[`stop_if_no_decrease_hook(...)`](../../tf/estimator/experimental/stop_if_no_decrease_hook.md): Creates hook to stop if metric does not decrease within given max steps.

[`stop_if_no_increase_hook(...)`](../../tf/estimator/experimental/stop_if_no_increase_hook.md): Creates hook to stop if metric does not increase within given max steps.

