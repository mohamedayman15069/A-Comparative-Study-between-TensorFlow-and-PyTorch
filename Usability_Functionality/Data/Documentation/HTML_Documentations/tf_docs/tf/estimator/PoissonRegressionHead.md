description: Creates a Head for poisson regression using <a href="../../tf/nn/log_poisson_loss.md"><code>tf.nn.log_poisson_loss</code></a>. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.PoissonRegressionHead" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_estimator_spec"/>
<meta itemprop="property" content="loss"/>
<meta itemprop="property" content="metrics"/>
<meta itemprop="property" content="predictions"/>
<meta itemprop="property" content="update_metrics"/>
</div>

# tf.estimator.PoissonRegressionHead

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/regression_head.py#L409-L496">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a `Head` for poisson regression using <a href="../../tf/nn/log_poisson_loss.md"><code>tf.nn.log_poisson_loss</code></a>. (deprecated)

Inherits From: [`RegressionHead`](../../tf/estimator/RegressionHead.md), [`Head`](../../tf/estimator/Head.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.PoissonRegressionHead`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.PoissonRegressionHead(
    label_dimension=1,
    weight_column=None,
    loss_reduction=tf.losses.Reduction.SUM_OVER_BATCH_SIZE,
    compute_full_loss=True,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use tf.keras instead.

The loss is the weighted sum over all input dimensions. Namely, if the input
labels have shape `[batch_size, label_dimension]`, the loss is the weighted
sum over both `batch_size` and `label_dimension`.

The head expects `logits` with shape `[D0, D1, ... DN, label_dimension]`.
In many applications, the shape is `[batch_size, label_dimension]`.

The `labels` shape must match `logits`, namely
`[D0, D1, ... DN, label_dimension]`. If `label_dimension=1`, shape
`[D0, D1, ... DN]` is also supported.

If `weight_column` is specified, weights must be of shape
`[D0, D1, ... DN]`, `[D0, D1, ... DN, 1]` or
`[D0, D1, ... DN, label_dimension]`.

This is implemented as a generalized linear model, see
https://en.wikipedia.org/wiki/Generalized_linear_model.

The head can be used with a canned estimator. Example:

```python
my_head = tf.estimator.PoissonRegressionHead()
my_estimator = tf.estimator.DNNEstimator(
    head=my_head,
    hidden_units=...,
    feature_columns=...)
```

It can also be used with a custom `model_fn`. Example:

```python
def _my_model_fn(features, labels, mode):
  my_head = tf.estimator.PoissonRegressionHead()
  logits = tf.keras.Model(...)(features)

  return my_head.create_estimator_spec(
      features=features,
      mode=mode,
      labels=labels,
      optimizer=tf.keras.optimizers.Adagrad(lr=0.1),
      logits=logits)

my_estimator = tf.estimator.Estimator(model_fn=_my_model_fn)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`weight_column`<a id="weight_column"></a>
</td>
<td>
A string or a `NumericColumn` created by
<a href="../../tf/feature_column/numeric_column.md"><code>tf.feature_column.numeric_column</code></a> defining feature column representing
weights. It is used to down weight or boost examples during training. It
will be multiplied by the loss of the example.
</td>
</tr><tr>
<td>
`label_dimension`<a id="label_dimension"></a>
</td>
<td>
Number of regression labels per example. This is the size
of the last dimension of the labels `Tensor` (typically, this has shape
`[batch_size, label_dimension]`).
</td>
</tr><tr>
<td>
`loss_reduction`<a id="loss_reduction"></a>
</td>
<td>
One of `tf.losses.Reduction` except `NONE`. Decides how to
reduce training loss over batch and label dimension. Defaults to
`SUM_OVER_BATCH_SIZE`, namely weighted sum of losses divided by `batch
size * label_dimension`.
</td>
</tr><tr>
<td>
`compute_full_loss`<a id="compute_full_loss"></a>
</td>
<td>
Whether to include the constant `log(z!)` term in
computing the poisson loss. See <a href="../../tf/nn/log_poisson_loss.md"><code>tf.nn.log_poisson_loss</code></a> for the full
documentation.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
name of the head. If provided, summary and metrics keys will be
suffixed by `"/" + name`. Also used as `name_scope` when creating ops.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`logits_dimension`<a id="logits_dimension"></a>
</td>
<td>
See `base_head.Head` for details.
</td>
</tr><tr>
<td>
`loss_reduction`<a id="loss_reduction"></a>
</td>
<td>
See `base_head.Head` for details.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
See `base_head.Head` for details.
</td>
</tr>
</table>



## Methods

<h3 id="create_estimator_spec"><code>create_estimator_spec</code></h3>

<a target="_blank" class="external" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/base_head.py#L224-L292">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_estimator_spec(
    features,
    mode,
    logits,
    labels=None,
    optimizer=None,
    trainable_variables=None,
    train_op_fn=None,
    update_ops=None,
    regularization_losses=None
)
</code></pre>

