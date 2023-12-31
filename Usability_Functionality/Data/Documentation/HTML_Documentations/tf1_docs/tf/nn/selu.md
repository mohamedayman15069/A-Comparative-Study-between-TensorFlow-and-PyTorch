<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.selu" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.selu

Computes scaled exponential linear: `scale * alpha * (exp(features) - 1)`

### Aliases:

* `tf.compat.v1.nn.selu`
* `tf.compat.v2.compat.v1.nn.selu`
* `tf.compat.v2.nn.selu`
* `tf.nn.selu`

``` python
tf.nn.selu(
    features,
    name=None
)
```

<!-- Placeholder for "Used in" -->

if < 0, `scale * features` otherwise.

To be used together with
`initializer = tf.variance_scaling_initializer(factor=1.0, mode='FAN_IN')`.
For correct dropout, use <a href="../../tf/contrib/nn/alpha_dropout.md"><code>tf.contrib.nn.alpha_dropout</code></a>.

See [Self-Normalizing Neural Networks](https://arxiv.org/abs/1706.02515)

#### Args:


* <b>`features`</b>: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `features`.
