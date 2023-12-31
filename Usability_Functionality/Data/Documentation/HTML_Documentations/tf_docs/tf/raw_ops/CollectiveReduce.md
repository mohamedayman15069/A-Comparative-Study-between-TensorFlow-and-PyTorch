description: Mutually reduces multiple tensors of identical type and shape.
robots: noindex

# tf.raw_ops.CollectiveReduce

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Mutually reduces multiple tensors of identical type and shape.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CollectiveReduce`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CollectiveReduce(
    input,
    group_size,
    group_key,
    instance_key,
    merge_op,
    final_op,
    subdiv_offsets,
    wait_for=[],
    communication_hint=&#x27;auto&#x27;,
    timeout_seconds=0,
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
`input`<a id="input"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `half`, `float64`, `int32`, `int64`.
</td>
</tr><tr>
<td>
`group_size`<a id="group_size"></a>
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`group_key`<a id="group_key"></a>
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`instance_key`<a id="instance_key"></a>
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`merge_op`<a id="merge_op"></a>
</td>
<td>
A `string` from: `"Min", "Max", "Mul", "Add"`.
</td>
</tr><tr>
<td>
`final_op`<a id="final_op"></a>
</td>
<td>
A `string` from: `"Id", "Div"`.
</td>
</tr><tr>
<td>
`subdiv_offsets`<a id="subdiv_offsets"></a>
</td>
<td>
A list of `ints`.
</td>
</tr><tr>
<td>
`wait_for`<a id="wait_for"></a>
</td>
<td>
An optional list of `ints`. Defaults to `[]`.
</td>
</tr><tr>
<td>
`communication_hint`<a id="communication_hint"></a>
</td>
<td>
An optional `string`. Defaults to `"auto"`.
</td>
</tr><tr>
<td>
`timeout_seconds`<a id="timeout_seconds"></a>
</td>
<td>
An optional `float`. Defaults to `0`.
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

