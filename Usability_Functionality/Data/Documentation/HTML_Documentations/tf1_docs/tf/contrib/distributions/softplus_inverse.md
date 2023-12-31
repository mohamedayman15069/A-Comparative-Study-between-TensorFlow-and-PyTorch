<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.distributions.softplus_inverse" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.distributions.softplus_inverse

Computes the inverse softplus, i.e., x = softplus_inverse(softplus(x)).

``` python
tf.contrib.distributions.softplus_inverse(
    x,
    name=None
)
```

<!-- Placeholder for "Used in" -->

Mathematically this op is equivalent to:

```none
softplus_inverse = log(exp(x) - 1.)
```

#### Args:


* <b>`x`</b>: `Tensor`. Non-negative (not enforced), floating-point.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`Tensor`. Has the same type/shape as input `x`.
