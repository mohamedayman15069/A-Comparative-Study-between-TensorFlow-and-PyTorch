description: Return substrings from Tensor of strings.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.strings.substr" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.strings.substr

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/string_ops.py">View source</a>



Return substrings from `Tensor` of strings.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.strings.substr(
    input, pos, len, name=None, unit=&#x27;BYTE&#x27;
)
</code></pre>



<!-- Placeholder for "Used in" -->

For each string in the input `Tensor`, creates a substring starting at index
`pos` with a total length of `len`.

If `len` defines a substring that would extend beyond the length of the input
string, or if `len` is negative, then as many characters as possible are used.

A negative `pos` indicates distance within the string backwards from the end.

If `pos` specifies an index which is out of range for any of the input strings,
then an `InvalidArgumentError` is thrown.

`pos` and `len` must have the same shape, otherwise a `ValueError` is thrown on
Op creation.

*NOTE*: `Substr` supports broadcasting up to two dimensions. More about
broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

---

Examples

Using scalar `pos` and `len`:

```python
input = [b'Hello', b'World']
position = 1
length = 3

output = [b'ell', b'orl']
```

Using `pos` and `len` with same shape as `input`:

```python
input = [[b'ten', b'eleven', b'twelve'],
         [b'thirteen', b'fourteen', b'fifteen'],
         [b'sixteen', b'seventeen', b'eighteen']]
position = [[1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]]
length =   [[2, 3, 4],
            [4, 3, 2],
            [5, 5, 5]]

output = [[b'en', b'eve', b'lve'],
          [b'hirt', b'urt', b'te'],
          [b'ixtee', b'vente', b'hteen']]
```

Broadcasting `pos` and `len` onto `input`:

```
input = [[b'ten', b'eleven', b'twelve'],
         [b'thirteen', b'fourteen', b'fifteen'],
         [b'sixteen', b'seventeen', b'eighteen'],
         [b'nineteen', b'twenty', b'twentyone']]
position = [1, 2, 3]
length =   [1, 2, 3]

output = [[b'e', b'ev', b'lve'],
          [b'h', b'ur', b'tee'],
          [b'i', b've', b'hte'],
          [b'i', b'en', b'nty']]
```

Broadcasting `input` onto `pos` and `len`:

```
input = b'thirteen'
position = [1, 5, 7]
length =   [3, 2, 1]

output = [b'hir', b'ee', b'n']
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>
<tr class="alt">
<td colspan="2">
* `ValueError`: If the first argument cannot be converted to a
   Tensor of `dtype string`.
* `InvalidArgumentError`: If indices are out of range.
* `ValueError`: If `pos` and `len` are not the same shape.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`<a id="input"></a>
</td>
<td>
A `Tensor` of type `string`. Tensor of strings
</td>
</tr><tr>
<td>
`pos`<a id="pos"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
Scalar defining the position of first character in each substring
</td>
</tr><tr>
<td>
`len`<a id="len"></a>
</td>
<td>
A `Tensor`. Must have the same type as `pos`.
Scalar defining the number of characters to include in each substring
</td>
</tr><tr>
<td>
`unit`<a id="unit"></a>
</td>
<td>
An optional `string` from: `"BYTE", "UTF8_CHAR"`. Defaults to `"BYTE"`.
The unit that is used to create the substring.  One of: `"BYTE"` (for
defining position and length by bytes) or `"UTF8_CHAR"` (for the UTF-8
encoded Unicode code points).  The default is `"BYTE"`. Results are undefined if
`unit=UTF8_CHAR` and the `input` strings do not contain structurally valid
UTF-8.
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

