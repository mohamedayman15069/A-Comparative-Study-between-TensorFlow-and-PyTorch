<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v2.test.assert_equal_graph_def" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v2.test.assert_equal_graph_def

Asserts that two `GraphDef`s are (mostly) the same.

``` python
tf.compat.v2.test.assert_equal_graph_def(
    expected,
    actual
)
```

<!-- Placeholder for "Used in" -->

Compares two `GraphDef` protos for equality, ignoring versions and ordering of
nodes, attrs, and control inputs.  Node names are used to match up nodes
between the graphs, so the naming of nodes must be consistent. This function
ignores randomized attribute values that may appear in V2 checkpoints.

#### Args:


* <b>`expected`</b>: The `GraphDef` we expected.
* <b>`actual`</b>: The `GraphDef` we have.


#### Raises:


* <b>`AssertionError`</b>: If the `GraphDef`s do not match.
* <b>`TypeError`</b>: If either argument is not a `GraphDef`.