description: Updates the table to associates keys with values.
robots: noindex

# tf.raw_ops.LookupTableInsert

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Updates the table to associates keys with values.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.LookupTableInsert`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.LookupTableInsert(
    table_handle, keys, values, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The tensor `keys` must be of the same type as the keys of the table.
The tensor `values` must be of the type of the table values.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`table_handle`<a id="table_handle"></a>
</td>
<td>
A `Tensor` of type mutable `string`. Handle to the table.
</td>
</tr><tr>
<td>
`keys`<a id="keys"></a>
</td>
<td>
A `Tensor`. Any shape.  Keys to look up.
</td>
</tr><tr>
<td>
`values`<a id="values"></a>
</td>
<td>
A `Tensor`. Values to associate with keys.
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

