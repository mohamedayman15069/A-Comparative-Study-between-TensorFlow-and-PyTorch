<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.losses.sparse_softmax_cross_entropy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.losses.sparse_softmax_cross_entropy

Cross-entropy loss using <a href="../../../tf/nn/sparse_softmax_cross_entropy_with_logits.md"><code>tf.nn.sparse_softmax_cross_entropy_with_logits</code></a>. (deprecated)

``` python
tf.contrib.losses.sparse_softmax_cross_entropy(
    logits,
    labels,
    weights=1.0,
    scope=None
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-12-30.
Instructions for updating:
Use tf.losses.sparse_softmax_cross_entropy instead. Note that the order of the logits and labels arguments has been changed.

`weights` acts as a coefficient for the loss. If a scalar is provided,
then the loss is simply scaled by the given value. If `weights` is a
tensor of size [`batch_size`], then the loss weights apply to each
corresponding sample.

#### Args:


* <b>`logits`</b>: [batch_size, num_classes] logits outputs of the network .
* <b>`labels`</b>: [batch_size, 1] or [batch_size] labels of dtype `int32` or `int64`
  in the range `[0, num_classes)`.
* <b>`weights`</b>: Coefficients for the loss. The tensor must be a scalar or a tensor
  of shape [batch_size] or [batch_size, 1].
* <b>`scope`</b>: the scope for the operations performed in computing the loss.


#### Returns:

A scalar `Tensor` representing the mean loss value.



#### Raises:


* <b>`ValueError`</b>: If the shapes of `logits`, `labels`, and `weights` are
  incompatible, or if `weights` is None.