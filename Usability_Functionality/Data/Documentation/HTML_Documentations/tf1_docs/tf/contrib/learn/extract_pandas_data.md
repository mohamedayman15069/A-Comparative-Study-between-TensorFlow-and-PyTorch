<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.learn.extract_pandas_data" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.learn.extract_pandas_data

Extract data from pandas.DataFrame for predictors. (deprecated)

``` python
tf.contrib.learn.extract_pandas_data(data)
```

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please access pandas data directly.

Given a DataFrame, will extract the values and cast them to float. The
DataFrame is expected to contain values of type int, float or bool.

#### Args:


* <b>`data`</b>: `pandas.DataFrame` containing the data to be extracted.


#### Returns:

A numpy `ndarray` of the DataFrame's values as floats.



#### Raises:


* <b>`ValueError`</b>: if data contains types other than int, float or bool.