description: Update '*var' as FOBOS algorithm with fixed learning rate.
robots: noindex

# tf.raw_ops.ApplyProximalGradientDescent

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Update '*var' as FOBOS algorithm with fixed learning rate.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ApplyProximalGradientDescent`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ApplyProximalGradientDescent(
    var, alpha, l1, l2, delta, use_locking=False, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

prox_v = var - alpha * delta
var = sign(prox_v)/(1+alpha*l2) * max{|prox_v|-alpha*l1,0}

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
`alpha`<a id="alpha"></a>
</td>
<td>
A `Tensor`. Must have the same type as `var`.
Scaling factor. Must be a scalar.
</td>
</tr><tr>
<td>
`l1`<a id="l1"></a>
</td>
<td>
A `Tensor`. Must have the same type as `var`.
L1 regularization. Must be a scalar.
</td>
</tr><tr>
<td>
`l2`<a id="l2"></a>
</td>
<td>
A `Tensor`. Must have the same type as `var`.
L2 regularization. Must be a scalar.
</td>
</tr><tr>
<td>
`delta`<a id="delta"></a>
</td>
<td>
A `Tensor`. Must have the same type as `var`. The change.
</td>
</tr><tr>
<td>
`use_locking`<a id="use_locking"></a>
</td>
<td>
An optional `bool`. Defaults to `False`.
If True, the subtraction will be protected by a lock;
otherwise the behavior is undefined, but may exhibit less contention.
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

