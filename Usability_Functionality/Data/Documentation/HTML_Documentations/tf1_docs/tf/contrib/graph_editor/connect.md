<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.graph_editor.connect" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.graph_editor.connect

Connect the outputs of sgv0 to the inputs of sgv1.

``` python
tf.contrib.graph_editor.connect(
    sgv0,
    sgv1,
    disconnect_first=False
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sgv0`</b>: the first subgraph to have its outputs swapped. This argument is
  converted to a subgraph using the same rules as the function
  subgraph.make_view.
  Note that sgv0 is modified in place.
* <b>`sgv1`</b>: the second subgraph to have its outputs swapped. This argument is
  converted to a subgraph using the same rules as the function
  subgraph.make_view.
  Note that sgv1 is modified in place.
* <b>`disconnect_first`</b>: if True the current outputs of sgv0 are disconnected.

#### Returns:

A tuple `(sgv0, sgv1)` of the now connected subgraphs.


#### Raises:


* <b>`StandardError`</b>: if sgv0 or sgv1 cannot be converted to a SubGraphView using
  the same rules than the function subgraph.make_view.