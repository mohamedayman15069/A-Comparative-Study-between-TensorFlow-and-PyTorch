<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.distributions.bijectors.Permute" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="forward_min_event_ndims"/>
<meta itemprop="property" content="graph_parents"/>
<meta itemprop="property" content="inverse_min_event_ndims"/>
<meta itemprop="property" content="is_constant_jacobian"/>
<meta itemprop="property" content="name"/>
<meta itemprop="property" content="permutation"/>
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

# tf.contrib.distributions.bijectors.Permute

## Class `Permute`

Permutes the rightmost dimension of a `Tensor`.

Inherits From: [`Bijector`](../../../../tf/contrib/distributions/bijectors/Bijector.md)

<!-- Placeholder for "Used in" -->

```python
import tensorflow_probability as tfp
tfb = tfp.bijectors

reverse = tfb.Permute(permutation=[2, 1, 0])

reverse.forward([-1., 0., 1.])
# ==> [1., 0., -1]

reverse.inverse([1., 0., -1])
# ==> [-1., 0., 1.]

reverse.forward_log_det_jacobian(any_value)
# ==> 0.

reverse.inverse_log_det_jacobian(any_value)
# ==> 0.
```

Warning: <a href="../../../../tf/estimator.md"><code>tf.estimator</code></a> may repeatedly build the graph thus
`Permute(np.random.permutation(event_size)).astype("int32"))` is not a
reliable parameterization (nor would it be even if using <a href="../../../../tf/constant.md"><code>tf.constant</code></a>). A
safe alternative is to use <a href="../../../../tf/get_variable.md"><code>tf.compat.v1.get_variable</code></a> to achieve "init once"
behavior,
i.e.,

```python
def init_once(x, name):
  return tf.compat.v1.get_variable(name, initializer=x, trainable=False)

Permute(permutation=init_once(
    np.random.permutation(event_size).astype("int32"),
    name="permutation"))
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    permutation,
    validate_args=False,
    name=None
)
```

Creates the `Permute` bijector. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2018-10-01.
Instructions for updating:
The TensorFlow Distributions library has moved to TensorFlow Probability (https://github.com/tensorflow/probability). You should update all references to use `tfp.distributions` instead of <a href="../../../../tf/contrib/distributions.md"><code>tf.contrib.distributions</code></a>.

#### Args:


* <b>`permutation`</b>: An `int`-like vector-shaped `Tensor` representing the
  permutation to apply to the rightmost dimension of the transformed
  `Tensor`.
* <b>`validate_args`</b>: Python `bool` indicating whether arguments should be
  checked for correctness.
* <b>`name`</b>: Python `str`, name given to ops managed by this object.


#### Raises:


* <b>`TypeError`</b>: if `not permutation.dtype.is_integer`.
* <b>`ValueError`</b>: if `permutation` does not contain exactly one of each of
  `{0, 1, ..., d}`.



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


<h3 id="permutation"><code>permutation</code></h3>




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



