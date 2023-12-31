description: Deserialize and concatenate SparseTensors from a serialized minibatch.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.deserialize_many_sparse" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.deserialize_many_sparse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/sparse_ops.py">View source</a>



Deserialize and concatenate `SparseTensors` from a serialized minibatch.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.deserialize_many_sparse`, `tf.compat.v1.io.deserialize_many_sparse`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.deserialize_many_sparse(
    serialized_sparse, dtype, rank=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The input `serialized_sparse` must be a string matrix of shape `[N x 3]` where
`N` is the minibatch size and the rows correspond to packed outputs of
`serialize_sparse`.  The ranks of the original `SparseTensor` objects
must all match.  When the final `SparseTensor` is created, it has rank one
higher than the ranks of the incoming `SparseTensor` objects (they have been
concatenated along a new row dimension).

The output `SparseTensor` object's shape values for all dimensions but the
first are the max across the input `SparseTensor` objects' shape values
for the corresponding dimensions.  Its first shape value is `N`, the minibatch
size.

The input `SparseTensor` objects' indices are assumed ordered in
standard lexicographic order.  If this is not the case, after this
step run <a href="../../tf/sparse/reorder.md"><code>sparse.reorder</code></a> to restore index ordering.

For example, if the serialized input is a `[2, 3]` matrix representing two
original `SparseTensor` objects:

    index = [ 0]
            [10]
            [20]
    values = [1, 2, 3]
    shape = [50]

and

    index = [ 2]
            [10]
    values = [4, 5]
    shape = [30]

then the final deserialized `SparseTensor` will be:

    index = [0  0]
            [0 10]
            [0 20]
            [1  2]
            [1 10]
    values = [1, 2, 3, 4, 5]
    shape = [2 50]

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`serialized_sparse`<a id="serialized_sparse"></a>
</td>
<td>
2-D `Tensor` of type `string` of shape `[N, 3]`.
The serialized and packed `SparseTensor` objects.
</td>
</tr><tr>
<td>
`dtype`<a id="dtype"></a>
</td>
<td>
The `dtype` of the serialized `SparseTensor` objects.
</td>
</tr><tr>
<td>
`rank`<a id="rank"></a>
</td>
<td>
(optional) Python int, the rank of the `SparseTensor` objects.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
A name prefix for the returned tensors (optional)
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensor` representing the deserialized `SparseTensor`s,
concatenated along the `SparseTensor`s' first dimension.

All of the serialized `SparseTensor`s must have had the same rank and type.
</td>
</tr>

</table>

