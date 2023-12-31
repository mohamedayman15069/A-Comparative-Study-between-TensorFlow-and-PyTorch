description: Creates a bidirectional recurrent neural network. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.static_bidirectional_rnn" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.static_bidirectional_rnn

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/rnn.py">View source</a>



Creates a bidirectional recurrent neural network. (deprecated)


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.static_bidirectional_rnn(
    cell_fw,
    cell_bw,
    inputs,
    initial_state_fw=None,
    initial_state_bw=None,
    dtype=None,
    sequence_length=None,
    scope=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please use `keras.layers.Bidirectional(keras.layers.RNN(cell, unroll=True))`, which is equivalent to this API

Similar to the unidirectional case above (rnn) but takes input and builds
independent forward and backward RNNs with the final forward and backward
outputs depth-concatenated, such that the output will have the format
[time][batch][cell_fw.output_size + cell_bw.output_size]. The input_size of
forward and backward cell must match. The initial state for both directions
is zero by default (but can be set optionally) and no intermediate states are
ever returned -- the network is fully unrolled for the given (passed in)
length(s) of the sequence(s) or completely unrolled if length(s) is not given.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`cell_fw`<a id="cell_fw"></a>
</td>
<td>
An instance of RNNCell, to be used for forward direction.
</td>
</tr><tr>
<td>
`cell_bw`<a id="cell_bw"></a>
</td>
<td>
An instance of RNNCell, to be used for backward direction.
</td>
</tr><tr>
<td>
`inputs`<a id="inputs"></a>
</td>
<td>
A length T list of inputs, each a tensor of shape [batch_size,
input_size], or a nested tuple of such elements.
</td>
</tr><tr>
<td>
`initial_state_fw`<a id="initial_state_fw"></a>
</td>
<td>
(optional) An initial state for the forward RNN. This must
be a tensor of appropriate type and shape `[batch_size,
cell_fw.state_size]`. If `cell_fw.state_size` is a tuple, this should be a
tuple of tensors having shapes `[batch_size, s] for s in
cell_fw.state_size`.
</td>
</tr><tr>
<td>
`initial_state_bw`<a id="initial_state_bw"></a>
</td>
<td>
(optional) Same as for `initial_state_fw`, but using the
corresponding properties of `cell_bw`.
</td>
</tr><tr>
<td>
`dtype`<a id="dtype"></a>
</td>
<td>
(optional) The data type for the initial state.  Required if either
of the initial states are not provided.
</td>
</tr><tr>
<td>
`sequence_length`<a id="sequence_length"></a>
</td>
<td>
(optional) An int32/int64 vector, size `[batch_size]`,
containing the actual lengths for each of the sequences.
</td>
</tr><tr>
<td>
`scope`<a id="scope"></a>
</td>
<td>
VariableScope for the created subgraph; defaults to
"bidirectional_rnn"
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tuple (outputs, output_state_fw, output_state_bw) where:
outputs is a length `T` list of outputs (one for each input), which
  are depth-concatenated forward and backward outputs.
output_state_fw is the final state of the forward rnn.
output_state_bw is the final state of the backward rnn.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`<a id="TypeError"></a>
</td>
<td>
If `cell_fw` or `cell_bw` is not an instance of `RNNCell`.
</td>
</tr><tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
If inputs is None or an empty list.
</td>
</tr>
</table>

