description: Converts CudnnRNN params from canonical form to usable form.
robots: noindex

# tf.raw_ops.CudnnRNNCanonicalToParams

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Converts CudnnRNN params from canonical form to usable form.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CudnnRNNCanonicalToParams`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CudnnRNNCanonicalToParams(
    num_layers,
    num_units,
    input_size,
    weights,
    biases,
    rnn_mode=&#x27;lstm&#x27;,
    input_mode=&#x27;linear_input&#x27;,
    direction=&#x27;unidirectional&#x27;,
    dropout=0,
    seed=0,
    seed2=0,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Writes a set of weights into the opaque params buffer so they can be used in
upcoming training or inferences.

Note that the params buffer may not be compatible across different GPUs. So any
save and restoration should be converted to and from the canonical weights and
biases.

num_layers: Specifies the number of layers in the RNN model.
num_units: Specifies the size of the hidden state.
input_size: Specifies the size of the input state.
weights: the canonical form of weights that can be used for saving
    and restoration. They are more likely to be compatible across different
    generations.
biases: the canonical form of biases that can be used for saving
    and restoration. They are more likely to be compatible across different
    generations.
num_params: number of parameter sets for all layers.
    Each layer may contain multiple parameter sets, with each set consisting of
    a weight matrix and a bias vector.
rnn_mode: Indicates the type of the RNN model.
input_mode: Indicate whether there is a linear projection between the input and
    The actual computation before the first layer. 'skip_input' is only allowed
    when input_size == num_units; 'auto_select' implies 'skip_input' when
    input_size == num_units; otherwise, it implies 'linear_input'.
direction: Indicates whether a bidirectional model will be used.
    dir = (direction == bidirectional) ? 2 : 1
dropout: dropout probability. When set to 0., dropout is disabled.
seed: the 1st part of a seed to initialize dropout.
seed2: the 2nd part of a seed to initialize dropout.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_layers`<a id="num_layers"></a>
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`num_units`<a id="num_units"></a>
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`input_size`<a id="input_size"></a>
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`weights`<a id="weights"></a>
</td>
<td>
A list of at least 1 `Tensor` objects with the same type in: `bfloat16`, `half`, `float32`, `float64`.
</td>
</tr><tr>
<td>
`biases`<a id="biases"></a>
</td>
<td>
A list with the same length as `weights` of `Tensor` objects with the same type as `weights`.
</td>
</tr><tr>
<td>
`rnn_mode`<a id="rnn_mode"></a>
</td>
<td>
An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
</td>
</tr><tr>
<td>
`input_mode`<a id="input_mode"></a>
</td>
<td>
An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
</td>
</tr><tr>
<td>
`direction`<a id="direction"></a>
</td>
<td>
An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
</td>
</tr><tr>
<td>
`dropout`<a id="dropout"></a>
</td>
<td>
An optional `float`. Defaults to `0`.
</td>
</tr><tr>
<td>
`seed`<a id="seed"></a>
</td>
<td>
An optional `int`. Defaults to `0`.
</td>
</tr><tr>
<td>
`seed2`<a id="seed2"></a>
</td>
<td>
An optional `int`. Defaults to `0`.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `weights`.
</td>
</tr>

</table>

