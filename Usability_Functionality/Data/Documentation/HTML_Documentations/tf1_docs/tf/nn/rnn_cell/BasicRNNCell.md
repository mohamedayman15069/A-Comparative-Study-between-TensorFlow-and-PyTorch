<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.rnn_cell.BasicRNNCell" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="graph"/>
<meta itemprop="property" content="output_size"/>
<meta itemprop="property" content="scope_name"/>
<meta itemprop="property" content="state_size"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_initial_state"/>
<meta itemprop="property" content="zero_state"/>
</div>

# tf.nn.rnn_cell.BasicRNNCell

## Class `BasicRNNCell`

The most basic RNN cell.

Inherits From: [`LayerRNNCell`](../../../tf/contrib/rnn/LayerRNNCell.md)

### Aliases:

* Class `tf.compat.v1.nn.rnn_cell.BasicRNNCell`
* Class `tf.compat.v2.compat.v1.nn.rnn_cell.BasicRNNCell`
* Class `tf.contrib.rnn.BasicRNNCell`
* Class `tf.nn.rnn_cell.BasicRNNCell`

<!-- Placeholder for "Used in" -->

Note that this cell is not optimized for performance. Please use
<a href="../../../tf/contrib/cudnn_rnn/CudnnRNNTanh.md"><code>tf.contrib.cudnn_rnn.CudnnRNNTanh</code></a> for better performance on GPU.

#### Args:


* <b>`num_units`</b>: int, The number of units in the RNN cell.
* <b>`activation`</b>: Nonlinearity to use.  Default: `tanh`. It could also be string
  that is within Keras activation function names.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables in an
  existing scope.  If not `True`, and the existing scope already has the
  given variables, an error is raised.
* <b>`name`</b>: String, the name of the layer. Layers with the same name will share
  weights, but to avoid mistakes we require reuse=True in such cases.
* <b>`dtype`</b>: Default dtype of the layer (default of `None` means use the type of
  the first input). Required when `build` is called before `call`.
* <b>`**kwargs`</b>: Dict, keyword named properties for common layer attributes, like
  `trainable` etc when constructing the cell from configs of get_config().

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    activation=None,
    reuse=None,
    name=None,
    dtype=None,
    **kwargs
)
```

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This class is equivalent as tf.keras.layers.SimpleRNNCell, and will be replaced by that in Tensorflow 2.0.



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




