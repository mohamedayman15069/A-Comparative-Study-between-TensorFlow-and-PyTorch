<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.rnn_cell.LSTMStateTuple" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="c"/>
<meta itemprop="property" content="h"/>
<meta itemprop="property" content="dtype"/>
</div>

# tf.nn.rnn_cell.LSTMStateTuple

## Class `LSTMStateTuple`

Tuple used by LSTM Cells for `state_size`, `zero_state`, and output state.



### Aliases:

* Class `tf.compat.v1.nn.rnn_cell.LSTMStateTuple`
* Class `tf.compat.v2.compat.v1.nn.rnn_cell.LSTMStateTuple`
* Class `tf.contrib.rnn.LSTMStateTuple`
* Class `tf.nn.rnn_cell.LSTMStateTuple`

<!-- Placeholder for "Used in" -->

Stores two elements: `(c, h)`, in that order. Where `c` is the hidden state
and `h` is the output.

Only used when `state_is_tuple=True`.

## Properties

<h3 id="c"><code>c</code></h3>




<h3 id="h"><code>h</code></h3>




<h3 id="dtype"><code>dtype</code></h3>






