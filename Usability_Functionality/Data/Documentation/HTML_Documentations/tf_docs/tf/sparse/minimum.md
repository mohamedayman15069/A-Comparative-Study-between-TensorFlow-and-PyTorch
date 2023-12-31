description: Returns the element-wise min of two SparseTensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.minimum" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.minimum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/sparse_ops.py">View source</a>



Returns the element-wise min of two SparseTensors.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.minimum`, `tf.compat.v1.sparse_minimum`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.minimum(
    sp_a, sp_b, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Assumes the two SparseTensors have the same shape, i.e., no broadcasting.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Example</h2></th></tr>
<tr class="alt">
<td colspan="2">
```
>>> sp_zero = tf.sparse.SparseTensor([[0]], [0], [7])
>>> sp_one = tf.sparse.SparseTensor([[1]], [1], [7])
>>> res = tf.sparse.minimum(sp_zero, sp_one)
>>> res.indices
<tf.Tensor: shape=(2, 1), dtype=int64, numpy=
array([[0],
       [1]])>
>>> res.values
<tf.Tensor: shape=(2,), dtype=int32, numpy=array([0, 0], dtype=int32)>
>>> res.dense_shape
<tf.Tensor: shape=(1,), dtype=int64, numpy=array([7])>
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
`sp_a`<a id="sp_a"></a>
</td>
<td>
a `SparseTensor` operand whose dtype is real, and indices
lexicographically ordered.
</td>
</tr><tr>
<td>
`sp_b`<a id="sp_b"></a>
</td>
<td>
the other `SparseTensor` operand with the same requirements (and the
same shape).
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
optional name of the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`output`<a id="output"></a>
</td>
<td>
the output SparseTensor.
</td>
</tr>
</table>

