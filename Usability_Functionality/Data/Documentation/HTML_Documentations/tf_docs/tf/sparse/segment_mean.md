description: Computes the mean along sparse segments of a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.segment_mean" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.segment_mean

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/math_ops.py">View source</a>



Computes the mean along sparse segments of a tensor.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.segment_mean(
    data,
    indices,
    segment_ids,
    num_segments=None,
    name=None,
    sparse_gradient=False
)
</code></pre>



<!-- Placeholder for "Used in" -->

Read [the section on
segmentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/math#about_segmentation)
for an explanation of segments.

Like <a href="../../tf/math/segment_mean.md"><code>tf.math.segment_mean</code></a>, but `segment_ids` can have rank less than
`data`'s first dimension, selecting a subset of dimension 0, specified by
`indices`.
`segment_ids` is allowed to have missing ids, in which case the output will
be zeros at those indices. In those cases `num_segments` is used to determine
the size of the output.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`data`<a id="data"></a>
</td>
<td>
A `Tensor` with data that will be assembled in the output.
</td>
</tr><tr>
<td>
`indices`<a id="indices"></a>
</td>
<td>
A 1-D `Tensor` with indices into `data`. Has same rank as
`segment_ids`.
</td>
</tr><tr>
<td>
`segment_ids`<a id="segment_ids"></a>
</td>
<td>
A 1-D `Tensor` with indices into the output `Tensor`. Values
should be sorted and can be repeated.
</td>
</tr><tr>
<td>
`num_segments`<a id="num_segments"></a>
</td>
<td>
An optional int32 scalar. Indicates the size of the output
`Tensor`.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`sparse_gradient`<a id="sparse_gradient"></a>
</td>
<td>
An optional `bool`. Defaults to `False`. If `True`, the
gradient of this function will be sparse (`IndexedSlices`) instead of
dense (`Tensor`). The sparse gradient will contain one non-zero row for
each unique index in `indices`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `tensor` of the shape as data, except for dimension 0 which
has size `k`, the number of segments specified via `num_segments` or
inferred for the last element in `segments_ids`.
</td>
</tr>

</table>

