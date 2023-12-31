<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.get_structure" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.get_structure

Returns the type specification of an element of a `Dataset` or `Iterator`.

### Aliases:

* `tf.compat.v1.data.experimental.get_structure`
* `tf.compat.v2.compat.v1.data.experimental.get_structure`
* `tf.compat.v2.data.experimental.get_structure`
* `tf.data.experimental.get_structure`

``` python
tf.data.experimental.get_structure(dataset_or_iterator)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`dataset_or_iterator`</b>: A <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> or <a href="../../../tf/data/Iterator.md"><code>tf.data.Iterator</code></a>.


#### Returns:

A nested structure of <a href="../../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> objects matching the structure of an
element of `dataset_or_iterator` and spacifying the type of individal
components.



#### Raises:


* <b>`TypeError`</b>: If `dataset_or_iterator` is not a `Dataset` or `Iterator` object.