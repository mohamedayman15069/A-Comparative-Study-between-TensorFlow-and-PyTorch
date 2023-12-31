description: Decode a JPEG-encoded image to a uint8 tensor.
robots: noindex

# tf.raw_ops.DecodeJpeg

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Decode a JPEG-encoded image to a uint8 tensor.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DecodeJpeg`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DecodeJpeg(
    contents,
    channels=0,
    ratio=1,
    fancy_upscaling=True,
    try_recover_truncated=False,
    acceptable_fraction=1,
    dct_method=&#x27;&#x27;,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The attr `channels` indicates the desired number of color channels for the
decoded image.

#### Accepted values are:



*   0: Use the number of channels in the JPEG-encoded image.
*   1: output a grayscale image.
*   3: output an RGB image.

If needed, the JPEG-encoded image is transformed to match the requested number
of color channels.

The attr `ratio` allows downscaling the image by an integer factor during
decoding.  Allowed values are: 1, 2, 4, and 8.  This is much faster than
downscaling the image later.


This op also supports decoding PNGs and non-animated GIFs since the interface is
the same, though it is cleaner to use <a href="../../tf/io/decode_image.md"><code>tf.io.decode_image</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`contents`<a id="contents"></a>
</td>
<td>
A `Tensor` of type `string`. 0-D.  The JPEG-encoded image.
</td>
</tr><tr>
<td>
`channels`<a id="channels"></a>
</td>
<td>
An optional `int`. Defaults to `0`.
Number of color channels for the decoded image.
</td>
</tr><tr>
<td>
`ratio`<a id="ratio"></a>
</td>
<td>
An optional `int`. Defaults to `1`. Downscaling ratio.
</td>
</tr><tr>
<td>
`fancy_upscaling`<a id="fancy_upscaling"></a>
</td>
<td>
An optional `bool`. Defaults to `True`.
If true use a slower but nicer upscaling of the
chroma planes (yuv420/422 only).
</td>
</tr><tr>
<td>
`try_recover_truncated`<a id="try_recover_truncated"></a>
</td>
<td>
An optional `bool`. Defaults to `False`.
If true try to recover an image from truncated input.
</td>
</tr><tr>
<td>
`acceptable_fraction`<a id="acceptable_fraction"></a>
</td>
<td>
An optional `float`. Defaults to `1`.
The minimum required fraction of lines before a truncated
input is accepted.
</td>
</tr><tr>
<td>
`dct_method`<a id="dct_method"></a>
</td>
<td>
An optional `string`. Defaults to `""`.
string specifying a hint about the algorithm used for
decompression.  Defaults to "" which maps to a system-specific
default.  Currently valid values are ["INTEGER_FAST",
"INTEGER_ACCURATE"].  The hint may be ignored (e.g., the internal
jpeg library changes to a version that does not have that specific
option.)
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
A `Tensor` of type `uint8`.
</td>
</tr>

</table>

