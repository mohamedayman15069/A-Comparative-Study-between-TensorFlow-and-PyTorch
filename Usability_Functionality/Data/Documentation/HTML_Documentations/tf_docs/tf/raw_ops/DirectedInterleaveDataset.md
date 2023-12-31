description: A substitute for InterleaveDataset on a fixed list of N datasets.
robots: noindex

# tf.raw_ops.DirectedInterleaveDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



A substitute for `InterleaveDataset` on a fixed list of `N` datasets.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DirectedInterleaveDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DirectedInterleaveDataset(
    selector_input_dataset,
    data_input_datasets,
    output_types,
    output_shapes,
    stop_on_empty_dataset=False,
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
`selector_input_dataset`<a id="selector_input_dataset"></a>
</td>
<td>
A `Tensor` of type `variant`.
A dataset of scalar `DT_INT64` elements that determines which of the
`N` data inputs should produce the next output element.
</td>
</tr><tr>
<td>
`data_input_datasets`<a id="data_input_datasets"></a>
</td>
<td>
A list of at least 1 `Tensor` objects with type `variant`.
`N` datasets with the same type that will be interleaved according to
the values of `selector_input_dataset`.
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
`stop_on_empty_dataset`<a id="stop_on_empty_dataset"></a>
</td>
<td>
An optional `bool`. Defaults to `False`.
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

