description: Interleave the values from the data tensors into a single tensor.
robots: noindex

# tf.raw_ops.ParallelDynamicStitch

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Interleave the values from the `data` tensors into a single tensor.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ParallelDynamicStitch`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ParallelDynamicStitch(
    indices, data, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Builds a merged tensor such that

```python
    merged[indices[m][i, ..., j], ...] = data[m][i, ..., j, ...]
```

For example, if each `indices[m]` is scalar or vector, we have

```python
    # Scalar indices:
    merged[indices[m], ...] = data[m][...]

    # Vector indices:
    merged[indices[m][i], ...] = data[m][i, ...]
```

Each `data[i].shape` must start with the corresponding `indices[i].shape`,
and the rest of `data[i].shape` must be constant w.r.t. `i`.  That is, we
must have `data[i].shape = indices[i].shape + constant`.  In terms of this
`constant`, the output shape is

    merged.shape = [max(indices)] + constant

Values may be merged in parallel, so if an index appears in both `indices[m][i]`
and `indices[n][j]`, the result may be invalid. This differs from the normal
DynamicStitch operator that defines the behavior in that case.

#### For example:



```python
    indices[0] = 6
    indices[1] = [4, 1]
    indices[2] = [[5, 2], [0, 3]]
    data[0] = [61, 62]
    data[1] = [[41, 42], [11, 12]]
    data[2] = [[[51, 52], [21, 22]], [[1, 2], [31, 32]]]
    merged = [[1, 2], [11, 12], [21, 22], [31, 32], [41, 42],
              [51, 52], [61, 62]]
```

This method can be used to merge partitions created by `dynamic_partition`
as illustrated on the following example:

```python
    # Apply function (increments x_i) on elements for which a certain condition
    # apply (x_i != -1 in this example).
    x=tf.constant([0.1, -1., 5.2, 4.3, -1., 7.4])
    condition_mask=tf.not_equal(x,tf.constant(-1.))
    partitioned_data = tf.dynamic_partition(
        x, tf.cast(condition_mask, tf.int32) , 2)
    partitioned_data[1] = partitioned_data[1] + 1.0
    condition_indices = tf.dynamic_partition(
        tf.range(tf.shape(x)[0]), tf.cast(condition_mask, tf.int32) , 2)
    x = tf.dynamic_stitch(condition_indices, partitioned_data)
    # Here x=[1.1, -1., 6.2, 5.3, -1, 8.4], the -1. values remain
    # unchanged.
```

<div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src="https://www.tensorflow.org/images/DynamicStitch.png" alt>
</div>

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`indices`<a id="indices"></a>
</td>
<td>
A list of at least 1 `Tensor` objects with type `int32`.
</td>
</tr><tr>
<td>
`data`<a id="data"></a>
</td>
<td>
A list with the same length as `indices` of `Tensor` objects with the same type.
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
A `Tensor`. Has the same type as `data`.
</td>
</tr>

</table>

