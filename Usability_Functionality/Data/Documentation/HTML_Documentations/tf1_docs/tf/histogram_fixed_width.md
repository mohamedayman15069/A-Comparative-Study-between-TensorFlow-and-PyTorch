<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.histogram_fixed_width" />
<meta itemprop="path" content="Stable" />
</div>

# tf.histogram_fixed_width

Return histogram of values.

### Aliases:

* `tf.compat.v1.histogram_fixed_width`
* `tf.compat.v2.compat.v1.histogram_fixed_width`
* `tf.compat.v2.histogram_fixed_width`
* `tf.histogram_fixed_width`

``` python
tf.histogram_fixed_width(
    values,
    value_range,
    nbins=100,
    dtype=tf.dtypes.int32,
    name=None
)
```

<!-- Placeholder for "Used in" -->

Given the tensor `values`, this operation returns a rank 1 histogram counting
the number of entries in `values` that fell into every bin.  The bins are
equal width and determined by the arguments `value_range` and `nbins`.

#### Args:


* <b>`values`</b>:  Numeric `Tensor`.
* <b>`value_range`</b>:  Shape [2] `Tensor` of same `dtype` as `values`.
  values <= value_range[0] will be mapped to hist[0],
  values >= value_range[1] will be mapped to hist[-1].
* <b>`nbins`</b>:  Scalar `int32 Tensor`.  Number of histogram bins.
* <b>`dtype`</b>:  dtype for returned histogram.
* <b>`name`</b>:  A name for this operation (defaults to 'histogram_fixed_width').


#### Returns:

A 1-D `Tensor` holding histogram of values.



#### Raises:


* <b>`TypeError`</b>: If any unsupported dtype is provided.
* <b>`tf.errors.InvalidArgumentError`</b>: If value_range does not
    satisfy value_range[0] < value_range[1].


#### Examples:



```python
# Bins will be:  (-inf, 1), [1, 2), [2, 3), [3, 4), [4, inf)
nbins = 5
value_range = [0.0, 5.0]
new_values = [-1.0, 0.0, 1.5, 2.0, 5.0, 15]

with tf.compat.v1.get_default_session() as sess:
  hist = tf.histogram_fixed_width(new_values, value_range, nbins=5)
  variables.global_variables_initializer().run()
  sess.run(hist) => [2, 1, 1, 0, 2]
```