description: Optimizer that implements the Adadelta algorithm.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.optimizers.legacy.Adadelta" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add_slot"/>
<meta itemprop="property" content="add_weight"/>
<meta itemprop="property" content="apply_gradients"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
<meta itemprop="property" content="get_gradients"/>
<meta itemprop="property" content="get_slot"/>
<meta itemprop="property" content="get_slot_names"/>
<meta itemprop="property" content="get_updates"/>
<meta itemprop="property" content="get_weights"/>
<meta itemprop="property" content="minimize"/>
<meta itemprop="property" content="set_weights"/>
<meta itemprop="property" content="variables"/>
</div>

# tf.keras.optimizers.legacy.Adadelta

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/adadelta.py#L27-L164">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Optimizer that implements the Adadelta algorithm.

Inherits From: [`Optimizer`](../../../../tf/keras/optimizers/legacy/Optimizer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.optimizers.legacy.Adadelta(
    learning_rate=0.001,
    rho=0.95,
    epsilon=1e-07,
    name=&#x27;Adadelta&#x27;,
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Adadelta optimization is a stochastic gradient descent method that is based
on adaptive learning rate per dimension to address two drawbacks:

- The continual decay of learning rates throughout training.
- The need for a manually selected global learning rate.

Adadelta is a more robust extension of Adagrad that adapts learning rates
based on a moving window of gradient updates, instead of accumulating all
past gradients. This way, Adadelta continues learning even when many updates
have been done. Compared to Adagrad, in the original version of Adadelta you
don't have to set an initial learning rate. In this version, the initial
learning rate can be set, as in most other Keras optimizers.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`learning_rate`<a id="learning_rate"></a>
</td>
<td>
Initial value for the learning rate:
either a floating point value,
or a <a href="../../../../tf/keras/optimizers/schedules/LearningRateSchedule.md"><code>tf.keras.optimizers.schedules.LearningRateSchedule</code></a> instance.
Note that `Adadelta` tends to benefit from higher initial learning rate
values compared to other optimizers.
To match the exact form in the original paper, use 1.0.
Defaults to `0.001`.
</td>
</tr><tr>
<td>
`rho`<a id="rho"></a>
</td>
<td>
A `Tensor` or a floating point value. The decay rate.
</td>
</tr><tr>
<td>
`epsilon`<a id="epsilon"></a>
</td>
<td>
Small floating point value used to maintain numerical stability.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
Optional name prefix for the operations created when applying
gradients.  Defaults to `"Adadelta"`.
</td>
</tr><tr>
<td>
`**kwargs`<a id="**kwargs"></a>
</td>
<td>
keyword arguments. Allowed arguments are `clipvalue`,
`clipnorm`, `global_clipnorm`.
If `clipvalue` (float) is set, the gradient of each weight
is clipped to be no higher than this value.
If `clipnorm` (float) is set, the gradient of each weight
is individually clipped so that its norm is no higher than this value.
If `global_clipnorm` (float) is set the gradient of all weights is
clipped so that their global norm is no higher than this value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Reference</h2></th></tr>
<tr class="alt">
<td colspan="2">
- [Zeiler, 2012](http://arxiv.org/abs/1212.5701)
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
in case of any invalid argument.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`clipnorm`<a id="clipnorm"></a>
</td>
<td>
`float` or `None`. If set, clips gradients to a maximum norm.
</td>
</tr><tr>
<td>
`clipvalue`<a id="clipvalue"></a>
</td>
<td>
`float` or `None`. If set, clips gradients to a maximum value.
</td>
</tr><tr>
<td>
`global_clipnorm`<a id="global_clipnorm"></a>
</td>
<td>
`float` or `None`.

If set, clips gradients to a maximum norm.

Check <a href="../../../../tf/clip_by_global_norm.md"><code>tf.clip_by_global_norm</code></a> for more details.
</td>
</tr><tr>
<td>
`iterations`<a id="iterations"></a>
</td>
<td>
Variable. The number of training steps this Optimizer has run.
</td>
</tr><tr>
<td>
`weights`<a id="weights"></a>
</td>
<td>
Returns variables of this Optimizer based on the order created.
</td>
</tr>
</table>



## Methods

<h3 id="add_slot"><code>add_slot</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/optimizer_v2.py#L1021-L1084">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_slot(
    var, slot_name, initializer=&#x27;zeros&#x27;, shape=None
)
</code></pre>

Add a new slot variable for `var`.

A slot variable is an additional variable associated with `var` to
train.  It is allocated and managed by optimizers, e.g. `Adam`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`var`
</td>
<td>
a `Variable` object.
</td>
</tr><tr>
<td>
`slot_name`
</td>
<td>
name of the slot variable.
</td>
</tr><tr>
<td>
`initializer`
</td>
<td>
initializer of the slot variable
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
(Optional) shape of the slot variable. If not set, it will
default to the shape of `var`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A slot variable.
</td>
</tr>

</table>



<h3 id="add_weight"><code>add_weight</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/optimizer_v2.py#L1343-L1388">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_weight(
    name,
    shape,
    dtype=None,
    initializer=&#x27;zeros&#x27;,
    trainable=None,
    synchronization=<a href="../../../../tf/VariableSynchronization.md#AUTO"><code>tf.VariableSynchronization.AUTO</code></a>,
    aggregation=<a href="../../../../tf/VariableAggregation.md#NONE"><code>tf.VariableAggregation.NONE</code></a>
)
</code></pre>




<h3 id="apply_gradients"><code>apply_gradients</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/optimizer_v2.py#L670-L767">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>apply_gradients(
    grads_and_vars, name=None, experimental_aggregate_gradients=True
)
</code></pre>

