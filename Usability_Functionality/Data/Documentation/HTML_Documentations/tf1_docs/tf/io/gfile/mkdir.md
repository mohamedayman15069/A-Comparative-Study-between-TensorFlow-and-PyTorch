<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.gfile.mkdir" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.gfile.mkdir

Creates a directory with the name given by 'path'.

### Aliases:

* `tf.compat.v1.io.gfile.mkdir`
* `tf.compat.v2.compat.v1.io.gfile.mkdir`
* `tf.compat.v2.io.gfile.mkdir`
* `tf.io.gfile.mkdir`

``` python
tf.io.gfile.mkdir(path)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`path`</b>: string, name of the directory to be created
Notes: The parent directories need to exist. Use recursive_create_dir instead
  if there is the possibility that the parent dirs don't exist.

#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.