description: Log provided 'op_log', and add additional model information below.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.profiler.write_op_log" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.profiler.write_op_log

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/profiler/tfprof_logger.py">View source</a>



Log provided 'op_log', and add additional model information below.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.profiler.write_op_log(
    graph, log_dir, op_log=None, run_meta=None, add_trace=True
)
</code></pre>



<!-- Placeholder for "Used in" -->

  The API also assigns ops in tf.compat.v1.trainable_variables() an op type
  called '_trainable_variables'.
  The API also logs 'flops' statistics for ops with op.RegisterStatistics()
  defined. flops calculation depends on Tensor shapes defined in 'graph',
  which might not be complete. 'run_meta', if provided, completes the shape
  information with best effort.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`graph`<a id="graph"></a>
</td>
<td>
tf.Graph. If None and eager execution is not enabled, use
default graph.
</td>
</tr><tr>
<td>
`log_dir`<a id="log_dir"></a>
</td>
<td>
directory to write the log file.
</td>
</tr><tr>
<td>
`op_log`<a id="op_log"></a>
</td>
<td>
(Optional) OpLogProto proto to be written. If not provided, an new
one is created.
</td>
</tr><tr>
<td>
`run_meta`<a id="run_meta"></a>
</td>
<td>
(Optional) RunMetadata proto that helps flops computation using
run time shape information.
</td>
</tr><tr>
<td>
`add_trace`<a id="add_trace"></a>
</td>
<td>
Whether to add python code trace information.
Used to support "code" view.
</td>
</tr>
</table>

