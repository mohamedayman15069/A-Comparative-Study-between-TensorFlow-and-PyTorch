<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.metrics.specificity_at_sensitivity" />
<meta itemprop="path" content="Stable" />
</div>

# tf.metrics.specificity_at_sensitivity

Computes the specificity at a given sensitivity.

### Aliases:

* `tf.compat.v1.metrics.specificity_at_sensitivity`
* `tf.compat.v2.compat.v1.metrics.specificity_at_sensitivity`
* `tf.metrics.specificity_at_sensitivity`

``` python
tf.metrics.specificity_at_sensitivity(
    labels,
    predictions,
    sensitivity,
    weights=None,
    num_thresholds=200,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```

<!-- Placeholder for "Used in" -->

The `specificity_at_sensitivity` function creates four local
variables, `true_positives`, `true_negatives`, `false_positives` and
`false_negatives` that are used to compute the specificity at the given
sensitivity value. The threshold for the given sensitivity value is computed
and used to evaluate the corresponding specificity.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
`specificity`. `update_op` increments the `true_positives`, `true_negatives`,
`false_positives` and `false_negatives` counts with the weight of each case
found in the `predictions` and `labels`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

For additional information about specificity and sensitivity, see the
following: https://en.wikipedia.org/wiki/Sensitivity_and_specificity

#### Args:


* <b>`labels`</b>: The ground truth values, a `Tensor` whose dimensions must match
  `predictions`. Will be cast to `bool`.
* <b>`predictions`</b>: A floating point `Tensor` of arbitrary shape and whose values
  are in the range `[0, 1]`.
* <b>`sensitivity`</b>: A scalar value in range `[0, 1]`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
  `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
  be either `1`, or the same as the corresponding `labels` dimension).
* <b>`num_thresholds`</b>: The number of thresholds to use for matching the given
  sensitivity.
* <b>`metrics_collections`</b>: An optional list of collections that `specificity`
  should be added to.
* <b>`updates_collections`</b>: An optional list of collections that `update_op` should
  be added to.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:


* <b>`specificity`</b>: A scalar `Tensor` representing the specificity at the given
  `sensitivity` value.
* <b>`update_op`</b>: An operation that increments the `true_positives`,
  `true_negatives`, `false_positives` and `false_negatives` variables
  appropriately and whose value matches `specificity`.


#### Raises:


* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, if
  `weights` is not `None` and its shape doesn't match `predictions`, or if
  `sensitivity` is not between 0 and 1, or if either `metrics_collections`
  or `updates_collections` are not a list or tuple.
* <b>`RuntimeError`</b>: If eager execution is enabled.