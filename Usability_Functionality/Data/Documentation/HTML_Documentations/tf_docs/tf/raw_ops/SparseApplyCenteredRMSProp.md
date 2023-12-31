description: Update '*var' according to the centered RMSProp algorithm.
robots: noindex

# tf.raw_ops.SparseApplyCenteredRMSProp

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Update '*var' according to the centered RMSProp algorithm.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseApplyCenteredRMSProp`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseApplyCenteredRMSProp(
    var,
    mg,
    ms,
    mom,
    lr,
    rho,
    momentum,
    epsilon,
    grad,
    indices,
    use_locking=False,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The centered RMSProp algorithm uses an estimate of the centered second moment
(i.e., the variance) for normalization, as opposed to regular RMSProp, which
uses the (uncentered) second moment. This often helps with training, but is
slightly more expensive in terms of computation and memory.

Note that in dense implementation of this algorithm, mg, ms, and mom will
update even if the grad is zero, but in this sparse implementation, mg, ms,
and mom will not update in iterations during which the grad is zero.

mean_square = decay * mean_square + (1-decay) * gradient ** 2
mean_grad = decay * mean_grad + (1-decay) * gradient
Delta = learning_rate * gradient / sqrt(mean_square + epsilon - mean_grad ** 2)

$$ms <- rho * ms_{t-1} + (1-rho) * grad * grad$$
$$mom <- momentum * mom_{t-1} + lr * grad / sqrt(ms + epsilon)$$
$$var <- var - mom$$

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`var`<a id="var"></a>
</td>
<td>
A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
Should be from a Variable().
</td>
</tr><tr>
<td>
`mg`<a id="mg"></a>
</td>
<td>
A mutable `Tensor`. Must have the same type as `var`.
Should be from a Variable().
</td>
</tr><tr>
<td>
`ms`<a id="ms"></a>
</td>
<td>
A mutable `Tensor`. Must have the same type as `var`.
Should be from a Variable().
</td>
</tr><tr>
<td>
`mom`<a id="mom"></a>
</td>
<td>
A mutable `Tensor`. Must have the same type as `var`.
Should be from a Variable().
</td>
</tr><tr>
<td>
`lr`<a id="lr"></a>
</td>
<td>
A `Tensor`. Must have the same type as `var`.
Scaling factor. Must be a scalar.
</td>
</tr><tr>
<td>
`rho`<a id="rho"></a>
</td>
<td>
A `Tensor`. Must have the same type as `var`.
Decay rate. Must be a scalar.
</td>
</tr><tr>
<td>
`momentum`<a id="momentum"></a>
</td>
<td>
A `Tensor`. Must have the same type as `var`.
</td>
</tr><tr>
<td>
`epsilon`<a id="epsilon"></a>
</td>
<td>
A `Tensor`. Must have the same type as `var`.
Ridge term. Must be a scalar.
</td>
</tr><tr>
<td>
`grad`<a id="grad"></a>
</td>
<td>
A `Tensor`. Must have the same type as `var`. The gradient.
</td>
</tr><tr>
<td>
`indices`<a id="indices"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A vector of indices into the first dimension of var, ms and mom.
</td>
</tr><tr>
<td>
`use_locking`<a id="use_locking"></a>
</td>
<td>
An optional `bool`. Defaults to `False`.
If `True`, updating of the var, mg, ms, and mom tensors is
protected by a lock; otherwise the behavior is undefined, but may exhibit less
contention.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A mutable `Tensor`. Has the same type as `var`.
</td>
</tr>

</table>

