description: Computes Python style division of x by y.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.math.divide" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.math.divide

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/math_ops.py">View source</a>



Computes Python style division of `x` by `y`.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.math.divide(
    x, y, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### For example:



```
>>> x = tf.constant([16, 12, 11])
>>> y = tf.constant([4, 6, 2])
>>> tf.divide(x,y)
<tf.Tensor: shape=(3,), dtype=float64,
numpy=array([4. , 2. , 5.5])>
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
A `Tensor`
</td>
</tr><tr>
<td>
`y`<a id="y"></a>
</td>
<td>
A `Tensor`
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
A `Tensor` with same shape as input
</td>
</tr>

</table>