Apply gradients to variables.

This is the second part of `minimize()`. It returns an `Operation` that
applies gradients.

The method sums gradients from all replicas in the presence of
<a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> by default. You can aggregate gradients
yourself by passing `experimental_aggregate_gradients=False`.

#### Example:



```python
grads = tape.gradient(loss, vars)
grads = tf.distribute.get_replica_context().all_reduce('sum', grads)
# Processing aggregated gradients.
optimizer.apply_gradients(zip(grads, vars),
    experimental_aggregate_gradients=False)

```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`grads_and_vars`
</td>
<td>
List of (gradient, variable) pairs.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the returned operation. When `None`, uses the
name passed to the `Optimizer` constructor. Defaults to `None`.
</td>
</tr><tr>
<td>
`experimental_aggregate_gradients`
</td>
<td>
Whether to sum gradients from
different replicas in the presence of <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>. If
False, it's user responsibility to aggregate the gradients. Default
to `True`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Operation` that applies the specified gradients. The `iterations`
will be automatically increased by 1.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `grads_and_vars` is malformed.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If none of the variables have gradients.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If called in a cross-replica context.
</td>
</tr>
</table>



<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/optimizer_v2.py#L1216-L1240">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config, custom_objects=None
)
</code></pre>

Creates an optimizer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same optimizer from the config
dictionary.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`config`
</td>
<td>
A Python dictionary, typically the output of get_config.
</td>
</tr><tr>
<td>
`custom_objects`
</td>
<td>
A Python dictionary mapping names to additional
Python objects used to create this optimizer, such as a function
used for a hyperparameter.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An optimizer instance.
</td>
</tr>

</table>



<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/adadelta.py#L152-L164">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>

Returns the config of the optimizer.

An optimizer config is a Python dictionary (serializable)
containing the configuration of an optimizer.
The same optimizer can be reinstantiated later
(without any saved state) from this configuration.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Python dictionary.
</td>
</tr>

</table>



<h3 id="get_gradients"><code>get_gradients</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/optimizer_v2.py#L849-L879">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_gradients(
    loss, params
)
</code></pre>

Returns gradients of `loss` with respect to `params`.

Should be used only in legacy v1 graph mode.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`loss`
</td>
<td>
Loss tensor.
</td>
</tr><tr>
<td>
`params`
</td>
<td>
List of variables.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
List of gradient tensors.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
In case any gradient cannot be computed (e.g. if gradient
function not implemented).
</td>
</tr>
</table>



<h3 id="get_slot"><code>get_slot</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/optimizer_v2.py#L1086-L1102">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_slot(
    var, slot_name
)
</code></pre>




<h3 id="get_slot_names"><code>get_slot_names</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/optimizer_v2.py#L1017-L1019">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_slot_names()
</code></pre>

A list of names for this optimizer's slots.


<h3 id="get_updates"><code>get_updates</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/optimizer_v2.py#L881-L891">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_updates(
    loss, params
)
</code></pre>




<h3 id="get_weights"><code>get_weights</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/optimizer_v2.py#L1263-L1290">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_weights()
</code></pre>

Returns the current weights of the optimizer.

The weights of an optimizer are its state (ie, variables).
This function returns the weight values associated with this
optimizer as a list of Numpy arrays. The first value is always the
iterations count of the optimizer, followed by the optimizer's state
variables in the order they were created. The returned list can in turn
be used to load state into similarly parameterized optimizers.

For example, the RMSprop optimizer for this simple model returns a list
of three values-- the iteration count, followed by the root-mean-square
value of the kernel and bias of the single Dense layer:

```
>>> opt = tf.keras.optimizers.legacy.RMSprop()
>>> m = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
>>> m.compile(opt, loss='mse')
>>> data = np.arange(100).reshape(5, 20)
>>> labels = np.zeros(5)
>>> results = m.fit(data, labels)  # Training.
>>> len(opt.get_weights())
3
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Weights values as a list of numpy arrays.
</td>
</tr>

