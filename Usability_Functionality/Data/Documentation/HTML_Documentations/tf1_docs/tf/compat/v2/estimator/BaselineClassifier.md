<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v2.estimator.BaselineClassifier" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="config"/>
<meta itemprop="property" content="export_savedmodel"/>
<meta itemprop="property" content="model_dir"/>
<meta itemprop="property" content="model_fn"/>
<meta itemprop="property" content="params"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="eval_dir"/>
<meta itemprop="property" content="evaluate"/>
<meta itemprop="property" content="experimental_export_all_saved_models"/>
<meta itemprop="property" content="export_saved_model"/>
<meta itemprop="property" content="get_variable_names"/>
<meta itemprop="property" content="get_variable_value"/>
<meta itemprop="property" content="latest_checkpoint"/>
<meta itemprop="property" content="predict"/>
<meta itemprop="property" content="train"/>
</div>

# tf.compat.v2.estimator.BaselineClassifier

## Class `BaselineClassifier`

A classifier that can establish a simple baseline.

Inherits From: [`Estimator`](../../../../tf/compat/v2/estimator/Estimator.md)



Defined in [`python/estimator/canned/baseline.py`](https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/canned/baseline.py).

<!-- Placeholder for "Used in" -->

This classifier ignores feature values and will learn to predict the average
value of each label. For single-label problems, this will predict the
probability distribution of the classes as seen in the labels. For multi-label
problems, this will predict the fraction of examples that are positive for
each class.

#### Example:



```python

# Build BaselineClassifier
classifier = BaselineClassifier(n_classes=3)

# Input builders
def input_fn_train:
  # Returns tf.data.Dataset of (x, y) tuple where y represents label's class
  # index.
  pass

def input_fn_eval:
  # Returns tf.data.Dataset of (x, y) tuple where y represents label's class
  # index.
  pass

# Fit model.
classifier.train(input_fn=input_fn_train)

# Evaluate cross entropy between the test and train labels.
loss = classifier.evaluate(input_fn=input_fn_eval)["loss"]

# predict outputs the probability distribution of the classes as seen in
# training.
predictions = classifier.predict(new_samples)

```

Input of `train` and `evaluate` should have following features,
  otherwise there will be a `KeyError`:

* if `weight_column` is not `None`, a feature with
   `key=weight_column` whose value is a `Tensor`.



#### Eager Compatibility
Estimators can be used while eager execution is enabled. Note that `input_fn`
and all hooks are executed inside a graph context, so they have to be written
to be compatible with graph mode. Note that `input_fn` code using <a href="../../../../tf/data.md"><code>tf.data</code></a>
generally works in both graph and eager modes.



<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    model_dir=None,
    n_classes=2,
    weight_column=None,
    label_vocabulary=None,
    optimizer='Ftrl',
    config=None,
    loss_reduction=losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE
)
```

Initializes a BaselineClassifier instance.


#### Args:


* <b>`model_dir`</b>: Directory to save model parameters, graph and etc. This can
  also be used to load checkpoints from the directory into a estimator to
  continue training a previously saved model.
* <b>`n_classes`</b>: number of label classes. Default is binary classification.
  It must be greater than 1. Note: Class labels are integers representing
  the class index (i.e. values from 0 to n_classes-1). For arbitrary
  label values (e.g. string labels), convert to class indices first.
* <b>`weight_column`</b>: A string or a `_NumericColumn` created by
  <a href="../../../../tf/feature_column/numeric_column.md"><code>tf.feature_column.numeric_column</code></a> defining feature column representing
   weights. It will be multiplied by the loss of the example.
* <b>`label_vocabulary`</b>: Optional list of strings with size `[n_classes]`
  defining the label vocabulary. Only supported for `n_classes` > 2.
* <b>`optimizer`</b>: String, `tf.Optimizer` object, or callable that creates the
  optimizer to use for training. If not specified, will use
  `FtrlOptimizer` with a default learning rate of 0.3.
* <b>`config`</b>: `RunConfig` object to configure the runtime settings.
* <b>`loss_reduction`</b>: One of <a href="../../../../tf/losses/Reduction.md"><code>tf.losses.Reduction</code></a> except `NONE`. Describes how
  to reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`.

