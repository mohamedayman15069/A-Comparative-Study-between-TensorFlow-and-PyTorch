description: Optimizer that implements the AdamW algorithm.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.optimizers.AdamW" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add_variable"/>
<meta itemprop="property" content="build"/>
<meta itemprop="property" content="compute_gradients"/>
<meta itemprop="property" content="exclude_from_weight_decay"/>
<meta itemprop="property" content="finalize_variable_values"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
<meta itemprop="property" content="load_own_variables"/>
<meta itemprop="property" content="minimize"/>
<meta itemprop="property" content="save_own_variables"/>
<meta itemprop="property" content="set_weights"/>
<meta itemprop="property" content="update_step"/>
</div>

# tf.keras.optimizers.AdamW

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/adamw.py#L27-L225">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Optimizer that implements the AdamW algorithm.

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.dtensor.experimental.optimizers.AdamW`, `tf.keras.optimizers.experimental.AdamW`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.optimizers.AdamW(
    learning_rate=0.001,
    weight_decay=0.004,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-07,
    amsgrad=False,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    jit_compile=True,
    name=&#x27;AdamW&#x27;,
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

AdamW optimization is a stochastic gradient descent method that is based on
adaptive estimation of first-order and second-order moments with an added
method to decay weights per the techniques discussed in the paper,
'Decoupled Weight Decay Regularization' by
[Loshchilov, Hutter et al., 2019](https://arxiv.org/abs/1711.05101).

According to
[Kingma et al., 2014](http://arxiv.org/abs/1412.6980),
the underying Adam method is "*computationally
efficient, has little memory requirement, invariant to diagonal rescaling of
gradients, and is well suited for problems that are large in terms of
data/parameters*".

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>
<tr class="alt">
<td colspan="2">
learning_rate: A <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, floating point value, a schedule that is a
    <a href="../../../tf/keras/optimizers/schedules/LearningRateSchedule.md"><code>tf.keras.optimizers.schedules.LearningRateSchedule</code></a>, or a callable
    that takes no arguments and returns the actual value to use. The
    learning rate. Defaults to 0.001.
beta_1: A float value or a constant float tensor, or a callable
    that takes no arguments and returns the actual value to use. The
    exponential decay rate for the 1st moment estimates.
    Defaults to 0.9.
beta_2: A float value or a constant float tensor, or a callable
    that takes no arguments and returns the actual value to use. The
    exponential decay rate for the 2nd moment estimates.
    Defaults to 0.999.
epsilon: A small constant for numerical stability. This epsilon is
    "epsilon hat" in the Kingma and Ba paper (in the formula just before
    Section 2.1), not the epsilon in Algorithm 1 of the paper.
    Defaults to 1e-7.
amsgrad: Boolean. Whether to apply AMSGrad variant of this algorithm
    from the paper "On the Convergence of Adam and beyond".
    Defaults to `False`.
name: String. The name to use
  for momentum accumulator weights created by
  the optimizer.
</td>
</tr>
<tr>
<td>
`weight_decay`<a id="weight_decay"></a>
</td>
<td>
Float, defaults to None. If set, weight decay is applied.
</td>
</tr><tr>
<td>
`clipnorm`<a id="clipnorm"></a>
</td>
<td>
Float. If set, the gradient of each weight is individually
clipped so that its norm is no higher than this value.
</td>
</tr><tr>
<td>
`clipvalue`<a id="clipvalue"></a>
</td>
<td>
Float. If set, the gradient of each weight is clipped to be no
higher than this value.
</td>
</tr><tr>
<td>
`global_clipnorm`<a id="global_clipnorm"></a>
</td>
<td>
Float. If set, the gradient of all weights is clipped so
that their global norm is no higher than this value.
</td>
</tr><tr>
<td>
`use_ema`<a id="use_ema"></a>
</td>
<td>
Boolean, defaults to False. If True, exponential moving average
(EMA) is applied. EMA consists of computing an exponential moving
average of the weights of the model (as the weight values change after
each training batch), and periodically overwriting the weights with
their moving average.
</td>
</tr><tr>
<td>
`ema_momentum`<a id="ema_momentum"></a>
</td>
<td>
Float, defaults to 0.99. Only used if `use_ema=True`.
This is the momentum to use when computing
the EMA of the model's weights:
`new_average = ema_momentum * old_average + (1 - ema_momentum) *
current_variable_value`.
</td>
</tr><tr>
<td>
`ema_overwrite_frequency`<a id="ema_overwrite_frequency"></a>
</td>
<td>
Int or None, defaults to None. Only used if
`use_ema=True`. Every `ema_overwrite_frequency` steps of iterations,
we overwrite the model variable by its moving average.
If None, the optimizer
does not overwrite model variables in the middle of training, and you
need to explicitly overwrite the variables at the end of training
by calling `optimizer.finalize_variable_values()`
(which updates the model
variables in-place). When using the built-in `fit()` training loop,
this happens automatically after the last epoch,
and you don't need to do anything.
</td>
</tr><tr>
<td>
`jit_compile`<a id="jit_compile"></a>
</td>
<td>
Boolean, defaults to True.
If True, the optimizer will use XLA
compilation. If no GPU device is found, this flag will be ignored.
</td>
</tr><tr>
<td>
`mesh`<a id="mesh"></a>
</td>
<td>
optional <a href="../../../tf/experimental/dtensor/Mesh.md"><code>tf.experimental.dtensor.Mesh</code></a> instance. When provided,
the optimizer will be run in DTensor mode, e.g. state
tracking variable will be a DVariable, and aggregation/reduction will
happen in the global DTensor context.
</td>
</tr><tr>
<td>
`**kwargs`<a id="**kwargs"></a>
</td>
<td>
keyword arguments only used for backward compatibility.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Reference</h2></th></tr>
<tr class="alt">
<td colspan="2">
- [Loshchilov et al., 2019](https://arxiv.org/abs/1711.05101)
- [Kingma et al., 2014](http://arxiv.org/abs/1412.6980) for `adam`
- [Reddi et al., 2018](
    https://openreview.net/pdf?id=ryQu7f-RZ) for `amsgrad`.
</td>
</tr>

</table>



#### Notes:



The sparse implementation of this algorithm (used when the gradient is an
IndexedSlices object, typically because of <a href="../../../tf/gather.md"><code>tf.gather</code></a> or an embedding
lookup in the forward pass) does apply momentum to variable slices even if
they were not used in the forward pass (meaning they have a gradient equal
to zero). Momentum decay (beta1) is also applied to the entire momentum
accumulator. This means that the sparse behavior is equivalent to the dense
behavior (in contrast to some momentum implementations which ignore momentum
unless a variable slice was actually used).



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`iterations`<a id="iterations"></a>
</td>
<td>
The number of training steps this `optimizer` has run.

By default, iterations would be incremented by one every time
`apply_gradients()` is called.
</td>
</tr><tr>
<td>
`learning_rate`<a id="learning_rate"></a>
</td>
<td>

</td>
</tr><tr>
<td>
`variables`<a id="variables"></a>
</td>
<td>
Returns variables of this optimizer.
</td>
</tr>
</table>



## Methods

<h3 id="add_variable"><code>add_variable</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/optimizer.py#L445-L470">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_variable(
    shape, dtype=None, initializer=&#x27;zeros&#x27;, name=None
)
</code></pre>

Create an optimizer variable.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`shape`
</td>
<td>
A list of integers, a tuple of integers, or a 1-D Tensor of
type int32. Defaults to scalar if unspecified.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The DType of the optimizer variable to be created. Defaults to
<a href="../../../tf/keras/backend/floatx.md"><code>tf.keras.backend.floatx</code></a> if unspecified.
</td>
</tr><tr>
<td>
`initializer`
</td>
<td>
string or callable. Initializer instance.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name of the optimizer variable to be created.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An optimizer variable, in the format of tf.Variable.
</td>
</tr>

</table>



<h3 id="build"><code>build</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/adamw.py#L132-L165">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>build(
    var_list
)
</code></pre>

Initialize optimizer variables.

AdamW optimizer has 3 types of variables: momentums, velocities and
velocity_hat (only set when amsgrad is applied),

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`var_list`
</td>
<td>
list of model variables to build AdamW variables on.
</td>
</tr>
</table>



<h3 id="compute_gradients"><code>compute_gradients</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/optimizer.py#L243-L277">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>compute_gradients(
    loss, var_list, tape=None
)
</code></pre>

Compute gradients of loss on trainable variables.


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
arguments and return the value to minimize.
</td>
</tr><tr>
<td>
`var_list`
</td>
<td>
list or tuple of `Variable` objects to update to minimize
`loss`, or a callable returning the list or tuple of `Variable`
objects. Use callable when the variable list would otherwise be
incomplete before `minimize` since the variables are created at the
first time `loss` is called.
</td>
</tr><tr>
<td>
`tape`
</td>
<td>
(Optional) <a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. If `loss` is provided as a
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
A list of (gradient, variable) pairs. Variable is always present, but
gradient can be `None`.
</td>
</tr>

</table>



<h3 id="exclude_from_weight_decay"><code>exclude_from_weight_decay</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/optimizer.py#L567-L594">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>exclude_from_weight_decay(
    var_list=None, var_names=None
)
</code></pre>

Exclude variables from weight decay.

This method must be called before the optimizer's `build` method is
called. You can set specific variables to exclude out, or set a list of
strings as the anchor words, if any of which appear in a variable's
name, then the variable is excluded.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`var_list`
</td>
<td>
A list of <a href="../../../tf/Variable.md"><code>tf.Variable</code></a>s to exclude from weight decay.
</td>
</tr><tr>
<td>
`var_names`
</td>
<td>
A list of strings. If any string in `var_names` appear
in the model variable's name, then this model variable is
excluded from weight decay. For example, `var_names=['bias']`
excludes all bias variables from weight decay.
</td>
</tr>
</table>



<h3 id="finalize_variable_values"><code>finalize_variable_values</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/optimizer.py#L704-L717">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>finalize_variable_values(
    var_list
)
</code></pre>

Set the final value of model's trainable variables.

Sometimes there are some extra steps before ending the variable updates,
such as overriding the model variables with its average value.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`var_list`
</td>
<td>
list of model variables.
</td>
</tr>
</table>



<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/optimizer.py#L759-L779">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config, custom_objects=None
)
</code></pre>

Creates an optimizer from its config.

This method is the reverse of `get_config`, capable of instantiating the
same optimizer from the config dictionary.

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
user-defined Python objects needed to recreate this optimizer.
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

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/adamw.py#L210-L225">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>

Returns the config of the optimizer.

An optimizer config is a Python dictionary (serializable)
containing the configuration of an optimizer.
The same optimizer can be reinstantiated later
(without any saved state) from this configuration.

Subclass optimizer should override this method to include other
hyperparameters.

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



<h3 id="load_own_variables"><code>load_own_variables</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/optimizer.py#L816-L832">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>load_own_variables(
    store
)
</code></pre>

Set the state of this optimizer object.


<h3 id="minimize"><code>minimize</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/optimizer.py#L522-L544">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>minimize(
    loss, var_list, tape=None
)
</code></pre>

Minimize `loss` by updating `var_list`.

This method simply computes gradient using <a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a> and calls
`apply_gradients()`. If you want to process the gradient before applying
then call <a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a> and `apply_gradients()` explicitly instead
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
arguments and return the value to minimize.
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
`tape`
</td>
<td>
(Optional) <a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
None
</td>
</tr>

</table>



<h3 id="save_own_variables"><code>save_own_variables</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/optimizer.py#L811-L814">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>save_own_variables(
    store
)
</code></pre>

Get the state of this optimizer object.


<h3 id="set_weights"><code>set_weights</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/optimizer.py#L786-L809">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_weights(
    weights
)
</code></pre>

Set the weights of the optimizer.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`weights`
</td>
<td>
a list of <a href="../../../tf/Variable.md"><code>tf.Variable</code></a>s or numpy arrays, the target values
of optimizer variables. It should have the same order as
`self._variables`.
</td>
</tr>
</table>



<h3 id="update_step"><code>update_step</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/adamw.py#L167-L208">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_step(
    gradient, variable
)
</code></pre>

Update step given gradient and the associated model variable.



