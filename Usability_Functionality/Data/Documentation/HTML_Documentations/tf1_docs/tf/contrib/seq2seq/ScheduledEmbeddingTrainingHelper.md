<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.seq2seq.ScheduledEmbeddingTrainingHelper" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="batch_size"/>
<meta itemprop="property" content="inputs"/>
<meta itemprop="property" content="sample_ids_dtype"/>
<meta itemprop="property" content="sample_ids_shape"/>
<meta itemprop="property" content="sequence_length"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="initialize"/>
<meta itemprop="property" content="next_inputs"/>
<meta itemprop="property" content="sample"/>
</div>

# tf.contrib.seq2seq.ScheduledEmbeddingTrainingHelper

## Class `ScheduledEmbeddingTrainingHelper`

A training helper that adds scheduled sampling.

Inherits From: [`TrainingHelper`](../../../tf/contrib/seq2seq/TrainingHelper.md)

<!-- Placeholder for "Used in" -->

Returns -1s for sample_ids where no sampling took place; valid sample id
values elsewhere.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    inputs,
    sequence_length,
    embedding,
    sampling_probability,
    time_major=False,
    seed=None,
    scheduling_seed=None,
    name=None
)
```

Initializer.


#### Args:


* <b>`inputs`</b>: A (structure of) input tensors.
* <b>`sequence_length`</b>: An int32 vector tensor.
* <b>`embedding`</b>: A callable that takes a vector tensor of `ids` (argmax ids),
  or the `params` argument for `embedding_lookup`.
* <b>`sampling_probability`</b>: A 0D `float32` tensor: the probability of sampling
  categorically from the output ids instead of reading directly from the
  inputs.
* <b>`time_major`</b>: Python bool.  Whether the tensors in `inputs` are time major.
  If `False` (default), they are assumed to be batch major.
* <b>`seed`</b>: The sampling seed.
* <b>`scheduling_seed`</b>: The schedule decision rule sampling seed.
* <b>`name`</b>: Name scope for any created operations.


#### Raises:


* <b>`ValueError`</b>: if `sampling_probability` is not a scalar or vector.



## Properties

<h3 id="batch_size"><code>batch_size</code></h3>

Batch size of tensor returned by `sample`.

Returns a scalar int32 tensor.

<h3 id="inputs"><code>inputs</code></h3>




<h3 id="sample_ids_dtype"><code>sample_ids_dtype</code></h3>

DType of tensor returned by `sample`.

Returns a DType.

<h3 id="sample_ids_shape"><code>sample_ids_shape</code></h3>

Shape of tensor returned by `sample`, excluding the batch dimension.

Returns a `TensorShape`.

<h3 id="sequence_length"><code>sequence_length</code></h3>






## Methods

<h3 id="initialize"><code>initialize</code></h3>

``` python
initialize(name=None)
```

Returns `(initial_finished, initial_inputs)`.


<h3 id="next_inputs"><code>next_inputs</code></h3>

``` python
next_inputs(
    time,
    outputs,
    state,
    sample_ids,
    name=None
)
```

next_inputs_fn for TrainingHelper.


<h3 id="sample"><code>sample</code></h3>

``` python
sample(
    time,
    outputs,
    state,
    name=None
)
```

Returns `sample_ids`.




