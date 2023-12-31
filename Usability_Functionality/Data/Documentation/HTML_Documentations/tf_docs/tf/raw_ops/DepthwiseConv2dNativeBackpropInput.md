description: Computes the gradients of depthwise convolution with respect to the input.
robots: noindex

# tf.raw_ops.DepthwiseConv2dNativeBackpropInput

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the gradients of depthwise convolution with respect to the input.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DepthwiseConv2dNativeBackpropInput`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DepthwiseConv2dNativeBackpropInput(
    input_sizes,
    filter,
    out_backprop,
    strides,
    padding,
    explicit_paddings=[],
    data_format=&#x27;NHWC&#x27;,
    dilations=[1, 1, 1, 1],
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
A `Tensor` of type `int32`.
An integer vector representing the shape of `input`, based
on `data_format`.  For example, if `data_format` is 'NHWC' then
 `input` is a 4-D `[batch, height, width, channels]` tensor.
</td>
</tr><tr>
<td>
`filter`<a id="filter"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
4-D with shape
`[filter_height, filter_width, in_channels, depthwise_multiplier]`.
</td>
</tr><tr>
<td>
`out_backprop`<a id="out_backprop"></a>
</td>
<td>
A `Tensor`. Must have the same type as `filter`.
4-D with shape  based on `data_format`.
For example, if `data_format` is 'NHWC' then
out_backprop shape is `[batch, out_height, out_width, out_channels]`.
Gradients w.r.t. the output of the convolution.
</td>
</tr><tr>
<td>
`strides`<a id="strides"></a>
</td>
<td>
A list of `ints`.
The stride of the sliding window for each dimension of the input
of the convolution.
</td>
</tr><tr>
<td>
`padding`<a id="padding"></a>
</td>
<td>
A `string` from: `"SAME", "VALID", "EXPLICIT"`.
The type of padding algorithm to use.
</td>
</tr><tr>
<td>
`explicit_paddings`<a id="explicit_paddings"></a>
</td>
<td>
An optional list of `ints`. Defaults to `[]`.
</td>
</tr><tr>
<td>
`data_format`<a id="data_format"></a>
</td>
<td>
An optional `string` from: `"NHWC", "NCHW"`. Defaults to `"NHWC"`.
Specify the data format of the input and output data. With the
default format "NHWC", the data is stored in the order of:
    [batch, height, width, channels].
Alternatively, the format could be "NCHW", the data storage order of:
    [batch, channels, height, width].
</td>
</tr><tr>
<td>
`dilations`<a id="dilations"></a>
</td>
<td>
An optional list of `ints`. Defaults to `[1, 1, 1, 1]`.
1-D tensor of length 4.  The dilation factor for each dimension of
`input`. If set to k > 1, there will be k-1 skipped cells between each filter
element on that dimension. The dimension order is determined by the value of
`data_format`, see above for details. Dilations in the batch and depth
dimensions must be 1.
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

