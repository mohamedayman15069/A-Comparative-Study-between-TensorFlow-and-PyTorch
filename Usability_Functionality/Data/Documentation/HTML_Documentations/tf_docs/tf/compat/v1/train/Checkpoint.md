description: Groups trackable objects, saving and restoring them.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.Checkpoint" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="restore"/>
<meta itemprop="property" content="save"/>
<meta itemprop="property" content="write"/>
</div>

# tf.compat.v1.train.Checkpoint

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/checkpoint/checkpoint.py">View source</a>



Groups trackable objects, saving and restoring them.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.Checkpoint(
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

`Checkpoint`'s constructor accepts keyword arguments whose values are types
that contain trackable state, such as <a href="../../../../tf/compat/v1/train/Optimizer.md"><code>tf.compat.v1.train.Optimizer</code></a>
implementations, <a href="../../../../tf/Variable.md"><code>tf.Variable</code></a>, `tf.keras.Layer` implementations, or
<a href="../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> implementations. It saves these values with a checkpoint, and
maintains a `save_counter` for numbering checkpoints.

Example usage when graph building:

```python
import tensorflow as tf
import os

checkpoint_directory = "/tmp/training_checkpoints"
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")

checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
status = checkpoint.restore(tf.train.latest_checkpoint(checkpoint_directory))
train_op = optimizer.minimize( ... )
status.assert_consumed()  # Optional sanity checks.
with tf.compat.v1.Session() as session:
  # Use the Session to restore variables, or initialize them if
  # tf.train.latest_checkpoint returned None.
  status.initialize_or_restore(session)
  for _ in range(num_training_steps):
    session.run(train_op)
  checkpoint.save(file_prefix=checkpoint_prefix)
```

Example usage with eager execution enabled:

```python
import tensorflow as tf
import os

tf.compat.v1.enable_eager_execution()

checkpoint_directory = "/tmp/training_checkpoints"
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")

checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
status = checkpoint.restore(tf.train.latest_checkpoint(checkpoint_directory))
for _ in range(num_training_steps):
  optimizer.minimize( ... )  # Variables will be restored on creation.
status.assert_consumed()  # Optional sanity checks.
checkpoint.save(file_prefix=checkpoint_prefix)
```

`Checkpoint.save` and `Checkpoint.restore` write and read object-based
checkpoints, in contrast to <a href="../../../../tf/compat/v1/train/Saver.md"><code>tf.compat.v1.train.Saver</code></a> which writes and reads
`variable.name` based checkpoints. Object-based checkpointing saves a graph of
dependencies between Python objects (`Layer`s, `Optimizer`s, `Variable`s,
etc.) with named edges, and this graph is used to match variables when
restoring a checkpoint. It can be more robust to changes in the Python
program, and helps to support restore-on-create for variables when executing
eagerly. Prefer <a href="../../../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a> over <a href="../../../../tf/compat/v1/train/Saver.md"><code>tf.compat.v1.train.Saver</code></a> for new
code.

`Checkpoint` objects have dependencies on the objects passed as keyword
arguments to their constructors, and each dependency is given a name that is
identical to the name of the keyword argument for which it was created.
TensorFlow classes like `Layer`s and `Optimizer`s will automatically add
dependencies on their variables (e.g. "kernel" and "bias" for
<a href="../../../../tf/keras/layers/Dense.md"><code>tf.keras.layers.Dense</code></a>). Inheriting from <a href="../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> makes managing
dependencies easy in user-defined classes, since `Model` hooks into attribute
assignment. For example:

```python
class Regress(tf.keras.Model):

  def __init__(self):
    super().__init__()
    self.input_transform = tf.keras.layers.Dense(10)
    # ...

  def call(self, inputs):
    x = self.input_transform(inputs)
    # ...
```

This `Model` has a dependency named "input_transform" on its `Dense` layer,
which in turn depends on its variables. As a result, saving an instance of
`Regress` using <a href="../../../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a> will also save all the variables created
by the `Dense` layer.

When variables are assigned to multiple workers, each worker writes its own
section of the checkpoint. These sections are then merged/re-indexed to behave
as a single checkpoint. This avoids copying all variables to one worker, but
does require that all workers see a common filesystem.

While <a href="../../../../tf/keras/Model.md#save_weights"><code>tf.keras.Model.save_weights</code></a> and <a href="../../../../tf/train/Checkpoint.md#save"><code>tf.train.Checkpoint.save</code></a> save in the
same format, note that the root of the resulting checkpoint is the object the
save method is attached to. This means saving a <a href="../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> using
`save_weights` and loading into a <a href="../../../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a> with a `Model`
attached (or vice versa) will not match the `Model`'s variables. See the
[guide to training
checkpoints](https://www.tensorflow.org/guide/checkpoint) for
details. Prefer <a href="../../../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a> over <a href="../../../../tf/keras/Model.md#save_weights"><code>tf.keras.Model.save_weights</code></a> for
training checkpoints.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`**kwargs`<a id="**kwargs"></a>
</td>
<td>
Keyword arguments are set as attributes of this object, and are
saved with the checkpoint. Values must be trackable objects.
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
If objects in `kwargs` are not trackable.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`save_counter`<a id="save_counter"></a>
</td>
<td>
Incremented when `save()` is called. Used to number
checkpoints.
</td>
</tr>
</table>



## Methods

<h3 id="restore"><code>restore</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/checkpoint/checkpoint.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>restore(
    save_path
)
</code></pre>

Restore a training checkpoint.

Restores this `Checkpoint` and any objects it depends on.

When executing eagerly, either assigns values immediately if variables to
restore have been created already, or defers restoration until the variables
are created. Dependencies added after this call will be matched if they have
a corresponding object in the checkpoint (the restore request will queue in
any trackable object waiting for the expected dependency to be added).

When graph building, restoration ops are added to the graph but not run
immediately.

```python
checkpoint = tf.train.Checkpoint( ... )
checkpoint.restore(path)
```

To ensure that loading is complete and no more deferred restorations will
take place, you can use the `assert_consumed()` method of the status object
returned by `restore`.
The assert will raise an exception if any Python objects in the dependency
graph were not found in the checkpoint, or if any checkpointed values do not
have a matching Python object:

```python
checkpoint = tf.train.Checkpoint( ... )
checkpoint.restore(path).assert_consumed()
```

When graph building, `assert_consumed()` indicates that all of the restore
ops that will be created for this checkpoint have been created. They can be
run via the `run_restore_ops()` method of the status object:

```python
checkpoint.restore(path).assert_consumed().run_restore_ops()
```

If the checkpoint has not been consumed completely, then the list of restore
ops will grow as more objects are added to the dependency graph.

To check that all variables in the Python object have restored values from
checkpoint, use `assert_existing_objects_matched()`. This assertion is
useful when called after the variables in your graph have been created.

Name-based <a href="../../../../tf/compat/v1/train/Saver.md"><code>tf.compat.v1.train.Saver</code></a> checkpoints can be loaded using this
method. Names are used to match variables. No restore ops are created/run
until `run_restore_ops()` or `initialize_or_restore()` are called on the
returned status object when graph building, but there is restore-on-creation
when executing eagerly. Re-encode name-based checkpoints using
<a href="../../../../tf/train/Checkpoint.md#save"><code>tf.train.Checkpoint.save</code></a> as soon as possible.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`save_path`
</td>
<td>
The path to the checkpoint, as returned by `save` or
<a href="../../../../tf/train/latest_checkpoint.md"><code>tf.train.latest_checkpoint</code></a>. If None (as when there is no latest
checkpoint for <a href="../../../../tf/train/latest_checkpoint.md"><code>tf.train.latest_checkpoint</code></a> to return), returns an
object which may run initializers for objects in the dependency graph.
If the checkpoint was written by the name-based
<a href="../../../../tf/compat/v1/train/Saver.md"><code>tf.compat.v1.train.Saver</code></a>, names are used to match variables.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A load status object, which can be used to make assertions about the
status of a checkpoint restoration and run initialization/restore ops.

The returned status object has the following methods:

* `assert_consumed()`:
    Raises an exception if any variables are unmatched: either
    checkpointed values which don't have a matching Python object or
    Python objects in the dependency graph with no values in the
    checkpoint. This method returns the status object, and so may be
    chained with `initialize_or_restore` or `run_restore_ops`.

* `assert_existing_objects_matched()`:
    Raises an exception if any existing Python objects in the dependency
    graph are unmatched. Unlike `assert_consumed`, this assertion will
    pass if values in the checkpoint have no corresponding Python
    objects. For example a `tf.keras.Layer` object which has not yet been
    built, and so has not created any variables, will pass this assertion
    but will fail `assert_consumed`. Useful when loading part of a larger
    checkpoint into a new Python program, e.g. a training checkpoint with
    a <a href="../../../../tf/compat/v1/train/Optimizer.md"><code>tf.compat.v1.train.Optimizer</code></a> was saved but only the state required
    for inference is being loaded. This method returns the status object,
    and so may be chained with `initialize_or_restore` or
    `run_restore_ops`.

* `assert_nontrivial_match()`: Asserts that something aside from the root
    object was matched. This is a very weak assertion, but is useful for
    sanity checking in library code where objects may exist in the
    checkpoint which haven't been created in Python and some Python
    objects may not have a checkpointed value.

* `expect_partial()`: Silence warnings about incomplete checkpoint
    restores. Warnings are otherwise printed for unused parts of the
    checkpoint file or object when the `Checkpoint` object is deleted
    (often at program shutdown).

* `initialize_or_restore(session=None)`:
    When graph building, runs variable initializers if `save_path` is
    `None`, but otherwise runs restore operations. If no `session` is
    explicitly specified, the default session is used. No effect when
    executing eagerly (variables are initialized or restored eagerly).

* `run_restore_ops(session=None)`:
    When graph building, runs restore operations. If no `session` is
    explicitly specified, the default session is used. No effect when
    executing eagerly (restore operations are run eagerly). May only be
    called when `save_path` is not `None`.
</td>
</tr>

</table>



<h3 id="save"><code>save</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/checkpoint/checkpoint.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>save(
    file_prefix, session=None, options=None
)
</code></pre>

Saves a training checkpoint and provides basic checkpoint management.

The saved checkpoint includes variables created by this object and any
trackable objects it depends on at the time `Checkpoint.save()` is
called.

`save` is a basic convenience wrapper around the `write` method,
sequentially numbering checkpoints using `save_counter` and updating the
metadata used by <a href="../../../../tf/train/latest_checkpoint.md"><code>tf.train.latest_checkpoint</code></a>. More advanced checkpoint
management, for example garbage collection and custom numbering, may be
provided by other utilities which also wrap `write`
(<a href="../../../../tf/train/CheckpointManager.md"><code>tf.train.CheckpointManager</code></a> for example).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`file_prefix`
</td>
<td>
A prefix to use for the checkpoint filenames
(/path/to/directory/and_a_prefix). Names are generated based on this
prefix and `Checkpoint.save_counter`.
</td>
</tr><tr>
<td>
`session`
</td>
<td>
The session to evaluate variables in. Ignored when executing
eagerly. If not provided when graph building, the default session is
used.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
Optional <a href="../../../../tf/train/CheckpointOptions.md"><code>tf.train.CheckpointOptions</code></a> object.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The full path to the checkpoint.
</td>
</tr>

</table>



<h3 id="write"><code>write</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/checkpoint/checkpoint.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>write(
    file_prefix, session=None, options=None
)
</code></pre>

Writes a training checkpoint.

The checkpoint includes variables created by this object and any
trackable objects it depends on at the time `Checkpoint.write()` is
called.

`write` does not number checkpoints, increment `save_counter`, or update the
metadata used by <a href="../../../../tf/train/latest_checkpoint.md"><code>tf.train.latest_checkpoint</code></a>. It is primarily intended for
use by higher level checkpoint management utilities. `save` provides a very
basic implementation of these features.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`file_prefix`
</td>
<td>
A prefix to use for the checkpoint filenames
(/path/to/directory/and_a_prefix).
</td>
</tr><tr>
<td>
`session`
</td>
<td>
The session to evaluate variables in. Ignored when executing
eagerly. If not provided when graph building, the default session is
used.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
Optional <a href="../../../../tf/train/CheckpointOptions.md"><code>tf.train.CheckpointOptions</code></a> object.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The full path to the checkpoint (i.e. `file_prefix`).
</td>
</tr>

</table>





