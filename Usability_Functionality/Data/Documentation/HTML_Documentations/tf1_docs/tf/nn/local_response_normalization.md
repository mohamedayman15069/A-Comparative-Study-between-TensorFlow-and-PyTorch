<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.local_response_normalization" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.local_response_normalization

Local Response Normalization.

### Aliases:

* `tf.compat.v1.nn.local_response_normalization`
* `tf.compat.v1.nn.lrn`
* `tf.compat.v2.compat.v1.nn.local_response_normalization`
* `tf.compat.v2.compat.v1.nn.lrn`
* `tf.compat.v2.nn.local_response_normalization`
* `tf.compat.v2.nn.lrn`
* `tf.nn.local_response_normalization`
* `tf.nn.lrn`

``` python
tf.nn.local_response_normalization(
    input,
    depth_radius=5,
    bias=1,
    alpha=1,
    beta=0.5,
    name=None
)
```

<!-- Placeholder for "Used in" -->

The 4-D `input` tensor is treated as a 3-D array of 1-D vectors (along the last
dimension), and each vector is normalized independently.  Within a given vector,
each component is divided by the weighted, squared sum of inputs within
`depth_radius`.  In detail,

    sqr_sum[a, b, c, d] =
        sum(input[a, b, c, d - depth_radius : d + depth_radius + 1] ** 2)
    output = input / (bias + alpha * sqr_sum) ** beta

For details, see [Krizhevsky et al., ImageNet classification with deep
convolutional neural networks (NIPS 2012)](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks).

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`.
  4-D.
* <b>`depth_radius`</b>: An optional `int`. Defaults to `5`.
  0-D.  Half-width of the 1-D normalization window.
* <b>`bias`</b>: An optional `float`. Defaults to `1`.
  An offset (usually positive to avoid dividing by 0).
* <b>`alpha`</b>: An optional `float`. Defaults to `1`.
  A scale factor, usually positive.
* <b>`beta`</b>: An optional `float`. Defaults to `0.5`. An exponent.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
