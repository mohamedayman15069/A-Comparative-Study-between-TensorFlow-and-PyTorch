description: An optimizer that averages gradients across TPU shards.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.CrossShardOptimizer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="apply_gradients"/>
<meta itemprop="property" content="compute_gradients"/>
<meta itemprop="property" content="get_name"/>
<meta itemprop="property" content="get_slot"/>
<meta itemprop="property" content="get_slot_names"/>
<meta itemprop="property" content="minimize"/>
<meta itemprop="property" content="variables"/>
<meta itemprop="property" content="GATE_GRAPH"/>
<meta itemprop="property" content="GATE_NONE"/>
<meta itemprop="property" content="GATE_OP"/>
</div>

# tf.compat.v1.tpu.CrossShardOptimizer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/tpu/tpu_optimizer.py">View source</a>



An optimizer that averages gradients across TPU shards.

Inherits From: [`Optimizer`](../../../../tf/compat/v1/train/Optimizer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.CrossShardOptimizer(
    opt,
    reduction=losses.Reduction.MEAN,
    name=&#x27;CrossShardOptimizer&#x27;,
    group_assignment=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`opt`<a id="opt"></a>
</td>
<td>
An existing `Optimizer` to encapsulate.
</td>
</tr><tr>
<td>
`reduction`<a id="reduction"></a>
</td>
<td>
The reduction to apply to the shard losses.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
Optional name prefix for the operations created when applying
gradients. Defaults to "CrossShardOptimizer".
</td>
</tr><tr>
<td>
`group_assignment`<a id="group_assignment"></a>
</td>
<td>
Optional 2d int32 lists with shape
[num_groups, num_replicas_per_group] which describles how to apply
optimizer to subgroups.
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
If reduction is not a valid cross-shard reduction.
</td>
</tr>
</table>



## Methods

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/tpu/tpu_optimizer.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>apply_gradients(
    grads_and_vars, global_step=None, name=None
)
</code></pre>

Apply gradients to variables.

Calls tpu_ops.cross_replica_sum() to sum gradient contributions across
replicas, and then applies the real optimizer.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`grads_and_vars`
</td>
<td>
List of (gradient, variable) pairs as returned by
compute_gradients().
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
Optional Variable to increment by one after the
variables have been updated.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the returned operation.  Default to the
name passed to the Optimizer constructor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Operation` that applies the gradients. If `global_step` was not None,
that operation also increments `global_step`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the grads_and_vars is malformed.
</td>
</tr>
</table>



<h3 id="compute_gradients"><code>compute_gradients</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/tpu/tpu_optimizer.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>compute_gradients(
    loss, var_list=None, **kwargs
)
</code></pre>

Compute gradients of "loss" for the variables in "var_list".

This simply wraps `compute_gradients()` from the real optimizer. The
gradients will be aggregated in `apply_gradients()` so that user can
modify the gradients like clipping with per replica global norm if needed.
The global norm with aggregated gradients can be bad as one replica's huge
gradients can hurt the gradients from other replicas.

When the CrossShardOptimizer is constructed with
`reduction == losses.Reduction.MEAN` (default), this function scales the
loss by `1.0 / num_shards` before computing the gradients. Assuming the
optimizer uses the default implementation of `compute_gradients()`, the
gradients of the scaled loss are scaled by `1.0 / num_shards` compared to
the gradients of the original loss. This scaling factor is important because
`apply_gradients()` sums gradients across shards, rather than averaging
them. However, the scaling factor must be taken into account when clipping
the norm of the gradients or performing other postprocessing.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`loss`
</td>
<td>
A Tensor containing the value to minimize.
</td>
</tr><tr>
<td>
`var_list`
</td>
<td>
Optional list or tuple of <a href="../../../../tf/Variable.md"><code>tf.Variable</code></a> to update to minimize
`loss`.  Defaults to the list of variables collected in the graph
under the key `GraphKey.TRAINABLE_VARIABLES`.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Keyword arguments for compute_gradients().
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of (gradient, variable) pairs.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If not within a tpu_shard_context or group_assignment is
invalid.
</td>
</tr>
</table>



<h3 id="get_name"><code>get_name</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/training/optimizer.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_name()
</code></pre>




<h3 id="get_slot"><code>get_slot</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/tpu/tpu_optimizer.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_slot(
    *args, **kwargs
)
</code></pre>

Return a slot named "name" created for "var" by the Optimizer.

This simply wraps the get_slot() from the actual optimizer.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`*args`
</td>
<td>
Arguments for get_slot().
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Keyword arguments for get_slot().
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The `Variable` for the slot if it was created, `None` otherwise.
</td>
</tr>

</table>



<h3 id="get_slot_names"><code>get_slot_names</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/tpu/tpu_optimizer.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_slot_names(
    *args, **kwargs
)
</code></pre>

Return a list of the names of slots created by the `Optimizer`.

This simply wraps the get_slot_names() from the actual optimizer.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`*args`
</td>
<td>
Arguments for get_slot().
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Keyword arguments for get_slot().
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of strings.
</td>
</tr>

</table>



<h3 id="minimize"><code>minimize</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/training/optimizer.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>minimize(
    loss,
    global_step=None,
    var_list=None,
    gate_gradients=GATE_OP,
    aggregation_method=None,
    colocate_gradients_with_ops=False,
    name=None,
    grad_loss=None
)
</code></pre>

Add operations to minimize `loss` by updating `var_list`.

This method simply combines calls `compute_gradients()` and
`apply_gradients()`. If you want to process the gradient before applying
them call `compute_gradients()` and `apply_gradients()` explicitly instead
of using this function.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`loss`
</td>
<td>
A `Tensor` containing the value to minimize.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
Optional `Variable` to increment by one after the
variables have been updated.
</td>
</tr><tr>
<td>
`var_list`
</td>
<td>
Optional list or tuple of `Variable` objects to update to
minimize `loss`.  Defaults to the list of variables collected in
the graph under the key `GraphKeys.TRAINABLE_VARIABLES`.
</td>
</tr><tr>
<td>
`gate_gradients`
</td>
<td>
How to gate the computation of gradients.  Can be
`GATE_NONE`, `GATE_OP`, or  `GATE_GRAPH`.
</td>
</tr><tr>
<td>
`aggregation_method`
</td>
<td>
Specifies the method used to combine gradient terms.
Valid values are defined in the class `AggregationMethod`.
</td>
</tr><tr>
<td>
`colocate_gradients_with_ops`
</td>
<td>
If True, try colocating gradients with
the corresponding op.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the returned operation.
</td>
</tr><tr>
<td>
`grad_loss`
</td>
<td>
Optional. A `Tensor` holding the gradient computed for `loss`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An Operation that updates the variables in `var_list`.  If `global_step`
was not `None`, that operation also increments `global_step`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If some of the variables are not `Variable` objects.
</td>
</tr>
</table>




 <section><devsite-expandable expanded>
 <h4 class="showalways">eager compatibility</h4>

When eager execution is enabled, `loss` should be a Python function that
takes no arguments and computes the value to be minimized. Minimization (and
gradient computation) is done with respect to the elements of `var_list` if
not None, else with respect to any trainable variables created during the
execution of the `loss` function. `gate_gradients`, `aggregation_method`,
`colocate_gradients_with_ops` and `grad_loss` are ignored when eager
execution is enabled.

 </devsite-expandable></section>



<h3 id="variables"><code>variables</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/tpu/tpu_optimizer.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>variables()
</code></pre>

Forwarding the variables from the underlying optimizer.






<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Class Variables</h2></th></tr>

<tr>
<td>
GATE_GRAPH<a id="GATE_GRAPH"></a>
</td>
<td>
`2`
</td>
</tr><tr>
<td>
GATE_NONE<a id="GATE_NONE"></a>
</td>
<td>
`0`
</td>
</tr><tr>
<td>
GATE_OP<a id="GATE_OP"></a>
</td>
<td>
`1`
</td>
</tr>
</table>

