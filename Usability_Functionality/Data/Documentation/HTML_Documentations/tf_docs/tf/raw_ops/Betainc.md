description: Compute the regularized incomplete beta integral \\(I_x(a, b)\\).
robots: noindex

# tf.raw_ops.Betainc

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Compute the regularized incomplete beta integral \\(I_x(a, b)\\).


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Betainc`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Betainc(
    a, b, x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The regularized incomplete beta integral is defined as:


\\(I_x(a, b) = \frac{B(x; a, b)}{B(a, b)}\\)

where


\\(B(x; a, b) = \int_0^x t^{a-1} (1 - t)^{b-1} dt\\)


is the incomplete beta function and \\(B(a, b)\\) is the *complete*
beta function.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`a`<a id="a"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`.
</td>
</tr><tr>
<td>
`b`<a id="b"></a>
</td>
<td>
A `Tensor`. Must have the same type as `a`.
</td>
</tr><tr>
<td>
`x`<a id="x"></a>
</td>
<td>
A `Tensor`. Must have the same type as `a`.
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
A `Tensor`. Has the same type as `a`.
</td>
</tr>

</table>

