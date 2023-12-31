<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.distributions.bijectors.MaskedAutoregressiveFlow" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="forward_min_event_ndims"/>
<meta itemprop="property" content="graph_parents"/>
<meta itemprop="property" content="inverse_min_event_ndims"/>
<meta itemprop="property" content="is_constant_jacobian"/>
<meta itemprop="property" content="name"/>
<meta itemprop="property" content="validate_args"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="forward"/>
<meta itemprop="property" content="forward_event_shape"/>
<meta itemprop="property" content="forward_event_shape_tensor"/>
<meta itemprop="property" content="forward_log_det_jacobian"/>
<meta itemprop="property" content="inverse"/>
<meta itemprop="property" content="inverse_event_shape"/>
<meta itemprop="property" content="inverse_event_shape_tensor"/>
<meta itemprop="property" content="inverse_log_det_jacobian"/>
</div>

# tf.contrib.distributions.bijectors.MaskedAutoregressiveFlow

## Class `MaskedAutoregressiveFlow`

Affine MaskedAutoregressiveFlow bijector for vector-valued events.

Inherits From: [`Bijector`](../../../../tf/contrib/distributions/bijectors/Bijector.md)

<!-- Placeholder for "Used in" -->

The affine autoregressive flow [(Papamakarios et al., 2016)][3] provides a
relatively simple framework for user-specified (deep) architectures to learn
a distribution over vector-valued events. Regarding terminology,

  "Autoregressive models decompose the joint density as a product of
  conditionals, and model each conditional in turn. Normalizing flows
  transform a base density (e.g. a standard Gaussian) into the target density
  by an invertible transformation with tractable Jacobian."
  [(Papamakarios et al., 2016)][3]

In other words, the "autoregressive property" is equivalent to the
decomposition, `p(x) = prod{ p(x[i] | x[0:i]) : i=0, ..., d }`. The provided
`shift_and_log_scale_fn`, `masked_autoregressive_default_template`, achieves
this property by zeroing out weights in its `masked_dense` layers.

In the `tfp` framework, a "normalizing flow" is implemented as a
`tfp.bijectors.Bijector`. The `forward` "autoregression"
is implemented using a <a href="../../../../tf/while_loop.md"><code>tf.while_loop</code></a> and a deep neural network (DNN) with
masked weights such that the autoregressive property is automatically met in
the `inverse`.

A `TransformedDistribution` using `MaskedAutoregressiveFlow(...)` uses the
(expensive) forward-mode calculation to draw samples and the (cheap)
reverse-mode calculation to compute log-probabilities. Conversely, a
`TransformedDistribution` using `Invert(MaskedAutoregressiveFlow(...))` uses
the (expensive) forward-mode calculation to compute log-probabilities and the
(cheap) reverse-mode calculation to compute samples.  See "Example Use"
[below] for more details.

Given a `shift_and_log_scale_fn`, the forward and inverse transformations are
(a sequence of) affine transformations. A "valid" `shift_and_log_scale_fn`
must compute each `shift` (aka `loc` or "mu" in [Germain et al. (2015)][1])
and `log(scale)` (aka "alpha" in [Germain et al. (2015)][1]) such that each
are broadcastable with the arguments to `forward` and `inverse`, i.e., such
that the calculations in `forward`, `inverse` [below] are possible.

For convenience, `masked_autoregressive_default_template` is offered as a
possible `shift_and_log_scale_fn` function. It implements the MADE
architecture [(Germain et al., 2015)][1]. MADE is a feed-forward network that
computes a `shift` and `log(scale)` using `masked_dense` layers in a deep
neural network. Weights are masked to ensure the autoregressive property. It
is possible that this architecture is suboptimal for your task. To build
alternative networks, either change the arguments to
`masked_autoregressive_default_template`, use the `masked_dense` function to
roll-out your own, or use some other architecture, e.g., using <a href="../../../../tf/layers.md"><code>tf.layers</code></a>.

Warning: no attempt is made to validate that the `shift_and_log_scale_fn`
enforces the "autoregressive property".

Assuming `shift_and_log_scale_fn` has valid shape and autoregressive
semantics, the forward transformation is

```python
def forward(x):
  y = zeros_like(x)
  event_size = x.shape[-1]
  for _ in range(event_size):
    shift, log_scale = shift_and_log_scale_fn(y)
    y = x * math_ops.exp(log_scale) + shift
  return y
```

