description: Optimization parameters for stochastic gradient descent for TPU embeddings.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tpu.experimental.embedding.SGD" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
</div>

# tf.tpu.experimental.embedding.SGD

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/tpu/tpu_embedding_v2_utils.py">View source</a>



Optimization parameters for stochastic gradient descent for TPU embeddings.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.tpu.experimental.embedding.SGD`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.tpu.experimental.embedding.SGD(
    learning_rate: Union[float, Callable[[], float]] = 0.01,
    use_gradient_accumulation: bool = True,
    clip_weight_min: Optional[float] = None,
    clip_weight_max: Optional[float] = None,
    weight_decay_factor: Optional[float] = None,
    multiply_weight_decay_factor_by_learning_rate: bool = None,
    clipvalue: Optional[ClipValueType] = None,
    low_dimensional_packing_status: bool = False
)
</code></pre>



<!-- Placeholder for "Used in" -->

Pass this to <a href="../../../../tf/tpu/experimental/embedding/TPUEmbedding.md"><code>tf.tpu.experimental.embedding.TPUEmbedding</code></a> via the `optimizer`
argument to set the global optimizer and its parameters:

```
embedding = tf.tpu.experimental.embedding.TPUEmbedding(
    ...
    optimizer=tf.tpu.experimental.embedding.SGD(0.1))
```

This can also be used in a <a href="../../../../tf/tpu/experimental/embedding/TableConfig.md"><code>tf.tpu.experimental.embedding.TableConfig</code></a> as the
optimizer parameter to set a table specific optimizer. This will override the
optimizer and parameters for global embedding optimizer defined above:

```
table_one = tf.tpu.experimental.embedding.TableConfig(
    vocabulary_size=...,
    dim=...,
    optimizer=tf.tpu.experimental.embedding.SGD(0.2))
table_two = tf.tpu.experimental.embedding.TableConfig(
    vocabulary_size=...,
    dim=...)

feature_config = (
    tf.tpu.experimental.embedding.FeatureConfig(
        table=table_one),
    tf.tpu.experimental.embedding.FeatureConfig(
        table=table_two))

embedding = tf.tpu.experimental.embedding.TPUEmbedding(
    feature_config=feature_config,
    batch_size=...
    optimizer=tf.tpu.experimental.embedding.SGD(0.1))
```

In the above example, the first feature will be looked up in a table that has
a learning rate of 0.2 while the second feature will be looked up in a table
that has a learning rate of 0.1.

See 'tensorflow/core/protobuf/tpu/optimization_parameters.proto' for a
complete description of these parameters and their impacts on the optimizer
algorithm.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`learning_rate`<a id="learning_rate"></a>
</td>
<td>
The learning rate. It should be a floating point value or a
callable taking no arguments for a dynamic learning rate.
</td>
</tr><tr>
<td>
`use_gradient_accumulation`<a id="use_gradient_accumulation"></a>
</td>
<td>
setting this to `False` makes embedding
gradients calculation less accurate but faster.
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
weights are not decayed. Weights are decayed by multiplying the weight
by this factor each step.
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
`clipvalue`<a id="clipvalue"></a>
</td>
<td>
Controls clipping of the gradient. Set to either a single
positive scalar value to get clipping or a tiple of scalar values (min,
max) to set a separate maximum or minimum. If one of the two entries is
None, then there will be no clipping that direction. Note if this is
set, you may see a decrease in performance as  gradient accumulation
will be enabled (it is normally off for SGD as it has no affect on
accuracy). See
'tensorflow/core/protobuf/tpu/optimization_parameters.proto' for more
information on gradient accumulation and its impact on tpu embeddings.
</td>
</tr><tr>
<td>
`low_dimensional_packing_status`<a id="low_dimensional_packing_status"></a>
</td>
<td>
Status of the low-dimensional embedding
packing optimization controls whether to optimize the packing of
1-dimensional, 2-dimensional, and 4-dimensional embedding tables in
memory.
</td>
</tr>
</table>



## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/tpu/tpu_embedding_v2_utils.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other: Any
) -> Union[Any, bool]
</code></pre>

Return self==value.




