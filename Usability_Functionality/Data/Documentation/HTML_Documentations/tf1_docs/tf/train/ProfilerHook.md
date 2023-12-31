<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.train.ProfilerHook" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="after_create_session"/>
<meta itemprop="property" content="after_run"/>
<meta itemprop="property" content="before_run"/>
<meta itemprop="property" content="begin"/>
<meta itemprop="property" content="end"/>
</div>

# tf.train.ProfilerHook

## Class `ProfilerHook`

Captures CPU/GPU profiling information every N steps or seconds.

Inherits From: [`SessionRunHook`](../../tf/train/SessionRunHook.md)

### Aliases:

* Class `tf.compat.v1.estimator.ProfilerHook`
* Class `tf.compat.v1.train.ProfilerHook`
* Class `tf.compat.v2.compat.v1.estimator.ProfilerHook`
* Class `tf.compat.v2.compat.v1.train.ProfilerHook`
* Class `tf.compat.v2.estimator.ProfilerHook`
* Class `tf.estimator.ProfilerHook`
* Class `tf.train.ProfilerHook`

<!-- Placeholder for "Used in" -->

This produces files called "timeline-<step>.json", which are in Chrome
Trace format.

For more information see:
https://github.com/catapult-project/catapult/blob/master/tracing/README.md

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    save_steps=None,
    save_secs=None,
    output_dir='',
    show_dataflow=True,
    show_memory=False
)
```

Initializes a hook that takes periodic profiling snapshots.

`options.run_metadata` argument of `tf.Session.Run` is used to collect
metadata about execution. This hook sets the metadata and dumps it in Chrome
Trace format.


#### Args:


* <b>`save_steps`</b>: `int`, save profile traces every N steps. Exactly one of
  `save_secs` and `save_steps` should be set.
* <b>`save_secs`</b>: `int` or `float`, save profile traces every N seconds.
* <b>`output_dir`</b>: `string`, the directory to save the profile traces to.
  Defaults to the current directory.
* <b>`show_dataflow`</b>: `bool`, if True, add flow events to the trace connecting
  producers and consumers of tensors.
* <b>`show_memory`</b>: `bool`, if True, add object snapshot events to the trace
  showing the sizes and lifetimes of tensors.



## Methods

<h3 id="after_create_session"><code>after_create_session</code></h3>

``` python
after_create_session(
    session,
    coord
)
```

Called when new TensorFlow session is created.

This is called to signal the hooks that a new session has been created. This
has two essential differences with the situation in which `begin` is called:

* When this is called, the graph is finalized and ops can no longer be added
    to the graph.
* This method will also be called as a result of recovering a wrapped
    session, not only at the beginning of the overall session.

#### Args:


* <b>`session`</b>: A TensorFlow Session that has been created.
* <b>`coord`</b>: A Coordinator object which keeps track of all threads.

<h3 id="after_run"><code>after_run</code></h3>

``` python
after_run(
    run_context,
    run_values
)
```

Called after each call to run().

The `run_values` argument contains results of requested ops/tensors by
`before_run()`.

The `run_context` argument is the same one send to `before_run` call.
`run_context.request_stop()` can be called to stop the iteration.

If `session.run()` raises any exceptions then `after_run()` is not called.

#### Args:


* <b>`run_context`</b>: A `SessionRunContext` object.
* <b>`run_values`</b>: A SessionRunValues object.

<h3 id="before_run"><code>before_run</code></h3>

``` python
before_run(run_context)
```

Called before each call to run().

You can return from this call a `SessionRunArgs` object indicating ops or
tensors to add to the upcoming `run()` call.  These ops/tensors will be run
together with the ops/tensors originally passed to the original run() call.
The run args you return can also contain feeds to be added to the run()
call.

The `run_context` argument is a `SessionRunContext` that provides
information about the upcoming `run()` call: the originally requested
op/tensors, the TensorFlow Session.

At this point graph is finalized and you can not add ops.

#### Args:


* <b>`run_context`</b>: A `SessionRunContext` object.


#### Returns:

None or a `SessionRunArgs` object.


<h3 id="begin"><code>begin</code></h3>

``` python
begin()
```

Called once before using the session.

When called, the default graph is the one that will be launched in the
session.  The hook can modify the graph by adding new operations to it.
After the `begin()` call the graph will be finalized and the other callbacks
can not modify the graph anymore. Second call of `begin()` on the same
graph, should not change the graph.

<h3 id="end"><code>end</code></h3>

``` python
end(session)
```

Called at the end of session.

The `session` argument can be used in case the hook wants to run final ops,
such as saving a last checkpoint.

If `session.run()` raises exception other than OutOfRangeError or
StopIteration then `end()` is not called.
Note the difference between `end()` and `after_run()` behavior when
`session.run()` raises OutOfRangeError or StopIteration. In that case
`end()` is called but `after_run()` is not called.

#### Args:


* <b>`session`</b>: A TensorFlow Session that will be soon closed.



