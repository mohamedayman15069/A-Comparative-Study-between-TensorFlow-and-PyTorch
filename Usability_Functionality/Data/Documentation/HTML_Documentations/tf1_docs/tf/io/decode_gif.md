<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.decode_gif" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.decode_gif

Decode the frame(s) of a GIF-encoded image to a uint8 tensor.

### Aliases:

* `tf.compat.v1.image.decode_gif`
* `tf.compat.v1.io.decode_gif`
* `tf.compat.v2.compat.v1.image.decode_gif`
* `tf.compat.v2.compat.v1.io.decode_gif`
* `tf.compat.v2.image.decode_gif`
* `tf.compat.v2.io.decode_gif`
* `tf.image.decode_gif`
* `tf.io.decode_gif`

``` python
tf.io.decode_gif(
    contents,
    name=None
)
```

<!-- Placeholder for "Used in" -->

GIF images with frame or transparency compression are not supported.
On Linux and MacOS systems, convert animated GIFs from compressed to
uncompressed by running:

    convert $src.gif -coalesce $dst.gif

This op also supports decoding JPEGs and PNGs, though it is cleaner to use
<a href="../../tf/io/decode_image.md"><code>tf.image.decode_image</code></a>.

#### Args:


* <b>`contents`</b>: A `Tensor` of type `string`. 0-D.  The GIF-encoded image.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `uint8`.
