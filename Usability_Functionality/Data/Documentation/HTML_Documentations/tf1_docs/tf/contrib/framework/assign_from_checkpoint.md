<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.framework.assign_from_checkpoint" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.framework.assign_from_checkpoint

Creates an operation to assign specific variables from a checkpoint.

``` python
tf.contrib.framework.assign_from_checkpoint(
    model_path,
    var_list,
    ignore_missing_vars=False
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`model_path`</b>: The full path to the model checkpoint. To get latest checkpoint
  use `model_path = tf.train.latest_checkpoint(checkpoint_dir)`
* <b>`var_list`</b>: A list of (possibly partitioned) `Variable` objects or a
  dictionary mapping names in the checkpoint to the corresponding variables
  or list of variables to initialize from that checkpoint value. For
  partitioned Variables, the name in the checkpoint must be the full
  variable, not the name of the partitioned variable, eg. "my_var" rather
  than "my_var/part_4". If empty, returns no_op(), {}.
* <b>`ignore_missing_vars`</b>: Boolean, if True ignore variables missing in the
  checkpoint with a warning instead of failing.


#### Returns:

the restore_op and the feed_dict that need to be run to restore var_list.



#### Raises:


* <b>`ValueError`</b>: If `ignore_missing_vars` is False and the checkpoint specified
    at `model_path` is missing one of the variables in `var_list`.