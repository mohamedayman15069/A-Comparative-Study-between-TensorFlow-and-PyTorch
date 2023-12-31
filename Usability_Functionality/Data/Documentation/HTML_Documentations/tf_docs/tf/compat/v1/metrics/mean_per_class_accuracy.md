description: Calculates the mean of the per-class accuracies.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.metrics.mean_per_class_accuracy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.metrics.mean_per_class_accuracy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/metrics_impl.py">View source</a>



Calculates the mean of the per-class accuracies.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.metrics.mean_per_class_accuracy(
    labels,
    predictions,
    num_classes,
    weights=None,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Calculates the accuracy for each class, then takes the mean of that.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates the accuracy of each class and returns
them.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`labels`<a id="labels"></a>
</td>
<td>
A `Tensor` of ground truth labels with shape [batch size] and of
type `int32` or `int64`. The tensor will be flattened if its rank > 1.
</td>
</tr><tr>
<td>
`predictions`<a id="predictions"></a>
</td>
<td>
A `Tensor` of prediction results for semantic labels, whose
shape is [batch size] and type `int32` or `int64`. The tensor will be
flattened if its rank > 1.
</td>
</tr><tr>
<td>
`num_classes`<a id="num_classes"></a>
</td>
<td>
The possible number of labels the prediction task can
have. This value must be provided, since two variables with shape =
[num_classes] will be allocated.
</td>
</tr><tr>
<td>
`weights`<a id="weights"></a>
</td>
<td>
Optional `Tensor` whose rank is either 0, or the same rank as
`labels`, and must be broadcastable to `labels` (i.e., all dimensions must
be either `1`, or the same as the corresponding `labels` dimension).
</td>
</tr><tr>
<td>
`metrics_collections`<a id="metrics_collections"></a>
</td>
<td>
An optional list of collections that
`mean_per_class_accuracy'
should be added to.
</td>
</tr><tr>
<td>
`updates_collections`<a id="updates_collections"></a>
</td>
<td>
An optional list of collections `update_op` should be
added to.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
An optional variable_scope name.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`mean_accuracy`<a id="mean_accuracy"></a>
</td>
<td>
A `Tensor` representing the mean per class accuracy.
</td>
</tr><tr>
<td>
`update_op`<a id="update_op"></a>
</td>
<td>
An operation that updates the accuracy tensor.
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
If `predictions` and `labels` have mismatched shapes, or if
`weights` is not `None` and its shape doesn't match `predictions`, or if
either `metrics_collections` or `updates_collections` are not a list or
tuple.
</td>
</tr><tr>
<td>
`RuntimeError`<a id="RuntimeError"></a>
</td>
<td>
If eager execution is enabled.
</td>
</tr>
</table>

