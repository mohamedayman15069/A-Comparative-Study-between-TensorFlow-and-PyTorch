description: Computes Relu(x * weight + biases).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.relu_layer" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.relu_layer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/nn_impl.py">View source</a>



Computes Relu(x * weight + biases).


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.relu_layer(
    x, weights, biases, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`<a id="x"></a>
</td>
<td>
a 2D tensor.  Dimensions typically: batch, in_units
</td>
</tr><tr>
<td>
`weights`<a id="weights"></a>
</td>
<td>
a 2D tensor.  Dimensions typically: in_units, out_units
</td>
</tr><tr>
<td>
`biases`<a id="biases"></a>
</td>
<td>
a 1D tensor.  Dimensions: out_units
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
A name for the operation (optional).  If not specified
"nn_relu_layer" is used.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A 2-D Tensor computing relu(matmul(x, weights) + biases).
Dimensions typically: batch, out_units.
</td>
</tr>

</table>

