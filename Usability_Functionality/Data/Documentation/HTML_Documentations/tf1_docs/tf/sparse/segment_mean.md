<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.segment_mean" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.segment_mean

Computes the mean along sparse segments of a tensor.

### Aliases:

* `tf.compat.v1.sparse.segment_mean`
* `tf.compat.v1.sparse_segment_mean`
* `tf.compat.v2.compat.v1.sparse.segment_mean`
* `tf.compat.v2.compat.v1.sparse_segment_mean`
* `tf.sparse.segment_mean`
* `tf.sparse_segment_mean`

``` python
tf.sparse.segment_mean(
    data,
    indices,
    segment_ids,
    name=None,
    num_segments=None
)
```

<!-- Placeholder for "Used in" -->

Read [the section on
segmentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/math#about_segmentation)
for an explanation of segments.

Like <a href="../../tf/math/segment_mean.md"><code>tf.math.segment_mean</code></a>, but `segment_ids` can have rank less than
`data`'s first dimension, selecting a subset of dimension 0, specified by
`indices`.
`segment_ids` is allowed to have missing ids, in which case the output will
be zeros at those indices. In those cases `num_segments` is used to determine
the size of the output.

#### Args:


* <b>`data`</b>: A `Tensor` with data that will be assembled in the output.
* <b>`indices`</b>: A 1-D `Tensor` with indices into `data`. Has same rank as
  `segment_ids`.
* <b>`segment_ids`</b>: A 1-D `Tensor` with indices into the output `Tensor`. Values
  should be sorted and can be repeated.
* <b>`name`</b>: A name for the operation (optional).
* <b>`num_segments`</b>: An optional int32 scalar. Indicates the size of the output
  `Tensor`.


#### Returns:

A `tensor` of the shape as data, except for dimension 0 which
has size `k`, the number of segments specified via `num_segments` or
inferred for the last element in `segments_ids`.
