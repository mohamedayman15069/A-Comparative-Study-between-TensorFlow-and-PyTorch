<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.estimator

Estimator: High level tools for working with models.

### Aliases:

* Module `tf.compat.v1.estimator`
* Module `tf.compat.v2.compat.v1.estimator`
* Module `tf.estimator`



Defined in [`python/estimator/api/_v1/estimator/__init__.py`](https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/api/_v1/estimator/__init__.py).

<!-- Placeholder for "Used in" -->


## Modules

[`experimental`](../tf/estimator/experimental.md) module: Public API for tf.estimator.experimental namespace.

[`export`](../tf/estimator/export.md) module: All public utility methods for exporting Estimator to SavedModel.

[`inputs`](../tf/estimator/inputs.md) module: Utility methods to create simple input_fns.

[`tpu`](../tf/estimator/tpu.md) module: Public API for tf.estimator.tpu namespace.

## Classes

[`class BaselineClassifier`](../tf/estimator/BaselineClassifier.md): A classifier that can establish a simple baseline.

[`class BaselineEstimator`](../tf/estimator/BaselineEstimator.md): An estimator that can establish a simple baseline.

[`class BaselineRegressor`](../tf/estimator/BaselineRegressor.md): A regressor that can establish a simple baseline.

[`class BestExporter`](../tf/estimator/BestExporter.md): This class exports the serving graph and checkpoints of the best models.

[`class BinaryClassHead`](../tf/estimator/BinaryClassHead.md): Creates a `Head` for single label binary classification.

[`class BoostedTreesClassifier`](../tf/estimator/BoostedTreesClassifier.md): A Classifier for Tensorflow Boosted Trees models.

[`class BoostedTreesEstimator`](../tf/estimator/BoostedTreesEstimator.md): An Estimator for Tensorflow Boosted Trees models.

[`class BoostedTreesRegressor`](../tf/estimator/BoostedTreesRegressor.md): A Regressor for Tensorflow Boosted Trees models.

[`class CheckpointSaverHook`](../tf/train/CheckpointSaverHook.md): Saves checkpoints every N steps or seconds.

[`class CheckpointSaverListener`](../tf/train/CheckpointSaverListener.md): Interface for listeners that take action before or after checkpoint save.

[`class DNNClassifier`](../tf/estimator/DNNClassifier.md): A classifier for TensorFlow DNN models.

[`class DNNEstimator`](../tf/estimator/DNNEstimator.md): An estimator for TensorFlow DNN models with user-specified head.

[`class DNNLinearCombinedClassifier`](../tf/estimator/DNNLinearCombinedClassifier.md): An estimator for TensorFlow Linear and DNN joined classification models.

[`class DNNLinearCombinedEstimator`](../tf/estimator/DNNLinearCombinedEstimator.md): An estimator for TensorFlow Linear and DNN joined models with custom head.

[`class DNNLinearCombinedRegressor`](../tf/estimator/DNNLinearCombinedRegressor.md): An estimator for TensorFlow Linear and DNN joined models for regression.

[`class DNNRegressor`](../tf/estimator/DNNRegressor.md): A regressor for TensorFlow DNN models.

[`class Estimator`](../tf/estimator/Estimator.md): Estimator class to train and evaluate TensorFlow models.

[`class EstimatorSpec`](../tf/estimator/EstimatorSpec.md): Ops and objects returned from a `model_fn` and passed to an `Estimator`.

[`class EvalSpec`](../tf/estimator/EvalSpec.md): Configuration for the "eval" part for the `train_and_evaluate` call.

[`class Exporter`](../tf/estimator/Exporter.md): A class representing a type of model export.

[`class FeedFnHook`](../tf/train/FeedFnHook.md): Runs `feed_fn` and sets the `feed_dict` accordingly.

[`class FinalExporter`](../tf/estimator/FinalExporter.md): This class exports the serving graph and checkpoints at the end.

[`class FinalOpsHook`](../tf/train/FinalOpsHook.md): A hook which evaluates `Tensors` at the end of a session.

[`class GlobalStepWaiterHook`](../tf/train/GlobalStepWaiterHook.md): Delays execution until global step reaches `wait_until_step`.

