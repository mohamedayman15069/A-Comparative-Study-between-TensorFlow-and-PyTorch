description: Casts a tensor to type float32. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.to_float" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.to_float

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/math_ops.py">View source</a>



Casts a tensor to type `float32`. (deprecated)


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.to_float(
    x, name=&#x27;ToFloat&#x27;
)
</code></pre>





 <section><devsite-expandable expanded>
 <h2 class="showalways">Migrate to TF2</h2>

Caution: This API was designed for TensorFlow v1.
Continue reading for details on how to migrate from this API to a native
TensorFlow v2 equivalent. See the
[TensorFlow v1 to TensorFlow v2 migration guide](https://www.tensorflow.org/guide/migrate)
for instructions on how to migrate the rest of your code.

This name was deprecated and removed in TF2, but has an exact replacement
<a href="../../../tf/cast.md"><code>tf.cast(..., tf.float32)</code></a>. There are no further issues with eager execution
or tf.function.

Before:

```
>>> tf.compat.v1.to_float(tf.constant(3.14, dtype=tf.double))
<tf.Tensor: shape=(), dtype=float32, numpy=3.14>
```

After:

```
>>> tf.cast(tf.constant(3.14, dtype=tf.double), tf.float32)
<tf.Tensor: shape=(), dtype=float32, numpy=3.14>
```


 </aside></devsite-expandable></section>

<h2>Description</h2>

<!-- Placeholder for "Used in" -->

Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/cast.md"><code>tf.cast</code></a> instead.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`<a id="x"></a>
</td>
<td>
A `Tensor` or `SparseTensor` or `IndexedSlices`.
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
A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
type `float32`.
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
If `x` cannot be cast to the `float32`.
</td>
</tr>
</table>


