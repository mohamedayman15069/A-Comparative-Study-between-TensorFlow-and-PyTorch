description: Computes a 2-D depthwise convolution given 4-D input and filter tensors.
robots: noindex

# tf.raw_ops.DepthwiseConv2dNative

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes a 2-D depthwise convolution given 4-D `input` and `filter` tensors.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DepthwiseConv2dNative`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DepthwiseConv2dNative(
    input,
    filter,
    strides,
    padding,
    explicit_paddings=[],
    data_format=&#x27;NHWC&#x27;,
    dilations=[1, 1, 1, 1],
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given an input tensor of shape `[batch, in_height, in_width, in_channels]`
and a filter / kernel tensor of shape
`[filter_height, filter_width, in_channels, channel_multiplier]`, containing
`in_channels` convolutional filters of depth 1, `depthwise_conv2d` applies
a different filter to each input channel (expanding from 1 channel to
`channel_multiplier` channels for each), then concatenates the results
together. Thus, the output has `in_channels * channel_multiplier` channels.

```
for k in 0..in_channels-1
  for q in 0..channel_multiplier-1
    output[b, i, j, k * channel_multiplier + q] =
      sum_{di, dj} input[b, strides[1] * i + di, strides[2] * j + dj, k] *
                        filter[di, dj, k, q]
```

Must have `strides[0] = strides[3] = 1`.  For the most common case of the same
horizontal and vertices strides, `strides = [1, stride, stride, 1]`.

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
</td>
</tr><tr>
<td>
`filter`<a id="filter"></a>
</td>
<td>
A `Tensor`. Must have the same type as `input`.
</td>
</tr><tr>
<td>
`strides`<a id="strides"></a>
</td>
<td>
A list of `ints`.
1-D of length 4.  The stride of the sliding window for each dimension
of `input`.
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

