description: Greedily selects a subset of bounding boxes in descending order of score.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.non_max_suppression" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.non_max_suppression

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/image_ops_impl.py">View source</a>



Greedily selects a subset of bounding boxes in descending order of score.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.non_max_suppression`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.non_max_suppression(
    boxes,
    scores,
    max_output_size,
    iou_threshold=0.5,
    score_threshold=float(&#x27;-inf&#x27;),
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Prunes away boxes that have high intersection-over-union (IOU) overlap
with previously selected boxes.  Bounding boxes are supplied as
`[y1, x1, y2, x2]`, where `(y1, x1)` and `(y2, x2)` are the coordinates of any
diagonal pair of box corners and the coordinates can be provided as normalized
(i.e., lying in the interval `[0, 1]`) or absolute.  Note that this algorithm
is agnostic to where the origin is in the coordinate system.  Note that this
algorithm is invariant to orthogonal transformations and translations
of the coordinate system; thus translating or reflections of the coordinate
system result in the same boxes being selected by the algorithm.
The output of this operation is a set of integers indexing into the input
collection of bounding boxes representing the selected boxes.  The bounding
box coordinates corresponding to the selected indices can then be obtained
using the <a href="../../tf/gather.md"><code>tf.gather</code></a> operation.  For example:
  ```python
  selected_indices = tf.image.non_max_suppression(
      boxes, scores, max_output_size, iou_threshold)
  selected_boxes = tf.gather(boxes, selected_indices)
  ```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`boxes`<a id="boxes"></a>
</td>
<td>
A 2-D float `Tensor` of shape `[num_boxes, 4]`.
</td>
</tr><tr>
<td>
`scores`<a id="scores"></a>
</td>
<td>
A 1-D float `Tensor` of shape `[num_boxes]` representing a single
score corresponding to each box (each row of boxes).
</td>
</tr><tr>
<td>
`max_output_size`<a id="max_output_size"></a>
</td>
<td>
A scalar integer `Tensor` representing the maximum number
of boxes to be selected by non-max suppression.
</td>
</tr><tr>
<td>
`iou_threshold`<a id="iou_threshold"></a>
</td>
<td>
A 0-D float tensor representing the threshold for deciding
whether boxes overlap too much with respect to IOU.
</td>
</tr><tr>
<td>
`score_threshold`<a id="score_threshold"></a>
</td>
<td>
A 0-D float tensor representing the threshold for deciding
when to remove boxes based on score.
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

<tr>
<td>
`selected_indices`<a id="selected_indices"></a>
</td>
<td>
A 1-D integer `Tensor` of shape `[M]` representing the
selected indices from the boxes tensor, where `M <= max_output_size`.
</td>
</tr>
</table>

