<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.crf.crf_binary_score" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.crf.crf_binary_score

Computes the binary scores of tag sequences.

``` python
tf.contrib.crf.crf_binary_score(
    tag_indices,
    sequence_lengths,
    transition_params
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`tag_indices`</b>: A [batch_size, max_seq_len] matrix of tag indices.
* <b>`sequence_lengths`</b>: A [batch_size] vector of true sequence lengths.
* <b>`transition_params`</b>: A [num_tags, num_tags] matrix of binary potentials.

#### Returns:


* <b>`binary_scores`</b>: A [batch_size] vector of binary scores.