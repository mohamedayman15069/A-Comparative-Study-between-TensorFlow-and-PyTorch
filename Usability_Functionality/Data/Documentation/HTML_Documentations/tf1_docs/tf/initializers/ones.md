<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.initializers.ones" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
</div>

# tf.initializers.ones

## Class `ones`

Initializer that generates tensors initialized to 1.

Inherits From: [`Initializer`](../../tf/keras/initializers/Initializer.md)

### Aliases:

* Class `tf.compat.v1.initializers.ones`
* Class `tf.compat.v1.keras.initializers.Ones`
* Class `tf.compat.v1.keras.initializers.ones`
* Class `tf.compat.v1.ones_initializer`
* Class `tf.compat.v2.compat.v1.initializers.ones`
* Class `tf.compat.v2.compat.v1.keras.initializers.Ones`
* Class `tf.compat.v2.compat.v1.keras.initializers.ones`
* Class `tf.compat.v2.compat.v1.ones_initializer`
* Class `tf.initializers.ones`
* Class `tf.keras.initializers.Ones`
* Class `tf.keras.initializers.ones`
* Class `tf.ones_initializer`

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(dtype=tf.dtypes.float32)
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




