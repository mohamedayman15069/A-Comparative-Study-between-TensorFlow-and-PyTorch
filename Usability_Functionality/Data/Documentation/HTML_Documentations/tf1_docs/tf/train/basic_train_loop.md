<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.train.basic_train_loop" />
<meta itemprop="path" content="Stable" />
</div>

# tf.train.basic_train_loop

Basic loop to train a model.

### Aliases:

* `tf.compat.v1.train.basic_train_loop`
* `tf.compat.v2.compat.v1.train.basic_train_loop`
* `tf.train.basic_train_loop`

``` python
tf.train.basic_train_loop(
    supervisor,
    train_step_fn,
    args=None,
    kwargs=None,
    master=''
)
```

<!-- Placeholder for "Used in" -->

Calls `train_step_fn` in a loop to train a model.  The function is called as:

```python
train_step_fn(session, *args, **kwargs)
```

It is passed a <a href="../../tf/Session.md"><code>tf.compat.v1.Session</code></a> in addition to `args` and `kwargs`.  The
function
typically runs one training step in the session.

#### Args:


* <b>`supervisor`</b>: <a href="../../tf/train/Supervisor.md"><code>tf.compat.v1.train.Supervisor</code></a> to run the training services.
* <b>`train_step_fn`</b>: Callable to execute one training step.  Called repeatedly as
  `train_step_fn(session, *args **kwargs)`.
* <b>`args`</b>: Optional positional arguments passed to `train_step_fn`.
* <b>`kwargs`</b>: Optional keyword arguments passed to `train_step_fn`.
* <b>`master`</b>: Master to use to create the training session.  Defaults to `""`
  which causes the session to be created in the local process.