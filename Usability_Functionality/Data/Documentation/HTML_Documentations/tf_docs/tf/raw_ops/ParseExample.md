description: Transforms a vector of brain.Example protos (as strings) into typed tensors.
robots: noindex

# tf.raw_ops.ParseExample

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Transforms a vector of brain.Example protos (as strings) into typed tensors.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ParseExample`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ParseExample(
    serialized,
    names,
    sparse_keys,
    dense_keys,
    dense_defaults,
    sparse_types,
    dense_shapes,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`serialized`<a id="serialized"></a>
</td>
<td>
A `Tensor` of type `string`.
A vector containing a batch of binary serialized Example protos.
</td>
</tr><tr>
<td>
`names`<a id="names"></a>
</td>
<td>
A `Tensor` of type `string`.
A vector containing the names of the serialized protos.
May contain, for example, table key (descriptive) names for the
corresponding serialized protos.  These are purely useful for debugging
purposes, and the presence of values here has no effect on the output.
May also be an empty vector if no names are available.
If non-empty, this vector must be the same length as "serialized".
</td>
</tr><tr>
<td>
`sparse_keys`<a id="sparse_keys"></a>
</td>
<td>
A list of `Tensor` objects with type `string`.
A list of Nsparse string Tensors (scalars).
The keys expected in the Examples' features associated with sparse values.
</td>
</tr><tr>
<td>
`dense_keys`<a id="dense_keys"></a>
</td>
<td>
A list of `Tensor` objects with type `string`.
A list of Ndense string Tensors (scalars).
The keys expected in the Examples' features associated with dense values.
</td>
</tr><tr>
<td>
`dense_defaults`<a id="dense_defaults"></a>
</td>
<td>
A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
A list of Ndense Tensors (some may be empty).
dense_defaults[j] provides default values
when the example's feature_map lacks dense_key[j].  If an empty Tensor is
provided for dense_defaults[j], then the Feature dense_keys[j] is required.
The input type is inferred from dense_defaults[j], even when it's empty.
If dense_defaults[j] is not empty, and dense_shapes[j] is fully defined,
then the shape of dense_defaults[j] must match that of dense_shapes[j].
If dense_shapes[j] has an undefined major dimension (variable strides dense
feature), dense_defaults[j] must contain a single element:
the padding element.
</td>
</tr><tr>
<td>
`sparse_types`<a id="sparse_types"></a>
</td>
<td>
A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`.
A list of Nsparse types; the data types of data in each Feature
given in sparse_keys.
Currently the ParseExample supports DT_FLOAT (FloatList),
DT_INT64 (Int64List), and DT_STRING (BytesList).
</td>
</tr><tr>
<td>
`dense_shapes`<a id="dense_shapes"></a>
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`).
A list of Ndense shapes; the shapes of data in each Feature
given in dense_keys.
The number of elements in the Feature corresponding to dense_key[j]
must always equal dense_shapes[j].NumEntries().
If dense_shapes[j] == (D0, D1, ..., DN) then the shape of output
Tensor dense_values[j] will be (|serialized|, D0, D1, ..., DN):
The dense outputs are just the inputs row-stacked by batch.
This works for dense_shapes[j] = (-1, D1, ..., DN).  In this case
the shape of the output Tensor dense_values[j] will be
(|serialized|, M, D1, .., DN), where M is the maximum number of blocks
of elements of length D1 * .... * DN, across all minibatch entries
in the input.  Any minibatch entry with less than M blocks of elements of
length D1 * ... * DN will be padded with the corresponding default_value
scalar element along the second dimension.
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
A tuple of `Tensor` objects (sparse_indices, sparse_values, sparse_shapes, dense_values).
</td>
</tr>
<tr>
<td>
`sparse_indices`<a id="sparse_indices"></a>
</td>
<td>
A list with the same length as `sparse_keys` of `Tensor` objects with type `int64`.
</td>
</tr><tr>
<td>
`sparse_values`<a id="sparse_values"></a>
</td>
<td>
A list of `Tensor` objects of type `sparse_types`.
</td>
</tr><tr>
<td>
`sparse_shapes`<a id="sparse_shapes"></a>
</td>
<td>
A list with the same length as `sparse_keys` of `Tensor` objects with type `int64`.
</td>
</tr><tr>
<td>
`dense_values`<a id="dense_values"></a>
</td>
<td>
A list of `Tensor` objects. Has the same type as `dense_defaults`.
</td>
</tr>
</table>

