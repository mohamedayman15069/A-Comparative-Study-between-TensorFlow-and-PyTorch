<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v2.debugging.assert_none_equal" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v2.debugging.assert_none_equal

Assert the condition `x != y` holds for all elements.

``` python
tf.compat.v2.debugging.assert_none_equal(
    x,
    y,
    summarize=None,
    message=None,
    name=None
)
```

<!-- Placeholder for "Used in" -->

This Op checks that `x[i] != y[i]` holds for every pair of (possibly
broadcast) elements of `x` and `y`. If both `x` and `y` are empty, this is
trivially satisfied.

If any elements of `x` and `y` are equal, `message`, as well as the first
`summarize` entries of `x` and `y` are printed, and `InvalidArgumentError`
is raised.

#### Args:


* <b>`x`</b>:  Numeric `Tensor`.
* <b>`y`</b>:  Numeric `Tensor`, same dtype as and broadcastable to `x`.
* <b>`summarize`</b>: Print this many entries of each tensor.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>: A name for this operation (optional).  Defaults to
"assert_none_equal".


#### Returns:

Op that raises `InvalidArgumentError` if `x != y` is ever False. This can
  be used with <a href="../../../../tf/control_dependencies.md"><code>tf.control_dependencies</code></a> inside of <a href="../../../../tf/function.md"><code>tf.function</code></a>s to block
  followup computation until the check has executed.




#### Raises:


* <b>`InvalidArgumentError`</b>: if the check can be performed immediately and
  `x != y` is False for any pair of elements in `x` and `y`. The check can
  be performed immediately during eager execution or if `x` and `y` are
  statically known.

#### Eager Compatibility
returns None

