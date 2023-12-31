description: Computes the gradients of 3-D convolution with respect to the input.
robots: noindex

# tf.raw_ops.Conv3DBackpropInputV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the gradients of 3-D convolution with respect to the input.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Conv3DBackpropInputV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Conv3DBackpropInputV2(
    input_sizes,
    filter,
    out_backprop,
    strides,
    padding,
    data_format=&#x27;NDHWC&#x27;,
    dilations=[1, 1, 1, 1, 1],
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_sizes`<a id="input_sizes"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
An integer vector representing the tensor shape of `input`,
where `input` is a 5-D
`[batch, depth, rows, cols, in_channels]` tensor.
</td>
</tr><tr>
<td>
`filter`<a id="filter"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
Shape `[depth, rows, cols, in_channels, out_channels]`.
`in_channels` must match between `input` and `filter`.
</td>
</tr><tr>
<td>
`out_backprop`<a id="out_backprop"></a>
</td>
<td>
A `Tensor`. Must have the same type as `filter`.
Backprop signal of shape `[batch, out_depth, out_rows, out_cols,
out_channels]`.
</td>
</tr><tr>
<td>
`strides`<a id="strides"></a>
</td>
<td>
A list of `ints` that has length `>= 5`.
1-D tensor of length 5. The stride of the sliding window for each
dimension of `input`. Must have `strides[0] = strides[4] = 1`.
</td>
</tr><tr>
<td>
`padding`<a id="padding"></a>
</td>
<td>
A `string` from: `"SAME", "VALID"`.
The type of padding algorithm to use.
</td>
</tr><tr>
<td>
`data_format`<a id="data_format"></a>
</td>
<td>
An optional `string` from: `"NDHWC", "NCDHW"`. Defaults to `"NDHWC"`.
The data format of the input and output data. With the
default format "NDHWC", the data is stored in the order of:
    [batch, in_depth, in_height, in_width, in_channels].
Alternatively, the format could be "NCDHW", the data storage order is:
    [batch, in_channels, in_depth, in_height, in_width].
</td>
</tr><tr>
<td>
`dilations`<a id="dilations"></a>
</td>
<td>
An optional list of `ints`. Defaults to `[1, 1, 1, 1, 1]`.
1-D tensor of length 5.  The dilation factor for each dimension of
`input`. If set to k > 1, there will be k-1 skipped cells between each
filter element on that dimension. The dimension order is determined by the
value of `data_format`, see above for details. Dilations in the batch and
depth dimensions must be 1.
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
A `Tensor`. Has the same type as `filter`.
</td>
</tr>

</table>

