description: V2 format specific: merges the metadata files of sharded checkpoints.
robots: noindex

# tf.raw_ops.MergeV2Checkpoints

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



V2 format specific: merges the metadata files of sharded checkpoints.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.MergeV2Checkpoints`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.MergeV2Checkpoints(
    checkpoint_prefixes,
    destination_prefix,
    delete_old_dirs=True,
    allow_missing_files=False,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->
  The

result is one logical checkpoint, with one physical metadata file and renamed
data files.

Intended for "grouping" multiple checkpoints in a sharded checkpoint setup.

If delete_old_dirs is true, attempts to delete recursively the dirname of each
path in the input checkpoint_prefixes.  This is useful when those paths are non
user-facing temporary locations.

If allow_missing_files is true, merges the checkpoint prefixes as long as
at least one file exists. Otherwise, if no files exist, an error will be thrown.
The default value for allow_missing_files is false.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`checkpoint_prefixes`<a id="checkpoint_prefixes"></a>
</td>
<td>
A `Tensor` of type `string`.
prefixes of V2 checkpoints to merge.
</td>
</tr><tr>
<td>
`destination_prefix`<a id="destination_prefix"></a>
</td>
<td>
A `Tensor` of type `string`.
scalar.  The desired final prefix.  Allowed to be the same
as one of the checkpoint_prefixes.
</td>
</tr><tr>
<td>
`delete_old_dirs`<a id="delete_old_dirs"></a>
</td>
<td>
An optional `bool`. Defaults to `True`. see above.
</td>
</tr><tr>
<td>
`allow_missing_files`<a id="allow_missing_files"></a>
</td>
<td>
An optional `bool`. Defaults to `False`. see above.
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
The created Operation.
</td>
</tr>

</table>

