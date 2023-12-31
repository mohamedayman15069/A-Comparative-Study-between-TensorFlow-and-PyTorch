<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.crf.viterbi_decode" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.crf.viterbi_decode

Decode the highest scoring sequence of tags outside of TensorFlow.

``` python
tf.contrib.crf.viterbi_decode(
    score,
    transition_params
)
```

<!-- Placeholder for "Used in" -->

This should only be used at test time.

#### Args:


* <b>`score`</b>: A [seq_len, num_tags] matrix of unary potentials.
* <b>`transition_params`</b>: A [num_tags, num_tags] matrix of binary potentials.


#### Returns:


* <b>`viterbi`</b>: A [seq_len] list of integers containing the highest scoring tag
    indices.
* <b>`viterbi_score`</b>: A float containing the score for the Viterbi sequence.