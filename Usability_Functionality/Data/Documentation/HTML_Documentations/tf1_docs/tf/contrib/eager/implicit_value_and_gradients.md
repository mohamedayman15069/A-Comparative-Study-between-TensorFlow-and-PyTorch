<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.eager.implicit_value_and_gradients" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.eager.implicit_value_and_gradients

Returns a function which differentiates f with respect to variables.

``` python
tf.contrib.eager.implicit_value_and_gradients(f)
```

<!-- Placeholder for "Used in" -->

The wrapped function returns the value and the gradient of f when called with
the same arguments. The gradient is with respect to all trainable TFE
variables accessed by `f`.

This function is useful when the exact set of variables to differentiate with
is not known ahead of time.

#### Example:



```python
dense_layer = tf.compat.v1.layers.Dense(1)
def loss(x, y):
  return tf.reduce_sum(tf.square(dense_layer(x) - y))

# Obtain the gradient function.
val_grad_fn = tfe.implicit_value_and_gradients(loss)

# Invoke the gradient function with concrete values of x and y.
x = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
y = tf.constant([[10.0], [20.0]])
value, grads_and_vars = val_grad_fn(x, y)
print('Value of loss: %s' % value)

# Apply the gradients to Variables.
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.1)
optimizer.apply_gradients(grads_and_vars)
```

#### Args:


* <b>`f`</b>: function to be differentiated. If `f` returns a scalar, this scalar will
  be differentiated. If `f` returns a tensor or list of tensors, by default
  a scalar will be computed by adding all their values to produce a single
  scalar.


#### Returns:

A function which, when called, returns a tuple pair.
Its first element is the value to which the function evaluates.
Its second element is list of (gradient, variable) pairs.



#### Raises:


* <b>`ValueError`</b>: if `f` returns None.