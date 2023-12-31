description: Provides the time since epoch in seconds.
robots: noindex

# tf.raw_ops.Timestamp

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Provides the time since epoch in seconds.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Timestamp`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Timestamp(
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns the timestamp as a `float64` for seconds since the Unix epoch.

#### Common usages include:


* Logging
* Providing a random number seed
* Debugging graph execution
* Generating timing information, mainly through comparison of timestamps

Note: In graph mode, the timestamp is computed when the op is executed,
not when it is added to the graph.  In eager mode, the timestamp is computed
when the op is eagerly executed.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
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
A `Tensor` of type `float64`.
</td>
</tr>

</table>

