description: Returns the truth value of x OR y element-wise.
robots: noindex

# tf.raw_ops.LogicalOr

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the truth value of x OR y element-wise.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.LogicalOr`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.LogicalOr(
    x, y, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Logical OR function.

Requires that `x` and `y` have the same shape or have
[broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
shapes. For example, `x` and `y` can be:

- Two single elements of type `bool`.
- One <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of type `bool` and one single `bool`, where the result will
  be calculated by applying logical OR with the single element to each
  element in the larger Tensor.
- Two <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> objects of type `bool` of the same shape. In this case,
  the result will be the element-wise logical OR of the two input tensors.

You can also use the `|` operator instead.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Usage</h2></th></tr>
<tr class="alt">
<td colspan="2">
```
>>> a = tf.constant([True])
>>> b = tf.constant([False])
>>> tf.math.logical_or(a, b)
<tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])>
>>> a | b
<tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])>
```

```
>>> c = tf.constant([False])
>>> x = tf.constant([False, True, True, False])
>>> tf.math.logical_or(c, x)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, True,  True, False])>
>>> c | x
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, True,  True, False])>
```

```
>>> y = tf.constant([False, False, True, True])
>>> z = tf.constant([False, True, False, True])
>>> tf.math.logical_or(y, z)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, True, True, True])>
>>> y | z
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, True, True, True])>
```

This op also supports broadcasting

```
>>> tf.logical_or([[True, False]], [[True], [False]])
<tf.Tensor: shape=(2, 2), dtype=bool, numpy=
array([[ True,  True],
     [ True, False]])>
```
</td>
</tr>

</table>


The reduction version of this elementwise operation is <a href="../../tf/math/reduce_any.md"><code>tf.math.reduce_any</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`<a id="x"></a>
</td>
<td>
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool.
</td>
</tr><tr>
<td>
`y`<a id="y"></a>
</td>
<td>
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool.
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
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool with the shape that `x` and `y` broadcast to.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`<a id="x"></a>
</td>
<td>
A `Tensor` of type `bool`.
</td>
</tr><tr>
<td>
`y`<a id="y"></a>
</td>
<td>
A `Tensor` of type `bool`.
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
A `Tensor` of type `bool`.
</td>
</tr>

</table>

