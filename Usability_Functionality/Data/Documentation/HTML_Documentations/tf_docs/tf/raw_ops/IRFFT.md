description: Inverse real-valued fast Fourier transform.
robots: noindex

# tf.raw_ops.IRFFT

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Inverse real-valued fast Fourier transform.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.IRFFT`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.IRFFT(
    input,
    fft_length,
    Treal=<a href="../../tf/dtypes.md#float32"><code>tf.dtypes.float32</code></a>,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the inverse 1-dimensional discrete Fourier transform of a real-valued
signal over the inner-most dimension of `input`.

The inner-most dimension of `input` is assumed to be the result of `RFFT`: the
`fft_length / 2 + 1` unique components of the DFT of a real-valued signal. If
`fft_length` is not provided, it is computed from the size of the inner-most
dimension of `input` (`fft_length = 2 * (inner - 1)`). If the FFT length used to
compute `input` is odd, it should be provided since it cannot be inferred
properly.

Along the axis `IRFFT` is computed on, if `fft_length / 2 + 1` is smaller
than the corresponding dimension of `input`, the dimension is cropped. If it is
larger, the dimension is padded with zeros.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`<a id="input"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
A complex tensor.
</td>
</tr><tr>
<td>
`fft_length`<a id="fft_length"></a>
</td>
<td>
A `Tensor` of type `int32`.
An int32 tensor of shape [1]. The FFT length.
</td>
</tr><tr>
<td>
`Treal`<a id="Treal"></a>
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.float32, tf.float64`. Defaults to <a href="../../tf.md#float32"><code>tf.float32</code></a>.
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
A `Tensor` of type `Treal`.
</td>
</tr>

</table>

