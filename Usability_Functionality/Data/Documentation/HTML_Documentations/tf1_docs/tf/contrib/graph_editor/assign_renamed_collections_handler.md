<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.graph_editor.assign_renamed_collections_handler" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.graph_editor.assign_renamed_collections_handler

Add the transformed elem to the (renamed) collections of elem.

``` python
tf.contrib.graph_editor.assign_renamed_collections_handler(
    info,
    elem,
    elem_
)
```

<!-- Placeholder for "Used in" -->

A collection is renamed only if is not a known key, as described in
<a href="../../../tf/GraphKeys.md"><code>tf.compat.v1.GraphKeys</code></a>.

#### Args:


* <b>`info`</b>: Transform._TmpInfo instance.
* <b>`elem`</b>: the original element (<a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a> or <a href="../../../tf/Operation.md"><code>tf.Operation</code></a>)
* <b>`elem_`</b>: the transformed element