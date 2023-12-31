description: Performs the average pooling on the input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.avg_pool" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.avg_pool

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/nn_ops.py">View source</a>



Performs the average pooling on the input.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.avg_pool2d`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.avg_pool(
    value,
    ksize,
    strides,
    padding,
    data_format=&#x27;NHWC&#x27;,
    name=None,
    input=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Each entry in `output` is the mean of the corresponding size `ksize`
window in `value`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`<a id="value"></a>
</td>
<td>
A 4-D `Tensor` of shape `[batch, height, width, channels]` and type
`float32`, `float64`, `qint8`, `quint8`, or `qint32`.
</td>
</tr><tr>
<td>
`ksize`<a id="ksize"></a>
</td>
<td>
An int or list of `ints` that has length `1`, `2` or `4`. The size of
the window for each dimension of the input tensor.
</td>
</tr><tr>
<td>
`strides`<a id="strides"></a>
</td>
<td>
An int or list of `ints` that has length `1`, `2` or `4`. The
stride of the sliding window for each dimension of the input tensor.
</td>
</tr><tr>
<td>
`padding`<a id="padding"></a>
</td>
<td>
A string, either `'VALID'` or `'SAME'`. The padding algorithm.
See the "returns" section of <a href="../../../../tf/nn/convolution.md"><code>tf.nn.convolution</code></a> for details.
</td>
</tr><tr>
<td>
`data_format`<a id="data_format"></a>
</td>
<td>
A string. 'NHWC' and 'NCHW' are supported.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
Optional name for the operation.
</td>
</tr><tr>
<td>
`input`<a id="input"></a>
</td>
<td>
Alias for value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with the same type as `value`.  The average pooled output tensor.
</td>
</tr>

</table>

