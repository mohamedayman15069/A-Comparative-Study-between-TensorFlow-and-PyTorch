<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.learn.build_parsing_serving_input_fn" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.learn.build_parsing_serving_input_fn

Build an input_fn appropriate for serving, expecting fed tf.Examples. (deprecated)

``` python
tf.contrib.learn.build_parsing_serving_input_fn(
    feature_spec,
    default_batch_size=None
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please use tf.estimator.export.build_parsing_serving_input_receiver_fn.

Creates an input_fn that expects a serialized tf.Example fed into a string
placeholder.  The function parses the tf.Example according to the provided
feature_spec, and returns all parsed Tensors as features.  This input_fn is
for use at serving time, so the labels return value is always None.

#### Args:


* <b>`feature_spec`</b>: a dict of string to `VarLenFeature`/`FixedLenFeature`.
* <b>`default_batch_size`</b>: the number of query examples expected per batch.
    Leave unset for variable batch size (recommended).


#### Returns:

An input_fn suitable for use in serving.
