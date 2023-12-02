robots: noindex

# tf.raw_ops.SnapshotDatasetReader

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>






<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SnapshotDatasetReader`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SnapshotDatasetReader(
    shard_dir,
    start_index,
    output_types,
    output_shapes,
    version,
    compression=&#x27;&#x27;,
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
`shard_dir`<a id="shard_dir"></a>
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`start_index`<a id="start_index"></a>
</td>
<td>
A `Tensor` of type `int64`.
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
`version`<a id="version"></a>
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`compression`<a id="compression"></a>
</td>
<td>
An optional `string`. Defaults to `""`.
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
