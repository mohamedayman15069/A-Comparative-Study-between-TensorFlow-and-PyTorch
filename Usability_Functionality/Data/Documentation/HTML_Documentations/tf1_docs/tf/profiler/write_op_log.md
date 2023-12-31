<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.profiler.write_op_log" />
<meta itemprop="path" content="Stable" />
</div>

# tf.profiler.write_op_log

Log provided 'op_log', and add additional model information below.

### Aliases:

* `tf.compat.v1.profiler.write_op_log`
* `tf.compat.v2.compat.v1.profiler.write_op_log`
* `tf.profiler.write_op_log`

``` python
tf.profiler.write_op_log(
    graph,
    log_dir,
    op_log=None,
    run_meta=None,
    add_trace=True
)
```

<!-- Placeholder for "Used in" -->

  The API also assigns ops in tf.compat.v1.trainable_variables() an op type
  called '_trainable_variables'.
  The API also logs 'flops' statistics for ops with op.RegisterStatistics()
  defined. flops calculation depends on Tensor shapes defined in 'graph',
  which might not be complete. 'run_meta', if provided, completes the shape
  information with best effort.

#### Args:


* <b>`graph`</b>: tf.Graph. If None and eager execution is not enabled, use
    default graph.
* <b>`log_dir`</b>: directory to write the log file.
* <b>`op_log`</b>: (Optional) OpLogProto proto to be written. If not provided, an new
    one is created.
* <b>`run_meta`</b>: (Optional) RunMetadata proto that helps flops computation using
    run time shape information.
* <b>`add_trace`</b>: Whether to add python code trace information.
    Used to support "code" view.