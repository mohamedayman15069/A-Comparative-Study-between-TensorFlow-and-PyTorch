description: Greedily selects a subset of bounding boxes in descending order of score.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.combined_non_max_suppression" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.combined_non_max_suppression

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
<p>`tf.compat.v1.image.combined_non_max_suppression`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.combined_non_max_suppression(
    boxes,
    scores,
    max_output_size_per_class,
    max_total_size,
    iou_threshold=0.5,
    score_threshold=float(&#x27;-inf&#x27;),
    pad_per_class=False,
    clip_boxes=True,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation performs non_max_suppression on the inputs per batch, across
all classes.
Prunes away boxes that have high intersection-over-union (IOU) overlap
with previously selected boxes.  Bounding boxes are supplied as
[y1, x1, y2, x2], where (y1, x1) and (y2, x2) are the coordinates of any
diagonal pair of box corners and the coordinates can be provided as normalized
(i.e., lying in the interval [0, 1]) or absolute.  Note that this algorithm
is agnostic to where the origin is in the coordinate system. Also note that
this algorithm is invariant to orthogonal transformations and translations
of the coordinate system; thus translating or reflections of the coordinate
system result in the same boxes being selected by the algorithm.
The output of this operation is the final boxes, scores and classes tensor
returned after performing non_max_suppression.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`boxes`<a id="boxes"></a>
</td>
<td>
A 4-D float `Tensor` of shape `[batch_size, num_boxes, q, 4]`. If `q`
is 1 then same boxes are used for all classes otherwise, if `q` is equal
to number of classes, class-specific boxes are used.
</td>
</tr><tr>
<td>
`scores`<a id="scores"></a>
</td>
<td>
A 3-D float `Tensor` of shape `[batch_size, num_boxes, num_classes]`
representing a single score corresponding to each box (each row of boxes).
</td>
</tr><tr>
<td>
`max_output_size_per_class`<a id="max_output_size_per_class"></a>
</td>
<td>
A scalar integer `Tensor` representing the
maximum number of boxes to be selected by non-max suppression per class
</td>
</tr><tr>
<td>
`max_total_size`<a id="max_total_size"></a>
</td>
<td>
A int32 scalar representing maximum number of boxes retained
over all classes. Note that setting this value to a large number may
result in OOM error depending on the system workload.
</td>
</tr><tr>
<td>
`iou_threshold`<a id="iou_threshold"></a>
</td>
<td>
A float representing the threshold for deciding whether boxes
overlap too much with respect to IOU.
</td>
</tr><tr>
<td>
`score_threshold`<a id="score_threshold"></a>
</td>
<td>
A float representing the threshold for deciding when to
remove boxes based on score.
</td>
</tr><tr>
<td>
`pad_per_class`<a id="pad_per_class"></a>
</td>
<td>
If false, the output nmsed boxes, scores and classes are
padded/clipped to `max_total_size`. If true, the output nmsed boxes,
scores and classes are padded to be of length
`max_size_per_class`*`num_classes`, unless it exceeds `max_total_size` in
which case it is clipped to `max_total_size`. Defaults to false.
</td>
</tr><tr>
<td>
`clip_boxes`<a id="clip_boxes"></a>
</td>
<td>
If true, the coordinates of output nmsed boxes will be clipped
to [0, 1]. If false, output the box coordinates as it is. Defaults to
true.
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
`'nmsed_boxes'`<a id="'nmsed_boxes'"></a>
</td>
<td>
A [batch_size, max_detections, 4] float32 tensor
containing the non-max suppressed boxes.
</td>
</tr><tr>
<td>
`'nmsed_scores'`<a id="'nmsed_scores'"></a>
</td>
<td>
A [batch_size, max_detections] float32 tensor containing
the scores for the boxes.
</td>
</tr><tr>
<td>
`'nmsed_classes'`<a id="'nmsed_classes'"></a>
</td>
<td>
A [batch_size, max_detections] float32 tensor
containing the class for boxes.
</td>
</tr><tr>
<td>
`'valid_detections'`<a id="'valid_detections'"></a>
</td>
<td>
A [batch_size] int32 tensor indicating the number of
valid detections per batch item. Only the top valid_detections[i] entries
in nms_boxes[i], nms_scores[i] and nms_class[i] are valid. The rest of the
entries are zero paddings.
</td>
</tr>
</table>

