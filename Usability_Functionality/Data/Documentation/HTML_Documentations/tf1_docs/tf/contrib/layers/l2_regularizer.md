<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.layers.l2_regularizer" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.layers.l2_regularizer

Returns a function that can be used to apply L2 regularization to weights.

``` python
tf.contrib.layers.l2_regularizer(
    scale,
    scope=None
)
```

<!-- Placeholder for "Used in" -->

Small values of L2 can help prevent overfitting the training data.

#### Args:


* <b>`scale`</b>: A scalar multiplier `Tensor`. 0.0 disables the regularizer.
* <b>`scope`</b>: An optional scope name.


#### Returns:

A function with signature `l2(weights)` that applies L2 regularization.



#### Raises:


* <b>`ValueError`</b>: If scale is negative or if scale is not a float.