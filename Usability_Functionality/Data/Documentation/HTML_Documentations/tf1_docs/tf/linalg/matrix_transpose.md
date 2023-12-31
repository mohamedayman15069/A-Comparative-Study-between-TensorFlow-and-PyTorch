<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.matrix_transpose" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.matrix_transpose

Transposes last two dimensions of tensor `a`.

### Aliases:

* `tf.compat.v1.linalg.matrix_transpose`
* `tf.compat.v1.linalg.transpose`
* `tf.compat.v1.matrix_transpose`
* `tf.compat.v2.compat.v1.linalg.matrix_transpose`
* `tf.compat.v2.compat.v1.linalg.transpose`
* `tf.compat.v2.compat.v1.matrix_transpose`
* `tf.compat.v2.linalg.matrix_transpose`
* `tf.linalg.matrix_transpose`
* `tf.linalg.transpose`
* `tf.matrix_transpose`

``` python
tf.linalg.matrix_transpose(
    a,
    name='matrix_transpose',
    conjugate=False
)
```

<!-- Placeholder for "Used in" -->


#### For example:



```python
x = tf.constant([[1, 2, 3], [4, 5, 6]])
tf.linalg.matrix_transpose(x)  # [[1, 4],
                               #  [2, 5],
                               #  [3, 6]]

x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],
                 [4 + 4j, 5 + 5j, 6 + 6j]])
tf.linalg.matrix_transpose(x, conjugate=True)  # [[1 - 1j, 4 - 4j],
                                               #  [2 - 2j, 5 - 5j],
                                               #  [3 - 3j, 6 - 6j]]

# Matrix with two batch dimensions.
# x.shape is [1, 2, 3, 4]
# tf.linalg.matrix_transpose(x) is shape [1, 2, 4, 3]
```

Note that <a href="../../tf/linalg/matmul.md"><code>tf.matmul</code></a> provides kwargs allowing for transpose of arguments.
This is done with minimal cost, and is preferable to using this function. E.g.

```python
# Good!  Transpose is taken at minimal additional cost.
tf.matmul(matrix, b, transpose_b=True)

# Inefficient!
tf.matmul(matrix, tf.linalg.matrix_transpose(b))
```



#### Args:


* <b>`a`</b>: A `Tensor` with `rank >= 2`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`conjugate`</b>: Optional bool. Setting it to `True` is mathematically equivalent
  to tf.math.conj(tf.linalg.matrix_transpose(input)).


#### Returns:

A transposed batch matrix `Tensor`.



#### Raises:


* <b>`ValueError`</b>:  If `a` is determined statically to have `rank < 2`.

#### Numpy Compatibility
In `numpy` transposes are memory-efficient constant time operations as they
simply return a new view of the same data with adjusted `strides`.

TensorFlow does not support strides, <a href="../../tf/linalg/matrix_transpose.md"><code>linalg.matrix_transpose</code></a> returns a new
tensor with the items permuted.

