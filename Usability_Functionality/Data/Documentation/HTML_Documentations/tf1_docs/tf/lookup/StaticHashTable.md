<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.lookup.StaticHashTable" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="default_value"/>
<meta itemprop="property" content="initializer"/>
<meta itemprop="property" content="key_dtype"/>
<meta itemprop="property" content="name"/>
<meta itemprop="property" content="resource_handle"/>
<meta itemprop="property" content="value_dtype"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="export"/>
<meta itemprop="property" content="lookup"/>
<meta itemprop="property" content="size"/>
</div>

# tf.lookup.StaticHashTable

## Class `StaticHashTable`

A generic hash table that is immutable once initialized.

Inherits From: [`StaticHashTable`](../../tf/compat/v2/lookup/StaticHashTable.md)

### Aliases:

* Class `tf.compat.v1.lookup.StaticHashTable`
* Class `tf.compat.v2.compat.v1.lookup.StaticHashTable`
* Class `tf.lookup.StaticHashTable`

<!-- Placeholder for "Used in" -->

When running in graph mode, you must evaluate the tensor returned by
<a href="../../tf/initializers/tables_initializer.md"><code>tf.tables_initializer()</code></a> before evaluating the tensor returned by
this class's `lookup()` method. Example usage in graph mode:

```python
keys_tensor = tf.constant([1, 2])
vals_tensor = tf.constant([3, 4])
input_tensor = tf.constant([1, 5])
table = tf.lookup.StaticHashTable(
    tf.lookup.KeyValueTensorInitializer(keys_tensor, vals_tensor), -1)
out = table.lookup(input_tensor)
with tf.Session() as sess:
    sess.run(tf.tables_initializer())
    print(sess.run(out))
```

In eager mode, no special code is needed to initialize the table.
Example usage in eager mode:

```python
tf.enable_eager_execution()
keys_tensor = tf.constant([1, 2])
vals_tensor = tf.constant([3, 4])
input_tensor = tf.constant([1, 5])
table = tf.lookup.StaticHashTable(
    tf.lookup.KeyValueTensorInitializer(keys_tensor, vals_tensor), -1)
print(table.lookup(input_tensor))
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    initializer,
    default_value,
    name=None
)
```

Creates a non-initialized `HashTable` object.

Creates a table, the type of its keys and values are specified by the
initializer.
Before using the table you will have to initialize it. After initialization
the table will be immutable.

#### Args:


* <b>`initializer`</b>: The table initializer to use. See `HashTable` kernel for
  supported key and value types.
* <b>`default_value`</b>: The value to use if a key is missing in the table.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `HashTable` object.




## Properties

<h3 id="default_value"><code>default_value</code></h3>

The default value of the table.


<h3 id="initializer"><code>initializer</code></h3>




<h3 id="key_dtype"><code>key_dtype</code></h3>

The table key dtype.


<h3 id="name"><code>name</code></h3>

The name of the table.


<h3 id="resource_handle"><code>resource_handle</code></h3>

Returns the resource handle associated with this Resource.


<h3 id="value_dtype"><code>value_dtype</code></h3>

The table value dtype.




## Methods

<h3 id="export"><code>export</code></h3>

``` python
export(name=None)
```

Returns tensors of all keys and values in the table.


#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A pair of tensors with the first tensor containing all keys and the
  second tensors containing all values in the table.


<h3 id="lookup"><code>lookup</code></h3>

``` python
lookup(
    keys,
    name=None
)
```

Looks up `keys` in a table, outputs the corresponding values.

The `default_value` is used for keys not present in the table.

#### Args:


* <b>`keys`</b>: Keys to look up. May be either a `SparseTensor` or dense `Tensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `SparseTensor` if keys are sparse, otherwise a dense `Tensor`.



#### Raises:


* <b>`TypeError`</b>: when `keys` or `default_value` doesn't match the table data
  types.

<h3 id="size"><code>size</code></h3>

``` python
size(name=None)
```

Compute the number of elements in this table.


#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A scalar tensor containing the number of elements in this table.




