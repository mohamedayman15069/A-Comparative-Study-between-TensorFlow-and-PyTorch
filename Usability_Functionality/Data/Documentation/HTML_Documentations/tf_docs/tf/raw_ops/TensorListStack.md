description: Stacks all tensors in the list.
robots: noindex

# tf.raw_ops.TensorListStack

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Stacks all tensors in the list.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TensorListStack`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TensorListStack(
    input_handle, element_shape, element_dtype, num_elements=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Requires that all tensors have the same shape.

input_handle: the input list
tensor: the gathered result
num_elements: optional. If not -1, the number of elements in the list.

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
`element_shape`<a id="element_shape"></a>
</td>
<td>
A `Tensor` of type `int32`.
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
`num_elements`<a id="num_elements"></a>
</td>
<td>
An optional `int`. Defaults to `-1`.
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
A `Tensor` of type `element_dtype`.
</td>
</tr>

</table>