Returns `EstimatorSpec` that a model_fn can return.

It is recommended to pass all args via name.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`features`
</td>
<td>
Input `dict` mapping string feature names to `Tensor` or
`SparseTensor` objects containing the values for that feature in a
minibatch. Often to be used to fetch example-weight tensor.
</td>
</tr><tr>
<td>
`mode`
</td>
<td>
Estimator's `ModeKeys`.
</td>
</tr><tr>
<td>
`logits`
</td>
<td>
Logits `Tensor` to be used by the head.
</td>
</tr><tr>
<td>
`labels`
</td>
<td>
Labels `Tensor`, or `dict` mapping string label names to `Tensor`
objects of the label values.
</td>
</tr><tr>
<td>
`optimizer`
</td>
<td>
An <a href="../../tf/keras/optimizers/Optimizer.md"><code>tf.keras.optimizers.Optimizer</code></a> instance to optimize the
loss in TRAIN mode. Namely, sets `train_op = optimizer.get_updates(loss,
trainable_variables)`, which updates variables to minimize `loss`.
</td>
</tr><tr>
<td>
`trainable_variables`
</td>
<td>
A list or tuple of `Variable` objects to update to
minimize `loss`. In Tensorflow 1.x, by default these are the list of
variables collected in the graph under the key
`GraphKeys.TRAINABLE_VARIABLES`. As Tensorflow 2.x doesn't have
collections and GraphKeys, trainable_variables need to be passed
explicitly here.
</td>
</tr><tr>
<td>
`train_op_fn`
</td>
<td>
Function that takes a scalar loss `Tensor` and returns an op
to optimize the model with the loss in TRAIN mode. Used if `optimizer`
is `None`. Exactly one of `train_op_fn` and `optimizer` must be set in
TRAIN mode. By default, it is `None` in other modes. If you want to
optimize loss yourself, you can pass `lambda _: tf.no_op()` and then use
  <a href="../../tf/estimator/EstimatorSpec.md#loss"><code>EstimatorSpec.loss</code></a> to compute and apply gradients.
</td>
</tr><tr>
<td>
`update_ops`
</td>
<td>
A list or tuple of update ops to be run at training time. For
example, layers such as BatchNormalization create mean and variance
update ops that need to be run at training time. In Tensorflow 1.x,
these are thrown into an UPDATE_OPS collection. As Tensorflow 2.x
doesn't have collections, update_ops need to be passed explicitly here.
</td>
</tr><tr>
<td>
`regularization_losses`
</td>
<td>
A list of additional scalar losses to be added to
the training loss, such as regularization losses.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`EstimatorSpec`.
</td>
</tr>

</table>



<h3 id="loss"><code>loss</code></h3>

<a target="_blank" class="external" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/regression_head.py#L203-L226">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>loss(
    labels, logits, features=None, mode=None, regularization_losses=None
)
</code></pre>

Return predictions based on keys. See `base_head.Head` for details.


<h3 id="metrics"><code>metrics</code></h3>

<a target="_blank" class="external" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/regression_head.py#L254-L269">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>metrics(
    regularization_losses=None
)
</code></pre>

Creates metrics. See `base_head.Head` for details.


<h3 id="predictions"><code>predictions</code></h3>

<a target="_blank" class="external" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/regression_head.py#L228-L252">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>predictions(
    logits
)
</code></pre>

Return predictions based on keys.

See `base_head.Head` for details.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`logits`
</td>
<td>
logits `Tensor` with shape `[D0, D1, ... DN, logits_dimension]`.
For many applications, the shape is `[batch_size, logits_dimension]`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dict of predictions.
</td>
</tr>

</table>



<h3 id="update_metrics"><code>update_metrics</code></h3>

<a target="_blank" class="external" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/head/regression_head.py#L271-L297">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_metrics(
    eval_metrics, features, logits, labels, regularization_losses=None
)
</code></pre>

Updates eval metrics. See `base_head.Head` for details.




