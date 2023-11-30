description: A LearningRateSchedule that uses a polynomial decay schedule.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.optimizers.schedules.PolynomialDecay" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
</div>

# tf.keras.optimizers.schedules.PolynomialDecay

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/schedules/learning_rate_schedule.py#L317-L467">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A LearningRateSchedule that uses a polynomial decay schedule.

Inherits From: [`LearningRateSchedule`](../../../../tf/keras/optimizers/schedules/LearningRateSchedule.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.optimizers.schedules.PolynomialDecay(
    initial_learning_rate,
    decay_steps,
    end_learning_rate=0.0001,
    power=1.0,
    cycle=False,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

It is commonly observed that a monotonically decreasing learning rate, whose
degree of change is carefully chosen, results in a better performing model.
This schedule applies a polynomial decay function to an optimizer step,
given a provided `initial_learning_rate`, to reach an `end_learning_rate`
in the given `decay_steps`.

It requires a `step` value to compute the decayed learning rate. You
can just pass a TensorFlow variable that you increment at each training
step.

The schedule is a 1-arg callable that produces a decayed learning rate
when passed the current optimizer step. This can be useful for changing the
learning rate value across different invocations of optimizer functions.
It is computed as:

```python
def decayed_learning_rate(step):
  step = min(step, decay_steps)
  return ((initial_learning_rate - end_learning_rate) *
          (1 - step / decay_steps) ^ (power)
         ) + end_learning_rate
```

If `cycle` is True then a multiple of `decay_steps` is used, the first one
that is bigger than `step`.

```python
def decayed_learning_rate(step):
  decay_steps = decay_steps * ceil(step / decay_steps)
  return ((initial_learning_rate - end_learning_rate) *
          (1 - step / decay_steps) ^ (power)
         ) + end_learning_rate
```

You can pass this schedule directly into a <a href="../../../../tf/keras/optimizers/Optimizer.md"><code>tf.keras.optimizers.Optimizer</code></a>
as the learning rate.
Example: Fit a model while decaying from 0.1 to 0.01 in 10000 steps using
sqrt (i.e. power=0.5):

```python
...
starter_learning_rate = 0.1
end_learning_rate = 0.01
decay_steps = 10000
learning_rate_fn = tf.keras.optimizers.schedules.PolynomialDecay(
    starter_learning_rate,
    decay_steps,
    end_learning_rate,
    power=0.5)

model.compile(optimizer=tf.keras.optimizers.SGD(
                  learning_rate=learning_rate_fn),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(data, labels, epochs=5)
```

The learning rate schedule is also serializable and deserializable using
<a href="../../../../tf/keras/optimizers/schedules/serialize.md"><code>tf.keras.optimizers.schedules.serialize</code></a> and
<a href="../../../../tf/keras/optimizers/schedules/deserialize.md"><code>tf.keras.optimizers.schedules.deserialize</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A 1-arg callable learning rate schedule that takes the current optimizer
step and outputs the decayed learning rate, a scalar `Tensor` of the same
type as `initial_learning_rate`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`initial_learning_rate`<a id="initial_learning_rate"></a>
</td>
<td>
A scalar `float32` or `float64` `Tensor` or a
Python number.  The initial learning rate.
</td>
</tr><tr>
<td>
`decay_steps`<a id="decay_steps"></a>
</td>
<td>
A scalar `int32` or `int64` `Tensor` or a Python number.
Must be positive.  See the decay computation above.
</td>
</tr><tr>
<td>
`end_learning_rate`<a id="end_learning_rate"></a>
</td>
<td>
A scalar `float32` or `float64` `Tensor` or a
Python number.  The minimal end learning rate.
</td>
</tr><tr>
<td>
`power`<a id="power"></a>
</td>
<td>
A scalar `float32` or `float64` `Tensor` or a
Python number. The power of the polynomial. Defaults to `1.0`.
</td>
</tr><tr>
<td>
`cycle`<a id="cycle"></a>
</td>
<td>
A boolean, whether it should cycle beyond decay_steps.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
String.  Optional name of the operation. Defaults to
'PolynomialDecay'.
</td>
</tr>
</table>



## Methods

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/schedules/learning_rate_schedule.py#L88-L98">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config
)
</code></pre>

Instantiates a `LearningRateSchedule` from its config.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`config`
</td>
<td>
Output of `get_config()`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `LearningRateSchedule` instance.
</td>
</tr>

</table>



<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/schedules/learning_rate_schedule.py#L459-L467">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>




<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/optimizers/schedules/learning_rate_schedule.py#L422-L457">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    step
)
</code></pre>

Call self as a function.



