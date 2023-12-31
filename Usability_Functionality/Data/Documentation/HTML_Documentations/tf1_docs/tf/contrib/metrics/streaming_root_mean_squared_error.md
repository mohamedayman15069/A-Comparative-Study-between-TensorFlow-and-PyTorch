<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.metrics.streaming_root_mean_squared_error" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.metrics.streaming_root_mean_squared_error

Computes the root mean squared error between the labels and predictions. (deprecated)

``` python
tf.contrib.metrics.streaming_root_mean_squared_error(
    predictions,
    labels,
    weights=None,
    metrics_collections=None,
    updates_collections=None,
    name=None
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please switch to tf.metrics.root_mean_squared_error. Note that the order of the labels and predictions arguments has been switched.

The `streaming_root_mean_squared_error` function creates two local variables,
`total` and `count` that are used to compute the root mean squared error.
This average is weighted by `weights`, and it is ultimately returned as
`root_mean_squared_error`: an idempotent operation that takes the square root
of the division of `total` by `count`.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
`root_mean_squared_error`. Internally, a `squared_error` operation computes
the element-wise square of the difference between `predictions` and `labels`.
Then `update_op` increments `total` with the reduced sum of the product of
`weights` and `squared_error`, and it increments `count` with the reduced sum
of `weights`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

#### Args:


* <b>`predictions`</b>: A `Tensor` of arbitrary shape.
* <b>`labels`</b>: A `Tensor` of the same shape as `predictions`.
* <b>`weights`</b>: Optional `Tensor` indicating the frequency with which an example is
  sampled. Rank must be 0, or the same rank as `labels`, and must be
  broadcastable to `labels` (i.e., all dimensions must be either `1`, or the
  same as the corresponding `labels` dimension).
* <b>`metrics_collections`</b>: An optional list of collections that
  `root_mean_squared_error` should be added to.
* <b>`updates_collections`</b>: An optional list of collections that `update_op` should
  be added to.
* <b>`name`</b>: An optional variable_scope name.


#### Returns:


* <b>`root_mean_squared_error`</b>: A `Tensor` representing the current mean, the value
  of `total` divided by `count`.
* <b>`update_op`</b>: An operation that increments the `total` and `count` variables
  appropriately and whose value matches `root_mean_squared_error`.


#### Raises:


* <b>`ValueError`</b>: If `predictions` and `labels` have mismatched shapes, or if
  `weights` is not `None` and its shape doesn't match `predictions`, or if
  either `metrics_collections` or `updates_collections` are not a list or
  tuple.