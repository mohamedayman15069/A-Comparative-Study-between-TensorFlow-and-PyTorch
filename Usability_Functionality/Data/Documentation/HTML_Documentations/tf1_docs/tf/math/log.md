<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.log" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.log

Computes natural logarithm of x element-wise.

### Aliases:

* `tf.compat.v1.log`
* `tf.compat.v1.math.log`
* `tf.compat.v2.compat.v1.log`
* `tf.compat.v2.compat.v1.math.log`
* `tf.compat.v2.math.log`
* `tf.log`
* `tf.math.log`

``` python
tf.math.log(
    x,
    name=None
)
```

<!-- Placeholder for "Used in" -->

I.e., \\(y = \log_e x\\).

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
