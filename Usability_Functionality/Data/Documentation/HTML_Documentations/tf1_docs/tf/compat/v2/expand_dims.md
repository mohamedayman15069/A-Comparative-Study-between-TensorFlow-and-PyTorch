<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v2.expand_dims" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v2.expand_dims

Inserts a dimension of 1 into a tensor's shape.

``` python
tf.compat.v2.expand_dims(
    input,
    axis,
    name=None
)
```

<!-- Placeholder for "Used in" -->

Given a tensor `input`, this operation inserts a dimension of 1 at the
dimension index `axis` of `input`'s shape. The dimension index `axis` starts
at zero; if you specify a negative number for `axis` it is counted backward
from the end.

This operation is useful if you want to add a batch dimension to a single
element. For example, if you have a single image of shape `[height, width,
channels]`, you can make it a batch of 1 image with `expand_dims(image, 0)`,
which will make the shape `[1, height, width, channels]`.

#### Other examples:



```python
# 't' is a tensor of shape [2]
tf.shape(tf.expand_dims(t, 0))  # [1, 2]
tf.shape(tf.expand_dims(t, 1))  # [2, 1]
tf.shape(tf.expand_dims(t, -1))  # [2, 1]

# 't2' is a tensor of shape [2, 3, 5]
tf.shape(tf.expand_dims(t2, 0))  # [1, 2, 3, 5]
tf.shape(tf.expand_dims(t2, 2))  # [2, 3, 1, 5]
tf.shape(tf.expand_dims(t2, 3))  # [2, 3, 5, 1]
```

This operation requires that:

`-1-input.dims() <= dim <= input.dims()`

This operation is related to `squeeze()`, which removes dimensions of
size 1.

#### Args:


* <b>`input`</b>: A `Tensor`.
* <b>`axis`</b>: 0-D (scalar). Specifies the dimension index at which to expand the
  shape of `input`. Must be in the range `[-rank(input) - 1, rank(input)]`.
* <b>`name`</b>: The name of the output `Tensor` (optional).


#### Returns:

A `Tensor` with the same data as `input`, but its shape has an additional
dimension of size 1 added.
