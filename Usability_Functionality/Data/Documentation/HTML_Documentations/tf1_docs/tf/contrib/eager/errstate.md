<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.eager.errstate" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.eager.errstate

Context manager setting error state.

``` python
tf.contrib.eager.errstate(
    *args,
    **kwds
)
```

<!-- Placeholder for "Used in" -->


#### Example:


```
c = tf.math.log(0.)  # -inf

with errstate(inf_or_nan=ExecutionCallback.RAISE):
  tf.math.log(0.)  # <-- Raises InfOrNanError.
```

#### Args:


* <b>`inf_or_nan`</b>: An `ExecutionCallback` determining the action for infinity
  (`inf`) and NaN (`nan`) values. A value of `None` leads to no change in
  the action of the condition.


#### Yields:

None.



#### Raises:


* <b>`ValueError`</b>: If the value of any keyword arguments is invalid.