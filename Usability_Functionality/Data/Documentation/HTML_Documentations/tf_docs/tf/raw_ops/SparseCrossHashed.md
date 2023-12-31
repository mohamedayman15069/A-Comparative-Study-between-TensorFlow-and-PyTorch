description: Generates sparse cross from a list of sparse and dense tensors.
robots: noindex

# tf.raw_ops.SparseCrossHashed

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Generates sparse cross from a list of sparse and dense tensors.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseCrossHashed`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseCrossHashed(
    indices,
    values,
    shapes,
    dense_inputs,
    num_buckets,
    strong_hash,
    salt,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The op takes two lists, one of 2D `SparseTensor` and one of 2D `Tensor`, each
representing features of one feature column. It outputs a 2D `SparseTensor` with
the batchwise crosses of these features.

For example, if the inputs are

    inputs[0]: SparseTensor with shape = [2, 2]
    [0, 0]: "a"
    [1, 0]: "b"
    [1, 1]: "c"

    inputs[1]: SparseTensor with shape = [2, 1]
    [0, 0]: "d"
    [1, 0]: "e"

    inputs[2]: Tensor [["f"], ["g"]]

then the output will be

    shape = [2, 2]
    [0, 0]: "a_X_d_X_f"
    [1, 0]: "b_X_e_X_g"
    [1, 1]: "c_X_e_X_g"

if hashed_output=true then the output will be

    shape = [2, 2]
    [0, 0]: FingerprintCat64(
                Fingerprint64("f"), FingerprintCat64(
                    Fingerprint64("d"), Fingerprint64("a")))
    [1, 0]: FingerprintCat64(
                Fingerprint64("g"), FingerprintCat64(
                    Fingerprint64("e"), Fingerprint64("b")))
    [1, 1]: FingerprintCat64(
                Fingerprint64("g"), FingerprintCat64(
                    Fingerprint64("e"), Fingerprint64("c")))

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`indices`<a id="indices"></a>
</td>
<td>
A list of `Tensor` objects with type `int64`.
2-D.  Indices of each input `SparseTensor`.
</td>
</tr><tr>
<td>
`values`<a id="values"></a>
</td>
<td>
A list of `Tensor` objects with types from: `int64`, `string`.
1-D.   values of each `SparseTensor`.
</td>
</tr><tr>
<td>
`shapes`<a id="shapes"></a>
</td>
<td>
A list with the same length as `indices` of `Tensor` objects with type `int64`.
1-D.   Shapes of each `SparseTensor`.
</td>
</tr><tr>
<td>
`dense_inputs`<a id="dense_inputs"></a>
</td>
<td>
A list of `Tensor` objects with types from: `int64`, `string`.
2-D.    Columns represented by dense `Tensor`.
</td>
</tr><tr>
<td>
`num_buckets`<a id="num_buckets"></a>
</td>
<td>
A `Tensor` of type `int64`.
It is used if hashed_output is true.
output = hashed_value%num_buckets if num_buckets > 0 else hashed_value.
</td>
</tr><tr>
<td>
`strong_hash`<a id="strong_hash"></a>
</td>
<td>
A `Tensor` of type `bool`.
boolean, if true, siphash with salt will be used instead of farmhash.
</td>
</tr><tr>
<td>
`salt`<a id="salt"></a>
</td>
<td>
A `Tensor` of type `int64`.
Specify the salt that will be used by the siphash function.
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
A tuple of `Tensor` objects (output_indices, output_values, output_shape).
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
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`output_shape`<a id="output_shape"></a>
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

