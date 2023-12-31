<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.learn.ProblemType" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="CLASSIFICATION"/>
<meta itemprop="property" content="LINEAR_REGRESSION"/>
<meta itemprop="property" content="LOGISTIC_REGRESSION"/>
<meta itemprop="property" content="UNSPECIFIED"/>
</div>

# tf.contrib.learn.ProblemType

## Class `ProblemType`

Enum-like values for the type of problem that the model solves.



<!-- Placeholder for "Used in" -->

THIS CLASS IS DEPRECATED.

These values are used when exporting the model to produce the appropriate
signature function for serving.

The following values are supported:
  UNSPECIFIED: Produces a predict signature_fn.
  CLASSIFICATION: Produces a classify signature_fn.
  LINEAR_REGRESSION: Produces a regression signature_fn.
  LOGISTIC_REGRESSION: Produces a classify signature_fn.

## Class Members

* `CLASSIFICATION = 1` <a id="CLASSIFICATION"></a>
* `LINEAR_REGRESSION = 2` <a id="LINEAR_REGRESSION"></a>
* `LOGISTIC_REGRESSION = 3` <a id="LOGISTIC_REGRESSION"></a>
* `UNSPECIFIED = 0` <a id="UNSPECIFIED"></a>
