description: Computes the approximate AUC via a Riemann sum. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.metrics.auc" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.metrics.auc

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/metrics_impl.py">View source</a>



Computes the approximate AUC via a Riemann sum. (deprecated)


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.metrics.auc(
    labels,
    predictions,
    weights=None,
    num_thresholds=200,
    metrics_collections=None,
    updates_collections=None,
    curve=&#x27;ROC&#x27;,
    name=None,
    summation_method=&#x27;trapezoidal&#x27;,
    thresholds=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
The value of AUC returned by this may race with the update so this is deprecated. Please use tf.keras.metrics.AUC instead.

The `auc` function creates four local variables, `true_positives`,
`true_negatives`, `false_positives` and `false_negatives` that are used to
compute the AUC. To discretize the AUC curve, a linearly spaced set of
thresholds is used to compute pairs of recall and precision values. The area
under the ROC-curve is therefore computed using the height of the recall
values by the false positive rate, while the area under the PR-curve is the
computed using the height of the precision values by the recall.

This value is ultimately returned as `auc`, an idempotent operation that
computes the area under a discretized curve of precision versus recall values
(computed using the aforementioned variables). The `num_thresholds` variable
controls the degree of discretization with larger numbers of thresholds more
closely approximating the true AUC. The quality of the approximation may vary
dramatically depending on `num_thresholds`.

For best results, `predictions` should be distributed approximately uniformly
in the range [0, 1] and not peaked around 0 or 1. The quality of the AUC
approximation may be poor if this is not the case. Setting `summation_method`
to 'minoring' or 'majoring' can help quantify the error in the approximation
by providing lower or upper bound estimate of the AUC. The `thresholds`
parameter can be used to manually specify thresholds which split the
predictions more evenly.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the `auc`.

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
A `Tensor` whose shape matches `predictions`. Will be cast to
`bool`.
</td>
</tr><tr>
<td>
`predictions`<a id="predictions"></a>
</td>
<td>
A floating point `Tensor` of arbitrary shape and whose values
are in the range `[0, 1]`.
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
`num_thresholds`<a id="num_thresholds"></a>
</td>
<td>
The number of thresholds to use when discretizing the roc
curve.
</td>
</tr><tr>
<td>
`metrics_collections`<a id="metrics_collections"></a>
</td>
<td>
An optional list of collections that `auc` should be
added to.
</td>
</tr><tr>
<td>
`updates_collections`<a id="updates_collections"></a>
</td>
<td>
An optional list of collections that `update_op` should
be added to.
</td>
</tr><tr>
<td>
`curve`<a id="curve"></a>
</td>
<td>
Specifies the name of the curve to be computed, 'ROC' [default] or
'PR' for the Precision-Recall-curve.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
An optional variable_scope name.
</td>
</tr><tr>
<td>
`summation_method`<a id="summation_method"></a>
</td>
<td>
Specifies the Riemann summation method used
(https://en.wikipedia.org/wiki/Riemann_sum): 'trapezoidal' [default] that
applies the trapezoidal rule; 'careful_interpolation', a variant of it
differing only by a more correct interpolation scheme for PR-AUC -
interpolating (true/false) positives but not the ratio that is precision;
'minoring' that applies left summation for increasing intervals and right
summation for decreasing intervals; 'majoring' that does the opposite.
Note that 'careful_interpolation' is strictly preferred to 'trapezoidal'
(to be deprecated soon) as it applies the same method for ROC, and a
better one (see Davis & Goadrich 2006 for details) for the PR curve.
</td>
</tr><tr>
<td>
`thresholds`<a id="thresholds"></a>
</td>
<td>
An optional list of floating point values to use as the
thresholds for discretizing the curve. If set, the `num_thresholds`
parameter is ignored. Values should be in [0, 1]. Endpoint thresholds
equal to {-epsilon, 1+epsilon} for a small positive epsilon value will be
automatically included with these to correctly handle predictions equal to
 exactly 0 or 1.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`auc`<a id="auc"></a>
</td>
<td>
A scalar `Tensor` representing the current area-under-curve.
</td>
</tr><tr>
<td>
`update_op`<a id="update_op"></a>
</td>
<td>
An operation that increments the `true_positives`,
`true_negatives`, `false_positives` and `false_negatives` variables
appropriately and whose value matches `auc`.
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

