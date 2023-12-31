description: Computes arctangent of y/x element-wise, respecting signs of the arguments.
robots: noindex

# tf.raw_ops.Atan2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes arctangent of `y/x` element-wise, respecting signs of the arguments.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Atan2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Atan2(
    y, x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is the angle \\( \theta \in [-\pi, \pi] \\) such that
\\[ x = r \cos(\theta) \\]
and
\\[ y = r \sin(\theta) \\]
where \\(r = \sqrt{x^2 + y^2} \\).

#### For example:



```
>>> x = [1., 1.]
>>> y = [1., -1.]
>>> print((tf.math.atan2(y,x) * (180 / np.pi)).numpy())
[ 45. -45.]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`y`<a id="y"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
</td>
</tr><tr>
<td>
`x`<a id="x"></a>
</td>
<td>
A `Tensor`. Must have the same type as `y`.
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
A `Tensor`. Has the same type as `y`.
</td>
</tr>

</table>

