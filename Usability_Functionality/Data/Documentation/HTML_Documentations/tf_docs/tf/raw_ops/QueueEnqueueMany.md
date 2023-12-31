description: Enqueues zero or more tuples of one or more tensors in the given queue.
robots: noindex

# tf.raw_ops.QueueEnqueueMany

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Enqueues zero or more tuples of one or more tensors in the given queue.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.QueueEnqueueMany`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.QueueEnqueueMany(
    handle, components, timeout_ms=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation slices each component tensor along the 0th dimension to
make multiple queue elements. All of the tuple components must have the
same size in the 0th dimension.

The components input has k elements, which correspond to the components of
tuples stored in the given queue.

N.B. If the queue is full, this operation will block until the given
elements have been enqueued (or 'timeout_ms' elapses, if specified).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`handle`<a id="handle"></a>
</td>
<td>
A `Tensor` of type mutable `string`. The handle to a queue.
</td>
</tr><tr>
<td>
`components`<a id="components"></a>
</td>
<td>
A list of `Tensor` objects.
One or more tensors from which the enqueued tensors should
be taken.
</td>
</tr><tr>
<td>
`timeout_ms`<a id="timeout_ms"></a>
</td>
<td>
An optional `int`. Defaults to `-1`.
If the queue is too full, this operation will block for up
to timeout_ms milliseconds.
Note: This option is not supported yet.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The created Operation.
</td>
</tr>

</table>

