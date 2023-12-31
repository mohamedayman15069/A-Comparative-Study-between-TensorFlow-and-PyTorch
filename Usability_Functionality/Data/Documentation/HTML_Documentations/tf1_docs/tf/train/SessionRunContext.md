<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.train.SessionRunContext" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="original_args"/>
<meta itemprop="property" content="session"/>
<meta itemprop="property" content="stop_requested"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="request_stop"/>
</div>

# tf.train.SessionRunContext

## Class `SessionRunContext`

Provides information about the `session.run()` call being made.



### Aliases:

* Class `tf.compat.v1.estimator.SessionRunContext`
* Class `tf.compat.v1.train.SessionRunContext`
* Class `tf.compat.v2.compat.v1.estimator.SessionRunContext`
* Class `tf.compat.v2.compat.v1.train.SessionRunContext`
* Class `tf.compat.v2.estimator.SessionRunContext`
* Class `tf.estimator.SessionRunContext`
* Class `tf.train.SessionRunContext`

<!-- Placeholder for "Used in" -->

Provides information about original request to `Session.Run()` function.
SessionRunHook objects can stop the loop by calling `request_stop()` of
`run_context`. In the future we may use this object to add more information
about run without changing the Hook API.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    original_args,
    session
)
```

Initializes SessionRunContext.




## Properties

<h3 id="original_args"><code>original_args</code></h3>

A `SessionRunArgs` object holding the original arguments of `run()`.

If user called <a href="../../tf/train/MonitoredSession.md#run"><code>MonitoredSession.run(fetches=a, feed_dict=b)</code></a>, then this
field is equal to SessionRunArgs(a, b).

#### Returns:

A `SessionRunArgs` object


<h3 id="session"><code>session</code></h3>

A TensorFlow session object which will execute the `run`.


<h3 id="stop_requested"><code>stop_requested</code></h3>

Returns whether a stop is requested or not.

If true, `MonitoredSession` stops iterations.
Returns:
  A `bool`



## Methods

<h3 id="request_stop"><code>request_stop</code></h3>

``` python
request_stop()
```

Sets stop requested field.

Hooks can use this function to request stop of iterations.
`MonitoredSession` checks whether this is called or not.



