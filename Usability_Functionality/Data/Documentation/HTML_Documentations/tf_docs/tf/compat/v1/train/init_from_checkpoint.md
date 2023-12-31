description: Replaces <a href="../../../../tf/Variable.md"><code>tf.Variable</code></a> initializers so they load from a checkpoint file.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.init_from_checkpoint" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.init_from_checkpoint

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/training/checkpoint_utils.py">View source</a>



Replaces <a href="../../../../tf/Variable.md"><code>tf.Variable</code></a> initializers so they load from a checkpoint file.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.init_from_checkpoint(
    ckpt_dir_or_file, assignment_map
)
</code></pre>





 <section><devsite-expandable expanded>
 <h2 class="showalways">Migrate to TF2</h2>

Caution: This API was designed for TensorFlow v1.
Continue reading for details on how to migrate from this API to a native
TensorFlow v2 equivalent. See the
[TensorFlow v1 to TensorFlow v2 migration guide](https://www.tensorflow.org/guide/migrate)
for instructions on how to migrate the rest of your code.

<a href="../../../../tf/compat/v1/train/init_from_checkpoint.md"><code>tf.compat.v1.train.init_from_checkpoint</code></a> is not recommended for restoring
variable values in TF2.

To restore checkpoints in TF2, please use
<a href="../../../../tf/keras/Model.md#load_weights"><code>tf.keras.Model.load_weights</code></a> or <a href="../../../../tf/train/Checkpoint.md#restore"><code>tf.train.Checkpoint.restore</code></a>. These APIs use
use an [object-based method of checkpointing]
(https://www.tensorflow.org/guide/checkpoint#loading_mechanics), while
`tf.compat.v1.init_from_checkpoint` relies on a more-fragile variable-name
based method of checkpointing. There is no object-based equivalent of
`init_from_checkpoint` in TF2.

Please re-write your checkpoints immediately using the object-based APIs,
see [migration guide]
(https://www.tensorflow.org/guide/migrate#checkpoint_compatibility) for more
details.

You can load a name-based checkpoint written by <a href="../../../../tf/compat/v1/train/Saver.md"><code>tf.compat.v1.train.Saver</code></a>
using <a href="../../../../tf/train/Checkpoint.md#restore"><code>tf.train.Checkpoint.restore</code></a> or <a href="../../../../tf/keras/Model.md#load_weights"><code>tf.keras.Model.load_weights</code></a>. However,
you may have to change the names of the variables in your model to match the
variable names in the name-based checkpoint, which can be viewed with
<a href="../../../../tf/train/list_variables.md"><code>tf.train.list_variables(path)</code></a>.

Another option is to create an `assignment_map` that maps the name of the
variables in the name-based checkpoint to the variables in your model, eg:
```
{
    'sequential/dense/bias': model.variables[0],
    'sequential/dense/kernel': model.variables[1]
}
```
and use <a href="../../../../tf/compat/v1/train/init_from_checkpoint.md"><code>tf.compat.v1.train.init_from_checkpoint(path, assignment_map)</code></a> to
restore the name-based checkpoint.

After restoring, re-encode your checkpoint using <a href="../../../../tf/train/Checkpoint.md#save"><code>tf.train.Checkpoint.save</code></a>
or <a href="../../../../tf/keras/Model.md#save_weights"><code>tf.keras.Model.save_weights</code></a>.


 </aside></devsite-expandable></section>

<h2>Description</h2>

<!-- Placeholder for "Used in" -->



Values are not loaded immediately, but when the initializer is run
(typically by running a <a href="../../../../tf/compat/v1/global_variables_initializer.md"><code>tf.compat.v1.global_variables_initializer</code></a> op).

Note: This overrides default initialization ops of specified variables and
redefines dtype.

Assignment map supports following syntax:

* `'checkpoint_scope_name/': 'scope_name/'` - will load all variables in
  current `scope_name` from `checkpoint_scope_name` with matching tensor
  names.
* `'checkpoint_scope_name/some_other_variable': 'scope_name/variable_name'` -
  will initialize `scope_name/variable_name` variable
  from `checkpoint_scope_name/some_other_variable`.
* `'scope_variable_name': variable` - will initialize given <a href="../../../../tf/Variable.md"><code>tf.Variable</code></a>
  object with tensor 'scope_variable_name' from the checkpoint.
* `'scope_variable_name': list(variable)` - will initialize list of
  partitioned variables with tensor 'scope_variable_name' from the checkpoint.
* `'/': 'scope_name/'` - will load all variables in current `scope_name` from
  checkpoint's root (e.g. no scope).

Supports loading into partitioned variables, which are represented as
`'<variable>/part_<part #>'`.

Assignment map can be a dict, or a list of pairs.  The latter is
necessary to initialize multiple variables in the current graph from
the same variable in the checkpoint.

#### Example:



```python

# Say, '/tmp/model.ckpt' has the following tensors:
#  -- name='old_scope_1/var1', shape=[20, 2]
#  -- name='old_scope_1/var2', shape=[50, 4]
#  -- name='old_scope_2/var3', shape=[100, 100]

# Create new model's variables
with tf.compat.v1.variable_scope('new_scope_1'):
  var1 = tf.compat.v1.get_variable('var1', shape=[20, 2],
                         initializer=tf.compat.v1.zeros_initializer())
with tf.compat.v1.variable_scope('new_scope_2'):
  var2 = tf.compat.v1.get_variable('var2', shape=[50, 4],
                         initializer=tf.compat.v1.zeros_initializer())
  # Partition into 5 variables along the first axis.
  var3 = tf.compat.v1.get_variable(name='var3', shape=[100, 100],
                         initializer=tf.compat.v1.zeros_initializer(),
                         partitioner=lambda shape, dtype: [5, 1])

# Initialize all variables in `new_scope_1` from `old_scope_1`.
init_from_checkpoint('/tmp/model.ckpt', {'old_scope_1/': 'new_scope_1/'})

# Use names to specify which variables to initialize from checkpoint.
init_from_checkpoint('/tmp/model.ckpt',
                     {'old_scope_1/var1': 'new_scope_1/var1',
                      'old_scope_1/var2': 'new_scope_2/var2'})

# Or use tf.Variable objects to identify what to initialize.
init_from_checkpoint('/tmp/model.ckpt',
                     {'old_scope_1/var1': var1,
                      'old_scope_1/var2': var2})

# Initialize partitioned variables using variable's name
init_from_checkpoint('/tmp/model.ckpt',
                     {'old_scope_2/var3': 'new_scope_2/var3'})

# Or specify the list of tf.Variable objects.
init_from_checkpoint('/tmp/model.ckpt',
                     {'old_scope_2/var3': var3._get_variable_list()})

```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ckpt_dir_or_file`<a id="ckpt_dir_or_file"></a>
</td>
<td>
Directory with checkpoints file or path to checkpoint.
</td>
</tr><tr>
<td>
`assignment_map`<a id="assignment_map"></a>
</td>
<td>
Dict, or a list of key-value pairs, where keys are names
of the variables in the checkpoint and values are current variables or
names of current variables (in default graph).
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
If missing variables in current graph, or if missing
checkpoints or tensors in checkpoints.
</td>
</tr>
</table>

