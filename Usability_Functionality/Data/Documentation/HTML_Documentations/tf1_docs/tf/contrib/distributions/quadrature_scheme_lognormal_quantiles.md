<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.distributions.quadrature_scheme_lognormal_quantiles" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.distributions.quadrature_scheme_lognormal_quantiles

Use LogNormal quantiles to form quadrature on positive-reals. (deprecated)

``` python
tf.contrib.distributions.quadrature_scheme_lognormal_quantiles(
    loc,
    scale,
    quadrature_size,
    validate_args=False,
    name=None
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2018-10-01.
Instructions for updating:
The TensorFlow Distributions library has moved to TensorFlow Probability (https://github.com/tensorflow/probability). You should update all references to use `tfp.distributions` instead of <a href="../../../tf/contrib/distributions.md"><code>tf.contrib.distributions</code></a>.

#### Args:


* <b>`loc`</b>: `float`-like (batch of) scalar `Tensor`; the location parameter of
  the LogNormal prior.
* <b>`scale`</b>: `float`-like (batch of) scalar `Tensor`; the scale parameter of
  the LogNormal prior.
* <b>`quadrature_size`</b>: Python `int` scalar representing the number of quadrature
  points.
* <b>`validate_args`</b>: Python `bool`, default `False`. When `True` distribution
  parameters are checked for validity despite possibly degrading runtime
  performance. When `False` invalid inputs may silently render incorrect
  outputs.
* <b>`name`</b>: Python `str` name prefixed to Ops created by this class.


#### Returns:


* <b>`grid`</b>: (Batch of) length-`quadrature_size` vectors representing the
  `log_rate` parameters of a `Poisson`.
* <b>`probs`</b>: (Batch of) length-`quadrature_size` vectors representing the
  weight associate with each `grid` value.