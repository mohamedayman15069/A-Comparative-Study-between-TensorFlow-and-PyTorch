<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.debugging.assert_all_finite" />
<meta itemprop="path" content="Stable" />
</div>

# tf.debugging.assert_all_finite

Assert that the tensor does not contain any NaN's or Inf's.

### Aliases:

* `tf.compat.v1.debugging.assert_all_finite`
* `tf.compat.v1.verify_tensor_all_finite`
* `tf.compat.v2.compat.v1.debugging.assert_all_finite`
* `tf.compat.v2.compat.v1.verify_tensor_all_finite`
* `tf.debugging.assert_all_finite`
* `tf.verify_tensor_all_finite`

``` python
tf.debugging.assert_all_finite(
    t=None,
    msg=None,
    name=None,
    x=None,
    message=None
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`t`</b>: Tensor to check.
* <b>`msg`</b>: Message to log on failure.
* <b>`name`</b>: A name for this operation (optional).
* <b>`x`</b>: Alias for t.
* <b>`message`</b>: Alias for msg.


#### Returns:

Same tensor as `t`.
