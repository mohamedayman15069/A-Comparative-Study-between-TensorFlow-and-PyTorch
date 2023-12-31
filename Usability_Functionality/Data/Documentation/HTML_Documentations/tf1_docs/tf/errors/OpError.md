<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.errors.OpError" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="error_code"/>
<meta itemprop="property" content="message"/>
<meta itemprop="property" content="node_def"/>
<meta itemprop="property" content="op"/>
<meta itemprop="property" content="__init__"/>
</div>

# tf.errors.OpError

## Class `OpError`

A generic error that is raised when TensorFlow execution fails.



### Aliases:

* Class `tf.OpError`
* Class `tf.compat.v1.OpError`
* Class `tf.compat.v1.errors.OpError`
* Class `tf.compat.v2.compat.v1.OpError`
* Class `tf.compat.v2.compat.v1.errors.OpError`
* Class `tf.compat.v2.errors.OpError`
* Class `tf.errors.OpError`

<!-- Placeholder for "Used in" -->

Whenever possible, the session will raise a more specific subclass
of `OpError` from the <a href="../../tf/errors.md"><code>tf.errors</code></a> module.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    node_def,
    op,
    message,
    error_code
)
```

Creates a new `OpError` indicating that a particular op failed.


#### Args:


* <b>`node_def`</b>: The `node_def_pb2.NodeDef` proto representing the op that
  failed, if known; otherwise None.
* <b>`op`</b>: The `ops.Operation` that failed, if known; otherwise None.
* <b>`message`</b>: The message string describing the failure.
* <b>`error_code`</b>: The `error_codes_pb2.Code` describing the error.



## Properties

<h3 id="error_code"><code>error_code</code></h3>

The integer error code that describes the error.


<h3 id="message"><code>message</code></h3>

The error message that describes the error.


<h3 id="node_def"><code>node_def</code></h3>

The `NodeDef` proto representing the op that failed.


<h3 id="op"><code>op</code></h3>

The operation that failed, if known.

*N.B.* If the failed op was synthesized at runtime, e.g. a `Send`
or `Recv` op, there will be no corresponding
<a href="../../tf/Operation.md"><code>tf.Operation</code></a>
object.  In that case, this will return `None`, and you should
instead use the <a href="../../tf/errors/OpError.md#node_def"><code>tf.errors.OpError.node_def</code></a> to
discover information about the op.

#### Returns:

The `Operation` that failed, or None.




