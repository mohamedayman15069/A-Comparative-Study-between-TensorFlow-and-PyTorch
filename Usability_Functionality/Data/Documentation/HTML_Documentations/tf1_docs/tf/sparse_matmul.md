<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse_matmul" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse_matmul

Multiply matrix "a" by matrix "b".

### Aliases:

* `tf.compat.v1.sparse_matmul`
* `tf.compat.v2.compat.v1.sparse_matmul`
* `tf.sparse_matmul`

``` python
tf.sparse_matmul(
    a,
    b,
    transpose_a=False,
    transpose_b=False,
    a_is_sparse=False,
    b_is_sparse=False,
    name=None
)
```

<!-- Placeholder for "Used in" -->

The inputs must be two-dimensional matrices and the inner dimension of "a" must
match the outer dimension of "b". Both "a" and "b" must be `Tensor`s not
`SparseTensor`s.  This op is optimized for the case where at least one of "a" or
"b" is sparse, in the sense that they have a large proportion of zero values.
The breakeven for using this versus a dense matrix multiply on one platform was
30% zero values in the sparse matrix.

The gradient computation of this operation will only take advantage of sparsity
in the input gradient when that gradient comes from a Relu.

#### Args:


* <b>`a`</b>: A `Tensor`. Must be one of the following types: `float32`, `bfloat16`.
* <b>`b`</b>: A `Tensor`. Must be one of the following types: `float32`, `bfloat16`.
* <b>`transpose_a`</b>: An optional `bool`. Defaults to `False`.
* <b>`transpose_b`</b>: An optional `bool`. Defaults to `False`.
* <b>`a_is_sparse`</b>: An optional `bool`. Defaults to `False`.
* <b>`b_is_sparse`</b>: An optional `bool`. Defaults to `False`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32`.
