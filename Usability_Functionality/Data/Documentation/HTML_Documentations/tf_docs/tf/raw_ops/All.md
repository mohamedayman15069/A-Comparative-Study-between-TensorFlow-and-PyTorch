description: Computes the "logical and" of elements across dimensions of a tensor.
robots: noindex

# tf.raw_ops.All

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the "logical and" of elements across dimensions of a tensor.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.All`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.All(
    input, axis, keep_dims=False, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Reduces `input` along the dimensions given in `axis`. Unless
`keep_dims` is true, the rank of the tensor is reduced by 1 for each entry in
`axis`. If `keep_dims` is true, the reduced dimensions are
retained with length 1.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`<a id="input"></a>
</td>
<td>
A `Tensor` of type `bool`. The tensor to reduce.
</td>
</tr><tr>
<td>
`axis`<a id="axis"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
The dimensions to reduce. Must be in the range
`[-rank(input), rank(input))`.
</td>
</tr><tr>
<td>
`keep_dims`<a id="keep_dims"></a>
</td>
<td>
An optional `bool`. Defaults to `False`.
If true, retain reduced dimensions with length 1.
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
A `Tensor` of type `bool`.
</td>
</tr>

</table>

