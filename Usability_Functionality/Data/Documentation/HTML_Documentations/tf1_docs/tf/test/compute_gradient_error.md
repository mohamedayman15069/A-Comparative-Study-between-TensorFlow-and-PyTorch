<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.test.compute_gradient_error" />
<meta itemprop="path" content="Stable" />
</div>

# tf.test.compute_gradient_error

Computes the gradient error. (deprecated)

### Aliases:

* `tf.compat.v1.test.compute_gradient_error`
* `tf.compat.v2.compat.v1.test.compute_gradient_error`
* `tf.test.compute_gradient_error`

``` python
tf.test.compute_gradient_error(
    x,
    x_shape,
    y,
    y_shape,
    x_init_value=None,
    delta=0.001,
    init_targets=None,
    extra_feed_dict=None
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use tf.test.compute_gradient in 2.0, which has better support for functions. Note that the two versions have different usage, so code change is needed.

Computes the maximum error for dy/dx between the computed Jacobian and the
numerically estimated Jacobian.

This function will modify the tensors passed in as it adds more operations
and hence changing the consumers of the operations of the input tensors.

This function adds operations to the current session. To compute the error
using a particular device, such as a GPU, use the standard methods for
setting a device (e.g. using with sess.graph.device() or setting a device
function in the session constructor).

#### Args:


* <b>`x`</b>: a tensor or list of tensors
* <b>`x_shape`</b>: the dimensions of x as a tuple or an array of ints. If x is a list,
then this is the list of shapes.
* <b>`y`</b>: a tensor
* <b>`y_shape`</b>: the dimensions of y as a tuple or an array of ints.
* <b>`x_init_value`</b>: (optional) a numpy array of the same shape as "x"
  representing the initial value of x. If x is a list, this should be a list
  of numpy arrays.  If this is none, the function will pick a random tensor
  as the initial value.
* <b>`delta`</b>: (optional) the amount of perturbation.
* <b>`init_targets`</b>: list of targets to run to initialize model params.
* <b>`extra_feed_dict`</b>: dict that allows fixing specified tensor values
  during the Jacobian calculation.


#### Returns:

The maximum error in between the two Jacobians.
