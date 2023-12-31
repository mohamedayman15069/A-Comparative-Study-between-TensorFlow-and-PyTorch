<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.crf.crf_decode" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.crf.crf_decode

Decode the highest scoring sequence of tags in TensorFlow.

``` python
tf.contrib.crf.crf_decode(
    potentials,
    transition_params,
    sequence_length
)
```

<!-- Placeholder for "Used in" -->

This is a function for tensor.

#### Args:


* <b>`potentials`</b>: A [batch_size, max_seq_len, num_tags] tensor of
          unary potentials.
* <b>`transition_params`</b>: A [num_tags, num_tags] matrix of
          binary potentials.
* <b>`sequence_length`</b>: A [batch_size] vector of true sequence lengths.


#### Returns:


* <b>`decode_tags`</b>: A [batch_size, max_seq_len] matrix, with dtype <a href="../../../tf.md#int32"><code>tf.int32</code></a>.
            Contains the highest scoring tag indices.
* <b>`best_score`</b>: A [batch_size] vector, containing the score of `decode_tags`.