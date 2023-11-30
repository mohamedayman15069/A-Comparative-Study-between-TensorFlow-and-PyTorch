robots: noindex

# tf.raw_ops.CreateSummaryFileWriter

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
<p>`tf.compat.v1.raw_ops.CreateSummaryFileWriter`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CreateSummaryFileWriter(
    writer, logdir, max_queue, flush_millis, filename_suffix, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`writer`<a id="writer"></a>
</td>
<td>
A `Tensor` of type `resource`.
</td>
</tr><tr>
<td>
`logdir`<a id="logdir"></a>
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`max_queue`<a id="max_queue"></a>
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`flush_millis`<a id="flush_millis"></a>
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`filename_suffix`<a id="filename_suffix"></a>
</td>
<td>
A `Tensor` of type `string`.
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
