<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.debugging.assert_non_negative" />
<meta itemprop="path" content="Stable" />
</div>

# tf.debugging.assert_non_negative

Assert the condition `x >= 0` holds element-wise.

### Aliases:

* `tf.assert_non_negative`
* `tf.compat.v1.assert_non_negative`
* `tf.compat.v1.debugging.assert_non_negative`
* `tf.compat.v2.compat.v1.assert_non_negative`
* `tf.compat.v2.compat.v1.debugging.assert_non_negative`
* `tf.debugging.assert_non_negative`

``` python
tf.debugging.assert_non_negative(
    x,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```

<!-- Placeholder for "Used in" -->

When running in graph mode, you should add a dependency on this operation
to ensure that it runs. Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.debugging.assert_non_negative(x, y)]):
  output = tf.reduce_sum(x)
```

Non-negative means, for every element `x[i]` of `x`, we have `x[i] >= 0`.
If `x` is empty this is trivially satisfied.

#### Args:


* <b>`x`</b>:  Numeric `Tensor`.
* <b>`data`</b>:  The tensors to print out if the condition is False.  Defaults to
  error message and first few entries of `x`.
* <b>`summarize`</b>: Print this many entries of each tensor.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>: A name for this operation (optional).  Defaults to "assert_non_negative".


#### Returns:

Op that raises `InvalidArgumentError` if `x >= 0` is False.




#### Raises:


* <b>`InvalidArgumentError`</b>: if the check can be performed immediately and
  `x >= 0` is False. The check can be performed immediately during 
  eager execution or if `x` is statically known.

#### Eager Compatibility
returns None

