<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.losses.compute_weighted_loss" />
<meta itemprop="path" content="Stable" />
</div>

# tf.losses.compute_weighted_loss

Computes the weighted loss.

### Aliases:

* `tf.compat.v1.losses.compute_weighted_loss`
* `tf.compat.v2.compat.v1.losses.compute_weighted_loss`
* `tf.losses.compute_weighted_loss`

``` python
tf.losses.compute_weighted_loss(
    losses,
    weights=1.0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`losses`</b>: `Tensor` of shape `[batch_size, d1, ... dN]`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
  `losses`, and must be broadcastable to `losses` (i.e., all dimensions must
  be either `1`, or the same as the corresponding `losses` dimension).
* <b>`scope`</b>: the scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: the loss will be added to these collections.
* <b>`reduction`</b>: Type of reduction to apply to loss.


#### Returns:

Weighted loss `Tensor` of the same type as `losses`. If `reduction` is
`NONE`, this has the same shape as `losses`; otherwise, it is scalar.



#### Raises:


* <b>`ValueError`</b>: If `weights` is `None` or the shape is not compatible with
  `losses`, or if the number of dimensions (rank) of either `losses` or
  `weights` is missing.


#### Note:

When calculating the gradient of a weighted loss contributions from
both `losses` and `weights` are considered. If your `weights` depend
on some model parameters but you do not want this to affect the loss
gradient, you need to apply <a href="../../tf/stop_gradient.md"><code>tf.stop_gradient</code></a> to `weights` before
passing them to `compute_weighted_loss`.




#### Eager Compatibility
The `loss_collection` argument is ignored when executing eagerly. Consider
holding on to the return value or collecting losses via a <a href="../../tf/keras/Model.md"><code>tf.keras.Model</code></a>.

