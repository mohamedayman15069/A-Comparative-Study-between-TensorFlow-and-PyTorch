<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.cross" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.cross

Generates sparse cross from a list of sparse and dense tensors.

### Aliases:

* `tf.compat.v1.sparse.cross`
* `tf.compat.v2.compat.v1.sparse.cross`
* `tf.compat.v2.sparse.cross`
* `tf.sparse.cross`

``` python
tf.sparse.cross(
    inputs,
    name=None
)
```

<!-- Placeholder for "Used in" -->

For example, if the inputs are

    * inputs[0]: SparseTensor with shape = [2, 2]
      [0, 0]: "a"
      [1, 0]: "b"
      [1, 1]: "c"
    * inputs[1]: SparseTensor with shape = [2, 1]
      [0, 0]: "d"
      [1, 0]: "e"
    * inputs[2]: Tensor [["f"], ["g"]]

then the output will be:

    shape = [2, 2]
    [0, 0]: "a_X_d_X_f"
    [1, 0]: "b_X_e_X_g"
    [1, 1]: "c_X_e_X_g"

#### Args:


* <b>`inputs`</b>: An iterable of `Tensor` or `SparseTensor`.
* <b>`name`</b>: Optional name for the op.


#### Returns:

A `SparseTensor` of type `string`.
