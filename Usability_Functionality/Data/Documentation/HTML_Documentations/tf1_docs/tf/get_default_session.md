<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.get_default_session" />
<meta itemprop="path" content="Stable" />
</div>

# tf.get_default_session

Returns the default session for the current thread.

### Aliases:

* `tf.compat.v1.get_default_session`
* `tf.compat.v2.compat.v1.get_default_session`
* `tf.get_default_session`

``` python
tf.get_default_session()
```

<!-- Placeholder for "Used in" -->

The returned `Session` will be the innermost session on which a
`Session` or <a href="../tf/InteractiveSession.md#as_default"><code>Session.as_default()</code></a> context has been entered.

NOTE: The default session is a property of the current thread. If you
create a new thread, and wish to use the default session in that
thread, you must explicitly add a `with sess.as_default():` in that
thread's function.

#### Returns:

The default `Session` being used in the current thread.
