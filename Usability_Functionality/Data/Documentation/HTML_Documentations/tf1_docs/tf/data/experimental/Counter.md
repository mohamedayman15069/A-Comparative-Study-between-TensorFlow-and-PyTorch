<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.Counter" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.Counter

Creates a `Dataset` that counts from `start` in steps of size `step`.

### Aliases:

* `tf.compat.v1.data.experimental.Counter`
* `tf.compat.v2.compat.v1.data.experimental.Counter`
* `tf.data.experimental.Counter`

``` python
tf.data.experimental.Counter(
    start=0,
    step=1,
    dtype=tf.dtypes.int64
)
```

<!-- Placeholder for "Used in" -->


#### For example:



```python
Dataset.count() == [0, 1, 2, ...)
Dataset.count(2) == [2, 3, ...)
Dataset.count(2, 5) == [2, 7, 12, ...)
Dataset.count(0, -1) == [0, -1, -2, ...)
Dataset.count(10, -1) == [10, 9, ...)
```

#### Args:


* <b>`start`</b>: (Optional.) The starting value for the counter. Defaults to 0.
* <b>`step`</b>: (Optional.) The step size for the counter. Defaults to 1.
* <b>`dtype`</b>: (Optional.) The data type for counter elements. Defaults to
  <a href="../../../tf.md#int64"><code>tf.int64</code></a>.


#### Returns:

A `Dataset` of scalar `dtype` elements.
