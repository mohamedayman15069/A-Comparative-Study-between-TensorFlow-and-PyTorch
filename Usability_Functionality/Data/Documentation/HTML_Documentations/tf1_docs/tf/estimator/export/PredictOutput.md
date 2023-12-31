<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.export.PredictOutput" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="outputs"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="as_signature_def"/>
</div>

# tf.estimator.export.PredictOutput

## Class `PredictOutput`

Represents the output of a generic prediction head.

Inherits From: [`ExportOutput`](../../../tf/estimator/export/ExportOutput.md)

### Aliases:

* Class `tf.compat.v1.estimator.export.PredictOutput`
* Class `tf.compat.v2.compat.v1.estimator.export.PredictOutput`
* Class `tf.compat.v2.estimator.export.PredictOutput`
* Class `tf.estimator.export.PredictOutput`

<!-- Placeholder for "Used in" -->

A generic prediction need not be either a classification or a regression.

Named outputs must be provided as a dict from string to `Tensor`,

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(outputs)
```

Constructor for PredictOutput.


#### Args:


* <b>`outputs`</b>: A `Tensor` or a dict of string to `Tensor` representing the
  predictions.


#### Raises:


* <b>`ValueError`</b>: if the outputs is not dict, or any of its keys are not
    strings, or any of its values are not `Tensor`s.



## Properties

<h3 id="outputs"><code>outputs</code></h3>






## Methods

<h3 id="as_signature_def"><code>as_signature_def</code></h3>

``` python
as_signature_def(receiver_tensors)
```

Generate a SignatureDef proto for inclusion in a MetaGraphDef.

The SignatureDef will specify outputs as described in this ExportOutput,
and will use the provided receiver_tensors as inputs.

#### Args:


* <b>`receiver_tensors`</b>: a `Tensor`, or a dict of string to `Tensor`, specifying
  input nodes that will be fed.