and the inverse transformation is

```python
def inverse(y):
  shift, log_scale = shift_and_log_scale_fn(y)
  return (y - shift) / math_ops.exp(log_scale)
```

Notice that the `inverse` does not need a for-loop. This is because in the
forward pass each calculation of `shift` and `log_scale` is based on the `y`
calculated so far (not `x`). In the `inverse`, the `y` is fully known, thus is
equivalent to the scaling used in `forward` after `event_size` passes, i.e.,
the "last" `y` used to compute `shift`, `log_scale`. (Roughly speaking, this
also proves the transform is bijective.)

#### Examples

```python
import tensorflow_probability as tfp
tfd = tfp.distributions
tfb = tfp.bijectors

dims = 5

# A common choice for a normalizing flow is to use a Gaussian for the base
# distribution. (However, any continuous distribution would work.) E.g.,
maf = tfd.TransformedDistribution(
    distribution=tfd.Normal(loc=0., scale=1.),
    bijector=tfb.MaskedAutoregressiveFlow(
        shift_and_log_scale_fn=tfb.masked_autoregressive_default_template(
            hidden_layers=[512, 512])),
    event_shape=[dims])

x = maf.sample()  # Expensive; uses `tf.while_loop`, no Bijector caching.
maf.log_prob(x)   # Almost free; uses Bijector caching.
maf.log_prob(0.)  # Cheap; no `tf.while_loop` despite no Bijector caching.

# [Papamakarios et al. (2016)][3] also describe an Inverse Autoregressive
# Flow [(Kingma et al., 2016)][2]:
iaf = tfd.TransformedDistribution(
    distribution=tfd.Normal(loc=0., scale=1.),
    bijector=tfb.Invert(tfb.MaskedAutoregressiveFlow(
        shift_and_log_scale_fn=tfb.masked_autoregressive_default_template(
            hidden_layers=[512, 512]))),
    event_shape=[dims])

x = iaf.sample()  # Cheap; no `tf.while_loop` despite no Bijector caching.
iaf.log_prob(x)   # Almost free; uses Bijector caching.
iaf.log_prob(0.)  # Expensive; uses `tf.while_loop`, no Bijector caching.

# In many (if not most) cases the default `shift_and_log_scale_fn` will be a
# poor choice. Here's an example of using a "shift only" version and with a
# different number/depth of hidden layers.
shift_only = True
maf_no_scale_hidden2 = tfd.TransformedDistribution(
    distribution=tfd.Normal(loc=0., scale=1.),
    bijector=tfb.MaskedAutoregressiveFlow(
        tfb.masked_autoregressive_default_template(
            hidden_layers=[32],
            shift_only=shift_only),
        is_constant_jacobian=shift_only),
    event_shape=[dims])
```

#### References

[1]: Mathieu Germain, Karol Gregor, Iain Murray, and Hugo Larochelle. MADE:
     Masked Autoencoder for Distribution Estimation. In _International
     Conference on Machine Learning_, 2015. https://arxiv.org/abs/1502.03509

[2]: Diederik P. Kingma, Tim Salimans, Rafal Jozefowicz, Xi Chen, Ilya
     Sutskever, and Max Welling. Improving Variational Inference with Inverse
     Autoregressive Flow. In _Neural Information Processing Systems_, 2016.
     https://arxiv.org/abs/1606.04934