#### Returns:

A `BaselineClassifier` estimator.



#### Raises:


* <b>`ValueError`</b>: If `n_classes` < 2.



## Properties

<h3 id="config"><code>config</code></h3>




<h3 id="export_savedmodel"><code>export_savedmodel</code></h3>




<h3 id="model_dir"><code>model_dir</code></h3>




<h3 id="model_fn"><code>model_fn</code></h3>

Returns the `model_fn` which is bound to `self.params`.


#### Returns:

The `model_fn` with following signature:
  `def model_fn(features, labels, mode, config)`


<h3 id="params"><code>params</code></h3>






## Methods

<h3 id="eval_dir"><code>eval_dir</code></h3>

``` python
eval_dir(name=None)
```

Shows the directory name where evaluation metrics are dumped.


#### Args:


* <b>`name`</b>: Name of the evaluation if user needs to run multiple evaluations on
  different data sets, such as on training data vs test data. Metrics for
  different evaluations are saved in separate folders, and appear
  separately in tensorboard.


#### Returns:

A string which is the path of directory contains evaluation metrics.


<h3 id="evaluate"><code>evaluate</code></h3>

``` python
evaluate(
    input_fn,
    steps=None,
    hooks=None,
    checkpoint_path=None,
    name=None
)
```

Evaluates the model given evaluation data `input_fn`.

For each step, calls `input_fn`, which returns one batch of data.
Evaluates until:
- `steps` batches are processed, or
- `input_fn` raises an end-of-input exception (<a href="../../../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a>
or
`StopIteration`).

#### Args:


