<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.learn.extract_pandas_labels" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.learn.extract_pandas_labels

Extract data from pandas.DataFrame for labels. (deprecated)

``` python
tf.contrib.learn.extract_pandas_labels(labels)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please access pandas data directly.

#### Args:


* <b>`labels`</b>: `pandas.DataFrame` or `pandas.Series` containing one column of
  labels to be extracted.


#### Returns:

A numpy `ndarray` of labels from the DataFrame.



#### Raises:


* <b>`ValueError`</b>: if more than one column is found or type is not int, float or
  bool.