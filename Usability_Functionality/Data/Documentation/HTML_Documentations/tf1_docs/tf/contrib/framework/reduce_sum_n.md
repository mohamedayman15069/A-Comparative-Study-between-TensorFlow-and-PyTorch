<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.framework.reduce_sum_n" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.framework.reduce_sum_n

Reduce tensors to a scalar sum.

``` python
tf.contrib.framework.reduce_sum_n(
    tensors,
    name=None
)
```

<!-- Placeholder for "Used in" -->

This reduces each tensor in `tensors` to a scalar via <a href="../../../tf/math/reduce_sum.md"><code>tf.reduce_sum</code></a>, then
adds them via <a href="../../../tf/math/add_n.md"><code>tf.add_n</code></a>.

#### Args:


* <b>`tensors`</b>: List of tensors, all of the same numeric type.
* <b>`name`</b>: Tensor name, and scope for all other ops.


#### Returns:

Total loss tensor, or None if no losses have been configured.



#### Raises:


* <b>`ValueError`</b>: if `losses` is missing or empty.