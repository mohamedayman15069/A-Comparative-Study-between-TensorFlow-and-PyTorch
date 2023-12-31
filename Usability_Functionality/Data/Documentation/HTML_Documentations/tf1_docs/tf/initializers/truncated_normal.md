<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.initializers.truncated_normal" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
</div>

# tf.initializers.truncated_normal

## Class `truncated_normal`

Initializer that generates a truncated normal distribution.

Inherits From: [`Initializer`](../../tf/keras/initializers/Initializer.md)

### Aliases:

* Class `tf.compat.v1.initializers.truncated_normal`
* Class `tf.compat.v1.truncated_normal_initializer`
* Class `tf.compat.v2.compat.v1.initializers.truncated_normal`
* Class `tf.compat.v2.compat.v1.truncated_normal_initializer`
* Class `tf.initializers.truncated_normal`
* Class `tf.truncated_normal_initializer`

<!-- Placeholder for "Used in" -->

These values are similar to values from a `random_normal_initializer`
except that values more than two standard deviations from the mean
are discarded and re-drawn. This is the recommended initializer for
neural network weights and filters.

#### Args:


* <b>`mean`</b>: a python scalar or a scalar tensor. Mean of the random values to
  generate.
* <b>`stddev`</b>: a python scalar or a scalar tensor. Standard deviation of the random
  values to generate.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
  <a href="../../tf/random/set_random_seed.md"><code>tf.compat.v1.set_random_seed</code></a> for behavior.
* <b>`dtype`</b>: Default data type, used if no `dtype` argument is provided when
  calling the initializer. Only floating point types are supported.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    mean=0.0,
    stddev=1.0,
    seed=None,
    dtype=tf.dtypes.float32
)
```

DEPRECATED FUNCTION ARGUMENTS

Warning: SOME ARGUMENTS ARE DEPRECATED: `(dtype)`. They will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor



## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    shape,
    dtype=None,
    partition_info=None
)
```

Returns a tensor object initialized as specified by the initializer.


#### Args:


* <b>`shape`</b>: Shape of the tensor.
* <b>`dtype`</b>: Optional dtype of the tensor. If not provided use the initializer
  dtype.
* <b>`partition_info`</b>: Optional information about the possible partitioning of a
  tensor.

<h3 id="from_config"><code>from_config</code></h3>

``` python
from_config(
    cls,
    config
)
```

Instantiates an initializer from a configuration dictionary.


#### Example:



```python
initializer = RandomUniform(-1, 1)
config = initializer.get_config()
initializer = RandomUniform.from_config(config)
```

#### Args:


* <b>`config`</b>: A Python dictionary. It will typically be the output of
  `get_config`.


#### Returns:

An Initializer instance.


<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```

Returns the configuration of the initializer as a JSON-serializable dict.


#### Returns:

A JSON-serializable Python dict.




