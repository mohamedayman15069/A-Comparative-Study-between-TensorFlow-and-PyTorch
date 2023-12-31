<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.adjust_jpeg_quality" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.adjust_jpeg_quality

Adjust jpeg encoding quality of an RGB image.

### Aliases:

* `tf.compat.v1.image.adjust_jpeg_quality`
* `tf.compat.v2.compat.v1.image.adjust_jpeg_quality`
* `tf.compat.v2.image.adjust_jpeg_quality`
* `tf.image.adjust_jpeg_quality`

``` python
tf.image.adjust_jpeg_quality(
    image,
    jpeg_quality,
    name=None
)
```

<!-- Placeholder for "Used in" -->

This is a convenience method that adjusts jpeg encoding quality of an
RGB image.

`image` is an RGB image.  The image's encoding quality is adjusted
to `jpeg_quality`.
`jpeg_quality` must be in the interval `[0, 100]`.

#### Args:


* <b>`image`</b>: RGB image or images. Size of the last dimension must be 3.
* <b>`jpeg_quality`</b>: Python int or Tensor of type int32.  jpeg encoding quality.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

Adjusted image(s), same shape and DType as `image`.



#### Usage Example:

```python
>> import tensorflow as tf
>> x = tf.random.normal(shape=(256, 256, 3))
>> tf.image.adjust_jpeg_quality(x, 75)
```


#### Raises:


* <b>`InvalidArgumentError`</b>: quality must be in [0,100]
* <b>`InvalidArgumentError`</b>: image must have 1 or 3 channels