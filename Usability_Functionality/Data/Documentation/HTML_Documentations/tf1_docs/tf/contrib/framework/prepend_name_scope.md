<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.framework.prepend_name_scope" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.framework.prepend_name_scope

Prepends name scope to a name.

``` python
tf.contrib.framework.prepend_name_scope(
    name,
    import_scope
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`name`</b>: A `string` name.
* <b>`import_scope`</b>: Optional `string`. Name scope to add.


#### Returns:

Name with name scope added, or the original name if import_scope
is None.
