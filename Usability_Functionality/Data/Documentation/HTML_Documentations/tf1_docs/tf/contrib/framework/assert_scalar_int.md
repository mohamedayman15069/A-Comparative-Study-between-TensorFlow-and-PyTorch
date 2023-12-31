<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.framework.assert_scalar_int" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.framework.assert_scalar_int

Assert `tensor` is 0-D, of type <a href="../../../tf.md#int32"><code>tf.int32</code></a> or <a href="../../../tf.md#int64"><code>tf.int64</code></a>.

``` python
tf.contrib.framework.assert_scalar_int(
    tensor,
    name=None
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`tensor`</b>: `Tensor` to test.
* <b>`name`</b>: Name of the op and of the new `Tensor` if one is created.

#### Returns:

`tensor`, for chaining.


#### Raises:


* <b>`ValueError`</b>: if `tensor` is not 0-D, of integer type.