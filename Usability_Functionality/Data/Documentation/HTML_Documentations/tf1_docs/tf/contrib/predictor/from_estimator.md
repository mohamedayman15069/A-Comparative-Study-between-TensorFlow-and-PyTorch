<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.predictor.from_estimator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.predictor.from_estimator

Constructs a `Predictor` from a `tf.python.estimator.Estimator`.

``` python
tf.contrib.predictor.from_estimator(
    estimator,
    serving_input_receiver_fn,
    output_key=None,
    graph=None,
    config=None
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`estimator`</b>: an instance of `learn.python.estimator.Estimator`.
* <b>`serving_input_receiver_fn`</b>: a function that takes no arguments and returns
  an instance of `ServingInputReceiver` compatible with `estimator`.
* <b>`output_key`</b>: Optional string specifying the export output to use. If
  `None`, then `DEFAULT_SERVING_SIGNATURE_DEF_KEY` is used.
* <b>`graph`</b>: Optional. The Tensorflow `graph` in which prediction should be
  done.
* <b>`config`</b>: `ConfigProto` proto used to configure the session.


#### Returns:

An initialized `Predictor`.



#### Raises:


* <b>`TypeError`</b>: if `estimator` is a contrib `Estimator` instead of a core
  `Estimator`.