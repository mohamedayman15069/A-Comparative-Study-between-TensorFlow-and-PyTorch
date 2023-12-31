description: Returns the max of x and y (i.e. x > y ? x : y) element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.math.maximum" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.math.maximum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the max of x and y (i.e. x > y ? x : y) element-wise.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.math.maximum(
    x: Annotated[Any, <a href="../../../../tf/raw_ops/Any.md"><code>tf.raw_ops.Any</code></a>],
    y: Annotated[Any, <a href="../../../../tf/raw_ops/Any.md"><code>tf.raw_ops.Any</code></a>],
    name=None
) -> Annotated[Any, <a href="../../../../tf/raw_ops/Any.md"><code>tf.raw_ops.Any</code></a>]
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example:



```
>>> x = tf.constant([0., 0., 0., 0.])
>>> y = tf.constant([-2., 0., 2., 5.])
>>> tf.math.maximum(x, y)
<tf.Tensor: shape=(4,), dtype=float32, numpy=array([0., 0., 2., 5.], dtype=float32)>
```

Note that `maximum` supports [broadcast semantics](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) for `x` and `y`.

```
>>> x = tf.constant([-5., 0., 0., 0.])
>>> y = tf.constant([-3.])
>>> tf.math.maximum(x, y)
<tf.Tensor: shape=(4,), dtype=float32, numpy=array([-3., 0., 0., 0.], dtype=float32)>
```

The reduction version of this elementwise operation is <a href="../../../../tf/math/reduce_max.md"><code>tf.math.reduce_max</code></a>

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`<a id="x"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, `int64`, `uint64`.
</td>
</tr><tr>
<td>
`y`<a id="y"></a>
</td>
<td>
A `Tensor`. Must have the same type as `x`.
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
A `Tensor`. Has the same type as `x`.
</td>
</tr>

</table>

