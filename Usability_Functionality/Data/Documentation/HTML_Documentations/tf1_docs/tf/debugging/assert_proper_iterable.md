<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.debugging.assert_proper_iterable" />
<meta itemprop="path" content="Stable" />
</div>

# tf.debugging.assert_proper_iterable

Static assert that values is a "proper" iterable.

### Aliases:

* `tf.assert_proper_iterable`
* `tf.compat.v1.assert_proper_iterable`
* `tf.compat.v1.debugging.assert_proper_iterable`
* `tf.compat.v2.compat.v1.assert_proper_iterable`
* `tf.compat.v2.compat.v1.debugging.assert_proper_iterable`
* `tf.compat.v2.debugging.assert_proper_iterable`
* `tf.debugging.assert_proper_iterable`

``` python
tf.debugging.assert_proper_iterable(values)
```

<!-- Placeholder for "Used in" -->

`Ops` that expect iterables of `Tensor` can call this to validate input.
Useful since `Tensor`, `ndarray`, byte/text type are all iterables themselves.

#### Args:


* <b>`values`</b>:  Object to be checked.


#### Raises:


* <b>`TypeError`</b>:  If `values` is not iterable or is one of
  `Tensor`, `SparseTensor`, `np.array`, <a href="../../tf/compat.md#bytes_or_text_types"><code>tf.compat.bytes_or_text_types</code></a>.