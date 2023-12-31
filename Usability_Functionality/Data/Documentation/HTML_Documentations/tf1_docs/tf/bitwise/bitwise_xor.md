<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.bitwise.bitwise_xor" />
<meta itemprop="path" content="Stable" />
</div>

# tf.bitwise.bitwise_xor

Elementwise computes the bitwise XOR of `x` and `y`.

### Aliases:

* `tf.bitwise.bitwise_xor`
* `tf.compat.v1.bitwise.bitwise_xor`
* `tf.compat.v2.bitwise.bitwise_xor`
* `tf.compat.v2.compat.v1.bitwise.bitwise_xor`

``` python
tf.bitwise.bitwise_xor(
    x,
    y,
    name=None
)
```

<!-- Placeholder for "Used in" -->

The result will have those bits set, that are different in `x` and `y`. The
computation is performed on the underlying representations of `x` and `y`.

#### For example:



```python
import tensorflow as tf
from tensorflow.python.ops import bitwise_ops
dtype_list = [tf.int8, tf.int16, tf.int32, tf.int64,
              tf.uint8, tf.uint16, tf.uint32, tf.uint64]

for dtype in dtype_list:
  lhs = tf.constant([0, 5, 3, 14], dtype=dtype)
  rhs = tf.constant([5, 0, 7, 11], dtype=dtype)
  exp = tf.constant([5, 5, 4, 5],  dtype=tf.float32)

  res = bitwise_ops.bitwise_xor(lhs, rhs)
  tf.assert_equal(tf.cast(res, tf.float32), exp) # TRUE
```

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
