description: Return true_fn() if the predicate pred is true else false_fn().

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.cond" />
<meta itemprop="path" content="Stable" />
</div>

# tf.cond

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/cond.py">View source</a>



Return `true_fn()` if the predicate `pred` is true else `false_fn()`.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.cond(
    pred, true_fn=None, false_fn=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note: This op is automatically used in a <a href="../tf/function.md"><code>tf.function</code></a> to convert Python
if-statements when the predicate is a <a href="../tf/Tensor.md"><code>tf.Tensor</code></a>, unless `autograph=False` is
explicitly specified in <a href="../tf/function.md"><code>tf.function</code></a> args. For example, the following are
equivalent:

```
>>> @tf.function
... def fun1(x,y):
...   if x > 0:  # AutoGraph converts if-statement to tf.cond().
...     z = y+1
...   else:
...     z = y-1
...   return z
>>> fun1(tf.constant(7), tf.constant(3)).numpy()
4
```

```
>>> @tf.function
... def fun2(x,y):
...   pred = x > 0
...   true_fn =  lambda: y+1
...   false_fn = lambda: y-1
...   return tf.cond(pred, true_fn, false_fn)  # Use tf.cond() explicitly.
>>> fun1(tf.constant(7), tf.constant(3)).numpy()
4
```

For more information, see [tf.function and AutoGraph guide](
https://www.tensorflow.org/guide/function#autograph_transformations).

`true_fn` and `false_fn` both return lists of output tensors. `true_fn` and
`false_fn` must have the same non-zero number and type of outputs.

**WARNING**: Any Tensors or Operations created outside of `true_fn` and
`false_fn` will be executed regardless of which branch is selected at runtime.

Although this behavior is consistent with the dataflow model of TensorFlow,
it has frequently surprised users who expected a lazier semantics.
Consider the following simple program:

```
>>> x, y = tf.constant(2, dtype=tf.int32), tf.constant(4, dtype=tf.int32)
>>> z = tf.multiply(x, y)
>>> r = tf.cond(x < y, lambda: tf.add(x, z), lambda: tf.square(y))
>>> r.numpy()
10
```

If `x < y`, the `tf.add` operation will be executed and `tf.square`
operation will not be executed. Since `z` is needed for at least one
branch of the `cond`, the <a href="../tf/math/multiply.md"><code>tf.multiply</code></a> operation is always executed,
unconditionally.

Note that `cond` calls `true_fn` and `false_fn` *exactly once* (inside the
call to `cond`, and not at all during `Session.run()`). `cond`
stitches together the graph fragments created during the `true_fn` and
`false_fn` calls with some additional graph nodes to ensure that the right
branch gets executed depending on the value of `pred`.

<a href="../tf/cond.md"><code>tf.cond</code></a> supports nested structures as implemented in
`tensorflow.python.util.nest`. Both `true_fn` and `false_fn` must return the
same (possibly nested) value structure of lists, tuples, and/or named tuples.
Singleton lists and tuples form the only exceptions to this: when returned by
`true_fn` and/or `false_fn`, they are implicitly unpacked to single values.

Note: It is illegal to "directly" use tensors created inside a cond branch
outside it, e.g. by storing a reference to a branch tensor in the python
state. If you need to use a tensor created in a branch function you should
return it as an output of the branch function and use the output from
<a href="../tf/cond.md"><code>tf.cond</code></a> instead.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`pred`<a id="pred"></a>
</td>
<td>
A scalar determining whether to return the result of `true_fn` or
`false_fn`.
</td>
</tr><tr>
<td>
`true_fn`<a id="true_fn"></a>
</td>
<td>
The callable to be performed if pred is true.
</td>
</tr><tr>
<td>
`false_fn`<a id="false_fn"></a>
</td>
<td>
The callable to be performed if pred is false.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
Optional name prefix for the returned tensors.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Tensors returned by the call to either `true_fn` or `false_fn`. If the
callables return a singleton list, the element is extracted from the list.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`<a id="TypeError"></a>
</td>
<td>
if `true_fn` or `false_fn` is not callable.
</td>
</tr><tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
if `true_fn` and `false_fn` do not return the same number of
tensors, or return tensors of different types.
</td>
</tr>
</table>



#### Example:



```
>>> x = tf.constant(2)
>>> y = tf.constant(5)
>>> def f1(): return tf.multiply(x, 7)
>>> def f2(): return tf.add(y, 3)
>>> r = tf.cond(tf.less(x, y), f1, f2)
>>> # r is set to f1().
>>> # Operations in f2 (e.g., tf.add) are not executed.
>>> r.numpy()
14
```