description: Resets the shape of a SparseTensor with indices and values unchanged.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.reset_shape" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.reset_shape

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/sparse_ops.py">View source</a>



Resets the shape of a `SparseTensor` with indices and values unchanged.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.reset_shape`, `tf.compat.v1.sparse_reset_shape`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.reset_shape(
    sp_input, new_shape=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If `new_shape` is None, returns a copy of `sp_input` with its shape reset
to the tight bounding box of `sp_input`. This will be a shape consisting of
all zeros if sp_input has no values.

If `new_shape` is provided, then it must be larger or equal in all dimensions
compared to the shape of `sp_input`. When this condition is met, the returned
SparseTensor will have its shape reset to `new_shape` and its indices and
values unchanged from that of `sp_input.`

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">For example</h2></th></tr>
<tr class="alt">
<td colspan="2">
Consider a `sp_input` with shape [2, 3, 5]:

  [0, 0, 1]: a
  [0, 1, 0]: b
  [0, 2, 2]: c
  [1, 0, 3]: d

- It is an error to set `new_shape` as [3, 7] since this represents a
  rank-2 tensor while `sp_input` is rank-3. This is either a ValueError
  during graph construction (if both shapes are known) or an OpError during
  run time.

- Setting `new_shape` as [2, 3, 6] will be fine as this shape is larger or
  equal in every dimension compared to the original shape [2, 3, 5].

- On the other hand, setting new_shape as [2, 3, 4] is also an error: The
  third dimension is smaller than the original shape [2, 3, 5] (and an
  `InvalidArgumentError` will be raised).

- If `new_shape` is None, the returned SparseTensor will have a shape
  [2, 3, 4], which is the tight bounding box of `sp_input`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_input`<a id="sp_input"></a>
</td>
<td>
The input `SparseTensor`.
</td>
</tr><tr>
<td>
`new_shape`<a id="new_shape"></a>
</td>
<td>
None or a vector representing the new shape for the returned
`SparseTensor`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensor` indices and values unchanged from `sp_input`. Its shape is
`new_shape` if that is set. Otherwise it is the tight bounding box of
 `sp_input`
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
If `sp_input` is not a `SparseTensor`.
</td>
</tr><tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
If `new_shape` represents a tensor with a different rank from
that of `sp_input` (if shapes are known when graph is constructed).
</td>
</tr><tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
 If `new_shape` is determined during graph build to have
dimension sizes that are too small.
</td>
</tr><tr>
<td>
`OpError`<a id="OpError"></a>
</td>
<td>
  - If `new_shape` has dimension sizes that are too small.
- If shapes are not known during graph construction time, and during run
  time it is found out that the ranks do not match.
</td>
</tr>
</table>

