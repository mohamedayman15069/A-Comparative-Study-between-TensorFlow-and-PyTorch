description: Retrieve frequency estimator embedding parameters.
robots: noindex

# tf.raw_ops.RetrieveTPUEmbeddingFrequencyEstimatorParameters

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Retrieve frequency estimator embedding parameters.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RetrieveTPUEmbeddingFrequencyEstimatorParameters`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RetrieveTPUEmbeddingFrequencyEstimatorParameters(
    num_shards,
    shard_id,
    table_id=-1,
    table_name=&#x27;&#x27;,
    config=&#x27;&#x27;,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

An op that retrieves optimization parameters from embedding to host
memory. Must be preceded by a ConfigureTPUEmbeddingHost op that sets up
the correct embedding table configuration. For example, this op is
used to retrieve updated parameters before saving a checkpoint.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_shards`<a id="num_shards"></a>
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`shard_id`<a id="shard_id"></a>
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`table_id`<a id="table_id"></a>
</td>
<td>
An optional `int`. Defaults to `-1`.
</td>
</tr><tr>
<td>
`table_name`<a id="table_name"></a>
</td>
<td>
An optional `string`. Defaults to `""`.
</td>
</tr><tr>
<td>
`config`<a id="config"></a>
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
A tuple of `Tensor` objects (parameters, last_hit_step).
</td>
</tr>
<tr>
<td>
`parameters`<a id="parameters"></a>
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`last_hit_step`<a id="last_hit_step"></a>
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr>
</table>

