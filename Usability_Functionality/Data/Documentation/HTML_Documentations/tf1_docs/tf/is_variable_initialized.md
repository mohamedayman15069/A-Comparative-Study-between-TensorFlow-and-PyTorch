<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.is_variable_initialized" />
<meta itemprop="path" content="Stable" />
</div>

# tf.is_variable_initialized

Tests if a variable has been initialized.

### Aliases:

* `tf.compat.v1.is_variable_initialized`
* `tf.compat.v2.compat.v1.is_variable_initialized`
* `tf.is_variable_initialized`

``` python
tf.is_variable_initialized(variable)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`variable`</b>: A `Variable`.


#### Returns:

Returns a scalar boolean Tensor, `True` if the variable has been
initialized, `False` otherwise.



**NOTE** The output of this function should be used.  If it is not, a warning will be logged.  To mark the output as used, call its .mark_used() method.