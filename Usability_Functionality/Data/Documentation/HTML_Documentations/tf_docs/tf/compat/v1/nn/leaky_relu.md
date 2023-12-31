description: Compute the Leaky ReLU activation function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.leaky_relu" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.leaky_relu

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/nn_ops.py">View source</a>



Compute the Leaky ReLU activation function.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.leaky_relu(
    features, alpha=0.2, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Source: [Rectifier Nonlinearities Improve Neural Network Acoustic Models.
AL Maas, AY Hannun, AY Ng - Proc. ICML, 2013]
(https://ai.stanford.edu/~amaas/papers/relu_hybrid_icml2013_final.pdf).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`features`<a id="features"></a>
</td>
<td>
A `Tensor` representing preactivation values. Must be one of
the following types: `float16`, `float32`, `float64`, `int32`, `int64`.
</td>
</tr><tr>
<td>
`alpha`<a id="alpha"></a>
</td>
<td>
Slope of the activation function at x < 0.
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
The activation value.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">References</h2></th></tr>
<tr class="alt">
<td colspan="2">
Rectifier Nonlinearities Improve Neural Network Acoustic Models:
[Maas et al., 2013]
(http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.693.1422)
([pdf]
(http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.693.1422&rep=rep1&type=pdf))
</td>
</tr>

</table>

