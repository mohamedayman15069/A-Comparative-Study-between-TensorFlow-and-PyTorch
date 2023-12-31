<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.seq2seq.BeamSearchDecoder" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="batch_size"/>
<meta itemprop="property" content="output_dtype"/>
<meta itemprop="property" content="output_size"/>
<meta itemprop="property" content="tracks_own_finished"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="finalize"/>
<meta itemprop="property" content="initialize"/>
<meta itemprop="property" content="step"/>
</div>

# tf.contrib.seq2seq.BeamSearchDecoder

## Class `BeamSearchDecoder`

BeamSearch sampling decoder.

Inherits From: [`Decoder`](../../../tf/contrib/seq2seq/Decoder.md)

<!-- Placeholder for "Used in" -->

**NOTE** If you are using the `BeamSearchDecoder` with a cell wrapped in
`AttentionWrapper`, then you must ensure that:

- The encoder output has been tiled to `beam_width` via
  <a href="../../../tf/contrib/seq2seq/tile_batch.md"><code>tf.contrib.seq2seq.tile_batch</code></a> (NOT <a href="../../../tf/tile.md"><code>tf.tile</code></a>).
- The `batch_size` argument passed to the `zero_state` method of this
  wrapper is equal to `true_batch_size * beam_width`.
- The initial state created with `zero_state` above contains a
  `cell_state` value containing properly tiled final state from the
  encoder.

#### An example:



```
tiled_encoder_outputs = tf.contrib.seq2seq.tile_batch(
    encoder_outputs, multiplier=beam_width)
tiled_encoder_final_state = tf.contrib.seq2seq.tile_batch(
    encoder_final_state, multiplier=beam_width)
tiled_sequence_length = tf.contrib.seq2seq.tile_batch(
    sequence_length, multiplier=beam_width)
attention_mechanism = MyFavoriteAttentionMechanism(
    num_units=attention_depth,
    memory=tiled_inputs,
    memory_sequence_length=tiled_sequence_length)
attention_cell = AttentionWrapper(cell, attention_mechanism, ...)
decoder_initial_state = attention_cell.zero_state(
    dtype, batch_size=true_batch_size * beam_width)
decoder_initial_state = decoder_initial_state.clone(
    cell_state=tiled_encoder_final_state)
```

Meanwhile, with `AttentionWrapper`, coverage penalty is suggested to use
when computing scores (https://arxiv.org/pdf/1609.08144.pdf). It encourages
the decoder to cover all inputs.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    cell,
    embedding,
    start_tokens,
    end_token,
    initial_state,
    beam_width,
    output_layer=None,
    length_penalty_weight=0.0,
    coverage_penalty_weight=0.0,
    reorder_tensor_arrays=True
)
```

Initialize the BeamSearchDecoder.


#### Args:


* <b>`cell`</b>: An `RNNCell` instance.
* <b>`embedding`</b>: A callable that takes a vector tensor of `ids` (argmax ids),
  or the `params` argument for `embedding_lookup`.
* <b>`start_tokens`</b>: `int32` vector shaped `[batch_size]`, the start tokens.
* <b>`end_token`</b>: `int32` scalar, the token that marks end of decoding.
* <b>`initial_state`</b>: A (possibly nested tuple of...) tensors and TensorArrays.
* <b>`beam_width`</b>:  Python integer, the number of beams.
* <b>`output_layer`</b>: (Optional) An instance of <a href="../../../tf/keras/layers/Layer.md"><code>tf.keras.layers.Layer</code></a>, i.e.,
  <a href="../../../tf/keras/layers/Dense.md"><code>tf.keras.layers.Dense</code></a>.  Optional layer to apply to the RNN output
  prior to storing the result or sampling.
* <b>`length_penalty_weight`</b>: Float weight to penalize length. Disabled with 0.0.
* <b>`coverage_penalty_weight`</b>: Float weight to penalize the coverage of source
  sentence. Disabled with 0.0.
* <b>`reorder_tensor_arrays`</b>: If `True`, `TensorArray`s' elements within the cell
  state will be reordered according to the beam search path. If the
  `TensorArray` can be reordered, the stacked form will be returned.
  Otherwise, the `TensorArray` will be returned as is. Set this flag to
  `False` if the cell state contains `TensorArray`s that are not amenable
  to reordering.


#### Raises:


* <b>`TypeError`</b>: if `cell` is not an instance of `RNNCell`,
  or `output_layer` is not an instance of <a href="../../../tf/keras/layers/Layer.md"><code>tf.keras.layers.Layer</code></a>.
* <b>`ValueError`</b>: If `start_tokens` is not a vector or
  `end_token` is not a scalar.



## Properties

<h3 id="batch_size"><code>batch_size</code></h3>




<h3 id="output_dtype"><code>output_dtype</code></h3>

A (possibly nested tuple of...) dtype[s].


<h3 id="output_size"><code>output_size</code></h3>




<h3 id="tracks_own_finished"><code>tracks_own_finished</code></h3>

The BeamSearchDecoder shuffles its beams and their finished state.

For this reason, it conflicts with the `dynamic_decode` function's
tracking of finished states.  Setting this property to true avoids
early stopping of decoding due to mismanagement of the finished state
in `dynamic_decode`.

#### Returns:

`True`.




## Methods

<h3 id="finalize"><code>finalize</code></h3>

``` python
finalize(
    outputs,
    final_state,
    sequence_lengths
)
```

Finalize and return the predicted_ids.


#### Args:


* <b>`outputs`</b>: An instance of BeamSearchDecoderOutput.
* <b>`final_state`</b>: An instance of BeamSearchDecoderState. Passed through to the
  output.
* <b>`sequence_lengths`</b>: An `int64` tensor shaped `[batch_size, beam_width]`.
  The sequence lengths determined for each beam during decode.
  **NOTE** These are ignored; the updated sequence lengths are stored in
  `final_state.lengths`.


#### Returns:


* <b>`outputs`</b>: An instance of `FinalBeamSearchDecoderOutput` where the
  predicted_ids are the result of calling _gather_tree.
* <b>`final_state`</b>: The same input instance of `BeamSearchDecoderState`.

<h3 id="initialize"><code>initialize</code></h3>

``` python
initialize(name=None)
```

Initialize the decoder.


#### Args:


* <b>`name`</b>: Name scope for any created operations.


#### Returns:

`(finished, start_inputs, initial_state)`.


<h3 id="step"><code>step</code></h3>

``` python
step(
    time,
    inputs,
    state,
    name=None
)
```

Perform a decoding step.


#### Args:


* <b>`time`</b>: scalar `int32` tensor.
* <b>`inputs`</b>: A (structure of) input tensors.
* <b>`state`</b>: A (structure of) state tensors and TensorArrays.
* <b>`name`</b>: Name scope for any created operations.


#### Returns:

`(outputs, next_state, next_inputs, finished)`.




