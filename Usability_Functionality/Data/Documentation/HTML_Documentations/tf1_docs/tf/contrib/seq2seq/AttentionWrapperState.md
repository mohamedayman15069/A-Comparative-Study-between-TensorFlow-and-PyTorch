<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.seq2seq.AttentionWrapperState" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="cell_state"/>
<meta itemprop="property" content="attention"/>
<meta itemprop="property" content="time"/>
<meta itemprop="property" content="alignments"/>
<meta itemprop="property" content="alignment_history"/>
<meta itemprop="property" content="attention_state"/>
<meta itemprop="property" content="clone"/>
</div>

# tf.contrib.seq2seq.AttentionWrapperState

## Class `AttentionWrapperState`

`namedtuple` storing the state of a `AttentionWrapper`.



<!-- Placeholder for "Used in" -->


#### Contains:


- `cell_state`: The state of the wrapped `RNNCell` at the previous time
  step.
- `attention`: The attention emitted at the previous time step.
- `time`: int32 scalar containing the current time step.
- `alignments`: A single or tuple of `Tensor`(s) containing the alignments
   emitted at the previous time step for each attention mechanism.
- `alignment_history`: (if enabled) a single or tuple of `TensorArray`(s)
   containing alignment matrices from all time steps for each attention
   mechanism. Call `stack()` on each to convert to a `Tensor`.
- `attention_state`: A single or tuple of nested objects
   containing attention mechanism state for each attention mechanism.
   The objects may contain Tensors or TensorArrays.


## Properties

<h3 id="cell_state"><code>cell_state</code></h3>




<h3 id="attention"><code>attention</code></h3>




<h3 id="time"><code>time</code></h3>




<h3 id="alignments"><code>alignments</code></h3>




<h3 id="alignment_history"><code>alignment_history</code></h3>




<h3 id="attention_state"><code>attention_state</code></h3>






## Methods

<h3 id="clone"><code>clone</code></h3>

``` python
clone(**kwargs)
```

Clone this object, overriding components provided by kwargs.

The new state fields' shape must match original state fields' shape. This
will be validated, and original fields' shape will be propagated to new
fields.

#### Example:



```python
initial_state = attention_wrapper.zero_state(dtype=..., batch_size=...)
initial_state = initial_state.clone(cell_state=encoder_state)
```

#### Args:


* <b>`**kwargs`</b>: Any properties of the state object to replace in the returned
  `AttentionWrapperState`.


#### Returns:

A new `AttentionWrapperState` whose properties are the same as
this one, except any overridden properties as provided in `kwargs`.




