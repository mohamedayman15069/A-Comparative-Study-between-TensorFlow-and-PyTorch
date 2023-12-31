description: Concats all tensors in the list along the 0th dimension.
robots: noindex

# tf.raw_ops.TensorListConcat

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Concats all tensors in the list along the 0th dimension.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TensorListConcat`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TensorListConcat(
    input_handle, element_dtype, element_shape=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Requires that all tensors have the same shape except the first dimension.

input_handle: The input list.
tensor: The concated result.
lengths: Output tensor containing sizes of the 0th dimension of tensors in the list, used for computing the gradient.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_handle`<a id="input_handle"></a>
</td>
<td>
A `Tensor` of type `variant`.
</td>
</tr><tr>
<td>
`element_dtype`<a id="element_dtype"></a>
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>.
</td>
</tr><tr>
<td>
`element_shape`<a id="element_shape"></a>
</td>
<td>
An optional <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`. Defaults to `None`.
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
A tuple of `Tensor` objects (tensor, lengths).
</td>
</tr>
<tr>
<td>
`tensor`<a id="tensor"></a>
</td>
<td>
A `Tensor` of type `element_dtype`.
</td>
</tr><tr>
<td>
`lengths`<a id="lengths"></a>
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

