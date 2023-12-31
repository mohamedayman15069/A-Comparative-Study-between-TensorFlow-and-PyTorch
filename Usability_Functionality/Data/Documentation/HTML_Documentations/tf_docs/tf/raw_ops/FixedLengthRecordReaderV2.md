description: A Reader that outputs fixed-length records from a file.
robots: noindex

# tf.raw_ops.FixedLengthRecordReaderV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



A Reader that outputs fixed-length records from a file.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.FixedLengthRecordReaderV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.FixedLengthRecordReaderV2(
    record_bytes,
    header_bytes=0,
    footer_bytes=0,
    hop_bytes=0,
    container=&#x27;&#x27;,
    shared_name=&#x27;&#x27;,
    encoding=&#x27;&#x27;,
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
`record_bytes`<a id="record_bytes"></a>
</td>
<td>
An `int`. Number of bytes in the record.
</td>
</tr><tr>
<td>
`header_bytes`<a id="header_bytes"></a>
</td>
<td>
An optional `int`. Defaults to `0`.
Number of bytes in the header, defaults to 0.
</td>
</tr><tr>
<td>
`footer_bytes`<a id="footer_bytes"></a>
</td>
<td>
An optional `int`. Defaults to `0`.
Number of bytes in the footer, defaults to 0.
</td>
</tr><tr>
<td>
`hop_bytes`<a id="hop_bytes"></a>
</td>
<td>
An optional `int`. Defaults to `0`.
Number of bytes to hop before each read. Default of 0 means using
record_bytes.
</td>
</tr><tr>
<td>
`container`<a id="container"></a>
</td>
<td>
An optional `string`. Defaults to `""`.
If non-empty, this reader is placed in the given container.
Otherwise, a default container is used.
</td>
</tr><tr>
<td>
`shared_name`<a id="shared_name"></a>
</td>
<td>
An optional `string`. Defaults to `""`.
If non-empty, this reader is named in the given bucket
with this shared_name. Otherwise, the node name is used instead.
</td>
</tr><tr>
<td>
`encoding`<a id="encoding"></a>
</td>
<td>
An optional `string`. Defaults to `""`.
The type of encoding for the file. Currently ZLIB and GZIP
are supported. Defaults to none.
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
A `Tensor` of type `resource`.
</td>
</tr>

</table>

