<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.equal" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.equal

Returns the truth value of (x == y) element-wise.

### Aliases:

* `tf.compat.v1.equal`
* `tf.compat.v1.math.equal`
* `tf.compat.v2.compat.v1.equal`
* `tf.compat.v2.compat.v1.math.equal`
* `tf.compat.v2.equal`
* `tf.compat.v2.math.equal`
* `tf.equal`
* `tf.math.equal`

``` python
tf.math.equal(
    x,
    y,
    name=None
)
```

<!-- Placeholder for "Used in" -->


#### Usage:



```python
x = tf.constant([2, 4])
y = tf.constant(2)
tf.math.equal(x, y) ==> array([True, False])

x = tf.constant([2, 4])
y = tf.constant([2, 4])
tf.math.equal(x, y) ==> array([True,  True])
```

**NOTE**: `Equal` supports broadcasting. More about broadcasting [here](
https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices`.
* <b>`y`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type bool with the same size as that of x or y.
