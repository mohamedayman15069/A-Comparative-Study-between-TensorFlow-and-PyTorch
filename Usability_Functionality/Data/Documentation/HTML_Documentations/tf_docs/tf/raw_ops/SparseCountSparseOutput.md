description: Performs sparse-output bin counting for a sparse tensor input.
robots: noindex

# tf.raw_ops.SparseCountSparseOutput

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Performs sparse-output bin counting for a sparse tensor input.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseCountSparseOutput`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseCountSparseOutput(
    indices,
    values,
    dense_shape,
    weights,
    binary_output,
    minlength=-1,
    maxlength=-1,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

  Counts the number of times each value occurs in the input.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`indices`<a id="indices"></a>
</td>
<td>
A `Tensor` of type `int64`.
Tensor containing the indices of the sparse tensor to count.
</td>
</tr><tr>
<td>
`values`<a id="values"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
Tensor containing values of the sparse tensor to count.
</td>
</tr><tr>
<td>
`dense_shape`<a id="dense_shape"></a>
</td>
<td>
A `Tensor` of type `int64`.
Tensor containing the dense shape of the sparse tensor to count.
</td>
</tr><tr>
<td>
`weights`<a id="weights"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`, `float32`, `float64`.
A Tensor of the same shape as indices containing per-index weight values.
May also be the empty tensor if no weights are used.
</td>
</tr><tr>
<td>
`binary_output`<a id="binary_output"></a>
</td>
<td>
A `bool`.
Whether to output the number of occurrences of each value or 1.
</td>
</tr><tr>
<td>
`minlength`<a id="minlength"></a>
</td>
<td>
An optional `int` that is `>= -1`. Defaults to `-1`.
Minimum value to count. Can be set to -1 for no minimum.
</td>
</tr><tr>
<td>
`maxlength`<a id="maxlength"></a>
</td>
<td>
An optional `int` that is `>= -1`. Defaults to `-1`.
Maximum value to count. Can be set to -1 for no maximum.
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
A tuple of `Tensor` objects (output_indices, output_values, output_dense_shape).
</td>
</tr>
<tr>
<td>
`output_indices`<a id="output_indices"></a>
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`output_values`<a id="output_values"></a>
</td>
<td>
A `Tensor`. Has the same type as `weights`.
</td>
</tr><tr>
<td>
`output_dense_shape`<a id="output_dense_shape"></a>
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

