description: Computes the Bessel k0e function of x element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.special.bessel_k0e" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.special.bessel_k0e

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/special_math_ops.py">View source</a>



Computes the Bessel k0e function of `x` element-wise.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.special.bessel_k0e(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Modified Bessel function of order 0.

```
>>> tf.math.special.bessel_k0e([0.5, 1., 2., 4.]).numpy()
array([1.52410939, 1.14446308, 0.84156822, 0.60929767], dtype=float32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`<a id="x"></a>
</td>
<td>
A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
`float32`, `float64`.
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
A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.
</td>
</tr>

</table>




 <section><devsite-expandable expanded>
 <h2 class="showalways">scipy compatibility</h2>

Equivalent to scipy.special.k0e

 </devsite-expandable></section>

