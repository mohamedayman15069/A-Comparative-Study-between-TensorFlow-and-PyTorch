<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.signal" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.contrib.signal

Signal processing operations.

<!-- Placeholder for "Used in" -->

<a href="../../tf/contrib/signal.md"><code>tf.contrib.signal</code></a> has been renamed to <a href="../../tf/signal.md"><code>tf.signal</code></a>. <a href="../../tf/contrib/signal.md"><code>tf.contrib.signal</code></a> will be
removed in TensorFlow 2.0.

See the
[Contrib Signal](https://tensorflow.org/api_guides/python/contrib.signal)
guide.


[hamming]: https://en.wikipedia.org/wiki/Window_function#Hamming_window
[hann]: https://en.wikipedia.org/wiki/Window_function#Hann_window
[mel]: https://en.wikipedia.org/wiki/Mel_scale
[mfcc]: https://en.wikipedia.org/wiki/Mel-frequency_cepstrum
[stft]: https://en.wikipedia.org/wiki/Short-time_Fourier_transform

## Functions

[`frame(...)`](../../tf/signal/frame.md): Expands `signal`'s `axis` dimension into frames of `frame_length`.

[`hamming_window(...)`](../../tf/signal/hamming_window.md): Generate a [Hamming][hamming] window.

[`hann_window(...)`](../../tf/signal/hann_window.md): Generate a [Hann window][hann].

[`inverse_stft(...)`](../../tf/signal/inverse_stft.md): Computes the inverse [Short-time Fourier Transform][stft] of `stfts`.

[`inverse_stft_window_fn(...)`](../../tf/signal/inverse_stft_window_fn.md): Generates a window function that can be used in `inverse_stft`.

[`linear_to_mel_weight_matrix(...)`](../../tf/signal/linear_to_mel_weight_matrix.md): Returns a matrix to warp linear scale spectrograms to the [mel scale][mel].

[`mfccs_from_log_mel_spectrograms(...)`](../../tf/signal/mfccs_from_log_mel_spectrograms.md): Computes [MFCCs][mfcc] of `log_mel_spectrograms`.

[`overlap_and_add(...)`](../../tf/signal/overlap_and_add.md): Reconstructs a signal from a framed representation.

[`stft(...)`](../../tf/signal/stft.md): Computes the [Short-time Fourier Transform][stft] of `signals`.

