description: Subtracts v into specified rows of x.
robots: noindex

# tf.raw_ops.InplaceSub

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Subtracts `v` into specified rows of `x`.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.InplaceSub`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.InplaceSub(
    x, i, v, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

  Computes y = x; y[i, :] -= v; return y.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`<a id="x"></a>
</td>
<td>
A `Tensor`. A `Tensor` of type T.
</td>
</tr><tr>
<td>
`i`<a id="i"></a>
</td>
<td>
A `Tensor` of type `int32`.
A vector. Indices into the left-most dimension of `x`.
</td>
</tr><tr>
<td>
`v`<a id="v"></a>
</td>
<td>
A `Tensor`. Must have the same type as `x`.
A `Tensor` of type T. Same dimension sizes as x except the first dimension, which must be the same as i's size.
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
A `Tensor`. Has the same type as `x`.
</td>
</tr>

</table>

