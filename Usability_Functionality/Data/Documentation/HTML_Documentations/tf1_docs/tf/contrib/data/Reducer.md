<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.data.Reducer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="finalize_func"/>
<meta itemprop="property" content="init_func"/>
<meta itemprop="property" content="reduce_func"/>
<meta itemprop="property" content="__init__"/>
</div>

# tf.contrib.data.Reducer

## Class `Reducer`

A reducer is used for reducing a set of elements.

Inherits From: [`Reducer`](../../../tf/data/experimental/Reducer.md)

<!-- Placeholder for "Used in" -->

A reducer is represented as a tuple of the three functions:
  1) initialization function: key => initial state
  2) reduce function: (old state, input) => new state
  3) finalization function: state => result

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    init_func,
    reduce_func,
    finalize_func
)
```

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/experimental/Reducer.md"><code>tf.data.experimental.Reducer(...)</code></a>.



## Properties

<h3 id="finalize_func"><code>finalize_func</code></h3>




<h3 id="init_func"><code>init_func</code></h3>




<h3 id="reduce_func"><code>reduce_func</code></h3>






