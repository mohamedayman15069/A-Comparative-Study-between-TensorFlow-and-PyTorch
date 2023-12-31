<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.losses.log_loss" />
<meta itemprop="path" content="Stable" />
</div>

# tf.losses.log_loss

Adds a Log Loss term to the training procedure.

### Aliases:

* `tf.compat.v1.losses.log_loss`
* `tf.compat.v2.compat.v1.losses.log_loss`
* `tf.losses.log_loss`

``` python
tf.losses.log_loss(
    labels,
    predictions,
    weights=1.0,
    epsilon=1e-07,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
)
```

<!-- Placeholder for "Used in" -->

`weights` acts as a coefficient for the loss. If a scalar is provided, then
the loss is simply scaled by the given value. If `weights` is a tensor of size
`[batch_size]`, then the total loss for each sample of the batch is rescaled
by the corresponding element in the `weights` vector. If the shape of
`weights` matches the shape of `predictions`, then the loss of each
measurable element of `predictions` is scaled by the corresponding value of
`weights`.

#### Args:


* <b>`labels`</b>: The ground truth output tensor, same dimensions as 'predictions'.
* <b>`predictions`</b>: The predicted outputs.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
  `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
  be either `1`, or the same as the corresponding `losses` dimension).
* <b>`epsilon`</b>: A small increment to add to avoid taking a log of zero.
* <b>`scope`</b>: The scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: collection to which the loss will be added.
* <b>`reduction`</b>: Type of reduction to apply to loss.


#### Returns:

Weighted loss float `Tensor`. If `reduction` is `NONE`, this has the same
shape as `labels`; otherwise, it is scalar.



#### Raises:


* <b>`ValueError`</b>: If the shape of `predictions` doesn't match that of `labels` or
  if the shape of `weights` is invalid.  Also if `labels` or `predictions`
  is None.



#### Eager Compatibility
The `loss_collection` argument is ignored when executing eagerly. Consider
holding on to the return value or collecting losses via a <a href="../../tf/keras/Model.md"><code>tf.keras.Model</code></a>.

