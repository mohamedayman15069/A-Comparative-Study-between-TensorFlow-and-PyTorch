<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.model_pruning.MaskedBasicLSTMCell" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="graph"/>
<meta itemprop="property" content="output_size"/>
<meta itemprop="property" content="scope_name"/>
<meta itemprop="property" content="state_size"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_initial_state"/>
<meta itemprop="property" content="zero_state"/>
</div>

# tf.contrib.model_pruning.MaskedBasicLSTMCell

## Class `MaskedBasicLSTMCell`

Basic LSTM recurrent network cell with pruning.

Inherits From: [`BasicLSTMCell`](../../../tf/nn/rnn_cell/BasicLSTMCell.md)

<!-- Placeholder for "Used in" -->

Overrides the call method of tensorflow BasicLSTMCell and injects the weight
masks

The implementation is based on: http://arxiv.org/abs/1409.2329.

We add forget_bias (default: 1) to the biases of the forget gate in order to
reduce the scale of forgetting in the beginning of the training.

It does not allow cell clipping, a projection layer, and does not
use peep-hole connections: it is the basic baseline.

For advanced models, please use the full <a href="../../../tf/nn/rnn_cell/LSTMCell.md"><code>tf.compat.v1.nn.rnn_cell.LSTMCell</code></a>
that follows.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    forget_bias=1.0,
    state_is_tuple=True,
    activation=None,
    reuse=None,
    name=None
)
```

Initialize the basic LSTM cell with pruning.


#### Args:


* <b>`num_units`</b>: int, The number of units in the LSTM cell.
* <b>`forget_bias`</b>: float, The bias added to forget gates (see above).
  Must set to `0.0` manually when restoring from CudnnLSTM-trained
  checkpoints.
* <b>`state_is_tuple`</b>: If True, accepted and returned states are 2-tuples of
  the `c_state` and `m_state`.  If False, they are concatenated
  along the column axis.  The latter behavior will soon be deprecated.
* <b>`activation`</b>: Activation function of the inner states.  Default: `tanh`.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
  in an existing scope.  If not `True`, and the existing scope already has
  the given variables, an error is raised.
* <b>`name`</b>: String, the name of the layer. Layers with the same name will
  share weights, but to avoid mistakes we require reuse=True in such
  cases.

When restoring from CudnnLSTM-trained checkpoints, must use
CudnnCompatibleLSTMCell instead.



## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="output_size"><code>output_size</code></h3>

Integer or TensorShape: size of outputs produced by this cell.


<h3 id="scope_name"><code>scope_name</code></h3>




<h3 id="state_size"><code>state_size</code></h3>

size(s) of state(s) used by this cell.

It can be represented by an Integer, a TensorShape or a tuple of Integers
or TensorShapes.



## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```




<h3 id="zero_state"><code>zero_state</code></h3>

``` python
zero_state(
    batch_size,
    dtype
)
```

Return zero-filled state tensor(s).


#### Args:


* <b>`batch_size`</b>: int, float, or unit Tensor representing the batch size.
* <b>`dtype`</b>: the data type to use for the state.


#### Returns:

If `state_size` is an int or TensorShape, then the return value is a
`N-D` tensor of shape `[batch_size, state_size]` filled with zeros.

If `state_size` is a nested list or tuple, then the return value is
a nested list or tuple (of the same structure) of `2-D` tensors with
the shapes `[batch_size, s]` for each s in `state_size`.




