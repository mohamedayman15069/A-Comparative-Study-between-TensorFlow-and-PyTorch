description: Creates a dataset that invokes a function to generate elements.
robots: noindex

# tf.raw_ops.GeneratorDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that invokes a function to generate elements.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.GeneratorDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.GeneratorDataset(
    init_func_other_args,
    next_func_other_args,
    finalize_func_other_args,
    init_func,
    next_func,
    finalize_func,
    output_types,
    output_shapes,
    metadata=&#x27;&#x27;,
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
`init_func_other_args`<a id="init_func_other_args"></a>
</td>
<td>
A list of `Tensor` objects.
</td>
</tr><tr>
<td>
`next_func_other_args`<a id="next_func_other_args"></a>
</td>
<td>
A list of `Tensor` objects.
</td>
</tr><tr>
<td>
`finalize_func_other_args`<a id="finalize_func_other_args"></a>
</td>
<td>
A list of `Tensor` objects.
</td>
</tr><tr>
<td>
`init_func`<a id="init_func"></a>
</td>
<td>
A function decorated with @Defun.
</td>
</tr><tr>
<td>
`next_func`<a id="next_func"></a>
</td>
<td>
A function decorated with @Defun.
</td>
</tr><tr>
<td>
`finalize_func`<a id="finalize_func"></a>
</td>
<td>
A function decorated with @Defun.
</td>
</tr><tr>
<td>
`output_types`<a id="output_types"></a>
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
</td>
</tr><tr>
<td>
`output_shapes`<a id="output_shapes"></a>
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
</td>
</tr><tr>
<td>
`metadata`<a id="metadata"></a>
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
A `Tensor` of type `variant`.
</td>
</tr>

</table>

