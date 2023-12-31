<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.layers.SeparableConv2D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="graph"/>
<meta itemprop="property" content="scope_name"/>
<meta itemprop="property" content="__init__"/>
</div>

# tf.layers.SeparableConv2D

## Class `SeparableConv2D`

Depthwise separable 2D convolution.

Inherits From: [`SeparableConv2D`](../../tf/keras/layers/SeparableConv2D.md), [`Layer`](../../tf/layers/Layer.md)

### Aliases:

* Class `tf.compat.v1.layers.SeparableConv2D`
* Class `tf.compat.v2.compat.v1.layers.SeparableConv2D`
* Class `tf.layers.SeparableConv2D`

<!-- Placeholder for "Used in" -->

This layer performs a depthwise convolution that acts separately on
channels, followed by a pointwise convolution that mixes channels.
If `use_bias` is True and a bias initializer is provided,
it adds a bias vector to the output.
It then optionally applies an activation function to produce the final output.

#### Arguments:


* <b>`filters`</b>: Integer, the dimensionality of the output space (i.e. the number
  of filters in the convolution).
* <b>`kernel_size`</b>: A tuple or list of 2 integers specifying the spatial
  dimensions of the filters. Can be a single integer to specify the same
  value for all spatial dimensions.
* <b>`strides`</b>: A tuple or list of 2 positive integers specifying the strides
  of the convolution. Can be a single integer to specify the same value for
  all spatial dimensions.
  Specifying any `stride` value != 1 is incompatible with specifying
  any `dilation_rate` value != 1.
* <b>`padding`</b>: One of `"valid"` or `"same"` (case-insensitive).
* <b>`data_format`</b>: A string, one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, height, width, channels)` while `channels_first` corresponds to
  inputs with shape `(batch, channels, height, width)`.

* <b>`dilation_rate`</b>: An integer or tuple/list of 2 integers, specifying
  the dilation rate to use for dilated convolution.
  Can be a single integer to specify the same value for
  all spatial dimensions.
  Currently, specifying any `dilation_rate` value != 1 is
  incompatible with specifying any stride value != 1.
* <b>`depth_multiplier`</b>: The number of depthwise convolution output channels for
  each input channel. The total number of depthwise convolution output
  channels will be equal to `num_filters_in * depth_multiplier`.
* <b>`activation`</b>: Activation function. Set it to None to maintain a
  linear activation.
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias.
* <b>`depthwise_initializer`</b>: An initializer for the depthwise convolution kernel.
* <b>`pointwise_initializer`</b>: An initializer for the pointwise convolution kernel.
* <b>`bias_initializer`</b>: An initializer for the bias vector. If None, the default
  initializer will be used.
* <b>`depthwise_regularizer`</b>: Optional regularizer for the depthwise
  convolution kernel.
* <b>`pointwise_regularizer`</b>: Optional regularizer for the pointwise
  convolution kernel.
* <b>`bias_regularizer`</b>: Optional regularizer for the bias vector.
* <b>`activity_regularizer`</b>: Optional regularizer function for the output.
* <b>`depthwise_constraint`</b>: Optional projection function to be applied to the
    depthwise kernel after being updated by an `Optimizer` (e.g. used for
    norm constraints or value constraints for layer weights). The function
    must take as input the unprojected variable and must return the
    projected variable (which must have the same shape). Constraints are
    not safe to use when doing asynchronous distributed training.
* <b>`pointwise_constraint`</b>: Optional projection function to be applied to the
    pointwise kernel after being updated by an `Optimizer`.
* <b>`bias_constraint`</b>: Optional projection function to be applied to the
    bias after being updated by an `Optimizer`.
* <b>`trainable`</b>: Boolean, if `True` also add variables to the graph collection
  <a href="../../tf/GraphKeys.md#TRAINABLE_VARIABLES"><code>GraphKeys.TRAINABLE_VARIABLES</code></a> (see <a href="../../tf/Variable.md"><code>tf.Variable</code></a>).
* <b>`name`</b>: A string, the name of the layer.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    filters,
    kernel_size,
    strides=(1, 1),
    padding='valid',
    data_format='channels_last',
    dilation_rate=(1, 1),
    depth_multiplier=1,
    activation=None,
    use_bias=True,
    depthwise_initializer=None,
    pointwise_initializer=None,
    bias_initializer=tf.zeros_initializer(),
    depthwise_regularizer=None,
    pointwise_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    depthwise_constraint=None,
    pointwise_constraint=None,
    bias_constraint=None,
    trainable=True,
    name=None,
    **kwargs
)
```






## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="scope_name"><code>scope_name</code></h3>






