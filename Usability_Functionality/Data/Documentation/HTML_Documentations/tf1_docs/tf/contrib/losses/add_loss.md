<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.losses.add_loss" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.losses.add_loss

Adds a externally defined loss to the collection of losses. (deprecated)

``` python
tf.contrib.losses.add_loss(
    loss,
    loss_collection=tf.GraphKeys.LOSSES
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-12-30.
Instructions for updating:
Use tf.losses.add_loss instead.

#### Args:


* <b>`loss`</b>: A loss `Tensor`.
* <b>`loss_collection`</b>: Optional collection to add the loss to.