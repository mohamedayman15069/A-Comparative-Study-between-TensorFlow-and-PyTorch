<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.qr" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.qr

Computes the QR decompositions of one or more matrices.

### Aliases:

* `tf.compat.v1.linalg.qr`
* `tf.compat.v1.qr`
* `tf.compat.v2.compat.v1.linalg.qr`
* `tf.compat.v2.compat.v1.qr`
* `tf.compat.v2.linalg.qr`
* `tf.linalg.qr`
* `tf.qr`

``` python
tf.linalg.qr(
    input,
    full_matrices=False,
    name=None
)
```

<!-- Placeholder for "Used in" -->

Computes the QR decomposition of each inner matrix in `tensor` such that
`tensor[..., :, :] = q[..., :, :] * r[..., :,:])`

```python
# a is a tensor.
# q is a tensor of orthonormal matrices.
# r is a tensor of upper triangular matrices.
q, r = qr(a)
q_full, r_full = qr(a, full_matrices=True)
```

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
  A tensor of shape `[..., M, N]` whose inner-most 2 dimensions
  form matrices of size `[M, N]`. Let `P` be the minimum of `M` and `N`.
* <b>`full_matrices`</b>: An optional `bool`. Defaults to `False`.
  If true, compute full-sized `q` and `r`. If false
  (the default), compute only the leading `P` columns of `q`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `Tensor` objects (q, r).


* <b>`q`</b>: A `Tensor`. Has the same type as `input`.
* <b>`r`</b>: A `Tensor`. Has the same type as `input`.