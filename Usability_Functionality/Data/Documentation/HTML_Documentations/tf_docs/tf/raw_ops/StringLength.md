description: String lengths of input.
robots: noindex

# tf.raw_ops.StringLength

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



String lengths of `input`.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StringLength`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StringLength(
    input, unit=&#x27;BYTE&#x27;, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the length of each string given in the input tensor.

```
>>> strings = tf.constant(['Hello','TensorFlow', '\U0001F642'])
>>> tf.strings.length(strings).numpy() # default counts bytes
array([ 5, 10, 4], dtype=int32)
>>> tf.strings.length(strings, unit="UTF8_CHAR").numpy()
array([ 5, 10, 1], dtype=int32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`<a id="input"></a>
</td>
<td>
A `Tensor` of type `string`.
The strings for which to compute the length for each element.
</td>
</tr><tr>
<td>
`unit`<a id="unit"></a>
</td>
<td>
An optional `string` from: `"BYTE", "UTF8_CHAR"`. Defaults to `"BYTE"`.
The unit that is counted to compute string length.  One of: `"BYTE"` (for
the number of bytes in each string) or `"UTF8_CHAR"` (for the number of UTF-8
encoded Unicode code points in each string).  Results are undefined
if `unit=UTF8_CHAR` and the `input` strings do not contain structurally
valid UTF-8.
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
A `Tensor` of type `int32`.
</td>
</tr>

</table>

