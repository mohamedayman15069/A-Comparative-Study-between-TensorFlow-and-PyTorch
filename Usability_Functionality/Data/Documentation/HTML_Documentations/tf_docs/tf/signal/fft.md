description: Fast Fourier transform.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.fft" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.fft

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Fast Fourier transform.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.fft`, `tf.compat.v1.signal.fft`, `tf.compat.v1.spectral.fft`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.fft(
    input: Annotated[Any, TV_FFT_Tcomplex], name=None
) -> Annotated[Any, TV_FFT_Tcomplex]
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the 1-dimensional discrete Fourier transform over the inner-most
dimension of `input`.

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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

