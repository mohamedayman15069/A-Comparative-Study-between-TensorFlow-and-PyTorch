<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.pad_to_bounding_box" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.pad_to_bounding_box

Pad `image` with zeros to the specified `height` and `width`.

### Aliases:

* `tf.compat.v1.image.pad_to_bounding_box`
* `tf.compat.v2.compat.v1.image.pad_to_bounding_box`
* `tf.compat.v2.image.pad_to_bounding_box`
* `tf.image.pad_to_bounding_box`

``` python
tf.image.pad_to_bounding_box(
    image,
    offset_height,
    offset_width,
    target_height,
    target_width
)
```

<!-- Placeholder for "Used in" -->

Adds `offset_height` rows of zeros on top, `offset_width` columns of
zeros on the left, and then pads the image on the bottom and right
with zeros until it has dimensions `target_height`, `target_width`.

This op does nothing if `offset_*` is zero and the image already has size
`target_height` by `target_width`.

#### Args:


* <b>`image`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
  of shape `[height, width, channels]`.
* <b>`offset_height`</b>: Number of rows of zeros to add on top.
* <b>`offset_width`</b>: Number of columns of zeros to add on the left.
* <b>`target_height`</b>: Height of output image.
* <b>`target_width`</b>: Width of output image.


#### Returns:

If `image` was 4-D, a 4-D float Tensor of shape
`[batch, target_height, target_width, channels]`
If `image` was 3-D, a 3-D float Tensor of shape
`[target_height, target_width, channels]`



#### Raises:


* <b>`ValueError`</b>: If the shape of `image` is incompatible with the `offset_*` or
  `target_*` arguments, or either `offset_height` or `offset_width` is
  negative.