description: Functional interface for the 3D convolution layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.layers.conv3d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.layers.conv3d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/legacy_tf_layers/convolutional.py#L728-L880">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Functional interface for the 3D convolution layer.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.layers.conv3d(
    inputs,
    filters,
    kernel_size,
    strides=(1, 1, 1),
    padding=&#x27;valid&#x27;,
    data_format=&#x27;channels_last&#x27;,
    dilation_rate=(1, 1, 1),
    activation=None,
    use_bias=True,
    kernel_initializer=None,
    bias_initializer=<a href="../../../../tf/compat/v1/zeros_initializer.md"><code>tf.compat.v1.zeros_initializer()</code></a>,
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    trainable=True,
    name=None,
    reuse=None
)
</code></pre>





 <section><devsite-expandable expanded>
 <h2 class="showalways">Migrate to TF2</h2>

Caution: This API was designed for TensorFlow v1.
Continue reading for details on how to migrate from this API to a native
TensorFlow v2 equivalent. See the
[TensorFlow v1 to TensorFlow v2 migration guide](https://www.tensorflow.org/guide/migrate)
for instructions on how to migrate the rest of your code.

This API is a legacy api that is only compatible with eager execution and
<a href="../../../../tf/function.md"><code>tf.function</code></a> if you combine it with
`tf.compat.v1.keras.utils.track_tf1_style_variables`

Please refer to [tf.layers model mapping section of the migration guide]
(https://www.tensorflow.org/guide/migrate/model_mapping)
to learn how to use your TensorFlow v1 model in TF2 with Keras.

The corresponding TensorFlow v2 layer is <a href="../../../../tf/keras/layers/Conv3D.md"><code>tf.keras.layers.Conv3D</code></a>.


#### Structural Mapping to Native TF2

None of the supported arguments have changed name.

Before:

```python
 y = tf.compat.v1.layers.conv3d(x, filters=3, kernel_size=3)
```

After:

To migrate code using TF1 functional layers use the [Keras Functional API]
(https://www.tensorflow.org/guide/keras/functional):

```python
 x = tf.keras.Input((28, 28, 1))
 y = tf.keras.layers.Conv3D(filters=3, kernels_size=3)(x)
 model = tf.keras.Model(x, y)
```

 </aside></devsite-expandable></section>

<h2>Description</h2>

<!-- Placeholder for "Used in" -->

This layer creates a convolution kernel that is convolved
(actually cross-correlated) with the layer input to produce a tensor of
outputs. If `use_bias` is True (and a `bias_initializer` is provided),
a bias vector is created and added to the outputs. Finally, if
`activation` is not `None`, it is applied to the outputs as well.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`<a id="inputs"></a>
</td>
<td>
Tensor input.
</td>
</tr><tr>
<td>
`filters`<a id="filters"></a>
</td>
<td>
Integer, the dimensionality of the output space (i.e. the number
of filters in the convolution).
</td>
</tr><tr>
<td>
`kernel_size`<a id="kernel_size"></a>
</td>
<td>
An integer or tuple/list of 3 integers, specifying the
depth, height and width of the 3D convolution window.
Can be a single integer to specify the same value for
all spatial dimensions.
</td>
</tr><tr>
<td>
`strides`<a id="strides"></a>
</td>
<td>
An integer or tuple/list of 3 integers,
specifying the strides of the convolution along the depth,
height and width.
Can be a single integer to specify the same value for
all spatial dimensions.
Specifying any stride value != 1 is incompatible with specifying
any `dilation_rate` value != 1.
</td>
</tr><tr>
<td>
`padding`<a id="padding"></a>
</td>
<td>
One of `"valid"` or `"same"` (case-insensitive).
`"valid"` means no padding. `"same"` results in padding evenly to
the left/right or up/down of the input such that output has the same
height/width dimension as the input.
</td>
</tr><tr>
<td>
`data_format`<a id="data_format"></a>
</td>
<td>
A string, one of `channels_last` (default) or
`channels_first`. The ordering of the dimensions in the inputs.
`channels_last` corresponds to inputs with shape
`(batch, depth, height, width, channels)` while `channels_first`
corresponds to inputs with shape
`(batch, channels, depth, height, width)`.
</td>
</tr><tr>
<td>
`dilation_rate`<a id="dilation_rate"></a>
</td>
<td>
An integer or tuple/list of 3 integers, specifying
the dilation rate to use for dilated convolution.
Can be a single integer to specify the same value for
all spatial dimensions.
Currently, specifying any `dilation_rate` value != 1 is
incompatible with specifying any stride value != 1.
</td>
</tr><tr>
<td>
`activation`<a id="activation"></a>
</td>
<td>
Activation function. Set it to None to maintain a
linear activation.
</td>
</tr><tr>
<td>
`use_bias`<a id="use_bias"></a>
</td>
<td>
Boolean, whether the layer uses a bias.
</td>
</tr><tr>
<td>
`kernel_initializer`<a id="kernel_initializer"></a>
</td>
<td>
An initializer for the convolution kernel.
</td>
</tr><tr>
<td>
`bias_initializer`<a id="bias_initializer"></a>
</td>
<td>
An initializer for the bias vector. If None, the default
initializer will be used.
</td>
</tr><tr>
<td>
`kernel_regularizer`<a id="kernel_regularizer"></a>
</td>
<td>
Optional regularizer for the convolution kernel.
</td>
</tr><tr>
<td>
`bias_regularizer`<a id="bias_regularizer"></a>
</td>
<td>
Optional regularizer for the bias vector.
</td>
</tr><tr>
<td>
`activity_regularizer`<a id="activity_regularizer"></a>
</td>
<td>
Optional regularizer function for the output.
</td>
</tr><tr>
<td>
`kernel_constraint`<a id="kernel_constraint"></a>
</td>
<td>
Optional projection function to be applied to the
kernel after being updated by an `Optimizer` (e.g. used to implement
norm constraints or value constraints for layer weights). The function
must take as input the unprojected variable and must return the
projected variable (which must have the same shape). Constraints are
not safe to use when doing asynchronous distributed training.
</td>
</tr><tr>
<td>
`bias_constraint`<a id="bias_constraint"></a>
</td>
<td>
Optional projection function to be applied to the
bias after being updated by an `Optimizer`.
</td>
</tr><tr>
<td>
`trainable`<a id="trainable"></a>
</td>
<td>
Boolean, if `True` also add variables to the graph collection
`GraphKeys.TRAINABLE_VARIABLES` (see <a href="../../../../tf/Variable.md"><code>tf.Variable</code></a>).
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
A string, the name of the layer.
</td>
</tr><tr>
<td>
`reuse`<a id="reuse"></a>
</td>
<td>
Boolean, whether to reuse the weights of a previous layer
by the same name.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Output tensor.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
if eager execution is enabled.
</td>
</tr>
</table>

