<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.boolean_mask" />
<meta itemprop="path" content="Stable" />
</div>

# tf.boolean_mask

Apply boolean mask to tensor.

### Aliases:

* `tf.boolean_mask`
* `tf.compat.v1.boolean_mask`
* `tf.compat.v2.compat.v1.boolean_mask`

``` python
tf.boolean_mask(
    tensor,
    mask,
    name='boolean_mask',
    axis=None
)
```

<!-- Placeholder for "Used in" -->

Numpy equivalent is `tensor[mask]`.

```python
# 1-D example
tensor = [0, 1, 2, 3]
mask = np.array([True, False, True, False])
boolean_mask(tensor, mask)  # [0, 2]
```

In general, `0 < dim(mask) = K <= dim(tensor)`, and `mask`'s shape must match
the first K dimensions of `tensor`'s shape.  We then have:
  `boolean_mask(tensor, mask)[i, j1,...,jd] = tensor[i1,...,iK,j1,...,jd]`
where `(i1,...,iK)` is the ith `True` entry of `mask` (row-major order).
The `axis` could be used with `mask` to indicate the axis to mask from.
In that case, `axis + dim(mask) <= dim(tensor)` and `mask`'s shape must match
the first `axis + dim(mask)` dimensions of `tensor`'s shape.

See also: <a href="../tf/ragged/boolean_mask.md"><code>tf.ragged.boolean_mask</code></a>, which can be applied to both dense and
ragged tensors, and can be used if you need to preserve the masked dimensions
of `tensor` (rather than flattening them, as <a href="../tf/boolean_mask.md"><code>tf.boolean_mask</code></a> does).

#### Args:


* <b>`tensor`</b>:  N-D tensor.
* <b>`mask`</b>:  K-D boolean tensor, K <= N and K must be known statically.
* <b>`name`</b>:  A name for this operation (optional).
* <b>`axis`</b>:  A 0-D int Tensor representing the axis in `tensor` to mask from. By
  default, axis is 0 which will mask from the first dimension. Otherwise K +
  axis <= N.


#### Returns:

(N-K+1)-dimensional tensor populated by entries in `tensor` corresponding
to `True` values in `mask`.



#### Raises:


* <b>`ValueError`</b>:  If shapes do not conform.


#### Examples:



```python
# 2-D example
tensor = [[1, 2], [3, 4], [5, 6]]
mask = np.array([True, False, True])
boolean_mask(tensor, mask)  # [[1, 2], [5, 6]]
```