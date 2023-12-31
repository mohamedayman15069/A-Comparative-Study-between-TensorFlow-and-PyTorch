<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.graph_util.must_run_on_cpu" />
<meta itemprop="path" content="Stable" />
</div>

# tf.graph_util.must_run_on_cpu

Returns True if the given node_def must run on CPU, otherwise False. (deprecated)

### Aliases:

* `tf.compat.v1.graph_util.must_run_on_cpu`
* `tf.compat.v2.compat.v1.graph_util.must_run_on_cpu`
* `tf.graph_util.must_run_on_cpu`

``` python
tf.graph_util.must_run_on_cpu(
    node,
    pin_variables_on_cpu=False
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../tf/graph_util/must_run_on_cpu.md"><code>tf.compat.v1.graph_util.must_run_on_cpu</code></a>

#### Args:


* <b>`node`</b>: The node to be assigned to a device. Could be either an ops.Operation
  or NodeDef.
* <b>`pin_variables_on_cpu`</b>: If True, this function will return False if node_def
  represents a variable-related op.


#### Returns:

True if the given node must run on CPU, otherwise False.
