description: A transformation that asserts which transformations happen next.
robots: noindex

# tf.raw_ops.AssertNextDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



A transformation that asserts which transformations happen next.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.AssertNextDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.AssertNextDataset(
    input_dataset, transformations, output_types, output_shapes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This transformation checks whether the camel-case names (i.e. "FlatMap", not
"flat_map") of the transformations following this transformation match the list
of names in the `transformations` argument. If there is a mismatch, the
transformation raises an exception.

The check occurs when iterating over the contents of the dataset, which
means that the check happens *after* any static optimizations are applied
to the dataset graph.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_dataset`<a id="input_dataset"></a>
</td>
<td>
A `Tensor` of type `variant`.
A variant tensor representing the input dataset.
`AssertNextDataset` passes through the outputs of its input dataset.
</td>
</tr><tr>
<td>
`transformations`<a id="transformations"></a>
</td>
<td>
A `Tensor` of type `string`.
A <a href="../../tf.md#string"><code>tf.string</code></a> vector <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> identifying the transformations that are
expected to happen next.
</td>
</tr><tr>
<td>
`output_types`<a id="output_types"></a>
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
</td>
</tr><tr>
<td>
`output_shapes`<a id="output_shapes"></a>
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
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
A `Tensor` of type `variant`.
</td>
</tr>

</table>

