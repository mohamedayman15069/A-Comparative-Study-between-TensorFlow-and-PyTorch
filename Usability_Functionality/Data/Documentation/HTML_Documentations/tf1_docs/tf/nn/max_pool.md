<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.max_pool" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.max_pool

Performs the max pooling on the input.

### Aliases:

* `tf.compat.v1.nn.max_pool`
* `tf.compat.v2.compat.v1.nn.max_pool`
* `tf.nn.max_pool`

``` python
tf.nn.max_pool(
    value,
    ksize,
    strides,
    padding,
    data_format='NHWC',
    name=None,
    input=None
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`value`</b>: A 4-D `Tensor` of the format specified by `data_format`.
* <b>`ksize`</b>: An int or list of `ints` that has length `1`, `2` or `4`.
  The size of the window for each dimension of the input tensor.
* <b>`strides`</b>: An int or list of `ints` that has length `1`, `2` or `4`.
  The stride of the sliding window for each dimension of the input tensor.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm.
  See the "returns" section of <a href="../../tf/nn/convolution.md"><code>tf.nn.convolution</code></a> for details.
* <b>`data_format`</b>: A string. 'NHWC', 'NCHW' and 'NCHW_VECT_C' are supported.
* <b>`name`</b>: Optional name for the operation.
* <b>`input`</b>: Alias for value.


#### Returns:

A `Tensor` of format specified by `data_format`.
The max pooled output tensor.
