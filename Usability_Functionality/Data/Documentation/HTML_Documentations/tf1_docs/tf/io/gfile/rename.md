<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.gfile.rename" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.gfile.rename

Rename or move a file / directory.

### Aliases:

* `tf.compat.v1.io.gfile.rename`
* `tf.compat.v2.compat.v1.io.gfile.rename`
* `tf.compat.v2.io.gfile.rename`
* `tf.io.gfile.rename`

``` python
tf.io.gfile.rename(
    src,
    dst,
    overwrite=False
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`src`</b>: string, pathname for a file
* <b>`dst`</b>: string, pathname to which the file needs to be moved
* <b>`overwrite`</b>: boolean, if false it's an error for `dst` to be occupied by an
  existing file.


#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.