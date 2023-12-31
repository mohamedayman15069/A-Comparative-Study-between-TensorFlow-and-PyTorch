<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.lookup.LookupInterface" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="key_dtype"/>
<meta itemprop="property" content="name"/>
<meta itemprop="property" content="resource_handle"/>
<meta itemprop="property" content="value_dtype"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="lookup"/>
<meta itemprop="property" content="size"/>
</div>

# tf.contrib.lookup.LookupInterface

## Class `LookupInterface`

Represent a lookup table that persists across different steps.



<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    key_dtype,
    value_dtype
)
```

Construct a lookup table interface.


#### Args:


* <b>`key_dtype`</b>: The table key type.
* <b>`value_dtype`</b>: The table value type.



## Properties

<h3 id="key_dtype"><code>key_dtype</code></h3>

The table key dtype.


<h3 id="name"><code>name</code></h3>

The name of the table.


<h3 id="resource_handle"><code>resource_handle</code></h3>

Returns the resource handle associated with this Resource.


<h3 id="value_dtype"><code>value_dtype</code></h3>

The table value dtype.




## Methods

<h3 id="lookup"><code>lookup</code></h3>

``` python
lookup(
    keys,
    name=None
)
```

Looks up `keys` in a table, outputs the corresponding values.


<h3 id="size"><code>size</code></h3>

``` python
size(name=None)
```

Compute the number of elements in this table.




