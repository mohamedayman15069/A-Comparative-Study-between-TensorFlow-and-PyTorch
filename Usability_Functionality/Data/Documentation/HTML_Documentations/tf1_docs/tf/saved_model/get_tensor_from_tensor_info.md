<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.saved_model.get_tensor_from_tensor_info" />
<meta itemprop="path" content="Stable" />
</div>

# tf.saved_model.get_tensor_from_tensor_info

Returns the Tensor or CompositeTensor described by a TensorInfo proto. (deprecated)

### Aliases:

* `tf.compat.v1.saved_model.get_tensor_from_tensor_info`
* `tf.compat.v1.saved_model.utils.get_tensor_from_tensor_info`
* `tf.compat.v2.compat.v1.saved_model.get_tensor_from_tensor_info`
* `tf.compat.v2.compat.v1.saved_model.utils.get_tensor_from_tensor_info`
* `tf.saved_model.get_tensor_from_tensor_info`
* `tf.saved_model.utils.get_tensor_from_tensor_info`

``` python
tf.saved_model.get_tensor_from_tensor_info(
    tensor_info,
    graph=None,
    import_scope=None
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This function will only be available through the v1 compatibility library as tf.compat.v1.saved_model.utils.get_tensor_from_tensor_info or tf.compat.v1.saved_model.get_tensor_from_tensor_info.

#### Args:


* <b>`tensor_info`</b>: A TensorInfo proto describing a Tensor or SparseTensor or
  CompositeTensor.
* <b>`graph`</b>: The tf.Graph in which tensors are looked up. If None, the
    current default graph is used.
* <b>`import_scope`</b>: If not None, names in `tensor_info` are prefixed with this
    string before lookup.


#### Returns:

The Tensor or SparseTensor or CompositeTensor in `graph` described by
`tensor_info`.



#### Raises:


* <b>`KeyError`</b>: If `tensor_info` does not correspond to a tensor in `graph`.
* <b>`ValueError`</b>: If `tensor_info` is malformed.