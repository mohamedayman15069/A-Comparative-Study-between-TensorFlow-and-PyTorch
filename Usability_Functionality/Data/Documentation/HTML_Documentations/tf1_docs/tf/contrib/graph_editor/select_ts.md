<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.graph_editor.select_ts" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.graph_editor.select_ts

Helper to select tensors.

``` python
tf.contrib.graph_editor.select_ts(
    *args,
    **kwargs
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`*args`</b>: list of 1) regular expressions (compiled or not) or 2) (array of)
  <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>. <a href="../../../tf/Operation.md"><code>tf.Operation</code></a> instances are silently ignored.
* <b>`**kwargs`</b>: 'graph': <a href="../../../tf/Graph.md"><code>tf.Graph</code></a> in which to perform the regex query.This is
  required when using regex.
  'positive_filter': an elem if selected only if `positive_filter(elem)` is
    `True`. This is optional.
  'restrict_ts_regex': a regular expression is ignored if it doesn't start
    with the substring "(?#ts)".

#### Returns:

A list of <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>.


#### Raises:


* <b>`TypeError`</b>: if the optional keyword argument graph is not a <a href="../../../tf/Graph.md"><code>tf.Graph</code></a>
  or if an argument in args is not an (array of) <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>
  or an (array of) <a href="../../../tf/Operation.md"><code>tf.Operation</code></a> (silently ignored) or a string
  or a regular expression.
* <b>`ValueError`</b>: if one of the keyword arguments is unexpected or if a regular
  expression is used without passing a graph as a keyword argument.