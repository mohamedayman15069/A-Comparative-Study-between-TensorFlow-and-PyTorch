description: Creates a tensor with all elements set to zero.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.zeros_like" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.zeros_like

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/array_ops.py">View source</a>



Creates a tensor with all elements set to zero.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.zeros_like(
    tensor, dtype=None, name=None, optimize=True
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../../../tf/zeros.md"><code>tf.zeros</code></a>.

Given a single tensor (`tensor`), this operation returns a tensor of the
same type and shape as `tensor` with all elements set to zero. Optionally,
you can use `dtype` to specify a new type for the returned tensor.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Examples</h2></th></tr>
<tr class="alt">
<td colspan="2">
```
>>> tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
>>> tf.zeros_like(tensor)
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[0, 0, 0],
       [0, 0, 0]], dtype=int32)>
```

```
>>> tf.zeros_like(tensor, dtype=tf.float32)
<tf.Tensor: shape=(2, 3), dtype=float32, numpy=
array([[0., 0., 0.],
       [0., 0., 0.]], dtype=float32)>
```
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`<a id="tensor"></a>
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`dtype`<a id="dtype"></a>
</td>
<td>
A type for the returned `Tensor`. Must be `float16`, `float32`,
`float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`,
`complex64`, `complex128`, `bool` or `string`. (optional)
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`optimize`<a id="optimize"></a>
</td>
<td>
if `True`, attempt to statically determine the shape of `tensor`
and encode it as a constant. (optional, defaults to `True`)
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with all elements set to zero.
</td>
</tr>

</table>

