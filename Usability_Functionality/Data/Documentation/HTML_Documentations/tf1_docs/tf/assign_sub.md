<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.assign_sub" />
<meta itemprop="path" content="Stable" />
</div>

# tf.assign_sub

Update `ref` by subtracting `value` from it.

### Aliases:

* `tf.assign_sub`
* `tf.compat.v1.assign_sub`
* `tf.compat.v2.compat.v1.assign_sub`

``` python
tf.assign_sub(
    ref,
    value,
    use_locking=None,
    name=None
)
```

<!-- Placeholder for "Used in" -->

This operation outputs `ref` after the update is done.
This makes it easier to chain operations that need to use the reset value.
Unlike <a href="../tf/math/subtract.md"><code>tf.math.subtract</code></a>, this op does not broadcast. `ref` and `value`
must have the same shape.

#### Args:


* <b>`ref`</b>: A mutable `Tensor`. Must be one of the following types: `float32`,
  `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`,
  `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`. Should be
  from a `Variable` node.
* <b>`value`</b>: A `Tensor`. Must have the same shape and dtype as `ref`. The value to
  be subtracted to the variable.
* <b>`use_locking`</b>: An optional `bool`. Defaults to `False`. If True, the
  subtraction will be protected by a lock; otherwise the behavior is
  undefined, but may exhibit less contention.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

Same as "ref".  Returned as a convenience for operations that want
to use the new value after the variable has been updated.
