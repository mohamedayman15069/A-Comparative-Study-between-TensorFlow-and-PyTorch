<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.learn.read_keyed_batch_examples" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.learn.read_keyed_batch_examples

Adds operations to read, queue, batch `Example` protos. (deprecated)

``` python
tf.contrib.learn.read_keyed_batch_examples(
    file_pattern,
    batch_size,
    reader,
    randomize_input=True,
    num_epochs=None,
    queue_capacity=10000,
    num_threads=1,
    read_batch_size=1,
    parse_fn=None,
    name=None,
    seed=None
)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use tf.data.

Given file pattern (or list of files), will setup a queue for file names,
read `Example` proto using provided `reader`, use batch queue to create
batches of examples of size `batch_size`.

All queue runners are added to the queue runners collection, and may be
started via `start_queue_runners`.

All ops are added to the default graph.

Use `parse_fn` if you need to do parsing / processing on single examples.

#### Args:


* <b>`file_pattern`</b>: List of files or patterns of file paths containing
    `Example` records. See <a href="../../../tf/io/gfile/glob.md"><code>tf.io.gfile.glob</code></a> for pattern rules.
* <b>`batch_size`</b>: An int or scalar `Tensor` specifying the batch size to use.
* <b>`reader`</b>: A function or class that returns an object with
  `read` method, (filename tensor) -> (example tensor).
* <b>`randomize_input`</b>: Whether the input should be randomized.
* <b>`num_epochs`</b>: Integer specifying the number of times to read through the
  dataset. If `None`, cycles through the dataset forever.
  NOTE - If specified, creates a variable that must be initialized, so call
  <a href="../../../tf/initializers/local_variables.md"><code>tf.compat.v1.local_variables_initializer()</code></a> and run the op in a session.
* <b>`queue_capacity`</b>: Capacity for input queue.
* <b>`num_threads`</b>: The number of threads enqueuing examples. In order to have
  predictable and repeatable order of reading and enqueueing, such as in
  prediction and evaluation mode, `num_threads` should be 1.
* <b>`read_batch_size`</b>: An int or scalar `Tensor` specifying the number of
  records to read at once.
* <b>`parse_fn`</b>: Parsing function, takes `Example` Tensor returns parsed
  representation. If `None`, no parsing is done.
* <b>`name`</b>: Name of resulting op.
* <b>`seed`</b>: An integer (optional). Seed used if randomize_input == True.


#### Returns:

Returns tuple of:
- `Tensor` of string keys.
- String `Tensor` of batched `Example` proto.



#### Raises:


* <b>`ValueError`</b>: for invalid inputs.