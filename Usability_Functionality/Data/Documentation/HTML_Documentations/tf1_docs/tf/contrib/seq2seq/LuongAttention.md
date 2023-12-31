<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.seq2seq.LuongAttention" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="alignments_size"/>
<meta itemprop="property" content="batch_size"/>
<meta itemprop="property" content="keys"/>
<meta itemprop="property" content="memory_layer"/>
<meta itemprop="property" content="query_layer"/>
<meta itemprop="property" content="state_size"/>
<meta itemprop="property" content="values"/>
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="initial_alignments"/>
<meta itemprop="property" content="initial_state"/>
</div>

# tf.contrib.seq2seq.LuongAttention

## Class `LuongAttention`

Implements Luong-style (multiplicative) attention scoring.



<!-- Placeholder for "Used in" -->

This attention has two forms.  The first is standard Luong attention,
as described in:

Minh-Thang Luong, Hieu Pham, Christopher D. Manning.
[Effective Approaches to Attention-based Neural Machine Translation.
EMNLP 2015.](https://arxiv.org/abs/1508.04025)

The second is the scaled form inspired partly by the normalized form of
Bahdanau attention.

To enable the second form, construct the object with parameter
`scale=True`.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    memory,
    memory_sequence_length=None,
    scale=False,
    probability_fn=None,
    score_mask_value=None,
    dtype=None,
    custom_key_value_fn=None,
    name='LuongAttention'
)
```

Construct the AttentionMechanism mechanism.


#### Args:


* <b>`num_units`</b>: The depth of the attention mechanism.
* <b>`memory`</b>: The memory to query; usually the output of an RNN encoder.  This
  tensor should be shaped `[batch_size, max_time, ...]`.
* <b>`memory_sequence_length`</b>: (optional) Sequence lengths for the batch entries
  in memory.  If provided, the memory tensor rows are masked with zeros
  for values past the respective sequence lengths.
* <b>`scale`</b>: Python boolean.  Whether to scale the energy term.
* <b>`probability_fn`</b>: (optional) A `callable`.  Converts the score to
  probabilities.  The default is <a href="../../../tf/nn/softmax.md"><code>tf.nn.softmax</code></a>. Other options include
  <a href="../../../tf/contrib/seq2seq/hardmax.md"><code>tf.contrib.seq2seq.hardmax</code></a> and <a href="../../../tf/contrib/sparsemax/sparsemax.md"><code>tf.contrib.sparsemax.sparsemax</code></a>.
  Its signature should be: `probabilities = probability_fn(score)`.
* <b>`score_mask_value`</b>: (optional) The mask value for score before passing into
  `probability_fn`. The default is -inf. Only used if
  `memory_sequence_length` is not None.
* <b>`dtype`</b>: The data type for the memory layer of the attention mechanism.
* <b>`custom_key_value_fn`</b>: (optional): The custom function for
  computing keys and values.
* <b>`name`</b>: Name to use when creating ops.



## Properties

<h3 id="alignments_size"><code>alignments_size</code></h3>




<h3 id="batch_size"><code>batch_size</code></h3>




<h3 id="keys"><code>keys</code></h3>




<h3 id="memory_layer"><code>memory_layer</code></h3>




<h3 id="query_layer"><code>query_layer</code></h3>




<h3 id="state_size"><code>state_size</code></h3>




<h3 id="values"><code>values</code></h3>






## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    query,
    state
)
```

Score the query based on the keys and values.


#### Args:


* <b>`query`</b>: Tensor of dtype matching `self.values` and shape `[batch_size,
  query_depth]`.
* <b>`state`</b>: Tensor of dtype matching `self.values` and shape `[batch_size,
  alignments_size]` (`alignments_size` is memory's `max_time`).


#### Returns:


* <b>`alignments`</b>: Tensor of dtype matching `self.values` and shape
  `[batch_size, alignments_size]` (`alignments_size` is memory's
  `max_time`).

<h3 id="initial_alignments"><code>initial_alignments</code></h3>

``` python
initial_alignments(
    batch_size,
    dtype
)
```

Creates the initial alignment values for the `AttentionWrapper` class.

This is important for AttentionMechanisms that use the previous alignment
to calculate the alignment at the next time step (e.g. monotonic attention).

The default behavior is to return a tensor of all zeros.

#### Args:


* <b>`batch_size`</b>: `int32` scalar, the batch_size.
* <b>`dtype`</b>: The `dtype`.


#### Returns:

A `dtype` tensor shaped `[batch_size, alignments_size]`
(`alignments_size` is the values' `max_time`).


<h3 id="initial_state"><code>initial_state</code></h3>

``` python
initial_state(
    batch_size,
    dtype
)
```

Creates the initial state values for the `AttentionWrapper` class.

This is important for AttentionMechanisms that use the previous alignment
to calculate the alignment at the next time step (e.g. monotonic attention).

The default behavior is to return the same output as initial_alignments.

#### Args:


* <b>`batch_size`</b>: `int32` scalar, the batch_size.
* <b>`dtype`</b>: The `dtype`.


#### Returns:

A structure of all-zero tensors with shapes as described by `state_size`.




