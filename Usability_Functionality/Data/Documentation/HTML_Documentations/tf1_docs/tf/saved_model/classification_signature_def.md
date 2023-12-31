<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.saved_model.classification_signature_def" />
<meta itemprop="path" content="Stable" />
</div>

# tf.saved_model.classification_signature_def

Creates classification signature from given examples and predictions.

### Aliases:

* `tf.compat.v1.saved_model.classification_signature_def`
* `tf.compat.v1.saved_model.signature_def_utils.classification_signature_def`
* `tf.compat.v2.compat.v1.saved_model.classification_signature_def`
* `tf.compat.v2.compat.v1.saved_model.signature_def_utils.classification_signature_def`
* `tf.saved_model.classification_signature_def`
* `tf.saved_model.signature_def_utils.classification_signature_def`

``` python
tf.saved_model.classification_signature_def(
    examples,
    classes,
    scores
)
```

<!-- Placeholder for "Used in" -->

This function produces signatures intended for use with the TensorFlow Serving
Classify API (tensorflow_serving/apis/prediction_service.proto), and so
constrains the input and output types to those allowed by TensorFlow Serving.

#### Args:


* <b>`examples`</b>: A string `Tensor`, expected to accept serialized tf.Examples.
* <b>`classes`</b>: A string `Tensor`.  Note that the ClassificationResponse message
  requires that class labels are strings, not integers or anything else.
* <b>`scores`</b>: a float `Tensor`.


#### Returns:

A classification-flavored signature_def.



#### Raises:


* <b>`ValueError`</b>: If examples is `None`.