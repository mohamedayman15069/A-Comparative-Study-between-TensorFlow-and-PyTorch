description: Optimization parameters for Adagrad with TPU embeddings.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.experimental.AdagradParameters" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.compat.v1.tpu.experimental.AdagradParameters

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/tpu/tpu_embedding.py">View source</a>



Optimization parameters for Adagrad with TPU embeddings.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.experimental.AdagradParameters(
    learning_rate: float,
    initial_accumulator: float = 0.1,
    use_gradient_accumulation: bool = True,
    clip_weight_min: Optional[float] = None,
    clip_weight_max: Optional[float] = None,
    weight_decay_factor: Optional[float] = None,
    multiply_weight_decay_factor_by_learning_rate: Optional[bool] = None,
    clip_gradient_min: Optional[float] = None,
    clip_gradient_max: Optional[float] = None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Pass this to `tf.estimator.tpu.experimental.EmbeddingConfigSpec` via the
`optimization_parameters` argument to set the optimizer and its parameters.
See the documentation for `tf.estimator.tpu.experimental.EmbeddingConfigSpec`
for more details.

```
estimator = tf.estimator.tpu.TPUEstimator(
    ...
    embedding_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
        ...
        optimization_parameters=tf.tpu.experimental.AdagradParameters(0.1),
        ...))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`learning_rate`<a id="learning_rate"></a>
</td>
<td>
used for updating embedding table.
</td>
</tr><tr>
<td>
`initial_accumulator`<a id="initial_accumulator"></a>
</td>
<td>
initial accumulator for Adagrad.
</td>
</tr><tr>
<td>
`use_gradient_accumulation`<a id="use_gradient_accumulation"></a>
</td>
<td>
setting this to `False` makes embedding
gradients calculation less accurate but faster. Please see
`optimization_parameters.proto` for details.
</td>
</tr><tr>
<td>
`clip_weight_min`<a id="clip_weight_min"></a>
</td>
<td>
the minimum value to clip by; None means -infinity.
</td>
</tr><tr>
<td>
`clip_weight_max`<a id="clip_weight_max"></a>
</td>
<td>
the maximum value to clip by; None means +infinity.
</td>
</tr><tr>
<td>
`weight_decay_factor`<a id="weight_decay_factor"></a>
</td>
<td>
amount of weight decay to apply; None means that the
weights are not decayed.
</td>
</tr><tr>
<td>
`multiply_weight_decay_factor_by_learning_rate`<a id="multiply_weight_decay_factor_by_learning_rate"></a>
</td>
<td>
if true,
`weight_decay_factor` is multiplied by the current learning rate.
</td>
</tr><tr>
<td>
`clip_gradient_min`<a id="clip_gradient_min"></a>
</td>
<td>
the minimum value to clip by; None means -infinity.
Gradient accumulation must be set to true if this is set.
</td>
</tr><tr>
<td>
`clip_gradient_max`<a id="clip_gradient_max"></a>
</td>
<td>
the maximum value to clip by; None means +infinity.
Gradient accumulation must be set to true if this is set.
</td>
</tr>
</table>



