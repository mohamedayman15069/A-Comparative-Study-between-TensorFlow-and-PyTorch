<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.profiler.Profiler" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add_step"/>
<meta itemprop="property" content="advise"/>
<meta itemprop="property" content="profile_graph"/>
<meta itemprop="property" content="profile_name_scope"/>
<meta itemprop="property" content="profile_operations"/>
<meta itemprop="property" content="profile_python"/>
<meta itemprop="property" content="serialize_to_string"/>
</div>

# tf.profiler.Profiler

## Class `Profiler`

TensorFlow multi-step profiler.



### Aliases:

* Class `tf.compat.v1.profiler.Profiler`
* Class `tf.compat.v2.compat.v1.profiler.Profiler`
* Class `tf.profiler.Profiler`

<!-- Placeholder for "Used in" -->

https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/README.md

```python
Typical use case:
  # Currently we are only allowed to create 1 profiler per process.
  profiler = Profiler(sess.graph)

  for i in xrange(total_steps):
    if i % 10000 == 0:
      run_meta = tf.compat.v1.RunMetadata()
      _ = sess.run(...,
                   options=tf.compat.v1.RunOptions(
                       trace_level=tf.RunOptions.FULL_TRACE),
                   run_metadata=run_meta)
      profiler.add_step(i, run_meta)

      # Profile the parameters of your model.
      profiler.profile_name_scope(options=(option_builder.ProfileOptionBuilder
          .trainable_variables_parameter()))

      # Or profile the timing of your model operations.
      opts = option_builder.ProfileOptionBuilder.time_and_memory()
      profiler.profile_operations(options=opts)

      # Or you can generate a timeline:
      opts = (option_builder.ProfileOptionBuilder(
              option_builder.ProfileOptionBuilder.time_and_memory())
              .with_step(i)
              .with_timeline_output(filename).build())
      profiler.profile_graph(options=opts)
    else:
      _ = sess.run(...)
  # Auto detect problems and generate advice.
  profiler.advise()
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    graph=None,
    op_log=None
)
```

Constructor.


#### Args:


* <b>`graph`</b>: tf.Graph. If None and eager execution is not enabled, use
    default graph.
* <b>`op_log`</b>: optional. tensorflow::tfprof::OpLogProto proto. Used to define
    extra op types.



## Methods

<h3 id="add_step"><code>add_step</code></h3>

``` python
add_step(
    step,
    run_meta
)
```

Add statistics of a step.


#### Args:


* <b>`step`</b>: int, An id used to group one or more different `run_meta` together.
    When profiling with the profile_xxx APIs, user can use the `step`
    id in the `options` to profile these `run_meta` together.
* <b>`run_meta`</b>: RunMetadata proto that contains statistics of a session run.

<h3 id="advise"><code>advise</code></h3>

``` python
advise(options)
```

Automatically detect problems and generate reports.


#### Args:


* <b>`options`</b>: A dict of options. See ALL_ADVICE example above.

#### Returns:

A Advise proto that conains the reports from all checkers.


<h3 id="profile_graph"><code>profile_graph</code></h3>

``` python
profile_graph(options)
```

Profile the statistics of graph nodes, organized by dataflow graph.


#### Args:


* <b>`options`</b>: A dict of options. See core/profiler/g3doc/options.md.

#### Returns:

a GraphNodeProto that records the results.


<h3 id="profile_name_scope"><code>profile_name_scope</code></h3>

``` python
profile_name_scope(options)
```

Profile the statistics of graph nodes, organized by name scope.


#### Args:


* <b>`options`</b>: A dict of options. See core/profiler/g3doc/options.md.

#### Returns:

a GraphNodeProto that records the results.


<h3 id="profile_operations"><code>profile_operations</code></h3>

``` python
profile_operations(options)
```

Profile the statistics of the Operation types (e.g. MatMul, Conv2D).


#### Args:


* <b>`options`</b>: A dict of options. See core/profiler/g3doc/options.md.

#### Returns:

a MultiGraphNodeProto that records the results.


<h3 id="profile_python"><code>profile_python</code></h3>

``` python
profile_python(options)
```

Profile the statistics of the Python codes.

  By default, it shows the call stack from root. To avoid
  redundant output, you may use options to filter as below
    options['show_name_regexes'] = ['.*my_code.py.*']

#### Args:


* <b>`options`</b>: A dict of options. See core/profiler/g3doc/options.md.

#### Returns:

a MultiGraphNodeProto that records the results.


<h3 id="serialize_to_string"><code>serialize_to_string</code></h3>

``` python
serialize_to_string()
```

Serialize the ProfileProto to a binary string.

  Users can write it to file for offline analysis by tfprof commandline
  or graphical interface.

#### Returns:

ProfileProto binary string.




