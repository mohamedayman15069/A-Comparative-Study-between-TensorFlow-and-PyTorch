<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.threading.set_inter_op_parallelism_threads" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.threading.set_inter_op_parallelism_threads

Set number of threads used for parallelism between independent operations.

### Aliases:

* `tf.compat.v1.config.threading.set_inter_op_parallelism_threads`
* `tf.compat.v2.compat.v1.config.threading.set_inter_op_parallelism_threads`
* `tf.compat.v2.config.threading.set_inter_op_parallelism_threads`
* `tf.config.threading.set_inter_op_parallelism_threads`

``` python
tf.config.threading.set_inter_op_parallelism_threads(num_threads)
```

<!-- Placeholder for "Used in" -->

Determines the number of threads used by independent non-blocking operations.
0 means the system picks an appropriate number.

#### Args:


* <b>`num_threads`</b>: Number of parallel threads