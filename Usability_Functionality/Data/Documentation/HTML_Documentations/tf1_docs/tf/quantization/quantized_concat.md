<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.quantization.quantized_concat" />
<meta itemprop="path" content="Stable" />
</div>

# tf.quantization.quantized_concat

Concatenates quantized tensors along one dimension.

### Aliases:

* `tf.compat.v1.quantization.quantized_concat`
* `tf.compat.v1.quantized_concat`
* `tf.compat.v2.compat.v1.quantization.quantized_concat`
* `tf.compat.v2.compat.v1.quantized_concat`
* `tf.compat.v2.quantization.quantized_concat`
* `tf.quantization.quantized_concat`
* `tf.quantized_concat`

``` python
tf.quantization.quantized_concat(
    concat_dim,
    values,
    input_mins,
    input_maxes,
    name=None
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`concat_dim`</b>: A `Tensor` of type `int32`.
  0-D.  The dimension along which to concatenate.  Must be in the
  range [0, rank(values)).
* <b>`values`</b>: A list of at least 2 `Tensor` objects with the same type.
  The `N` Tensors to concatenate. Their ranks and types must match,
  and their sizes must match in all dimensions except `concat_dim`.
* <b>`input_mins`</b>: A list with the same length as `values` of `Tensor` objects with type `float32`.
  The minimum scalar values for each of the input tensors.
* <b>`input_maxes`</b>: A list with the same length as `values` of `Tensor` objects with type `float32`.
  The maximum scalar values for each of the input tensors.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `Tensor` objects (output, output_min, output_max).


* <b>`output`</b>: A `Tensor`. Has the same type as `values`.
* <b>`output_min`</b>: A `Tensor` of type `float32`.
* <b>`output_max`</b>: A `Tensor` of type `float32`.