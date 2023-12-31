description: Computes the mean of elements across dimensions of a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.reduce_mean" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.reduce_mean

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/math_ops.py">View source</a>



Computes the mean of elements across dimensions of a tensor.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.reduce_mean`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.reduce_mean(
    input_tensor, axis=None, keepdims=False, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Reduces `input_tensor` along the dimensions given in `axis` by computing the
mean of elements across the dimensions in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
of the entries in `axis`, which must be unique. If `keepdims` is true, the
reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a tensor with a single
element is returned.

#### For example:



```
>>> x = tf.constant([[1., 1.], [2., 2.]])
>>> tf.reduce_mean(x)
<tf.Tensor: shape=(), dtype=float32, numpy=1.5>
>>> tf.reduce_mean(x, 0)
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([1.5, 1.5], dtype=float32)>
>>> tf.reduce_mean(x, 1)
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([1., 2.], dtype=float32)>
```

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

Equivalent to np.mean

Please note that `np.mean` has a `dtype` parameter that could be used to
specify the output type. By default this is `dtype=float64`. On the other
hand, <a href="../../tf/math/reduce_mean.md"><code>tf.reduce_mean</code></a> has an aggressive type inference from `input_tensor`,
for example:

```
>>> x = tf.constant([1, 0, 1, 0])
>>> tf.reduce_mean(x)
<tf.Tensor: shape=(), dtype=int32, numpy=0>
>>> y = tf.constant([1., 0., 1., 0.])
>>> tf.reduce_mean(y)
<tf.Tensor: shape=(), dtype=float32, numpy=0.5>
```


 </devsite-expandable></section>

