description: Returns the next representable value of x1 in the direction of x2, element-wise.
robots: noindex

# tf.raw_ops.NextAfter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the next representable value of `x1` in the direction of `x2`, element-wise.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.NextAfter`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.NextAfter(
    x1, x2, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation returns the same result as the C++ std::nextafter function.

It can also return a subnormal number.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x1`<a id="x1"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `float64`, `float32`.
</td>
</tr><tr>
<td>
`x2`<a id="x2"></a>
</td>
<td>
A `Tensor`. Must have the same type as `x1`.
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
A `Tensor`. Has the same type as `x1`.
</td>
</tr>

</table>



 <section><devsite-expandable expanded>
 <h2 class="showalways">cpp compatibility</h2>

Equivalent to C++ std::nextafter function.

 </devsite-expandable></section>

