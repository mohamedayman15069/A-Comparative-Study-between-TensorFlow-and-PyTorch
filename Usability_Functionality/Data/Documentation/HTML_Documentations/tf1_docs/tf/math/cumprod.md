<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.cumprod" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.cumprod

Compute the cumulative product of the tensor `x` along `axis`.

### Aliases:

* `tf.compat.v1.cumprod`
* `tf.compat.v1.math.cumprod`
* `tf.compat.v2.compat.v1.cumprod`
* `tf.compat.v2.compat.v1.math.cumprod`
* `tf.compat.v2.math.cumprod`
* `tf.cumprod`
* `tf.math.cumprod`

``` python
tf.math.cumprod(
    x,
    axis=0,
    exclusive=False,
    reverse=False,
    name=None
)
```

<!-- Placeholder for "Used in" -->

By default, this op performs an inclusive cumprod, which means that the
first element of the input is identical to the first element of the output:

```python
tf.math.cumprod([a, b, c])  # [a, a * b, a * b * c]
```

By setting the `exclusive` kwarg to `True`, an exclusive cumprod is
performed
instead:

```python
tf.math.cumprod([a, b, c], exclusive=True)  # [1, a, a * b]
```

By setting the `reverse` kwarg to `True`, the cumprod is performed in the
opposite direction:

```python
tf.math.cumprod([a, b, c], reverse=True)  # [a * b * c, b * c, c]
```

This is more efficient than using separate <a href="../../tf/reverse.md"><code>tf.reverse</code></a> ops.
The `reverse` and `exclusive` kwargs can also be combined:

```python
tf.math.cumprod([a, b, c], exclusive=True, reverse=True)  # [b * c, c, 1]
```

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`,
  `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`,
  `complex128`, `qint8`, `quint8`, `qint32`, `half`.
* <b>`axis`</b>: A `Tensor` of type `int32` (default: 0). Must be in the range
  `[-rank(x), rank(x))`.
* <b>`exclusive`</b>: If `True`, perform exclusive cumprod.
* <b>`reverse`</b>: A `bool` (default: False).
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
