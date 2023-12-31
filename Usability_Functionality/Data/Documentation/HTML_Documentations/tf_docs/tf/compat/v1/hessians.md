description: Constructs the Hessian of sum of ys with respect to x in xs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.hessians" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.hessians

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/gradients_impl.py">View source</a>



Constructs the Hessian of sum of `ys` with respect to `x` in `xs`.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.hessians(
    ys,
    xs,
    name=&#x27;hessians&#x27;,
    colocate_gradients_with_ops=False,
    gate_gradients=False,
    aggregation_method=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`hessians()` adds ops to the graph to output the Hessian matrix of `ys`
with respect to `xs`.  It returns a list of `Tensor` of length `len(xs)`
where each tensor is the Hessian of `sum(ys)`.

The Hessian is a matrix of second-order partial derivatives of a scalar
tensor (see https://en.wikipedia.org/wiki/Hessian_matrix for more details).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ys`<a id="ys"></a>
</td>
<td>
A `Tensor` or list of tensors to be differentiated.
</td>
</tr><tr>
<td>
`xs`<a id="xs"></a>
</td>
<td>
A `Tensor` or list of tensors to be used for differentiation.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
Optional name to use for grouping all the gradient ops together.
defaults to 'hessians'.
</td>
</tr><tr>
<td>
`colocate_gradients_with_ops`<a id="colocate_gradients_with_ops"></a>
</td>
<td>
See `gradients()` documentation for details.
</td>
</tr><tr>
<td>
`gate_gradients`<a id="gate_gradients"></a>
</td>
<td>
See `gradients()` documentation for details.
</td>
</tr><tr>
<td>
`aggregation_method`<a id="aggregation_method"></a>
</td>
<td>
See `gradients()` documentation for details.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list of Hessian matrices of `sum(ys)` for each `x` in `xs`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`LookupError`<a id="LookupError"></a>
</td>
<td>
if one of the operations between `xs` and `ys` does not
have a registered gradient function.
</td>
</tr>
</table>

