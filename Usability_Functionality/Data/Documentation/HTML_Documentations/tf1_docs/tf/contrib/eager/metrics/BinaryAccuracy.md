<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.eager.metrics.BinaryAccuracy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="name"/>
<meta itemprop="property" content="variables"/>
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add_variable"/>
<meta itemprop="property" content="aggregate"/>
<meta itemprop="property" content="build"/>
<meta itemprop="property" content="call"/>
<meta itemprop="property" content="init_variables"/>
<meta itemprop="property" content="result"/>
<meta itemprop="property" content="value"/>
</div>

# tf.contrib.eager.metrics.BinaryAccuracy

## Class `BinaryAccuracy`

Calculates how often `predictions` matches `labels`.

Inherits From: [`Mean`](../../../../tf/contrib/eager/metrics/Mean.md)

<!-- Placeholder for "Used in" -->

This class is compatible with <a href="../../../../tf/keras/losses/binary_crossentropy.md"><code>tf.keras.losses.binary_crossentropy</code></a>,
<a href="../../../../tf/losses/sigmoid_cross_entropy.md"><code>tf.compat.v1.losses.sigmoid_cross_entropy</code></a>,
<a href="../../../../tf/nn/sigmoid_cross_entropy_with_logits.md"><code>tf.nn.sigmoid_cross_entropy_with_logits</code></a>.
If there is more than one label, this will become multi-label classification.

#### Attributes:


* <b>`name`</b>: name of the accuracy object.
* <b>`threshold`</b>: Used for rounding off the predictions.
           If the predictions are,
            1. probabilities then set the threshold to 0.5.
            2. logits then set the threshold to 0.
          You can set the threshold appropriately,
          to trade off with precision and recall.
* <b>`dtype`</b>: data type of tensor.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    threshold,
    name=None,
    dtype=tf.dtypes.double
)
```

Inits BinaryAccuracy with name, threshold and dtype.




## Properties

<h3 id="name"><code>name</code></h3>




<h3 id="variables"><code>variables</code></h3>






## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    *args,
    **kwargs
)
```

Returns op to execute to update this metric for these inputs.

Returns None if eager execution is enabled.
Returns a graph-mode function if graph execution is enabled.

#### Args:


* <b>`*args`</b>: * <b>`**kwargs`</b>: A mini-batch of inputs to the Metric, passed on to `call()`.

<h3 id="add_variable"><code>add_variable</code></h3>

``` python
add_variable(
    name,
    shape=None,
    dtype=None,
    initializer=None
)
```

***Only for use by descendants of Metric***.


<h3 id="aggregate"><code>aggregate</code></h3>

``` python
aggregate(metrics)
```

Adds in the state from a list of metrics.

Default implementation sums all the metric variables.

#### Args:


* <b>`metrics`</b>: A list of metrics with the same type as `self`.


#### Raises:


* <b>`ValueError`</b>: If metrics contains invalid data.

<h3 id="build"><code>build</code></h3>

``` python
build(
    *args,
    **kwargs
)
```

Method to create variables.

Called by `__call__()` before `call()` for the first time.

#### Args:


* <b>`*args`</b>: * <b>`**kwargs`</b>: The arguments to the first invocation of `__call__()`.
 `build()` may use the shape and/or dtype of these arguments
 when deciding how to create variables.

<h3 id="call"><code>call</code></h3>

``` python
call(
    labels,
    predictions,
    weights=None
)
```

Accumulate accuracy statistics.

`labels` and `predictions` should have the same shape and type.

#### Args:


* <b>`labels`</b>: Binary Tensor(containing 0 or 1).
* <b>`predictions`</b>: Tensor with probabilities or logits.
* <b>`weights`</b>: Optional weighting of each example. Defaults to 1.


#### Returns:

The arguments, for easy chaining.


<h3 id="init_variables"><code>init_variables</code></h3>

``` python
init_variables()
```

Initializes this Metric's variables.

Should be called after variables are created in the first execution
of `__call__()`. If using graph execution, the return value should be
`run()` in a session before running the op returned by `__call__()`.
(See example above.)

#### Returns:

If using graph execution, this returns an op to perform the
initialization. Under eager execution, the variables are reset to their
initial values as a side effect and this function returns None.


<h3 id="result"><code>result</code></h3>

``` python
result(write_summary=True)
```

Returns the result of the Metric.


#### Args:


* <b>`write_summary`</b>: bool indicating whether to feed the result to the summary
  before returning.

#### Returns:

aggregated metric as float.


#### Raises:


* <b>`ValueError`</b>: if the optional argument is not bool

<h3 id="value"><code>value</code></h3>

``` python
value()
```

In graph mode returns the result Tensor while in eager the callable.




