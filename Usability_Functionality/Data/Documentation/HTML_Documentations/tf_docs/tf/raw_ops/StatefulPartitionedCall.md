description: returns f(inputs), where f's body is placed and partitioned.
robots: noindex

# tf.raw_ops.StatefulPartitionedCall

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



returns `f(inputs)`, where `f`'s body is placed and partitioned.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StatefulPartitionedCall`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StatefulPartitionedCall(
    args,
    Tout,
    f,
    config=&#x27;&#x27;,
    config_proto=&#x27;&#x27;,
    executor_type=&#x27;&#x27;,
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
`args`<a id="args"></a>
</td>
<td>
A list of `Tensor` objects. A list of input tensors.
</td>
</tr><tr>
<td>
`Tout`<a id="Tout"></a>
</td>
<td>
A list of `tf.DTypes`. A list of output types.
</td>
</tr><tr>
<td>
`f`<a id="f"></a>
</td>
<td>
A function decorated with @Defun.
A function that takes 'args', a list of tensors, and returns 'output',
another list of tensors. Input and output types are specified by 'Tin'
and 'Tout'. The function body of f will be placed and partitioned across
devices, setting this op apart from the regular Call op. This op is
stateful.
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
`config_proto`<a id="config_proto"></a>
</td>
<td>
An optional `string`. Defaults to `""`.
</td>
</tr><tr>
<td>
`executor_type`<a id="executor_type"></a>
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
A list of `Tensor` objects of type `Tout`.
</td>
</tr>

</table>

