description: Compute gradients for a FakeQuantWithMinMaxVars operation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.quantization.fake_quant_with_min_max_vars_gradient" />
<meta itemprop="path" content="Stable" />
</div>

# tf.quantization.fake_quant_with_min_max_vars_gradient

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Compute gradients for a FakeQuantWithMinMaxVars operation.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.fake_quant_with_min_max_vars_gradient`, `tf.compat.v1.quantization.fake_quant_with_min_max_vars_gradient`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.quantization.fake_quant_with_min_max_vars_gradient(
    gradients: Annotated[Any, _atypes.Float32],
    inputs: Annotated[Any, _atypes.Float32],
    min: Annotated[Any, _atypes.Float32],
    max: Annotated[Any, _atypes.Float32],
    num_bits: int = 8,
    narrow_range: bool = False,
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
`gradients`<a id="gradients"></a>
</td>
<td>
A `Tensor` of type `float32`.
Backpropagated gradients above the FakeQuantWithMinMaxVars operation.
</td>
</tr><tr>
<td>
`inputs`<a id="inputs"></a>
</td>
<td>
A `Tensor` of type `float32`.
Values passed as inputs to the FakeQuantWithMinMaxVars operation.
min, max: Quantization interval, scalar floats.
</td>
</tr><tr>
<td>
`min`<a id="min"></a>
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`max`<a id="max"></a>
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`num_bits`<a id="num_bits"></a>
</td>
<td>
An optional `int`. Defaults to `8`.
The bitwidth of the quantization; between 2 and 8, inclusive.
</td>
</tr><tr>
<td>
`narrow_range`<a id="narrow_range"></a>
</td>
<td>
An optional `bool`. Defaults to `False`.
Whether to quantize into 2^num_bits - 1 distinct values.
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
A tuple of `Tensor` objects (backprops_wrt_input, backprop_wrt_min, backprop_wrt_max).
</td>
</tr>
<tr>
<td>
`backprops_wrt_input`<a id="backprops_wrt_input"></a>
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`backprop_wrt_min`<a id="backprop_wrt_min"></a>
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`backprop_wrt_max`<a id="backprop_wrt_max"></a>
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr>
</table>

