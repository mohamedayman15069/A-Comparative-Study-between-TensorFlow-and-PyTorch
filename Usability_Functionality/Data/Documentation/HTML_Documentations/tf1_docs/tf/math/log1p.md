<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.log1p" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.log1p

Computes natural logarithm of (1 + x) element-wise.

### Aliases:

* `tf.compat.v1.log1p`
* `tf.compat.v1.math.log1p`
* `tf.compat.v2.compat.v1.log1p`
* `tf.compat.v2.compat.v1.math.log1p`
* `tf.compat.v2.math.log1p`
* `tf.log1p`
* `tf.math.log1p`

``` python
tf.math.log1p(
    x,
    name=None
)
```

<!-- Placeholder for "Used in" -->

I.e., \\(y = \log_e (1 + x)\\).

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
