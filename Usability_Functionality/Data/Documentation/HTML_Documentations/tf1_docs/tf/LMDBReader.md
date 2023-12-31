<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.LMDBReader" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="reader_ref"/>
<meta itemprop="property" content="supports_serialize"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="num_records_produced"/>
<meta itemprop="property" content="num_work_units_completed"/>
<meta itemprop="property" content="read"/>
<meta itemprop="property" content="read_up_to"/>
<meta itemprop="property" content="reset"/>
<meta itemprop="property" content="restore_state"/>
<meta itemprop="property" content="serialize_state"/>
</div>

# tf.LMDBReader

## Class `LMDBReader`

A Reader that outputs the records from a LMDB file.

Inherits From: [`ReaderBase`](../tf/ReaderBase.md)

### Aliases:

* Class `tf.LMDBReader`
* Class `tf.compat.v1.LMDBReader`
* Class `tf.compat.v2.compat.v1.LMDBReader`

<!-- Placeholder for "Used in" -->

See ReaderBase for supported methods.



#### Eager Compatibility
Readers are not compatible with eager execution. Instead, please
use <a href="../tf/data.md"><code>tf.data</code></a> to get data into your model.



<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    name=None,
    options=None
)
```

Create a LMDBReader. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Queue-based input pipelines have been replaced by <a href="../tf/data.md"><code>tf.data</code></a>. Use <a href="../tf/contrib/data/LMDBDataset.md"><code>tf.contrib.data.LMDBDataset</code></a>.

#### Args:


* <b>`name`</b>: A name for the operation (optional).
* <b>`options`</b>: A LMDBRecordOptions object (optional).



## Properties

<h3 id="reader_ref"><code>reader_ref</code></h3>

Op that implements the reader.


<h3 id="supports_serialize"><code>supports_serialize</code></h3>

Whether the Reader implementation can serialize its state.




## Methods

<h3 id="num_records_produced"><code>num_records_produced</code></h3>

``` python
num_records_produced(name=None)
```

Returns the number of records this reader has produced.

This is the same as the number of Read executions that have
succeeded.

#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

An int64 Tensor.


<h3 id="num_work_units_completed"><code>num_work_units_completed</code></h3>

``` python
num_work_units_completed(name=None)
```

Returns the number of work units this reader has finished processing.


#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

An int64 Tensor.


<h3 id="read"><code>read</code></h3>

``` python
read(
    queue,
    name=None
)
```

Returns the next record (key, value) pair produced by a reader.

Will dequeue a work unit from queue if necessary (e.g. when the
Reader needs to start reading from a new file since it has
finished with the previous file).

#### Args:


* <b>`queue`</b>: A Queue or a mutable string Tensor representing a handle
  to a Queue, with string work items.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of Tensors (key, value).

* <b>`key`</b>: A string scalar Tensor.
* <b>`value`</b>: A string scalar Tensor.

<h3 id="read_up_to"><code>read_up_to</code></h3>

``` python
read_up_to(
    queue,
    num_records,
    name=None
)
```

Returns up to num_records (key, value) pairs produced by a reader.

Will dequeue a work unit from queue if necessary (e.g., when the
Reader needs to start reading from a new file since it has
finished with the previous file).
It may return less than num_records even before the last batch.

#### Args:


* <b>`queue`</b>: A Queue or a mutable string Tensor representing a handle
  to a Queue, with string work items.
* <b>`num_records`</b>: Number of records to read.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of Tensors (keys, values).

* <b>`keys`</b>: A 1-D string Tensor.
* <b>`values`</b>: A 1-D string Tensor.

<h3 id="reset"><code>reset</code></h3>

``` python
reset(name=None)
```

Restore a reader to its initial clean state.


#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.


<h3 id="restore_state"><code>restore_state</code></h3>

``` python
restore_state(
    state,
    name=None
)
```

Restore a reader to a previously saved state.

Not all Readers support being restored, so this can produce an
Unimplemented error.

#### Args:


* <b>`state`</b>: A string Tensor.
  Result of a SerializeState of a Reader with matching type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.


<h3 id="serialize_state"><code>serialize_state</code></h3>

``` python
serialize_state(name=None)
```

Produce a string tensor that encodes the state of a reader.

Not all Readers support being serialized, so this can produce an
Unimplemented error.

#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A string Tensor.




