<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v2.math.in_top_k" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v2.math.in_top_k

Says whether the targets are in the top `K` predictions.

### Aliases:

* `tf.compat.v2.math.in_top_k`
* `tf.compat.v2.nn.in_top_k`

``` python
tf.compat.v2.math.in_top_k(
    targets,
    predictions,
    k,
    name=None
)
```

<!-- Placeholder for "Used in" -->

This outputs a `batch_size` bool array, an entry `out[i]` is `true` if the
prediction for the target class is finite (not inf, -inf, or nan) and among
the top `k` predictions among all predictions for example `i`. Note that the
behavior of `InTopK` differs from the `TopK` op in its handling of ties; if
multiple classes have the same prediction value and straddle the top-`k`
boundary, all of those classes are considered to be in the top `k`.

More formally, let

  \\(predictions_i\\) be the predictions for all classes for example `i`,
  \\(targets_i\\) be the target class for example `i`,
  \\(out_i\\) be the output for example `i`,

$$out_i = predictions_{i, targets_i} \in TopKIncludingTies(predictions_i)$$

#### Args:


* <b>`predictions`</b>: A `Tensor` of type `float32`.
  A `batch_size` x `classes` tensor.
* <b>`targets`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  A `batch_size` vector of class ids.
* <b>`k`</b>: An `int`. Number of top elements to look at for computing precision.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`. Computed Precision at `k` as a `bool Tensor`.
