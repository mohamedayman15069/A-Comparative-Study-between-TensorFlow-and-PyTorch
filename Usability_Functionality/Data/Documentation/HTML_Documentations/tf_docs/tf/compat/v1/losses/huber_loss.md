description: Adds a [Huber Loss](https://en.wikipedia.org/wiki/Huber_loss) term to the training procedure.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.losses.huber_loss" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.losses.huber_loss

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/losses/losses_impl.py">View source</a>



Adds a [Huber Loss](https://en.wikipedia.org/wiki/Huber_loss) term to the training procedure.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.losses.huber_loss(
    labels,
    predictions,
    weights=1.0,
    delta=1.0,
    scope=None,
    loss_collection=ops.GraphKeys.LOSSES,
    reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
)
</code></pre>



<!-- Placeholder for "Used in" -->

For each value x in `error=labels-predictions`, the following is calculated:

```
  0.5 * x^2                  if |x| <= d
  0.5 * d^2 + d * (|x| - d)  if |x| > d
```

where d is `delta`.

`weights` acts as a coefficient for the loss. If a scalar is provided, then
the loss is simply scaled by the given value. If `weights` is a tensor of size
`[batch_size]`, then the total loss for each sample of the batch is rescaled
by the corresponding element in the `weights` vector. If the shape of
`weights` matches the shape of `predictions`, then the loss of each
measurable element of `predictions` is scaled by the corresponding value of
`weights`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`labels`<a id="labels"></a>
</td>
<td>
The ground truth output tensor, same dimensions as 'predictions'.
</td>
</tr><tr>
<td>
`predictions`<a id="predictions"></a>
</td>
<td>
The predicted outputs.
</td>
</tr><tr>
<td>
`weights`<a id="weights"></a>
</td>
<td>
Optional `Tensor` whose rank is either 0, or the same rank as
`labels`, and must be broadcastable to `labels` (i.e., all dimensions must
be either `1`, or the same as the corresponding `losses` dimension).
</td>
</tr><tr>
<td>
`delta`<a id="delta"></a>
</td>
<td>
`float`, the point where the huber loss function changes from a
quadratic to linear.
</td>
</tr><tr>
<td>
`scope`<a id="scope"></a>
</td>
<td>
The scope for the operations performed in computing the loss.
</td>
</tr><tr>
<td>
`loss_collection`<a id="loss_collection"></a>
</td>
<td>
collection to which the loss will be added.
</td>
</tr><tr>
<td>
`reduction`<a id="reduction"></a>
</td>
<td>
Type of reduction to apply to loss.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Weighted loss float `Tensor`. If `reduction` is `NONE`, this has the same
shape as `labels`; otherwise, it is scalar.
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
If the shape of `predictions` doesn't match that of `labels` or
 if the shape of `weights` is invalid.  Also if `labels` or
`predictions` is None.
</td>
</tr>
</table>




 <section><devsite-expandable expanded>
 <h2 class="showalways">eager compatibility</h2>

The `loss_collection` argument is ignored when executing eagerly. Consider
holding on to the return value or collecting losses via a <a href="../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a>.

 </devsite-expandable></section>

