<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.framework.load_checkpoint" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.framework.load_checkpoint

Returns CheckpointReader for latest checkpoint.

``` python
tf.contrib.framework.load_checkpoint(filepattern)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`filepattern`</b>: Directory with checkpoints file or path to checkpoint.


#### Returns:

`CheckpointReader` object.



#### Raises:


* <b>`ValueError`</b>: if checkpoint_dir doesn't have 'checkpoint' file or checkpoints.