<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.model_variables" />
<meta itemprop="path" content="Stable" />
</div>

# tf.model_variables

Returns all variables in the MODEL_VARIABLES collection.

### Aliases:

* `tf.compat.v1.model_variables`
* `tf.compat.v2.compat.v1.model_variables`
* `tf.model_variables`

``` python
tf.model_variables(scope=None)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`scope`</b>: (Optional.) A string. If supplied, the resulting list is filtered to
  include only items whose `name` attribute matches `scope` using
  `re.match`. Items without a `name` attribute are never returned if a scope
  is supplied. The choice of `re.match` means that a `scope` without special
  tokens filters by prefix.


#### Returns:

A list of local Variable objects.
