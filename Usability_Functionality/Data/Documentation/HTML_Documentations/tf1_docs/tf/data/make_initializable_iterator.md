<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.make_initializable_iterator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.make_initializable_iterator

Creates a <a href="../../tf/data/Iterator.md"><code>tf.compat.v1.data.Iterator</code></a> for enumerating the elements of a dataset.

### Aliases:

* `tf.compat.v1.data.make_initializable_iterator`
* `tf.compat.v2.compat.v1.data.make_initializable_iterator`
* `tf.data.make_initializable_iterator`

``` python
tf.data.make_initializable_iterator(
    dataset,
    shared_name=None
)
```

<!-- Placeholder for "Used in" -->

Note: The returned iterator will be in an uninitialized state,
and you must run the `iterator.initializer` operation before using it:

```python
dataset = ...
iterator = tf.compat.v1.data.make_initializable_iterator(dataset)
# ...
sess.run(iterator.initializer)
```

#### Args:


* <b>`dataset`</b>: A <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.
* <b>`shared_name`</b>: (Optional.) If non-empty, the returned iterator will be shared
  under the given name across multiple sessions that share the same devices
  (e.g. when using a remote server).


#### Returns:

A <a href="../../tf/data/Iterator.md"><code>tf.compat.v1.data.Iterator</code></a> over the elements of `dataset`.



#### Raises:


* <b>`RuntimeError`</b>: If eager execution is enabled.