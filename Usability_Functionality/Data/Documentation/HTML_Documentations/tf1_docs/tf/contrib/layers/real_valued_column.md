<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.layers.real_valued_column" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.layers.real_valued_column

Creates a `_RealValuedColumn` for dense numeric data.

``` python
tf.contrib.layers.real_valued_column(
    column_name,
    dimension=1,
    default_value=None,
    dtype=tf.dtypes.float32,
    normalizer=None
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`column_name`</b>: A string defining real valued column name.
* <b>`dimension`</b>: An integer specifying dimension of the real valued column. The
  default is 1.
* <b>`default_value`</b>: A single value compatible with dtype or a list of values
  compatible with dtype which the column takes on during tf.Example parsing
  if data is missing. When dimension is not None, a default value of None
  will cause tf.io.parse_example to fail if an example does not contain this
  column. If a single value is provided, the same value will be applied as
  the default value for every dimension. If a list of values is provided,
  the length of the list should be equal to the value of `dimension`. Only
  scalar default value is supported in case dimension is not specified.
* <b>`dtype`</b>: defines the type of values. Default value is tf.float32. Must be a
  non-quantized, real integer or floating point type.
* <b>`normalizer`</b>: If not None, a function that can be used to normalize the value
  of the real valued column after default_value is applied for parsing.
  Normalizer function takes the input tensor as its argument, and returns
  the output tensor. (e.g. lambda x: (x - 3.0) / 4.2). Note that for
    variable length columns, the normalizer should expect an input_tensor of
    type `SparseTensor`.


#### Returns:

A _RealValuedColumn.


#### Raises:


* <b>`TypeError`</b>: if dimension is not an int
* <b>`ValueError`</b>: if dimension is not a positive integer
* <b>`TypeError`</b>: if default_value is a list but its length is not equal to the
  value of `dimension`.
* <b>`TypeError`</b>: if default_value is not compatible with dtype.
* <b>`ValueError`</b>: if dtype is not convertible to tf.float32.