description: Computes the LU decomposition of one or more square matrices.
robots: noindex

# tf.raw_ops.Lu

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the LU decomposition of one or more square matrices.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Lu`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Lu(
    input,
    output_idx_type=<a href="../../tf/dtypes.md#int32"><code>tf.dtypes.int32</code></a>,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices.

The input has to be invertible.

The output consists of two tensors LU and P containing the LU decomposition
of all input submatrices `[..., :, :]`. LU encodes the lower triangular and
upper triangular factors.

For each input submatrix of shape `[M, M]`, L is a lower triangular matrix of
shape `[M, M]` with unit diagonal whose entries correspond to the strictly lower
triangular part of LU. U is a upper triangular matrix of shape `[M, M]` whose
entries correspond to the upper triangular part, including the diagonal, of LU.

P represents a permutation matrix encoded as a list of indices each between `0`
and `M-1`, inclusive. If P_mat denotes the permutation matrix corresponding to
P, then the L, U and P satisfies P_mat * input = L * U.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`<a id="input"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
A tensor of shape `[..., M, M]` whose inner-most 2 dimensions form matrices of
size `[M, M]`.
</td>
</tr><tr>
<td>
`output_idx_type`<a id="output_idx_type"></a>
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../../tf.md#int32"><code>tf.int32</code></a>.
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
A tuple of `Tensor` objects (lu, p).
</td>
</tr>
<tr>
<td>
`lu`<a id="lu"></a>
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`p`<a id="p"></a>
</td>
<td>
A `Tensor` of type `output_idx_type`.
</td>
</tr>
</table>

