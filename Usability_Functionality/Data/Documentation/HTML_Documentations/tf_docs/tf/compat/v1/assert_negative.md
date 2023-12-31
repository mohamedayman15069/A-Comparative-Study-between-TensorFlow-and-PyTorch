description: Assert the condition x < 0 holds element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.assert_negative" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.assert_negative

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/check_ops.py">View source</a>



Assert the condition `x < 0` holds element-wise.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.debugging.assert_negative`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.assert_negative(
    x, data=None, summarize=None, message=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

When running in graph mode, you should add a dependency on this operation
to ensure that it runs. Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.debugging.assert_negative(x, y)]):
  output = tf.reduce_sum(x)
```

Negative means, for every element `x[i]` of `x`, we have `x[i] < 0`.
If `x` is empty this is trivially satisfied.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`<a id="x"></a>
</td>
<td>
 Numeric `Tensor`.
</td>
</tr><tr>
<td>
`data`<a id="data"></a>
</td>
<td>
 The tensors to print out if the condition is False.  Defaults to
error message and first few entries of `x`.
</td>
</tr><tr>
<td>
`summarize`<a id="summarize"></a>
</td>
<td>
Print this many entries of each tensor.
</td>
</tr><tr>
<td>
`message`<a id="message"></a>
</td>
<td>
A string to prefix to the default message.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
A name for this operation (optional).  Defaults to "assert_negative".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Op that raises `InvalidArgumentError` if `x < 0` is False.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`InvalidArgumentError`<a id="InvalidArgumentError"></a>
</td>
<td>
if the check can be performed immediately and
`x < 0` is False. The check can be performed immediately during
eager execution or if `x` is statically known.
</td>
</tr>
</table>



 <section><devsite-expandable expanded>
 <h2 class="showalways">eager compatibility</h2>

returns None

 </devsite-expandable></section>

