<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.graph_editor.filter_ops_from_regex" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.graph_editor.filter_ops_from_regex

Get all the operations that match the given regex.

``` python
tf.contrib.graph_editor.filter_ops_from_regex(
    ops,
    regex
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`ops`</b>: an object convertible to a list of <a href="../../../tf/Operation.md"><code>tf.Operation</code></a>.
* <b>`regex`</b>: a regular expression matching the operation's name.
  For example, `"^foo(/.*)?$"` will match all the operations in the "foo"
  scope.

#### Returns:

A list of <a href="../../../tf/Operation.md"><code>tf.Operation</code></a>.


#### Raises:


* <b>`TypeError`</b>: if ops cannot be converted to a list of <a href="../../../tf/Operation.md"><code>tf.Operation</code></a>.