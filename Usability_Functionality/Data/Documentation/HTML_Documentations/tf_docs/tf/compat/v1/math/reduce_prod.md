description: Computes <a href="../../../../tf/math/multiply.md"><code>tf.math.multiply</code></a> of elements across dimensions of a tensor. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.math.reduce_prod" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.math.reduce_prod

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/math_ops.py">View source</a>



Computes <a href="../../../../tf/math/multiply.md"><code>tf.math.multiply</code></a> of elements across dimensions of a tensor. (deprecated arguments)


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.math.reduce_prod(
    input_tensor,
    axis=None,
    keepdims=None,
    name=None,
    reduction_indices=None,
    keep_dims=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Deprecated: SOME ARGUMENTS ARE DEPRECATED: `(keep_dims)`. They will be removed in a future version.
Instructions for updating:
keep_dims is deprecated, use keepdims instead

This is the reduction operation for the elementwise <a href="../../../../tf/math/multiply.md"><code>tf.math.multiply</code></a> op.

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
of the entries in `axis`, which must be unique. If `keepdims` is true, the
reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a
tensor with a single element is returned.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">For example</h2></th></tr>
<tr class="alt">
<td colspan="2">
```
>>> x = tf.constant([[1., 2.], [3., 4.]])
>>> tf.math.reduce_prod(x)
<tf.Tensor: shape=(), dtype=float32, numpy=24.>
>>> tf.math.reduce_prod(x, 0)
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([3., 8.], dtype=float32)>
>>> tf.math.reduce_prod(x, 1)
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([2., 12.],
dtype=float32)>
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
`input_tensor`<a id="input_tensor"></a>
</td>
<td>
The tensor to reduce. Should have numeric type.
</td>
</tr><tr>
<td>
`axis`<a id="axis"></a>
</td>
<td>
The dimensions to reduce. If `None` (the default), reduces all
dimensions. Must be in the range `[-rank(input_tensor),
rank(input_tensor))`.
</td>
</tr><tr>
<td>
`keepdims`<a id="keepdims"></a>
</td>
<td>
If true, retains reduced dimensions with length 1.
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
`reduction_indices`<a id="reduction_indices"></a>
</td>
<td>
The old (deprecated) name for axis.
</td>
</tr><tr>
<td>
`keep_dims`<a id="keep_dims"></a>
</td>
<td>
Deprecated alias for `keepdims`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The reduced tensor.
</td>
</tr>

</table>




 <section><devsite-expandable expanded>
 <h2 class="showalways">numpy compatibility</h2>

Equivalent to np.prod

 </devsite-expandable></section>

