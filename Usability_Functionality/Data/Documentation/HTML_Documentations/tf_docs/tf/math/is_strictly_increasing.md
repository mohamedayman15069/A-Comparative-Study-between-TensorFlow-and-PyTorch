description: Returns True if x is strictly increasing.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.is_strictly_increasing" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.is_strictly_increasing

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/check_ops.py">View source</a>



Returns `True` if `x` is strictly increasing.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.debugging.is_strictly_increasing`, `tf.compat.v1.is_strictly_increasing`, `tf.compat.v1.math.is_strictly_increasing`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.is_strictly_increasing(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Elements of `x` are compared in row-major order.  The tensor `[x[0],...]`
is strictly increasing if for every adjacent pair we have `x[i] < x[i+1]`.
If `x` has less than two elements, it is trivially strictly increasing.

See also:  `is_non_decreasing`

```
>>> x1 = tf.constant([1.0, 2.0, 3.0])
>>> tf.math.is_strictly_increasing(x1)
<tf.Tensor: shape=(), dtype=bool, numpy=True>
>>> x2 = tf.constant([3.0, 1.0, 2.0])
>>> tf.math.is_strictly_increasing(x2)
<tf.Tensor: shape=(), dtype=bool, numpy=False>
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
Numeric `Tensor`.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
A name for this operation (optional).
Defaults to "is_strictly_increasing"
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Boolean `Tensor`, equal to `True` iff `x` is strictly increasing.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`<a id="TypeError"></a>
</td>
<td>
if `x` is not a numeric tensor.
</td>
</tr>
</table>

