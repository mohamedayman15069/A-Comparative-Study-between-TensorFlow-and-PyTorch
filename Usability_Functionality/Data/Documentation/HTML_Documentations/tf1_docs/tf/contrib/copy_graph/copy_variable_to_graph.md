<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.copy_graph.copy_variable_to_graph" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.copy_graph.copy_variable_to_graph

Given a `Variable` instance from one `Graph`, initializes and returns

``` python
tf.contrib.copy_graph.copy_variable_to_graph(
    org_instance,
    to_graph,
    scope=''
)
```

<!-- Placeholder for "Used in" -->
a copy of it from another `Graph`, under the specified scope
(default `""`).

#### Args:


* <b>`org_instance`</b>: A `Variable` from some `Graph`.
* <b>`to_graph`</b>: The `Graph` to copy the `Variable` to.
* <b>`scope`</b>: A scope for the new `Variable` (default `""`).


#### Returns:

The copied `Variable` from `to_graph`.



#### Raises:


* <b>`TypeError`</b>: If `org_instance` is not a `Variable`.