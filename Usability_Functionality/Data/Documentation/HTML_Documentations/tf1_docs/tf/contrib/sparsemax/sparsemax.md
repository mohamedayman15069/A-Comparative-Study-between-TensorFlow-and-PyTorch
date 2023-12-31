<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.sparsemax.sparsemax" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.sparsemax.sparsemax

Computes sparsemax activations [1].

``` python
tf.contrib.sparsemax.sparsemax(
    logits,
    name=None
)
```

<!-- Placeholder for "Used in" -->

For each batch `i` and class `j` we have
  $$sparsemax[i, j] = max(logits[i, j] - tau(logits[i, :]), 0)$$

[1]: https://arxiv.org/abs/1602.02068

#### Args:


* <b>`logits`</b>: A `Tensor`. Must be one of the following types: `half`, `float32`,
  `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `logits`.
