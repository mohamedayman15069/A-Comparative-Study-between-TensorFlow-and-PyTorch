<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.layers.spatial_softmax" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.layers.spatial_softmax

Computes the spatial softmax of a convolutional feature map.

``` python
tf.contrib.layers.spatial_softmax(
    features,
    temperature=None,
    name=None,
    variables_collections=None,
    trainable=True,
    data_format='NHWC'
)
```

<!-- Placeholder for "Used in" -->

First computes the softmax over the spatial extent of each channel of a
convolutional feature map. Then computes the expected 2D position of the
points of maximal activation for each channel, resulting in a set of
feature keypoints [i1, j1, ... iN, jN] for all N channels.

#### Read more here:


"Learning visual feature spaces for robotic manipulation with
deep spatial autoencoders." Finn et al., http://arxiv.org/abs/1509.06113.

#### Args:


* <b>`features`</b>: A `Tensor` of size [batch_size, W, H, num_channels]; the
  convolutional feature map.
* <b>`temperature`</b>: Softmax temperature (optional). If None, a learnable
  temperature is created.
* <b>`name`</b>: A name for this operation (optional).
* <b>`variables_collections`</b>: Collections for the temperature variable.
* <b>`trainable`</b>: If `True` also add variables to the graph collection
  `GraphKeys.TRAINABLE_VARIABLES` (see <a href="../../../tf/Variable.md"><code>tf.Variable</code></a>).
* <b>`data_format`</b>: A string. `NHWC` (default) and `NCHW` are supported.


#### Returns:


* <b>`feature_keypoints`</b>: A `Tensor` with size [batch_size, num_channels * 2];
  the expected 2D locations of each channel's feature keypoint (normalized
  to the range (-1,1)). The inner dimension is arranged as
  [i1, j1, ... iN, jN].

#### Raises:


* <b>`ValueError`</b>: If unexpected data_format specified.
* <b>`ValueError`</b>: If num_channels dimension is unspecified.