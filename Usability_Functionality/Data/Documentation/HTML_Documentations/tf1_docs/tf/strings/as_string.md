<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings.as_string" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strings.as_string

Converts each entry in the given tensor to strings.

### Aliases:

* `tf.as_string`
* `tf.compat.v1.as_string`
* `tf.compat.v1.dtypes.as_string`
* `tf.compat.v1.strings.as_string`
* `tf.compat.v2.as_string`
* `tf.compat.v2.compat.v1.as_string`
* `tf.compat.v2.compat.v1.dtypes.as_string`
* `tf.compat.v2.compat.v1.strings.as_string`
* `tf.compat.v2.strings.as_string`
* `tf.dtypes.as_string`
* `tf.strings.as_string`

``` python
tf.strings.as_string(
    input,
    precision=-1,
    scientific=False,
    shortest=False,
    width=-1,
    fill='',
    name=None
)
```

<!-- Placeholder for "Used in" -->

Supports many numeric types and boolean.

For Unicode, see the
[https://www.tensorflow.org/tutorials/representation/unicode](Working with Unicode text)
tutorial.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `float32`, `float64`, `bool`.
* <b>`precision`</b>: An optional `int`. Defaults to `-1`.
  The post-decimal precision to use for floating point numbers.
  Only used if precision > -1.
* <b>`scientific`</b>: An optional `bool`. Defaults to `False`.
  Use scientific notation for floating point numbers.
* <b>`shortest`</b>: An optional `bool`. Defaults to `False`.
  Use shortest representation (either scientific or standard) for
  floating point numbers.
* <b>`width`</b>: An optional `int`. Defaults to `-1`.
  Pad pre-decimal numbers to this width.
  Applies to both floating point and integer numbers.
  Only used if width > -1.
* <b>`fill`</b>: An optional `string`. Defaults to `""`.
  The value to pad if width > -1.  If empty, pads with spaces.
  Another typical value is '0'.  String cannot be longer than 1 character.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
