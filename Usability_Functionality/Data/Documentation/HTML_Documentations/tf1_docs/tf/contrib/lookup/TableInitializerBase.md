<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.lookup.TableInitializerBase" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="key_dtype"/>
<meta itemprop="property" content="value_dtype"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="initialize"/>
</div>

# tf.contrib.lookup.TableInitializerBase

## Class `TableInitializerBase`

Base class for lookup table initializers.

Inherits From: [`CheckpointableBase`](../../../tf/contrib/checkpoint/CheckpointableBase.md)

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    key_dtype,
    value_dtype
)
```

Construct a table initializer object.


#### Args:


* <b>`key_dtype`</b>: Type of the table keys.
* <b>`value_dtype`</b>: Type of the table values.



## Properties

<h3 id="key_dtype"><code>key_dtype</code></h3>

The expected table key dtype.


<h3 id="value_dtype"><code>value_dtype</code></h3>

The expected table value dtype.




## Methods

<h3 id="initialize"><code>initialize</code></h3>

``` python
initialize(table)
```

Returns the table initialization op.




