<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.train.natural_exp_decay" />
<meta itemprop="path" content="Stable" />
</div>

# tf.train.natural_exp_decay

Applies natural exponential decay to the initial learning rate.

### Aliases:

* `tf.compat.v1.train.natural_exp_decay`
* `tf.compat.v2.compat.v1.train.natural_exp_decay`
* `tf.train.natural_exp_decay`

``` python
tf.train.natural_exp_decay(
    learning_rate,
    global_step,
    decay_steps,
    decay_rate,
    staircase=False,
    name=None
)
```

<!-- Placeholder for "Used in" -->

When training a model, it is often recommended to lower the learning rate as
the training progresses.  This function applies an exponential decay function
to a provided initial learning rate.  It requires an `global_step` value to
compute the decayed learning rate.  You can just pass a TensorFlow variable
that you increment at each training step.

The function returns the decayed learning rate.  It is computed as:

```python
decayed_learning_rate = learning_rate * exp(-decay_rate * global_step /
decay_step)
```

or, if `staircase` is `True`, as:

```python
decayed_learning_rate = learning_rate * exp(-decay_rate * floor(global_step /
decay_step))
```

Example: decay exponentially with a base of 0.96:

```python
...
global_step = tf.Variable(0, trainable=False)
learning_rate = 0.1
decay_steps = 5
k = 0.5
learning_rate = tf.compat.v1.train.natural_exp_decay(learning_rate,
global_step,
                                           decay_steps, k)

# Passing global_step to minimize() will increment it at each step.
learning_step = (
    tf.compat.v1.train.GradientDescentOptimizer(learning_rate)
    .minimize(...my loss..., global_step=global_step)
)
```

#### Args:


* <b>`learning_rate`</b>: A scalar `float32` or `float64` `Tensor` or a Python number.
  The initial learning rate.
* <b>`global_step`</b>: A Python number. Global step to use for the decay computation.
  Must not be negative.
* <b>`decay_steps`</b>: How often to apply decay.
* <b>`decay_rate`</b>: A Python number.  The decay rate.
* <b>`staircase`</b>: Whether to apply decay in a discrete staircase, as opposed to
  continuous, fashion.
* <b>`name`</b>: String.  Optional name of the operation.  Defaults to
  'ExponentialTimeDecay'.


#### Returns:

A scalar `Tensor` of the same type as `learning_rate`.  The decayed
learning rate.



#### Raises:


* <b>`ValueError`</b>: if `global_step` is not supplied.



#### Eager Compatibility
When eager execution is enabled, this function returns a function which in
turn returns the decayed learning rate Tensor. This can be useful for changing
the learning rate value across different invocations of optimizer functions.

