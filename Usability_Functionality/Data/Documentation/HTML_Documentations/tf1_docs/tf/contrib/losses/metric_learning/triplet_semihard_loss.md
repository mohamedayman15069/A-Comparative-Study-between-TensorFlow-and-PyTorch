<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.losses.metric_learning.triplet_semihard_loss" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.losses.metric_learning.triplet_semihard_loss

Computes the triplet loss with semi-hard negative mining.

``` python
tf.contrib.losses.metric_learning.triplet_semihard_loss(
    labels,
    embeddings,
    margin=1.0
)
```

<!-- Placeholder for "Used in" -->

The loss encourages the positive distances (between a pair of embeddings with
the same labels) to be smaller than the minimum negative distance among
which are at least greater than the positive distance plus the margin constant
(called semi-hard negative) in the mini-batch. If no such negative exists,
uses the largest negative distance instead.
See: https://arxiv.org/abs/1503.03832.

#### Args:


* <b>`labels`</b>: 1-D tf.int32 `Tensor` with shape [batch_size] of
  multiclass integer labels.
* <b>`embeddings`</b>: 2-D float `Tensor` of embedding vectors. Embeddings should
  be l2 normalized.
* <b>`margin`</b>: Float, margin term in the loss definition.


#### Returns:


* <b>`triplet_loss`</b>: tf.float32 scalar.