<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.resource_variables_enabled" />
<meta itemprop="path" content="Stable" />
</div>

# tf.resource_variables_enabled

Returns `True` if resource variables are enabled.

### Aliases:

* `tf.compat.v1.resource_variables_enabled`
* `tf.compat.v2.compat.v1.resource_variables_enabled`
* `tf.resource_variables_enabled`

``` python
tf.resource_variables_enabled()
```

<!-- Placeholder for "Used in" -->

Resource variables are improved versions of TensorFlow variables with a
well-defined memory model. Accessing a resource variable reads its value, and
all ops which access a specific read value of the variable are guaranteed to
see the same value for that tensor. Writes which happen after a read (by
having a control or data dependency on the read) are guaranteed not to affect
the value of the read tensor, and similarly writes which happen before a read
are guaranteed to affect the value. No guarantees are made about unordered
read/write pairs.

Calling tf.enable_resource_variables() lets you opt-in to this TensorFlow 2.0
feature.