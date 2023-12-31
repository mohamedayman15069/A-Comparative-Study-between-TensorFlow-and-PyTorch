description: Updates the content of the 'checkpoint' file. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.update_checkpoint_state" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.update_checkpoint_state

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/checkpoint/checkpoint_management.py">View source</a>



Updates the content of the 'checkpoint' file. (deprecated)


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.update_checkpoint_state(
    save_dir,
    model_checkpoint_path,
    all_model_checkpoint_paths=None,
    latest_filename=None,
    all_model_checkpoint_timestamps=None,
    last_preserved_timestamp=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../../tf/train/CheckpointManager.md"><code>tf.train.CheckpointManager</code></a> to manage checkpoints rather than manually editing the Checkpoint proto.

This updates the checkpoint file containing a CheckpointState
proto.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`save_dir`<a id="save_dir"></a>
</td>
<td>
Directory where the model was saved.
</td>
</tr><tr>
<td>
`model_checkpoint_path`<a id="model_checkpoint_path"></a>
</td>
<td>
The checkpoint file.
</td>
</tr><tr>
<td>
`all_model_checkpoint_paths`<a id="all_model_checkpoint_paths"></a>
</td>
<td>
List of strings.  Paths to all not-yet-deleted
checkpoints, sorted from oldest to newest.  If this is a non-empty list,
the last element must be equal to model_checkpoint_path.  These paths
are also saved in the CheckpointState proto.
</td>
</tr><tr>
<td>
`latest_filename`<a id="latest_filename"></a>
</td>
<td>
Optional name of the checkpoint file.  Default to
'checkpoint'.
</td>
</tr><tr>
<td>
`all_model_checkpoint_timestamps`<a id="all_model_checkpoint_timestamps"></a>
</td>
<td>
Optional list of timestamps (floats,
seconds since the Epoch) indicating when the checkpoints in
`all_model_checkpoint_paths` were created.
</td>
</tr><tr>
<td>
`last_preserved_timestamp`<a id="last_preserved_timestamp"></a>
</td>
<td>
A float, indicating the number of seconds since
the Epoch when the last preserved checkpoint was written, e.g. due to a
`keep_checkpoint_every_n_hours` parameter (see
<a href="../../../../tf/train/CheckpointManager.md"><code>tf.train.CheckpointManager</code></a> for an implementation).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`RuntimeError`<a id="RuntimeError"></a>
</td>
<td>
If any of the model checkpoint paths conflict with the file
containing CheckpointSate.
</td>
</tr>
</table>

