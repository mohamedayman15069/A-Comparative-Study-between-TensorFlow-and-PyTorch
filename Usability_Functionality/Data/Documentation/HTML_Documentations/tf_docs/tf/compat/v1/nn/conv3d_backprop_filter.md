description: Computes the gradients of 3-D convolution with respect to the filter.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.conv3d_backprop_filter" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.conv3d_backprop_filter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the gradients of 3-D convolution with respect to the filter.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.conv3d_backprop_filter_v2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.conv3d_backprop_filter(
    input: Annotated[Any, TV_Conv3DBackpropFilterV2_T],
    filter_sizes: Annotated[Any, _atypes.Int32],
    out_backprop: Annotated[Any, TV_Conv3DBackpropFilterV2_T],
    strides,
    padding: str,
    data_format: str = &#x27;NDHWC&#x27;,
    dilations=[1, 1, 1, 1, 1],
    name=None
) -> Annotated[Any, TV_Conv3DBackpropFilterV2_T]
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`<a id="input"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
Shape `[batch, depth, rows, cols, in_channels]`.
</td>
</tr><tr>
<td>
`filter_sizes`<a id="filter_sizes"></a>
</td>
<td>
A `Tensor` of type `int32`.
An integer vector representing the tensor shape of `filter`,
where `filter` is a 5-D
`[filter_depth, filter_height, filter_width, in_channels, out_channels]`
tensor.
</td>
</tr><tr>
<td>
`out_backprop`<a id="out_backprop"></a>
</td>
<td>
A `Tensor`. Must have the same type as `input`.
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

