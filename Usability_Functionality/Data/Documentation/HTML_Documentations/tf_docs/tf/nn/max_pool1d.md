description: Performs the max pooling on the input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.max_pool1d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.max_pool1d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/nn_ops.py">View source</a>



Performs the max pooling on the input.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.max_pool1d`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.max_pool1d(
    input, ksize, strides, padding, data_format=&#x27;NWC&#x27;, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note internally this op reshapes and uses the underlying 2d operation.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`<a id="input"></a>
</td>
<td>
A 3-D `Tensor` of the format specified by `data_format`.
</td>
</tr><tr>
<td>
`ksize`<a id="ksize"></a>
</td>
<td>
An int or list of `ints` that has length `1` or `3`. The size of the
window for each dimension of the input tensor.
</td>
</tr><tr>
<td>
`strides`<a id="strides"></a>
</td>
<td>
An int or list of `ints` that has length `1` or `3`. The stride of
the sliding window for each dimension of the input tensor.
</td>
</tr><tr>
<td>
`padding`<a id="padding"></a>
</td>
<td>
Either the `string` `"SAME"` or `"VALID"` indicating the type of
padding algorithm to use, or a list indicating the explicit paddings at
the start and end of each dimension. See
[here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
for more information. When explicit padding is used and data_format is
`"NWC"`, this should be in the form `[[0, 0], [pad_left, pad_right], [0,
0]]`. When explicit padding used and data_format is `"NCW"`, this should
be in the form `[[0, 0], [0, 0], [pad_left, pad_right]]`. When using
explicit padding, the size of the paddings cannot be greater than the
sliding window size.
</td>
</tr><tr>
<td>
`data_format`<a id="data_format"></a>
</td>
<td>
An optional string from: "NWC", "NCW". Defaults to "NWC".
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
A `Tensor` of format specified by `data_format`.
The max pooled output tensor.
</td>
</tr>

</table>

