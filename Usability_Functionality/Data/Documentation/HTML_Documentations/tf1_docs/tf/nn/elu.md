<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.elu" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.elu

Computes exponential linear: `exp(features) - 1` if < 0, `features` otherwise.

### Aliases:

* `tf.compat.v1.nn.elu`
* `tf.compat.v2.compat.v1.nn.elu`
* `tf.compat.v2.nn.elu`
* `tf.nn.elu`

``` python
tf.nn.elu(
    features,
    name=None
)
```

<!-- Placeholder for "Used in" -->

See [Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs)
](http://arxiv.org/abs/1511.07289)

#### Args:


* <b>`features`</b>: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `features`.
