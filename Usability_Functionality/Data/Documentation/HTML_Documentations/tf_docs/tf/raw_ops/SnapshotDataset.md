description: Creates a dataset that will write to / read from a snapshot.
robots: noindex

# tf.raw_ops.SnapshotDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that will write to / read from a snapshot.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SnapshotDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SnapshotDataset(
    input_dataset,
    path,
    output_types,
    output_shapes,
    compression=&#x27;&#x27;,
    reader_path_prefix=&#x27;&#x27;,
    writer_path_prefix=&#x27;&#x27;,
    shard_size_bytes=10737418240,
    pending_snapshot_expiry_seconds=86400,
    num_reader_threads=1,
    reader_buffer_size=1,
    num_writer_threads=1,
    writer_buffer_size=1,
    shuffle_on_read=False,
    seed=0,
    seed2=0,
    mode=&#x27;auto&#x27;,
    snapshot_name=&#x27;&#x27;,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This dataset attempts to determine whether a valid snapshot exists at the
`snapshot_path`, and reads from the snapshot in lieu of using `input_dataset`.
If not, it will run the preprocessing pipeline as usual, and write out a
snapshot of the data processed for future use.

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
</td>
</tr><tr>
<td>
`path`<a id="path"></a>
</td>
<td>
A `Tensor` of type `string`.
The path we should write snapshots to / read snapshots from.
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
`compression`<a id="compression"></a>
</td>
<td>
An optional `string`. Defaults to `""`.
</td>
</tr><tr>
<td>
`reader_path_prefix`<a id="reader_path_prefix"></a>
</td>
<td>
An optional `string`. Defaults to `""`.
</td>
</tr><tr>
<td>
`writer_path_prefix`<a id="writer_path_prefix"></a>
</td>
<td>
An optional `string`. Defaults to `""`.
</td>
</tr><tr>
<td>
`shard_size_bytes`<a id="shard_size_bytes"></a>
</td>
<td>
An optional `int`. Defaults to `10737418240`.
</td>
</tr><tr>
<td>
`pending_snapshot_expiry_seconds`<a id="pending_snapshot_expiry_seconds"></a>
</td>
<td>
An optional `int`. Defaults to `86400`.
</td>
</tr><tr>
<td>
`num_reader_threads`<a id="num_reader_threads"></a>
</td>
<td>
An optional `int`. Defaults to `1`.
</td>
</tr><tr>
<td>
`reader_buffer_size`<a id="reader_buffer_size"></a>
</td>
<td>
An optional `int`. Defaults to `1`.
</td>
</tr><tr>
<td>
`num_writer_threads`<a id="num_writer_threads"></a>
</td>
<td>
An optional `int`. Defaults to `1`.
</td>
</tr><tr>
<td>
`writer_buffer_size`<a id="writer_buffer_size"></a>
</td>
<td>
An optional `int`. Defaults to `1`.
</td>
</tr><tr>
<td>
`shuffle_on_read`<a id="shuffle_on_read"></a>
</td>
<td>
An optional `bool`. Defaults to `False`.
</td>
</tr><tr>
<td>
`seed`<a id="seed"></a>
</td>
<td>
An optional `int`. Defaults to `0`.
</td>
</tr><tr>
<td>
`seed2`<a id="seed2"></a>
</td>
<td>
An optional `int`. Defaults to `0`.
</td>
</tr><tr>
<td>
`mode`<a id="mode"></a>
</td>
<td>
An optional `string`. Defaults to `"auto"`.
</td>
</tr><tr>
<td>
`snapshot_name`<a id="snapshot_name"></a>
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

