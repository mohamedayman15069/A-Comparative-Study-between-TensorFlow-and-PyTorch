<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.learn.infer_real_valued_columns_from_input_fn" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.learn.infer_real_valued_columns_from_input_fn

Creates `FeatureColumn` objects for inputs defined by `input_fn`. (deprecated)

``` python
tf.contrib.learn.infer_real_valued_columns_from_input_fn(input_fn)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please specify feature columns explicitly.

This interprets all inputs as dense, fixed-length float values. This creates
a local graph in which it calls `input_fn` to build the tensors, then discards
it.

#### Args:


* <b>`input_fn`</b>: Input function returning a tuple of:
    features - Dictionary of string feature name to `Tensor` or `Tensor`.
    labels - `Tensor` of label values.


#### Returns:

List of `FeatureColumn` objects.
