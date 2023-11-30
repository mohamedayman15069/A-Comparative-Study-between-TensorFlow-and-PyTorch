robots: noindex

# tf.raw_ops.CreateSummaryDbWriter

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
<p>`tf.compat.v1.raw_ops.CreateSummaryDbWriter`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CreateSummaryDbWriter(
    writer, db_uri, experiment_name, run_name, user_name, name=None
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
`db_uri`<a id="db_uri"></a>
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`experiment_name`<a id="experiment_name"></a>
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`run_name`<a id="run_name"></a>
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`user_name`<a id="user_name"></a>
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
