<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.profiler.advise" />
<meta itemprop="path" content="Stable" />
</div>

# tf.profiler.advise

Auto profile and advise.

### Aliases:

* `tf.compat.v1.profiler.advise`
* `tf.compat.v2.compat.v1.profiler.advise`
* `tf.profiler.advise`

``` python
tf.profiler.advise(
    graph=None,
    run_meta=None,
    options=_DEFAULT_ADVISE_OPTIONS
)
```

<!-- Placeholder for "Used in" -->

  Builds profiles and automatically check anomalies of various
  aspects. For more details:
  https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/README.md

#### Args:


* <b>`graph`</b>: tf.Graph. If None and eager execution is not enabled, use
    default graph.
* <b>`run_meta`</b>: optional tensorflow.RunMetadata proto. It is necessary to
    to support run time information profiling, such as time and memory.
* <b>`options`</b>: see ALL_ADVICE example above. Default checks everything.

#### Returns:

Returns AdviceProto proto
