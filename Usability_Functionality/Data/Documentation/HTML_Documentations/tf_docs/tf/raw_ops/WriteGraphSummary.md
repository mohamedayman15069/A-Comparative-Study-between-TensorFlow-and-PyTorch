description: Writes a graph summary.
robots: noindex

# tf.raw_ops.WriteGraphSummary

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Writes a graph summary.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.WriteGraphSummary`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.WriteGraphSummary(
    writer, step, tensor, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Writes TensorFlow graph `tensor` at `step` using summary `writer`.

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
`step`<a id="step"></a>
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`tensor`<a id="tensor"></a>
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