</table>



<h3 id="minimize"><code>minimize</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/optimizer_v2.py#L567-L601">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>minimize(
    loss, var_list, grad_loss=None, name=None, tape=None
)
</code></pre>

Minimize `loss` by updating `var_list`.

This method simply computes gradient using <a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a> and calls
`apply_gradients()`. If you want to process the gradient before applying
then call <a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a> and `apply_gradients()` explicitly instead
of using this function.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`loss`
</td>
<td>
`Tensor` or callable. If a callable, `loss` should take no
arguments and return the value to minimize. If a `Tensor`, the
`tape` argument must be passed.
</td>
</tr><tr>
<td>
`var_list`
</td>
<td>
list or tuple of `Variable` objects to update to minimize
`loss`, or a callable returning the list or tuple of `Variable`
objects.  Use callable when the variable list would otherwise be
incomplete before `minimize` since the variables are created at the
first time `loss` is called.
</td>
</tr><tr>
<td>
`grad_loss`
</td>
<td>
(Optional). A `Tensor` holding the gradient computed for
`loss`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(Optional) str. Name for the returned operation.
</td>
</tr><tr>
<td>
`tape`
</td>
<td>
(Optional) <a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. If `loss` is provided as a
`Tensor`, the tape that computed the `loss` must be provided.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Operation` that updates the variables in `var_list`. The
`iterations` will be automatically increased by 1.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If some of the variables are not `Variable` objects.
</td>
</tr>
</table>



<h3 id="set_weights"><code>set_weights</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/adadelta.py#L104-L111">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_weights(
    weights
)
</code></pre>

Set the weights of the optimizer.

The weights of an optimizer are its state (ie, variables).
This function takes the weight values associated with this
optimizer as a list of Numpy arrays. The first value is always the
iterations count of the optimizer, followed by the optimizer's state
variables in the order they are created. The passed values are used to
set the new state of the optimizer.

For example, the RMSprop optimizer for this simple model takes a list of
three values-- the iteration count, followed by the root-mean-square
value of the kernel and bias of the single Dense layer:

```
>>> opt = tf.keras.optimizers.legacy.RMSprop()
>>> m = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
>>> m.compile(opt, loss='mse')
>>> data = np.arange(100).reshape(5, 20)
>>> labels = np.zeros(5)
>>> results = m.fit(data, labels)  # Training.
>>> new_weights = [np.array(10), np.ones([20, 10]), np.zeros([10])]
>>> opt.set_weights(new_weights)
>>> opt.iterations
<tf.Variable 'RMSprop/iter:0' shape=() dtype=int64, numpy=10>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`weights`
</td>
<td>
weight values as a list of numpy arrays.
</td>
</tr>
</table>



<h3 id="variables"><code>variables</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/legacy/optimizer_v2.py#L1254-L1256">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>variables()
</code></pre>

Returns variables of this Optimizer based on the order created.



