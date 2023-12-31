description: Op removes and returns the values associated with the key
robots: noindex

# tf.raw_ops.OrderedMapUnstage

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Op removes and returns the values associated with the key


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.OrderedMapUnstage`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.OrderedMapUnstage(
    key,
    indices,
    dtypes,
    capacity=0,
    memory_limit=0,
    container=&#x27;&#x27;,
    shared_name=&#x27;&#x27;,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


from the underlying container.   If the underlying container
does not contain this key, the op will block until it does.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`key`<a id="key"></a>
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`indices`<a id="indices"></a>
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`dtypes`<a id="dtypes"></a>
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
</td>
</tr><tr>
<td>
`capacity`<a id="capacity"></a>
</td>
<td>
An optional `int` that is `>= 0`. Defaults to `0`.
</td>
</tr><tr>
<td>
`memory_limit`<a id="memory_limit"></a>
</td>
<td>
An optional `int` that is `>= 0`. Defaults to `0`.
</td>
</tr><tr>
<td>
`container`<a id="container"></a>
</td>
<td>
An optional `string`. Defaults to `""`.
</td>
</tr><tr>
<td>
`shared_name`<a id="shared_name"></a>
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
A list of `Tensor` objects of type `dtypes`.
</td>
</tr>

</table>

