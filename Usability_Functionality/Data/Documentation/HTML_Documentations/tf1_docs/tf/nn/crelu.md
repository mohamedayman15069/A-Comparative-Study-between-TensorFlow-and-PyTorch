<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.crelu" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.crelu

Computes Concatenated ReLU.

### Aliases:

* `tf.compat.v1.nn.crelu`
* `tf.compat.v2.compat.v1.nn.crelu`
* `tf.nn.crelu`

``` python
tf.nn.crelu(
    features,
    name=None,
    axis=-1
)
```

<!-- Placeholder for "Used in" -->

Concatenates a ReLU which selects only the positive part of the activation
with a ReLU which selects only the *negative* part of the activation.
Note that as a result this non-linearity doubles the depth of the activations.
Source: [Understanding and Improving Convolutional Neural Networks via
Concatenated Rectified Linear Units. W. Shang, et
al.](https://arxiv.org/abs/1603.05201)

#### Args:


* <b>`features`</b>: A `Tensor` with type `float`, `double`, `int32`, `int64`, `uint8`,
  `int16`, or `int8`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`axis`</b>: The axis that the output values are concatenated along. Default is -1.


#### Returns:

A `Tensor` with the same type as `features`.
