<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.lite.toco_convert" />
<meta itemprop="path" content="Stable" />
</div>

# tf.lite.toco_convert

Convert a model using TOCO. (deprecated)

### Aliases:

* `tf.compat.v1.lite.toco_convert`
* `tf.compat.v2.compat.v1.lite.toco_convert`
* `tf.lite.toco_convert`

``` python
tf.lite.toco_convert(
    input_data,
    input_tensors,
    output_tensors,
    *args,
    **kwargs
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../tf/lite/TFLiteConverter.md"><code>lite.TFLiteConverter</code></a> instead.

Typically this function is used to convert from TensorFlow GraphDef to TFLite.
Conversion can be customized by providing arguments that are forwarded to
`build_toco_convert_protos` (see documentation for details). This function has
been deprecated. Please use <a href="../../tf/lite/TFLiteConverter.md"><code>lite.TFLiteConverter</code></a> instead.

#### Args:


* <b>`input_data`</b>: Input data (i.e. often `sess.graph_def`),
* <b>`input_tensors`</b>: List of input tensors. Type and shape are computed using
  `foo.shape` and `foo.dtype`.
* <b>`output_tensors`</b>: List of output tensors (only .name is used from this).
* <b>`*args`</b>: See `build_toco_convert_protos`,
* <b>`**kwargs`</b>: See `build_toco_convert_protos`.


#### Returns:

The converted data. For example if TFLite was the destination, then
this will be a tflite flatbuffer in a bytes array.



#### Raises:

Defined in `build_toco_convert_protos`.
