<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.safe_embedding_lookup_sparse" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.safe_embedding_lookup_sparse

Lookup embedding results, accounting for invalid IDs and empty features.

### Aliases:

* `tf.compat.v1.nn.safe_embedding_lookup_sparse`
* `tf.compat.v2.compat.v1.nn.safe_embedding_lookup_sparse`
* `tf.nn.safe_embedding_lookup_sparse`

``` python
tf.nn.safe_embedding_lookup_sparse(
    embedding_weights,
    sparse_ids,
    sparse_weights=None,
    combiner='mean',
    default_id=None,
    name=None,
    partition_strategy='div',
    max_norm=None
)
```

<!-- Placeholder for "Used in" -->

The partitioned embedding in `embedding_weights` must all be the same shape
except for the first dimension. The first dimension is allowed to vary as the
vocabulary size is not necessarily a multiple of `P`.  `embedding_weights`
may be a `PartitionedVariable` as returned by using
<a href="../../tf/get_variable.md"><code>tf.compat.v1.get_variable()</code></a> with a
partitioner.

Invalid IDs (< 0) are pruned from input IDs and weights, as well as any IDs
with non-positive weight. For an entry with no features, the embedding vector
for `default_id` is returned, or the 0-vector if `default_id` is not supplied.

The ids and weights may be multi-dimensional. Embeddings are always aggregated
along the last dimension.

#### Args:


* <b>`embedding_weights`</b>:  A list of `P` float `Tensor`s or values representing
  partitioned embedding `Tensor`s.  Alternatively, a `PartitionedVariable`
  created by partitioning along dimension 0.  The total unpartitioned shape
  should be `[e_0, e_1, ..., e_m]`, where `e_0` represents the vocab size
  and `e_1, ..., e_m` are the embedding dimensions.
* <b>`sparse_ids`</b>: `SparseTensor` of shape `[d_0, d_1, ..., d_n]` containing the
  ids. `d_0` is typically batch size.
* <b>`sparse_weights`</b>: `SparseTensor` of same shape as `sparse_ids`, containing
  float weights corresponding to `sparse_ids`, or `None` if all weights are
  be assumed to be 1.0.
* <b>`combiner`</b>: A string specifying how to combine embedding results for each
  entry. Currently "mean", "sqrtn" and "sum" are supported, with "mean" the
  default.
* <b>`default_id`</b>: The id to use for an entry with no features.
* <b>`name`</b>: A name for this operation (optional).
* <b>`partition_strategy`</b>: A string specifying the partitioning strategy. Currently
  `"div"` and `"mod"` are supported. Default is `"div"`.
* <b>`max_norm`</b>: If not `None`, all embeddings are l2-normalized to max_norm before
  combining.


#### Returns:

Dense `Tensor` of shape `[d_0, d_1, ..., d_{n-1}, e_1, ..., e_m]`.



#### Raises:


* <b>`ValueError`</b>: if `embedding_weights` is empty.