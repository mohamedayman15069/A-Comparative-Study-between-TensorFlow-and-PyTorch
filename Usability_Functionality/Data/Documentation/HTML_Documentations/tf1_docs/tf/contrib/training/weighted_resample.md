<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.training.weighted_resample" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.training.weighted_resample

Performs an approximate weighted resampling of `inputs`.

``` python
tf.contrib.training.weighted_resample(
    inputs,
    weights,
    overall_rate,
    scope=None,
    mean_decay=0.999,
    seed=None
)
```

<!-- Placeholder for "Used in" -->

This method chooses elements from `inputs` where each item's rate of
selection is proportional to its value in `weights`, and the average
rate of selection across all inputs (and many invocations!) is
`overall_rate`.

#### Args:


* <b>`inputs`</b>: A list of tensors whose first dimension is `batch_size`.
* <b>`weights`</b>: A `[batch_size]`-shaped tensor with each batch member's weight.
* <b>`overall_rate`</b>: Desired overall rate of resampling.
* <b>`scope`</b>: Scope to use for the op.
* <b>`mean_decay`</b>: How quickly to decay the running estimate of the mean weight.
* <b>`seed`</b>: Random seed.


#### Returns:

A list of tensors exactly like `inputs`, but with an unknown (and
  possibly zero) first dimension.
A tensor containing the effective resampling rate used for each output.
