<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.assign" />
<meta itemprop="path" content="Stable" />
</div>

# tf.assign

Update `ref` by assigning `value` to it.

### Aliases:

* `tf.assign`
* `tf.compat.v1.assign`
* `tf.compat.v2.compat.v1.assign`

``` python
tf.assign(
    ref,
    value,
    validate_shape=None,
    use_locking=None,
    name=None
)
```

<!-- Placeholder for "Used in" -->

This operation outputs a Tensor that holds the new value of `ref` after
the value has been assigned. This makes it easier to chain operations that
need to use the reset value.

#### Args:


* <b>`ref`</b>: A mutable `Tensor`. Should be from a `Variable` node. May be
  uninitialized.
* <b>`value`</b>: A `Tensor`. Must have the same shape and dtype as `ref`. The value to
  be assigned to the variable.
* <b>`validate_shape`</b>: An optional `bool`. Defaults to `True`. If true, the
  operation will validate that the shape of 'value' matches the shape of the
  Tensor being assigned to.  If false, 'ref' will take on the shape of
  'value'.
* <b>`use_locking`</b>: An optional `bool`. Defaults to `True`. If True, the assignment
  will be protected by a lock; otherwise the behavior is undefined, but may
  exhibit less contention.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` that will hold the new value of `ref` after
  the assignment has completed.
