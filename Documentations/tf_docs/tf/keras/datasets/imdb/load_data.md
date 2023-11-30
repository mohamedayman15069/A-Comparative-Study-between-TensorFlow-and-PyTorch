description: Loads the [IMDB dataset](https://ai.stanford.edu/~amaas/data/sentiment/).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.datasets.imdb.load_data" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.datasets.imdb.load_data

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/keras-team/keras/tree/v2.15.0/keras/datasets/imdb.py#L29-L169">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Loads the [IMDB dataset](https://ai.stanford.edu/~amaas/data/sentiment/).


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.datasets.imdb.load_data(
    path=&#x27;imdb.npz&#x27;,
    num_words=None,
    skip_top=0,
    maxlen=None,
    seed=113,
    start_char=1,
    oov_char=2,
    index_from=3,
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a dataset of 25,000 movies reviews from IMDB, labeled by sentiment
(positive/negative). Reviews have been preprocessed, and each review is
encoded as a list of word indexes (integers).
For convenience, words are indexed by overall frequency in the dataset,
so that for instance the integer "3" encodes the 3rd most frequent word in
the data. This allows for quick filtering operations such as:
"only consider the top 10,000 most
common words, but eliminate the top 20 most common words".

As a convention, "0" does not stand for a specific word, but instead is used
to encode the pad token.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`path`<a id="path"></a>
</td>
<td>
where to cache the data (relative to `~/.keras/dataset`).
</td>
</tr><tr>
<td>
`num_words`<a id="num_words"></a>
</td>
<td>
integer or None. Words are
ranked by how often they occur (in the training set) and only
the `num_words` most frequent words are kept. Any less frequent word
will appear as `oov_char` value in the sequence data. If None,
all words are kept. Defaults to `None`.
</td>
</tr><tr>
<td>
`skip_top`<a id="skip_top"></a>
</td>
<td>
skip the top N most frequently occurring words
(which may not be informative). These words will appear as
`oov_char` value in the dataset. When 0, no words are
skipped. Defaults to `0`.
</td>
</tr><tr>
<td>
`maxlen`<a id="maxlen"></a>
</td>
<td>
int or None. Maximum sequence length.
Any longer sequence will be truncated. None, means no truncation.
Defaults to `None`.
</td>
</tr><tr>
<td>
`seed`<a id="seed"></a>
</td>
<td>
int. Seed for reproducible data shuffling.
</td>
</tr><tr>
<td>
`start_char`<a id="start_char"></a>
</td>
<td>
int. The start of a sequence will be marked with this
character. 0 is usually the padding character. Defaults to `1`.
</td>
</tr><tr>
<td>
`oov_char`<a id="oov_char"></a>
</td>
<td>
int. The out-of-vocabulary character.
Words that were cut out because of the `num_words` or
`skip_top` limits will be replaced with this character.
</td>
</tr><tr>
<td>
`index_from`<a id="index_from"></a>
</td>
<td>
int. Index actual words with this index and higher.
</td>
</tr><tr>
<td>
`**kwargs`<a id="**kwargs"></a>
</td>
<td>
Used for backwards compatibility.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.
</td>
</tr>

</table>


**x_train, x_test**: lists of sequences, which are lists of indexes
  (integers). If the num_words argument was specific, the maximum
  possible index value is `num_words - 1`. If the `maxlen` argument was
  specified, the largest possible sequence length is `maxlen`.

**y_train, y_test**: lists of integer labels (1 or 0).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
in case `maxlen` is so low
that no input sequence could be kept.
</td>
</tr>
</table>


Note that the 'out of vocabulary' character is only used for
words that were present in the training set but are not included
because they're not making the `num_words` cut here.
Words that were not seen in the training set but are in the test set
have simply been skipped.