[3]: George Papamakarios, Theo Pavlakou, and Iain Murray. Masked
     Autoregressive Flow for Density Estimation. In _Neural Information
     Processing Systems_, 2017. https://arxiv.org/abs/1705.07057

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    shift_and_log_scale_fn,
    is_constant_jacobian=False,
    validate_args=False,
    unroll_loop=False,
    name=None
)
```

Creates the MaskedAutoregressiveFlow bijector. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2018-10-01.
Instructions for updating:
The TensorFlow Distributions library has moved to TensorFlow Probability (https://github.com/tensorflow/probability). You should update all references to use `tfp.distributions` instead of <a href="../../../../tf/contrib/distributions.md"><code>tf.contrib.distributions</code></a>.

#### Args:


* <b>`shift_and_log_scale_fn`</b>: Python `callable` which computes `shift` and
  `log_scale` from both the forward domain (`x`) and the inverse domain
  (`y`). Calculation must respect the "autoregressive property" (see class
  docstring). Suggested default
  `masked_autoregressive_default_template(hidden_layers=...)`. Typically
  the function contains `tf.Variables` and is wrapped using
  <a href="../../../../tf/make_template.md"><code>tf.compat.v1.make_template</code></a>. Returning `None` for either (both)
  `shift`, `log_scale` is equivalent to (but more efficient than)
  returning zero.
* <b>`is_constant_jacobian`</b>: Python `bool`. Default: `False`. When `True` the
  implementation assumes `log_scale` does not depend on the forward domain
  (`x`) or inverse domain (`y`) values. (No validation is made;
  `is_constant_jacobian=False` is always safe but possibly computationally
  inefficient.)
* <b>`validate_args`</b>: Python `bool` indicating whether arguments should be
  checked for correctness.
* <b>`unroll_loop`</b>: Python `bool` indicating whether the <a href="../../../../tf/while_loop.md"><code>tf.while_loop</code></a> in
  `_forward` should be replaced with a static for loop. Requires that the
  final dimension of `x` be known at graph construction time. Defaults to
  `False`.
* <b>`name`</b>: Python `str`, name given to ops managed by this object.



## Properties

<h3 id="dtype"><code>dtype</code></h3>

dtype of `Tensor`s transformable by this distribution.


<h3 id="forward_min_event_ndims"><code>forward_min_event_ndims</code></h3>

Returns the minimal number of dimensions bijector.forward operates on.


<h3 id="graph_parents"><code>graph_parents</code></h3>

Returns this `Bijector`'s graph_parents as a Python list.


<h3 id="inverse_min_event_ndims"><code>inverse_min_event_ndims</code></h3>

Returns the minimal number of dimensions bijector.inverse operates on.


<h3 id="is_constant_jacobian"><code>is_constant_jacobian</code></h3>

Returns true iff the Jacobian matrix is not a function of x.

Note: Jacobian matrix is either constant for both forward and inverse or
neither.

#### Returns:


* <b>`is_constant_jacobian`</b>: Python `bool`.

<h3 id="name"><code>name</code></h3>

Returns the string name of this `Bijector`.


<h3 id="validate_args"><code>validate_args</code></h3>

Returns True if Tensor arguments will be validated.




## Methods

<h3 id="forward"><code>forward</code></h3>

``` python
forward(
    x,
    name='forward'
)
```

Returns the forward `Bijector` evaluation, i.e., X = g(Y).


#### Args:


* <b>`x`</b>: `Tensor`. The input to the "forward" evaluation.
* <b>`name`</b>: The name to give this op.


#### Returns:

`Tensor`.



#### Raises:


* <b>`TypeError`</b>: if `self.dtype` is specified and `x.dtype` is not
  `self.dtype`.
* <b>`NotImplementedError`</b>: if `_forward` is not implemented.

<h3 id="forward_event_shape"><code>forward_event_shape</code></h3>

``` python
forward_event_shape(input_shape)
```

Shape of a single sample from a single batch as a `TensorShape`.

Same meaning as `forward_event_shape_tensor`. May be only partially defined.

#### Args:


* <b>`input_shape`</b>: `TensorShape` indicating event-portion shape passed into
  `forward` function.


#### Returns:


* <b>`forward_event_shape_tensor`</b>: `TensorShape` indicating event-portion shape
  after applying `forward`. Possibly unknown.

<h3 id="forward_event_shape_tensor"><code>forward_event_shape_tensor</code></h3>

``` python
forward_event_shape_tensor(
    input_shape,
    name='forward_event_shape_tensor'
)
```

Shape of a single sample from a single batch as an `int32` 1D `Tensor`.


#### Args:


* <b>`input_shape`</b>: `Tensor`, `int32` vector indicating event-portion shape
  passed into `forward` function.
* <b>`name`</b>: name to give to the op


#### Returns:


* <b>`forward_event_shape_tensor`</b>: `Tensor`, `int32` vector indicating
  event-portion shape after applying `forward`.

<h3 id="forward_log_det_jacobian"><code>forward_log_det_jacobian</code></h3>

``` python
forward_log_det_jacobian(
    x,
    event_ndims,
    name='forward_log_det_jacobian'
)
```

Returns both the forward_log_det_jacobian.


#### Args:


* <b>`x`</b>: `Tensor`. The input to the "forward" Jacobian determinant evaluation.
* <b>`event_ndims`</b>: Number of dimensions in the probabilistic events being
  transformed. Must be greater than or equal to
  `self.forward_min_event_ndims`. The result is summed over the final
  dimensions to produce a scalar Jacobian determinant for each event,
  i.e. it has shape `x.shape.ndims - event_ndims` dimensions.
* <b>`name`</b>: The name to give this op.


#### Returns:

`Tensor`, if this bijector is injective.
  If not injective this is not implemented.



#### Raises:


* <b>`TypeError`</b>: if `self.dtype` is specified and `y.dtype` is not
  `self.dtype`.
* <b>`NotImplementedError`</b>: if neither `_forward_log_det_jacobian`
  nor {`_inverse`, `_inverse_log_det_jacobian`} are implemented, or
  this is a non-injective bijector.

<h3 id="inverse"><code>inverse</code></h3>

``` python
inverse(
    y,
    name='inverse'
)
```

Returns the inverse `Bijector` evaluation, i.e., X = g^{-1}(Y).


#### Args:


* <b>`y`</b>: `Tensor`. The input to the "inverse" evaluation.
* <b>`name`</b>: The name to give this op.


#### Returns:

`Tensor`, if this bijector is injective.
  If not injective, returns the k-tuple containing the unique
  `k` points `(x1, ..., xk)` such that `g(xi) = y`.



#### Raises:


* <b>`TypeError`</b>: if `self.dtype` is specified and `y.dtype` is not
  `self.dtype`.
* <b>`NotImplementedError`</b>: if `_inverse` is not implemented.

<h3 id="inverse_event_shape"><code>inverse_event_shape</code></h3>

``` python
inverse_event_shape(output_shape)
```

Shape of a single sample from a single batch as a `TensorShape`.

Same meaning as `inverse_event_shape_tensor`. May be only partially defined.

#### Args:


* <b>`output_shape`</b>: `TensorShape` indicating event-portion shape passed into
  `inverse` function.


#### Returns:


* <b>`inverse_event_shape_tensor`</b>: `TensorShape` indicating event-portion shape
  after applying `inverse`. Possibly unknown.

<h3 id="inverse_event_shape_tensor"><code>inverse_event_shape_tensor</code></h3>

``` python
inverse_event_shape_tensor(
    output_shape,
    name='inverse_event_shape_tensor'
)
```

Shape of a single sample from a single batch as an `int32` 1D `Tensor`.


#### Args:


* <b>`output_shape`</b>: `Tensor`, `int32` vector indicating event-portion shape
  passed into `inverse` function.
* <b>`name`</b>: name to give to the op


#### Returns:


* <b>`inverse_event_shape_tensor`</b>: `Tensor`, `int32` vector indicating
  event-portion shape after applying `inverse`.

<h3 id="inverse_log_det_jacobian"><code>inverse_log_det_jacobian</code></h3>

``` python
inverse_log_det_jacobian(
    y,
    event_ndims,
    name='inverse_log_det_jacobian'
)
```

Returns the (log o det o Jacobian o inverse)(y).

Mathematically, returns: `log(det(dX/dY))(Y)`. (Recall that: `X=g^{-1}(Y)`.)

Note that `forward_log_det_jacobian` is the negative of this function,
evaluated at `g^{-1}(y)`.

#### Args:


* <b>`y`</b>: `Tensor`. The input to the "inverse" Jacobian determinant evaluation.
* <b>`event_ndims`</b>: Number of dimensions in the probabilistic events being
  transformed. Must be greater than or equal to
  `self.inverse_min_event_ndims`. The result is summed over the final
  dimensions to produce a scalar Jacobian determinant for each event,
  i.e. it has shape `y.shape.ndims - event_ndims` dimensions.
* <b>`name`</b>: The name to give this op.


#### Returns:

`Tensor`, if this bijector is injective.
  If not injective, returns the tuple of local log det
  Jacobians, `log(det(Dg_i^{-1}(y)))`, where `g_i` is the restriction
  of `g` to the `ith` partition `Di`.



#### Raises:


* <b>`TypeError`</b>: if `self.dtype` is specified and `y.dtype` is not
  `self.dtype`.
* <b>`NotImplementedError`</b>: if `_inverse_log_det_jacobian` is not implemented.



