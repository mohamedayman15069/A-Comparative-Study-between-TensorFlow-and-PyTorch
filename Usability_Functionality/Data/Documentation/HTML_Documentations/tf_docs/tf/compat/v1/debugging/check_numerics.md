description: Checks a tensor for NaN and Inf values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.debugging.check_numerics" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.debugging.check_numerics

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Checks a tensor for NaN and Inf values.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.debugging.check_numerics(
    tensor: Annotated[Any, TV_CheckNumerics_T], message: str, name=None
) -> Annotated[Any, TV_CheckNumerics_T]
</code></pre>



<!-- Placeholder for "Used in" -->

When run, reports an `InvalidArgument` error if `tensor` has any values
that are not a number (NaN) or infinity (Inf). Otherwise, returns the input
tensor.

#### Example usage:



``` python
a = tf.Variable(1.0)
tf.debugging.check_numerics(a, message='')

b = tf.Variable(np.nan)
try:
  tf.debugging.check_numerics(b, message='Checking b')
except Exception as e:
  assert "Checking b : Tensor had NaN values" in e.message

c = tf.Variable(np.inf)
try:
  tf.debugging.check_numerics(c, message='Checking c')
except Exception as e:
  assert "Checking c : Tensor had Inf values" in e.message
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`<a id="tensor"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
</td>
</tr><tr>
<td>
`message`<a id="message"></a>
</td>
<td>
A `string`. Prefix of the error message.
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
A `Tensor`. Has the same type as `tensor`.
</td>
</tr>

</table>

