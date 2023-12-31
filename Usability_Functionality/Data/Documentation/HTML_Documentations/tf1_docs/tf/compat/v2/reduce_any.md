<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v2.reduce_any" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v2.reduce_any

Computes the "logical or" of elements across dimensions of a tensor.

### Aliases:

* `tf.compat.v2.math.reduce_any`
* `tf.compat.v2.reduce_any`

``` python
tf.compat.v2.reduce_any(
    input_tensor,
    axis=None,
    keepdims=False,
    name=None
)
```

<!-- Placeholder for "Used in" -->

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
entry in `axis`. If `keepdims` is true, the reduced dimensions
are retained with length 1.

If `axis` is None, all dimensions are reduced, and a
tensor with a single element is returned.

#### For example:



```python
x = tf.constant([[True,  True], [False, False]])
tf.reduce_any(x)  # True
tf.reduce_any(x, 0)  # [True, True]
tf.reduce_any(x, 1)  # [True, False]
```

#### Args:


* <b>`input_tensor`</b>: The boolean tensor to reduce.
* <b>`axis`</b>: The dimensions to reduce. If `None` (the default), reduces all
  dimensions. Must be in the range `[-rank(input_tensor),
  rank(input_tensor))`.
* <b>`keepdims`</b>: If true, retains reduced dimensions with length 1.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The reduced tensor.




#### Numpy Compatibility
Equivalent to np.any

