<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.xw_plus_b" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.xw_plus_b

Computes matmul(x, weights) + biases.

### Aliases:

* `tf.compat.v1.nn.xw_plus_b`
* `tf.compat.v2.compat.v1.nn.xw_plus_b`
* `tf.nn.xw_plus_b`

``` python
tf.nn.xw_plus_b(
    x,
    weights,
    biases,
    name=None
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: a 2D tensor.  Dimensions typically: batch, in_units
* <b>`weights`</b>: a 2D tensor.  Dimensions typically: in_units, out_units
* <b>`biases`</b>: a 1D tensor.  Dimensions: out_units
* <b>`name`</b>: A name for the operation (optional).  If not specified
  "xw_plus_b" is used.


#### Returns:

A 2-D Tensor computing matmul(x, weights) + biases.
Dimensions typically: batch, out_units.
