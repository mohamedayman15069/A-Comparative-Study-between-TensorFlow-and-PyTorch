<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.random_crop" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.random_crop

Randomly crops a tensor to a given size.

### Aliases:

* `tf.compat.v1.image.random_crop`
* `tf.compat.v1.random_crop`
* `tf.compat.v2.compat.v1.image.random_crop`
* `tf.compat.v2.compat.v1.random_crop`
* `tf.compat.v2.image.random_crop`
* `tf.image.random_crop`
* `tf.random_crop`

``` python
tf.image.random_crop(
    value,
    size,
    seed=None,
    name=None
)
```

<!-- Placeholder for "Used in" -->

Slices a shape `size` portion out of `value` at a uniformly chosen offset.
Requires `value.shape >= size`.

If a dimension should not be cropped, pass the full size of that dimension.
For example, RGB images can be cropped with
`size = [crop_height, crop_width, 3]`.

#### Args:


* <b>`value`</b>: Input tensor to crop.
* <b>`size`</b>: 1-D tensor with size the rank of `value`.
* <b>`seed`</b>: Python integer. Used to create a random seed. See
  <a href="../../tf/random/set_random_seed.md"><code>tf.compat.v1.set_random_seed</code></a>
  for behavior.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

A cropped tensor of the same rank as `value` and shape `size`.
