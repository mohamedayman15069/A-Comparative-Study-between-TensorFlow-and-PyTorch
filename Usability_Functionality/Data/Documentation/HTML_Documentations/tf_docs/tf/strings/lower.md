description: Converts all uppercase characters into their respective lowercase replacements.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings.lower" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strings.lower

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Converts all uppercase characters into their respective lowercase replacements.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.strings.lower`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.strings.lower(
    input: Annotated[Any, _atypes.String],
    encoding: str = &#x27;&#x27;,
    name=None
) -> Annotated[Any, _atypes.String]
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example:



```
>>> tf.strings.lower("CamelCase string and ALL CAPS")
<tf.Tensor: shape=(), dtype=string, numpy=b'camelcase string and all caps'>
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
A `Tensor` of type `string`. The input to be lower-cased.
</td>
</tr><tr>
<td>
`encoding`<a id="encoding"></a>
</td>
<td>
An optional `string`. Defaults to `""`.
Character encoding of `input`. Allowed values are '' and 'utf-8'.
Value '' is interpreted as ASCII.
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
A `Tensor` of type `string`.
</td>
</tr>

</table>

