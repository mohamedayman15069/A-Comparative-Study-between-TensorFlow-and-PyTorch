<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.yuv_to_rgb" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.yuv_to_rgb

Converts one or more images from YUV to RGB.

### Aliases:

* `tf.compat.v1.image.yuv_to_rgb`
* `tf.compat.v2.compat.v1.image.yuv_to_rgb`
* `tf.compat.v2.image.yuv_to_rgb`
* `tf.image.yuv_to_rgb`

``` python
tf.image.yuv_to_rgb(images)
```

<!-- Placeholder for "Used in" -->

Outputs a tensor of the same shape as the `images` tensor, containing the RGB
value of the pixels.
The output is only well defined if the Y value in images are in [0,1],
U and V value are in [-0.5,0.5].

#### Args:


* <b>`images`</b>: 2-D or higher rank. Image data to convert. Last dimension must be
  size 3.


#### Returns:


* <b>`images`</b>: tensor with the same shape as `images`.