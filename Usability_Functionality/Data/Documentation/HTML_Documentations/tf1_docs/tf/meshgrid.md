<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.meshgrid" />
<meta itemprop="path" content="Stable" />
</div>

# tf.meshgrid

Broadcasts parameters for evaluation on an N-D grid.

### Aliases:

* `tf.compat.v1.meshgrid`
* `tf.compat.v2.compat.v1.meshgrid`
* `tf.compat.v2.meshgrid`
* `tf.meshgrid`

``` python
tf.meshgrid(
    *args,
    **kwargs
)
```

<!-- Placeholder for "Used in" -->

Given N one-dimensional coordinate arrays `*args`, returns a list `outputs`
of N-D coordinate arrays for evaluating expressions on an N-D grid.

#### Notes:



`meshgrid` supports cartesian ('xy') and matrix ('ij') indexing conventions.
When the `indexing` argument is set to 'xy' (the default), the broadcasting
instructions for the first two dimensions are swapped.

#### Examples:



Calling `X, Y = meshgrid(x, y)` with the tensors

```python
x = [1, 2, 3]
y = [4, 5, 6]
X, Y = tf.meshgrid(x, y)
# X = [[1, 2, 3],
#      [1, 2, 3],
#      [1, 2, 3]]
# Y = [[4, 4, 4],
#      [5, 5, 5],
#      [6, 6, 6]]
```

#### Args:


* <b>`*args`</b>: `Tensor`s with rank 1.
* <b>`**kwargs`</b>:   - indexing: Either 'xy' or 'ij' (optional, default: 'xy').
  - name: A name for the operation (optional).


#### Returns:


* <b>`outputs`</b>: A list of N `Tensor`s with rank N.


#### Raises:


* <b>`TypeError`</b>: When no keyword arguments (kwargs) are passed.
* <b>`ValueError`</b>: When indexing keyword argument is not one of `xy` or `ij`.