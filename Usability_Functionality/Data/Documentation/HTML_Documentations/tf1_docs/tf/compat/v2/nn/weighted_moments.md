<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v2.nn.weighted_moments" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v2.nn.weighted_moments

Returns the frequency-weighted mean and variance of `x`.

``` python
tf.compat.v2.nn.weighted_moments(
    x,
    axes,
    frequency_weights,
    keepdims=False,
    name=None
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: A tensor.
* <b>`axes`</b>: 1-d tensor of int32 values; these are the axes along which
  to compute mean and variance.
* <b>`frequency_weights`</b>: A tensor of positive weights which can be
  broadcast with x.
* <b>`keepdims`</b>: Produce moments with the same dimensionality as the input.
* <b>`name`</b>: Name used to scope the operation.


#### Returns:

Two tensors: `weighted_mean` and `weighted_variance`.
