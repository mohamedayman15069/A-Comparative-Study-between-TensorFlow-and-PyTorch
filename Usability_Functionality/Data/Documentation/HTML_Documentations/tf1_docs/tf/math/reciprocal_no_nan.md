<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.reciprocal_no_nan" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.reciprocal_no_nan

Performs a safe reciprocal operation, element wise.

### Aliases:

* `tf.compat.v1.math.reciprocal_no_nan`
* `tf.compat.v2.compat.v1.math.reciprocal_no_nan`
* `tf.compat.v2.math.reciprocal_no_nan`
* `tf.math.reciprocal_no_nan`

``` python
tf.math.reciprocal_no_nan(
    x,
    name=None
)
```

<!-- Placeholder for "Used in" -->

If a particular element is zero, the reciprocal for that element is
also set to zero.

#### For example:


```python
x = tf.constant([2.0, 0.5, 0, 1], dtype=tf.float32)
tf.math.reciprocal_no_nan(x)  # [ 0.5, 2, 0.0, 1.0 ]
```

#### Args:


* <b>`x`</b>: A `Tensor` of type `float16`, `float32`, `float64` `complex64` or
  `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of same shape and type as `x`.



#### Raises:


* <b>`TypeError`</b>: x must be of a valid dtype.