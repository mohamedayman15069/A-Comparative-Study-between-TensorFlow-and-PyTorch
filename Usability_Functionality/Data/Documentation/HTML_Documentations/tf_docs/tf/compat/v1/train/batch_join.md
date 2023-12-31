description: Runs a list of tensors to fill a queue to create batches of examples. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.batch_join" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.batch_join

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/training/input.py">View source</a>



Runs a list of tensors to fill a queue to create batches of examples. (deprecated)


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.batch_join(
    tensors_list,
    batch_size,
    capacity=32,
    enqueue_many=False,
    shapes=None,
    dynamic_pad=False,
    allow_smaller_final_batch=False,
    shared_name=None,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Queue-based input pipelines have been replaced by <a href="../../../../tf/data.md"><code>tf.data</code></a>. Use `tf.data.Dataset.interleave(...).batch(batch_size)` (or `padded_batch(...)` if `dynamic_pad=True`).

The `tensors_list` argument is a list of tuples of tensors, or a list of
dictionaries of tensors.  Each element in the list is treated similarly
to the `tensors` argument of <a href="../../../../tf/compat/v1/train/batch.md"><code>tf.compat.v1.train.batch()</code></a>.

WARNING: This function is nondeterministic, since it starts a separate thread
for each tensor.

Enqueues a different list of tensors in different threads.
Implemented using a queue -- a `QueueRunner` for the queue
is added to the current `Graph`'s `QUEUE_RUNNER` collection.

`len(tensors_list)` threads will be started,
with thread `i` enqueuing the tensors from
`tensors_list[i]`. `tensors_list[i1][j]` must match
`tensors_list[i2][j]` in type and shape, except in the first
dimension if `enqueue_many` is true.

If `enqueue_many` is `False`, each `tensors_list[i]` is assumed
to represent a single example. An input tensor `x` will be output as a
tensor with shape `[batch_size] + x.shape`.

If `enqueue_many` is `True`, `tensors_list[i]` is assumed to
represent a batch of examples, where the first dimension is indexed
by example, and all members of `tensors_list[i]` should have the
same size in the first dimension.  The slices of any input tensor
`x` are treated as examples, and the output tensors will have shape
`[batch_size] + x.shape[1:]`.

The `capacity` argument controls the how long the prefetching is allowed to
grow the queues.

The returned operation is a dequeue operation and will throw
<a href="../../../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a> if the input queue is exhausted. If this
operation is feeding another input queue, its queue runner will catch
this exception, however, if this operation is used in your main thread
you are responsible for catching this yourself.

*N.B.:* If `dynamic_pad` is `False`, you must ensure that either
(i) the `shapes` argument is passed, or (ii) all of the tensors in
`tensors_list` must have fully-defined shapes. `ValueError` will be
raised if neither of these conditions holds.

If `dynamic_pad` is `True`, it is sufficient that the *rank* of the
tensors is known, but individual dimensions may have value `None`.
In this case, for each enqueue the dimensions with value `None`
may have a variable length; upon dequeue, the output tensors will be padded
on the right to the maximum shape of the tensors in the current minibatch.
For numbers, this padding takes value 0.  For strings, this padding is
the empty string.  See `PaddingFIFOQueue` for more info.

If `allow_smaller_final_batch` is `True`, a smaller batch value than
`batch_size` is returned when the queue is closed and there are not enough
elements to fill the batch, otherwise the pending elements are discarded.
In addition, all output tensors' static shapes, as accessed via the
`shape` property will have a first `Dimension` value of `None`, and
operations that depend on fixed batch_size would fail.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensors_list`<a id="tensors_list"></a>
</td>
<td>
A list of tuples or dictionaries of tensors to enqueue.
</td>
</tr><tr>
<td>
`batch_size`<a id="batch_size"></a>
</td>
<td>
An integer. The new batch size pulled from the queue.
</td>
</tr><tr>
<td>
`capacity`<a id="capacity"></a>
</td>
<td>
An integer. The maximum number of elements in the queue.
</td>
</tr><tr>
<td>
`enqueue_many`<a id="enqueue_many"></a>
</td>
<td>
Whether each tensor in `tensor_list_list` is a single
example.
</td>
</tr><tr>
<td>
`shapes`<a id="shapes"></a>
</td>
<td>
(Optional) The shapes for each example.  Defaults to the
inferred shapes for `tensor_list_list[i]`.
</td>
</tr><tr>
<td>
`dynamic_pad`<a id="dynamic_pad"></a>
</td>
<td>
Boolean.  Allow variable dimensions in input shapes.
The given dimensions are padded upon dequeue so that tensors within a
batch have the same shapes.
</td>
</tr><tr>
<td>
`allow_smaller_final_batch`<a id="allow_smaller_final_batch"></a>
</td>
<td>
(Optional) Boolean. If `True`, allow the final
batch to be smaller if there are insufficient items left in the queue.
</td>
</tr><tr>
<td>
`shared_name`<a id="shared_name"></a>
</td>
<td>
(Optional) If set, this queue will be shared under the given
name across multiple sessions.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
(Optional) A name for the operations.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list or dictionary of tensors with the same number and types as
`tensors_list[i]`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
If the `shapes` are not specified, and cannot be
inferred from the elements of `tensor_list_list`.
</td>
</tr>
</table>




 <section><devsite-expandable expanded>
 <h2 class="showalways">eager compatibility</h2>

Input pipelines based on Queues are not supported when eager execution is
enabled. Please use the <a href="../../../../tf/data.md"><code>tf.data</code></a> API to ingest data under eager execution.

 </devsite-expandable></section>

