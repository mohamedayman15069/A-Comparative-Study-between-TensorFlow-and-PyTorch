<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.trace" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.trace

Compute the trace of a tensor `x`.

### Aliases:

* `tf.compat.v1.linalg.trace`
* `tf.compat.v1.trace`
* `tf.compat.v2.compat.v1.linalg.trace`
* `tf.compat.v2.compat.v1.trace`
* `tf.compat.v2.linalg.trace`
* `tf.linalg.trace`
* `tf.trace`

``` python
tf.linalg.trace(
    x,
    name=None
)
```

<!-- Placeholder for "Used in" -->

`trace(x)` returns the sum along the main diagonal of each inner-most matrix
in x. If x is of rank `k` with shape `[I, J, K, ..., L, M, N]`, then output
is a tensor of rank `k-2` with dimensions `[I, J, K, ..., L]` where

`output[i, j, k, ..., l] = trace(x[i, j, i, ..., l, :, :])`

#### For example:



```python
x = tf.constant([[1, 2], [3, 4]])
tf.linalg.trace(x)  # 5

x = tf.constant([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
tf.linalg.trace(x)  # 15

x = tf.constant([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],
                 [[-1, -2, -3],
                  [-4, -5, -6],
                  [-7, -8, -9]]])
tf.linalg.trace(x)  # [15, -15]
```

#### Args:


* <b>`x`</b>: tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The trace of input tensor.