[`class Head`](../tf/estimator/Head.md): Interface for the head/top of a model.

[`class LatestExporter`](../tf/estimator/LatestExporter.md): This class regularly exports the serving graph and checkpoints.

[`class LinearClassifier`](../tf/estimator/LinearClassifier.md): Linear classifier model.

[`class LinearEstimator`](../tf/estimator/LinearEstimator.md): An estimator for TensorFlow linear models with user-specified head.

[`class LinearRegressor`](../tf/estimator/LinearRegressor.md): An estimator for TensorFlow Linear regression problems.

[`class LoggingTensorHook`](../tf/train/LoggingTensorHook.md): Prints the given tensors every N local steps, every N seconds, or at end.

[`class LogisticRegressionHead`](../tf/estimator/LogisticRegressionHead.md): Creates a `Head` for logistic regression.

[`class ModeKeys`](../tf/estimator/ModeKeys.md): Standard names for Estimator model modes.

[`class MultiClassHead`](../tf/estimator/MultiClassHead.md): Creates a `Head` for multi class classification.

[`class MultiHead`](../tf/estimator/MultiHead.md): Creates a `Head` for multi-objective learning.

[`class MultiLabelHead`](../tf/estimator/MultiLabelHead.md): Creates a `Head` for multi-label classification.

[`class NanLossDuringTrainingError`](../tf/train/NanLossDuringTrainingError.md): Unspecified run-time error.

[`class NanTensorHook`](../tf/train/NanTensorHook.md): Monitors the loss tensor and stops training if loss is NaN.

[`class PoissonRegressionHead`](../tf/estimator/PoissonRegressionHead.md): Creates a `Head` for poisson regression using <a href="../tf/nn/log_poisson_loss.md"><code>tf.nn.log_poisson_loss</code></a>.

[`class ProfilerHook`](../tf/train/ProfilerHook.md): Captures CPU/GPU profiling information every N steps or seconds.

[`class RegressionHead`](../tf/estimator/RegressionHead.md): Creates a `Head` for regression using the `mean_squared_error` loss.

[`class RunConfig`](../tf/estimator/RunConfig.md): This class specifies the configurations for an `Estimator` run.

[`class SecondOrStepTimer`](../tf/train/SecondOrStepTimer.md): Timer that triggers at most once every N seconds or once every N steps.

[`class SessionRunArgs`](../tf/train/SessionRunArgs.md): Represents arguments to be added to a <a href="../tf/InteractiveSession.md#run"><code>Session.run()</code></a> call.

[`class SessionRunContext`](../tf/train/SessionRunContext.md): Provides information about the `session.run()` call being made.

[`class SessionRunHook`](../tf/train/SessionRunHook.md): Hook to extend calls to MonitoredSession.run().

[`class SessionRunValues`](../tf/train/SessionRunValues.md): Contains the results of <a href="../tf/InteractiveSession.md#run"><code>Session.run()</code></a>.

[`class StepCounterHook`](../tf/train/StepCounterHook.md): Hook that counts steps per second.

[`class StopAtStepHook`](../tf/train/StopAtStepHook.md): Hook that requests stop at a specified step.

[`class SummarySaverHook`](../tf/train/SummarySaverHook.md): Saves summaries every N steps.

[`class TrainSpec`](../tf/estimator/TrainSpec.md): Configuration for the "train" part for the `train_and_evaluate` call.

[`class VocabInfo`](../tf/train/VocabInfo.md): Vocabulary information for warm-starting.

[`class WarmStartSettings`](../tf/estimator/WarmStartSettings.md): Settings for warm-starting in `tf.estimator.Estimators`.

## Functions

[`add_metrics(...)`](../tf/estimator/add_metrics.md): Creates a new <a href="../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a> which has given metrics.

[`classifier_parse_example_spec(...)`](../tf/estimator/classifier_parse_example_spec.md): Generates parsing spec for tf.parse_example to be used with classifiers.

[`regressor_parse_example_spec(...)`](../tf/estimator/regressor_parse_example_spec.md): Generates parsing spec for tf.parse_example to be used with regressors.

[`train_and_evaluate(...)`](../tf/estimator/train_and_evaluate.md): Train and evaluate the `estimator`.

