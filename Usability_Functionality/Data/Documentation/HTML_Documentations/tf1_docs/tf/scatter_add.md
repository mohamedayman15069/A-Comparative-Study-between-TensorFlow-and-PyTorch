<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.scatter_add" />
<meta itemprop="path" content="Stable" />
</div>

# tf.scatter_add

Adds sparse updates to the variable referenced by `resource`.

### Aliases:

* `tf.compat.v1.scatter_add`
* `tf.compat.v2.compat.v1.scatter_add`
* `tf.scatter_add`

``` python
tf.scatter_add(
    ref,
    indices,
    updates,
    use_locking=False,
    name=None
)
```

<!-- Placeholder for "Used in" -->

This operation computes

```python
    # Scalar indices
    ref[indices, ...] += updates[...]

    # Vector indices (for each i)
    ref[indices[i], ...] += updates[i, ...]

    # High rank indices (for each i, ..., j)
    ref[indices[i, ..., j], ...] += updates[i, ..., j, ...]
```

This operation outputs `ref` after the update is done.
This makes it easier to chain operations that need to use the updated value.
Duplicate entries are handled correctly: if multiple `indices` reference
the same location, their contributions add.

Requires `updates.shape = indices.shape + ref.shape[1:]`.

<div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src='https://www.tensorflow.org/images/ScatterAdd.png' alt>
</div>

#### Args:


* <b>`ref`</b>: A `Variable`.
* <b>`indices`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  A tensor of indices into the first dimension of `ref`.
* <b>`updates`</b>: A `Tensor`. Must have the same type as `ref`.
  A tensor of updated values to store in `ref`.
* <b>`use_locking`</b>: An optional `bool`. Defaults to `False`.
  If True, the assignment will be protected by a lock;
  otherwise the behavior is undefined, but may exhibit less contention.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

Same as `ref`.  Returned as a convenience for operations that want
to use the updated values after the update is done.
