<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.training.clip_gradient_norms" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.training.clip_gradient_norms

Clips the gradients by the given value.

``` python
tf.contrib.training.clip_gradient_norms(
    gradients_to_variables,
    max_norm
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`gradients_to_variables`</b>: A list of gradient to variable pairs (tuples).
* <b>`max_norm`</b>: the maximum norm value.


#### Returns:

A list of clipped gradient to variable pairs.
