<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.disable_control_flow_v2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.disable_control_flow_v2

Opts out of control flow v2.

### Aliases:

* `tf.compat.v1.disable_control_flow_v2`
* `tf.compat.v2.compat.v1.disable_control_flow_v2`
* `tf.disable_control_flow_v2`

``` python
tf.disable_control_flow_v2()
```

<!-- Placeholder for "Used in" -->

Note: v2 control flow is always enabled inside of tf.function. Calling this
function has no effect in that case.

If your code needs tf.disable_control_flow_v2() to be called to work
properly please file a bug.