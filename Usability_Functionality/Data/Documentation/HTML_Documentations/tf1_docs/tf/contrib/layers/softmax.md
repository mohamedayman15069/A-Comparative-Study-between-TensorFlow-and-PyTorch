<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.layers.softmax" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.layers.softmax

Performs softmax on Nth dimension of N-dimensional logit tensor.

``` python
tf.contrib.layers.softmax(
    logits,
    scope=None
)
```

<!-- Placeholder for "Used in" -->

For two-dimensional logits this reduces to tf.nn.softmax. The N-th dimension
needs to have a specified number of elements (number of classes).

#### Args:


* <b>`logits`</b>: N-dimensional `Tensor` with logits, where N > 1.
* <b>`scope`</b>: Optional scope for variable_scope.


#### Returns:

A `Tensor` with same shape and type as logits.
