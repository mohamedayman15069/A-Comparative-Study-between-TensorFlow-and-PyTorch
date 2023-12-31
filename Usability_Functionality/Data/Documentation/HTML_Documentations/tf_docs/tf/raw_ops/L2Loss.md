description: L2 Loss.
robots: noindex

# tf.raw_ops.L2Loss

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



L2 Loss.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.L2Loss`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.L2Loss(
    t, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes half the L2 norm of a tensor without the `sqrt`:

    output = sum(t ** 2) / 2

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`t`<a id="t"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
Typically 2-D, but may have any dimensions.
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
A `Tensor`. Has the same type as `t`.
</td>
</tr>

</table>