* <b>`input_fn`</b>: A function that constructs the input data for evaluation. See
  [Premade Estimators](
  https://tensorflow.org/guide/premade_estimators#create_input_functions)
  for more information. The
  function should construct and return one of the following:  * A
  <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object: Outputs of `Dataset` object must be a tuple
  `(features, labels)` with same constraints as below. * A tuple
  `(features, labels)`: Where `features` is a <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> or a dictionary
  of string feature name to `Tensor` and `labels` is a `Tensor` or a
  dictionary of string label name to `Tensor`. Both `features` and
  `labels` are consumed by `model_fn`. They should satisfy the expectation
  of `model_fn` from inputs.
* <b>`steps`</b>: Number of steps for which to evaluate model. If `None`, evaluates
  until `input_fn` raises an end-of-input exception.
* <b>`hooks`</b>: List of <a href="../../../../tf/train/SessionRunHook.md"><code>tf.train.SessionRunHook</code></a> subclass instances. Used for
  callbacks inside the evaluation call.
* <b>`checkpoint_path`</b>: Path of a specific checkpoint to evaluate. If `None`, the
  latest checkpoint in `model_dir` is used.  If there are no checkpoints
  in `model_dir`, evaluation is run with newly initialized `Variables`
  instead of ones restored from checkpoint.
* <b>`name`</b>: Name of the evaluation if user needs to run multiple evaluations on
  different data sets, such as on training data vs test data. Metrics for
  different evaluations are saved in separate folders, and appear
  separately in tensorboard.


#### Returns:

A dict containing the evaluation metrics specified in `model_fn` keyed by
name, as well as an entry `global_step` which contains the value of the
global step for which this evaluation was performed. For canned
estimators, the dict contains the `loss` (mean loss per mini-batch) and
the `average_loss` (mean loss per sample). Canned classifiers also return
the `accuracy`. Canned regressors also return the `label/mean` and the
`prediction/mean`.



#### Raises:


* <b>`ValueError`</b>: If `steps <= 0`.

<h3 id="experimental_export_all_saved_models"><code>experimental_export_all_saved_models</code></h3>

``` python
experimental_export_all_saved_models(
    export_dir_base,
    input_receiver_fn_map,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None
)
```

Exports a `SavedModel` with `tf.MetaGraphDefs` for each requested mode.

For each mode passed in via the `input_receiver_fn_map`,
this method builds a new graph by calling the `input_receiver_fn` to obtain
feature and label `Tensor`s. Next, this method calls the `Estimator`'s
`model_fn` in the passed mode to generate the model graph based on
those features and labels, and restores the given checkpoint
(or, lacking that, the most recent checkpoint) into the graph.
Only one of the modes is used for saving variables to the `SavedModel`
(order of preference: <a href="../../../../tf/estimator/ModeKeys.md#TRAIN"><code>tf.estimator.ModeKeys.TRAIN</code></a>,
<a href="../../../../tf/estimator/ModeKeys.md#EVAL"><code>tf.estimator.ModeKeys.EVAL</code></a>, then
<a href="../../../../tf/estimator/ModeKeys.md#PREDICT"><code>tf.estimator.ModeKeys.PREDICT</code></a>), such that up to three
`tf.MetaGraphDefs` are saved with a single set of variables in a single
`SavedModel` directory.

For the variables and `tf.MetaGraphDefs`, a timestamped export directory
below
`export_dir_base`, and writes a `SavedModel` into it containing
the <a href="../../../../tf/MetaGraphDef.md"><code>tf.MetaGraphDef</code></a> for the given mode and its associated signatures.

For prediction, the exported `MetaGraphDef` will provide one `SignatureDef`
for each element of the `export_outputs` dict returned from the `model_fn`,
named using the same keys.  One of these keys is always
<a href="../../../../tf/saved_model/signature_constants.md#DEFAULT_SERVING_SIGNATURE_DEF_KEY"><code>tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY</code></a>,
indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
<a href="../../../../tf/estimator/export/ExportOutput.md"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
receivers provided by
the `serving_input_receiver_fn`.

For training and evaluation, the `train_op` is stored in an extra
collection,
and loss, metrics, and predictions are included in a `SignatureDef` for the
mode in question.

Extra assets may be written into the `SavedModel` via the `assets_extra`
argument.  This should be a dict, where each key gives a destination path
(including the filename) relative to the assets.extra directory.  The
corresponding value gives the full path of the source file to be copied.
For example, the simple case of copying a single file without renaming it
is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

#### Args:


* <b>`export_dir_base`</b>: A string containing a directory in which to create
  timestamped subdirectories containing exported `SavedModel`s.
* <b>`input_receiver_fn_map`</b>: dict of <a href="../../../../tf/estimator/ModeKeys.md"><code>tf.estimator.ModeKeys</code></a> to
  `input_receiver_fn` mappings, where the `input_receiver_fn` is a
  function that takes no arguments and returns the appropriate subclass of
  `InputReceiver`.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
  within the exported `SavedModel`, or `None` if no extra assets are
  needed.
* <b>`as_text`</b>: whether to write the `SavedModel` proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
  the most recent checkpoint found within the model directory is chosen.


#### Returns:

The string path to the exported directory.



#### Raises:


* <b>`ValueError`</b>: if any `input_receiver_fn` is `None`, no `export_outputs`
  are provided, or no checkpoint can be found.

<h3 id="export_saved_model"><code>export_saved_model</code></h3>

``` python
export_saved_model(
    export_dir_base,
    serving_input_receiver_fn,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None,
    experimental_mode=ModeKeys.PREDICT
)
```

Exports inference graph as a `SavedModel` into the given dir.

For a detailed guide, see
[Using SavedModel with Estimators](https://tensorflow.org/guide/saved_model#using_savedmodel_with_estimators).

This method builds a new graph by first calling the
`serving_input_receiver_fn` to obtain feature `Tensor`s, and then calling
this `Estimator`'s `model_fn` to generate the model graph based on those
features. It restores the given checkpoint (or, lacking that, the most
recent checkpoint) into this graph in a fresh session.  Finally it creates
a timestamped export directory below the given `export_dir_base`, and writes
a `SavedModel` into it containing a single <a href="../../../../tf/MetaGraphDef.md"><code>tf.MetaGraphDef</code></a> saved from this
session.

The exported `MetaGraphDef` will provide one `SignatureDef` for each
element of the `export_outputs` dict returned from the `model_fn`, named
using
the same keys.  One of these keys is always
<a href="../../../../tf/saved_model/signature_constants.md#DEFAULT_SERVING_SIGNATURE_DEF_KEY"><code>tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY</code></a>,
indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
<a href="../../../../tf/estimator/export/ExportOutput.md"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
receivers provided by
the `serving_input_receiver_fn`.

Extra assets may be written into the `SavedModel` via the `assets_extra`
argument.  This should be a dict, where each key gives a destination path
(including the filename) relative to the assets.extra directory.  The
corresponding value gives the full path of the source file to be copied.
For example, the simple case of copying a single file without renaming it
is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

The experimental_mode parameter can be used to export a single
train/eval/predict graph as a `SavedModel`.
See `experimental_export_all_saved_models` for full docs.

#### Args:


* <b>`export_dir_base`</b>: A string containing a directory in which to create
  timestamped subdirectories containing exported `SavedModel`s.
* <b>`serving_input_receiver_fn`</b>: A function that takes no argument and returns a
  <a href="../../../../tf/estimator/export/ServingInputReceiver.md"><code>tf.estimator.export.ServingInputReceiver</code></a> or
  <a href="../../../../tf/estimator/export/TensorServingInputReceiver.md"><code>tf.estimator.export.TensorServingInputReceiver</code></a>.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
  within the exported `SavedModel`, or `None` if no extra assets are
  needed.
* <b>`as_text`</b>: whether to write the `SavedModel` proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
  the most recent checkpoint found within the model directory is chosen.
* <b>`experimental_mode`</b>: <a href="../../../../tf/estimator/ModeKeys.md"><code>tf.estimator.ModeKeys</code></a> value indicating with mode
  will be exported. Note that this feature is experimental.


#### Returns:

The string path to the exported directory.



#### Raises:


* <b>`ValueError`</b>: if no `serving_input_receiver_fn` is provided, no
`export_outputs` are provided, or no checkpoint can be found.

<h3 id="get_variable_names"><code>get_variable_names</code></h3>

``` python
get_variable_names()
```

Returns list of all variable names in this model.


#### Returns:

List of names.



#### Raises:


* <b>`ValueError`</b>: If the `Estimator` has not produced a checkpoint yet.

<h3 id="get_variable_value"><code>get_variable_value</code></h3>

``` python
get_variable_value(name)
```

Returns value of the variable given by name.


#### Args:


* <b>`name`</b>: string or a list of string, name of the tensor.


#### Returns:

Numpy array - value of the tensor.



#### Raises:


* <b>`ValueError`</b>: If the `Estimator` has not produced a checkpoint yet.

<h3 id="latest_checkpoint"><code>latest_checkpoint</code></h3>

``` python
latest_checkpoint()
```

Finds the filename of the latest saved checkpoint file in `model_dir`.


#### Returns:

The full path to the latest checkpoint or `None` if no checkpoint was
found.


<h3 id="predict"><code>predict</code></h3>

``` python
predict(
    input_fn,
    predict_keys=None,
    hooks=None,
    checkpoint_path=None,
    yield_single_examples=True
)
```

Yields predictions for given features.

Please note that interleaving two predict outputs does not work. See:
[issue/20506](
https://github.com/tensorflow/tensorflow/issues/20506#issuecomment-422208517)

#### Args:


* <b>`input_fn`</b>: A function that constructs the features. Prediction continues
  until `input_fn` raises an end-of-input exception
  (<a href="../../../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a> or `StopIteration`).
  See [Premade Estimators](
  https://tensorflow.org/guide/premade_estimators#create_input_functions)
  for more information. The function should construct and return one of
  the following:

    * A <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object: Outputs of `Dataset` object must have
      same constraints as below.
    * features: A <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> or a dictionary of string feature name to
      `Tensor`. features are consumed by `model_fn`. They should satisfy
      the expectation of `model_fn` from inputs.
    * A tuple, in which case the first item is extracted as features.

* <b>`predict_keys`</b>: list of `str`, name of the keys to predict. It is used if
  the <a href="../../../../tf/estimator/EstimatorSpec.md#predictions"><code>tf.estimator.EstimatorSpec.predictions</code></a> is a `dict`. If
  `predict_keys` is used then rest of the predictions will be filtered
  from the dictionary. If `None`, returns all.
* <b>`hooks`</b>: List of <a href="../../../../tf/train/SessionRunHook.md"><code>tf.train.SessionRunHook</code></a> subclass instances. Used for
  callbacks inside the prediction call.
* <b>`checkpoint_path`</b>: Path of a specific checkpoint to predict. If `None`, the
  latest checkpoint in `model_dir` is used.  If there are no checkpoints
  in `model_dir`, prediction is run with newly initialized `Variables`
  instead of ones restored from checkpoint.
* <b>`yield_single_examples`</b>: If `False`, yields the whole batch as returned by
  the `model_fn` instead of decomposing the batch into individual
  elements. This is useful if `model_fn` returns some tensors whose first
  dimension is not equal to the batch size.


#### Yields:

Evaluated values of `predictions` tensors.



#### Raises:


* <b>`ValueError`</b>: If batch length of predictions is not the same and
  `yield_single_examples` is `True`.
* <b>`ValueError`</b>: If there is a conflict between `predict_keys` and
  `predictions`. For example if `predict_keys` is not `None` but
  <a href="../../../../tf/estimator/EstimatorSpec.md#predictions"><code>tf.estimator.EstimatorSpec.predictions</code></a> is not a `dict`.

<h3 id="train"><code>train</code></h3>

``` python
train(
    input_fn,
    hooks=None,
    steps=None,
    max_steps=None,
    saving_listeners=None
)
```

Trains a model given training data `input_fn`.


#### Args:


* <b>`input_fn`</b>: A function that provides input data for training as minibatches.
  See [Premade Estimators](
  https://tensorflow.org/guide/premade_estimators#create_input_functions)
  for more information. The function should construct and return one of
  the following:
    * A <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object: Outputs of `Dataset` object must be
      a tuple `(features, labels)` with same constraints as below.
    * A tuple `(features, labels)`: Where `features` is a <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> or
      a dictionary of string feature name to `Tensor` and `labels` is a
      `Tensor` or a dictionary of string label name to `Tensor`. Both
      `features` and `labels` are consumed by `model_fn`. They should
      satisfy the expectation of `model_fn` from inputs.
* <b>`hooks`</b>: List of <a href="../../../../tf/train/SessionRunHook.md"><code>tf.train.SessionRunHook</code></a> subclass instances. Used for
  callbacks inside the training loop.
* <b>`steps`</b>: Number of steps for which to train the model. If `None`, train
  forever or train until `input_fn` generates the `tf.errors.OutOfRange`
  error or `StopIteration` exception. `steps` works incrementally. If you
  call two times `train(steps=10)` then training occurs in total 20 steps.
  If `OutOfRange` or `StopIteration` occurs in the middle, training stops
  before 20 steps. If you don't want to have incremental behavior please
  set `max_steps` instead. If set, `max_steps` must be `None`.
* <b>`max_steps`</b>: Number of total steps for which to train model. If `None`,
  train forever or train until `input_fn` generates the
  `tf.errors.OutOfRange` error or `StopIteration` exception. If set,
  `steps` must be `None`. If `OutOfRange` or `StopIteration` occurs in the
  middle, training stops before `max_steps` steps. Two calls to
  `train(steps=100)` means 200 training iterations. On the other hand, two
  calls to `train(max_steps=100)` means that the second call will not do
  any iteration since first call did all 100 steps.
* <b>`saving_listeners`</b>: list of `CheckpointSaverListener` objects. Used for
  callbacks that run immediately before or after checkpoint savings.


#### Returns:

`self`, for chaining.



#### Raises:


* <b>`ValueError`</b>: If both `steps` and `max_steps` are not `None`.
* <b>`ValueError`</b>: If either `steps` or `max_steps <= 0`.



