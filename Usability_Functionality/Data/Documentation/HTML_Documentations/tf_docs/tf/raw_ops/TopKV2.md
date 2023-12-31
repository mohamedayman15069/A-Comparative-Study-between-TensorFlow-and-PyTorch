description: Finds values and indices of the k largest elements for the last dimension.
robots: noindex

# tf.raw_ops.TopKV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Finds values and indices of the `k` largest elements for the last dimension.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TopKV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TopKV2(
    input,
    k,
    sorted=True,
    index_type=<a href="../../tf/dtypes.md#int32"><code>tf.dtypes.int32</code></a>,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If the input is a vector (rank-1), finds the `k` largest entries in the vector
and outputs their values and indices as vectors.  Thus `values[j]` is the
`j`-th largest entry in `input`, and its index is `indices[j]`.

For matrices (resp. higher rank input), computes the top `k` entries in each
row (resp. vector along the last dimension).  Thus,

    values.shape = indices.shape = input.shape[:-1] + [k]

If two elements are equal, the lower-index element appears first.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`<a id="input"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
1-D or higher with last dimension at least `k`.
</td>
</tr><tr>
<td>
`k`<a id="k"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `int16`, `int32`, `int64`.
0-D.  Number of top elements to look for along the last dimension (along each
row for matrices).
</td>
</tr><tr>
<td>
`sorted`<a id="sorted"></a>
</td>
<td>
An optional `bool`. Defaults to `True`.
If true the resulting `k` elements will be sorted by the values in
descending order.
</td>
</tr><tr>
<td>
`index_type`<a id="index_type"></a>
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int16, tf.int32, tf.int64`. Defaults to <a href="../../tf.md#int32"><code>tf.int32</code></a>.
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
A tuple of `Tensor` objects (values, indices).
</td>
</tr>
<tr>
<td>
`values`<a id="values"></a>
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`indices`<a id="indices"></a>
</td>
<td>
A `Tensor` of type `index_type`.
</td>
</tr>
</table>

