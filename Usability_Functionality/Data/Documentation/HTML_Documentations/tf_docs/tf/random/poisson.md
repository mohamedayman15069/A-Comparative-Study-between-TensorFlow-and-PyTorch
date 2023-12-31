description: Draws shape samples from each of the given Poisson distribution(s).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.poisson" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.poisson

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/random_ops.py">View source</a>



Draws `shape` samples from each of the given Poisson distribution(s).


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.poisson(
    shape,
    lam,
    dtype=<a href="../../tf/dtypes.md#float32"><code>tf.dtypes.float32</code></a>,
    seed=None,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`lam` is the rate parameter describing the distribution(s).

#### Example:



```python
samples = tf.random.poisson([10], [0.5, 1.5])
# samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
# the samples drawn from each distribution

samples = tf.random.poisson([7, 5], [12.2, 3.3])
# samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
# represents the 7x5 samples drawn from each of the two distributions
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`<a id="shape"></a>
</td>
<td>
A 1-D integer Tensor or Python array. The shape of the output samples
to be drawn per "rate"-parameterized distribution.
</td>
</tr><tr>
<td>
`lam`<a id="lam"></a>
</td>
<td>
A Tensor or Python value or N-D array of type `dtype`.
`lam` provides the rate parameter(s) describing the poisson
distribution(s) to sample.
</td>
</tr><tr>
<td>
`dtype`<a id="dtype"></a>
</td>
<td>
The type of the output: `float16`, `float32`, `float64`, `int32` or
`int64`.
</td>
</tr><tr>
<td>
`seed`<a id="seed"></a>
</td>
<td>
A Python integer. Used to create a random seed for the distributions.
See
<a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a>
for behavior.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
Optional name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`samples`<a id="samples"></a>
</td>
<td>
a `Tensor` of shape `tf.concat([shape, tf.shape(lam)], axis=0)`
with values of type `dtype`.
</td>
</tr>
</table>

