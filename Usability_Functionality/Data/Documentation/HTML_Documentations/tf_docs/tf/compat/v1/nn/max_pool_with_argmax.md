description: Performs max pooling on the input and outputs both max values and indices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.max_pool_with_argmax" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.max_pool_with_argmax

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/nn_ops.py">View source</a>



Performs max pooling on the input and outputs both max values and indices.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.max_pool_with_argmax(
    input,
    ksize,
    strides,
    padding,
    data_format=&#x27;NHWC&#x27;,
    Targmax=None,
    name=None,
    output_dtype=None,
    include_batch_in_index=False
)
</code></pre>



<!-- Placeholder for "Used in" -->

The indices in `argmax` are flattened, so that a maximum value at position
`[b, y, x, c]` becomes flattened index:
`(y * width + x) * channels + c` if `include_batch_in_index` is False;
`((b * height + y) * width + x) * channels + c` if `include_batch_in_index` is True.

The indices returned are always in `[0, height) x [0, width)` before flattening,
even if padding is involved and the mathematically correct answer is outside
(either negative or too large).  This is a bug, but fixing it is difficult to do
in a safe backwards compatible way, especially due to flattening.

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
4-D with shape `[batch, height, width, channels]`.  Input to pool over.
</td>
</tr><tr>
<td>
`ksize`<a id="ksize"></a>
</td>
<td>
A list of `ints` that has length `>= 4`.
The size of the window for each dimension of the input tensor.
</td>
</tr><tr>
<td>
`strides`<a id="strides"></a>
</td>
<td>
A list of `ints` that has length `>= 4`.
The stride of the sliding window for each dimension of the
input tensor.
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
`Targmax`<a id="Targmax"></a>
</td>
<td>
An optional <a href="../../../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../../../../tf.md#int64"><code>tf.int64</code></a>.
</td>
</tr><tr>
<td>
`include_batch_in_index`<a id="include_batch_in_index"></a>
</td>
<td>
An optional `bool`. Defaults to `False`.
Whether to include batch dimension in flattened index of `argmax`.
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
A tuple of `Tensor` objects (output, argmax).
</td>
</tr>
<tr>
<td>
`output`<a id="output"></a>
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`argmax`<a id="argmax"></a>
</td>
<td>
A `Tensor` of type `Targmax`.
</td>
</tr>
</table>

