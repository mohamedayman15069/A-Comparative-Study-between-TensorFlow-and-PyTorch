<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.to_dense" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.to_dense

Converts a `SparseTensor` into a dense tensor.

### Aliases:

* `tf.compat.v1.sparse.to_dense`
* `tf.compat.v1.sparse_tensor_to_dense`
* `tf.compat.v2.compat.v1.sparse.to_dense`
* `tf.compat.v2.compat.v1.sparse_tensor_to_dense`
* `tf.compat.v2.sparse.to_dense`
* `tf.sparse.to_dense`
* `tf.sparse_tensor_to_dense`

``` python
tf.sparse.to_dense(
    sp_input,
    default_value=None,
    validate_indices=True,
    name=None
)
```

<!-- Placeholder for "Used in" -->

This op is a convenience wrapper around `sparse_to_dense` for `SparseTensor`s.

For example, if `sp_input` has shape `[3, 5]` and non-empty string values:

    [0, 1]: a
    [0, 3]: b
    [2, 0]: c

and `default_value` is `x`, then the output will be a dense `[3, 5]`
string tensor with values:

    [[x a x b x]
     [x x x x x]
     [c x x x x]]

Indices must be without repeats.  This is only
tested if `validate_indices` is `True`.

#### Args:


* <b>`sp_input`</b>: The input `SparseTensor`.
* <b>`default_value`</b>: Scalar value to set for indices not specified in
  `sp_input`.  Defaults to zero.
* <b>`validate_indices`</b>: A boolean value.  If `True`, indices are checked to make
  sure they are sorted in lexicographic order and that there are no repeats.
* <b>`name`</b>: A name prefix for the returned tensors (optional).


#### Returns:

A dense tensor with shape `sp_input.dense_shape` and values specified by
the non-empty values in `sp_input`. Indices not in `sp_input` are assigned
`default_value`.



#### Raises:


* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.