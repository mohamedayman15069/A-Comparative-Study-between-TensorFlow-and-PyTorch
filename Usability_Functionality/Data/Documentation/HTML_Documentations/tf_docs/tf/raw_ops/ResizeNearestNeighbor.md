description: Resize images to size using nearest neighbor interpolation.
robots: noindex

# tf.raw_ops.ResizeNearestNeighbor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Resize `images` to `size` using nearest neighbor interpolation.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ResizeNearestNeighbor`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ResizeNearestNeighbor(
    images, size, align_corners=False, half_pixel_centers=False, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`images`<a id="images"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`, `half`, `float32`, `float64`, `bfloat16`.
4-D with shape `[batch, height, width, channels]`.
</td>
</tr><tr>
<td>
`size`<a id="size"></a>
</td>
<td>
 A 1-D int32 Tensor of 2 elements: `new_height, new_width`.  The
new size for the images.
</td>
</tr><tr>
<td>
`align_corners`<a id="align_corners"></a>
</td>
<td>
An optional `bool`. Defaults to `False`.
If true, the centers of the 4 corner pixels of the input and output tensors are
aligned, preserving the values at the corner pixels. Defaults to false.
</td>
</tr><tr>
<td>
`half_pixel_centers`<a id="half_pixel_centers"></a>
</td>
<td>
An optional `bool`. Defaults to `False`.
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
A `Tensor`. Has the same type as `images`.
</td>
</tr>

</table>

