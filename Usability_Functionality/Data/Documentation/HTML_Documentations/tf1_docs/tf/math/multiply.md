<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.multiply" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.multiply

Returns x * y element-wise.

### Aliases:

* `tf.RaggedTensor.__mul__`
* `tf.compat.v1.RaggedTensor.__mul__`
* `tf.compat.v1.math.multiply`
* `tf.compat.v1.multiply`
* `tf.compat.v2.RaggedTensor.__mul__`
* `tf.compat.v2.compat.v1.RaggedTensor.__mul__`
* `tf.compat.v2.compat.v1.math.multiply`
* `tf.compat.v2.compat.v1.multiply`
* `tf.compat.v2.math.multiply`
* `tf.compat.v2.multiply`
* `tf.math.multiply`
* `tf.multiply`

``` python
tf.math.multiply(
    x,
    y,
    name=None
)
```

<!-- Placeholder for "Used in" -->

*NOTE*: <a href="../../tf/math/multiply.md"><code>tf.multiply</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
