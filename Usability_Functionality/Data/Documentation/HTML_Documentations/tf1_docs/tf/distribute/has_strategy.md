<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.has_strategy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.distribute.has_strategy

Return if there is a current non-default <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>.

### Aliases:

* `tf.compat.v1.distribute.has_strategy`
* `tf.compat.v2.compat.v1.distribute.has_strategy`
* `tf.compat.v2.distribute.has_strategy`
* `tf.contrib.distribute.has_distribution_strategy`
* `tf.contrib.distribute.has_strategy`
* `tf.distribute.has_strategy`

``` python
tf.distribute.has_strategy()
```

<!-- Placeholder for "Used in" -->

```
assert not tf.distribute.has_strategy()
with strategy.scope():
  assert tf.distribute.has_strategy()
```

#### Returns:

True if inside a `with strategy.scope():`.
