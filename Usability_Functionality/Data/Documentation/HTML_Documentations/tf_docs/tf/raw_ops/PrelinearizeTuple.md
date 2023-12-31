description: An op which linearizes multiple Tensor values to an opaque variant tensor.
robots: noindex

# tf.raw_ops.PrelinearizeTuple

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



An op which linearizes multiple Tensor values to an opaque variant tensor.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.PrelinearizeTuple`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.PrelinearizeTuple(
    inputs, shapes, layouts=[], name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`<a id="inputs"></a>
</td>
<td>
A list of `Tensor` objects.
A list of tensors that will be provided using the infeed mechanism.
</td>
</tr><tr>
<td>
`shapes`<a id="shapes"></a>
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`).
The shapes of each tensor in `inputs`.
</td>
</tr><tr>
<td>
`layouts`<a id="layouts"></a>
</td>
<td>
An optional list of `ints`. Defaults to `[]`.
A vector holding the requested layout in minor-to-major sequence for all the
tuple shapes in the order the shapes appear in the "shapes" input. The layout
elements for a sub-shape can be set to -1 in which case the corresponding layout
will be computed by the infeed operation.
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

