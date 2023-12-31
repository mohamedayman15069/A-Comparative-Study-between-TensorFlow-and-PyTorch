<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.batch_to_space" />
<meta itemprop="path" content="Stable" />
</div>

# tf.batch_to_space

BatchToSpace for 4-D tensors of type T.

### Aliases:

* `tf.batch_to_space`
* `tf.compat.v1.batch_to_space`
* `tf.compat.v2.compat.v1.batch_to_space`

``` python
tf.batch_to_space(
    input,
    crops,
    block_size,
    name=None,
    block_shape=None
)
```

<!-- Placeholder for "Used in" -->

This is a legacy version of the more general BatchToSpaceND.

Rearranges (permutes) data from batch into blocks of spatial data, followed by
cropping. This is the reverse transformation of SpaceToBatch. More specifically,
this op outputs a copy of the input tensor where values from the `batch`
dimension are moved in spatial blocks to the `height` and `width` dimensions,
followed by cropping along the `height` and `width` dimensions.

#### Args:


* <b>`input`</b>: A `Tensor`. 4-D tensor with shape
  `[batch*block_size*block_size, height_pad/block_size, width_pad/block_size,
    depth]`. Note that the batch size of the input tensor must be divisible by
  `block_size * block_size`.
* <b>`crops`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  2-D tensor of non-negative integers with shape `[2, 2]`. It specifies
  how many elements to crop from the intermediate result across the spatial
  dimensions as follows:

      crops = [[crop_top, crop_bottom], [crop_left, crop_right]]
* <b>`block_size`</b>: An `int` that is `>= 2`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
