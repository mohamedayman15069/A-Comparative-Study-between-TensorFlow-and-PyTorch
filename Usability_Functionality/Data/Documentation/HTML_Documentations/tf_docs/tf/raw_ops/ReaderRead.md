description: Returns the next record (key, value pair) produced by a Reader.
robots: noindex

# tf.raw_ops.ReaderRead

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the next record (key, value pair) produced by a Reader.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ReaderRead`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ReaderRead(
    reader_handle, queue_handle, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Will dequeue from the input queue if necessary (e.g. when the
Reader needs to start reading from a new file since it has finished
with the previous file).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`reader_handle`<a id="reader_handle"></a>
</td>
<td>
A `Tensor` of type mutable `string`. Handle to a Reader.
</td>
</tr><tr>
<td>
`queue_handle`<a id="queue_handle"></a>
</td>
<td>
A `Tensor` of type mutable `string`.
Handle to a Queue, with string work items.
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
A tuple of `Tensor` objects (key, value).
</td>
</tr>
<tr>
<td>
`key`<a id="key"></a>
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`value`<a id="value"></a>
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr>
</table>

