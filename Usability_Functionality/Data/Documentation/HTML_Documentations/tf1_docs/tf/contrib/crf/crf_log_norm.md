<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.crf.crf_log_norm" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.crf.crf_log_norm

Computes the normalization for a CRF.

``` python
tf.contrib.crf.crf_log_norm(
    inputs,
    sequence_lengths,
    transition_params
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`inputs`</b>: A [batch_size, max_seq_len, num_tags] tensor of unary potentials
    to use as input to the CRF layer.
* <b>`sequence_lengths`</b>: A [batch_size] vector of true sequence lengths.
* <b>`transition_params`</b>: A [num_tags, num_tags] transition matrix.

#### Returns:


* <b>`log_norm`</b>: A [batch_size] vector of normalizers for a CRF.