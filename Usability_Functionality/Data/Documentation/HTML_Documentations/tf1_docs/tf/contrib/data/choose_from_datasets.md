<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.data.choose_from_datasets" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.data.choose_from_datasets

Creates a dataset that deterministically chooses elements from `datasets`. (deprecated)

``` python
tf.contrib.data.choose_from_datasets(
    datasets,
    choice_dataset
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/experimental/choose_from_datasets.md"><code>tf.data.experimental.choose_from_datasets(...)</code></a>.

For example, given the following datasets:

```python
datasets = [tf.data.Dataset.from_tensors("foo").repeat(),
            tf.data.Dataset.from_tensors("bar").repeat(),
            tf.data.Dataset.from_tensors("baz").repeat()]

# Define a dataset containing `[0, 1, 2, 0, 1, 2, 0, 1, 2]`.
choice_dataset = tf.data.Dataset.range(3).repeat(3)

result = tf.data.experimental.choose_from_datasets(datasets, choice_dataset)
```

The elements of `result` will be:

```
"foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz"
```

#### Args:


* <b>`datasets`</b>: A list of <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> objects with compatible structure.
* <b>`choice_dataset`</b>: A <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> of scalar <a href="../../../tf.md#int64"><code>tf.int64</code></a> tensors between
  `0` and `len(datasets) - 1`.


#### Returns:

A dataset that interleaves elements from `datasets` according to the values
of `choice_dataset`.



#### Raises:


* <b>`TypeError`</b>: If the `datasets` or `choice_dataset` arguments have the wrong
  type.