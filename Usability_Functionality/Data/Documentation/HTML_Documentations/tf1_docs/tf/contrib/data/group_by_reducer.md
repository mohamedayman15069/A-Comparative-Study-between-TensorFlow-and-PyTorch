<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.data.group_by_reducer" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.data.group_by_reducer

A transformation that groups elements and performs a reduction. (deprecated)

``` python
tf.contrib.data.group_by_reducer(
    key_func,
    reducer
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/experimental/group_by_reducer.md"><code>tf.data.experimental.group_by_reducer(...)</code></a>.

This transformation maps element of a dataset to a key using `key_func` and
groups the elements by key. The `reducer` is used to process each group; its
`init_func` is used to initialize state for each group when it is created, the
`reduce_func` is used to update the state every time an element is mapped to
the matching group, and the `finalize_func` is used to map the final state to
an output value.

#### Args:


* <b>`key_func`</b>: A function mapping a nested structure of tensors
  (having shapes and types defined by `self.output_shapes` and
  `self.output_types`) to a scalar <a href="../../../tf.md#int64"><code>tf.int64</code></a> tensor.
* <b>`reducer`</b>: An instance of `Reducer`, which captures the reduction logic using
  the `init_func`, `reduce_func`, and `finalize_func` functions.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset.md#apply"><code>tf.data.Dataset.apply</code></a>.
