<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.debugging.assert_integer" />
<meta itemprop="path" content="Stable" />
</div>

# tf.debugging.assert_integer

Assert that `x` is of integer dtype.

### Aliases:

* `tf.assert_integer`
* `tf.compat.v1.assert_integer`
* `tf.compat.v1.debugging.assert_integer`
* `tf.compat.v2.compat.v1.assert_integer`
* `tf.compat.v2.compat.v1.debugging.assert_integer`
* `tf.debugging.assert_integer`

``` python
tf.debugging.assert_integer(
    x,
    message=None,
    name=None
)
```

<!-- Placeholder for "Used in" -->

Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.compat.v1.assert_integer(x)]):
  output = tf.reduce_sum(x)
```

#### Args:


* <b>`x`</b>: `Tensor` whose basetype is integer and is not quantized.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>: A name for this operation (optional).  Defaults to "assert_integer".


#### Raises:


* <b>`TypeError`</b>:  If `x.dtype` is anything other than non-quantized integer.


#### Returns:

A `no_op` that does nothing.  Type can be determined statically.
