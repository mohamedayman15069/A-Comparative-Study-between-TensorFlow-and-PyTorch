<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.lookup.TextFileIndex" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="LINE_NUMBER"/>
<meta itemprop="property" content="WHOLE_LINE"/>
</div>

# tf.lookup.TextFileIndex

## Class `TextFileIndex`

The key and value content to get from each line.



### Aliases:

* Class `tf.compat.v1.lookup.TextFileIndex`
* Class `tf.compat.v2.compat.v1.lookup.TextFileIndex`
* Class `tf.compat.v2.lookup.TextFileIndex`
* Class `tf.contrib.lookup.TextFileIndex`
* Class `tf.lookup.TextFileIndex`

<!-- Placeholder for "Used in" -->

This class defines the key and value used for tf.lookup.TextFileInitializer.

The key and value content to get from each line is specified either
by the following, or a value `>=0`.
* <a href="../../tf/lookup/TextFileIndex.md#LINE_NUMBER"><code>TextFileIndex.LINE_NUMBER</code></a> means use the line number starting from zero,
  expects data type int64.
* <a href="../../tf/lookup/TextFileIndex.md#WHOLE_LINE"><code>TextFileIndex.WHOLE_LINE</code></a> means use the whole line content, expects data
  type string.

A value `>=0` means use the index (starting at zero) of the split line based
    on `delimiter`.

## Class Members

* `LINE_NUMBER = -1` <a id="LINE_NUMBER"></a>
* `WHOLE_LINE = -2` <a id="WHOLE_LINE"></a>
