description: LinearOperator acting like a [batch] zero matrix.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.LinearOperatorZeros" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__matmul__"/>
<meta itemprop="property" content="add_to_tensor"/>
<meta itemprop="property" content="adjoint"/>
<meta itemprop="property" content="assert_non_singular"/>
<meta itemprop="property" content="assert_positive_definite"/>
<meta itemprop="property" content="assert_self_adjoint"/>
<meta itemprop="property" content="batch_shape_tensor"/>
<meta itemprop="property" content="cholesky"/>
<meta itemprop="property" content="cond"/>
<meta itemprop="property" content="determinant"/>
<meta itemprop="property" content="diag_part"/>
<meta itemprop="property" content="domain_dimension_tensor"/>
<meta itemprop="property" content="eigvals"/>
<meta itemprop="property" content="inverse"/>
<meta itemprop="property" content="log_abs_determinant"/>
<meta itemprop="property" content="matmul"/>
<meta itemprop="property" content="matvec"/>
<meta itemprop="property" content="range_dimension_tensor"/>
<meta itemprop="property" content="shape_tensor"/>
<meta itemprop="property" content="solve"/>
<meta itemprop="property" content="solvevec"/>
<meta itemprop="property" content="tensor_rank_tensor"/>
<meta itemprop="property" content="to_dense"/>
<meta itemprop="property" content="trace"/>
</div>

# tf.linalg.LinearOperatorZeros

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator_zeros.py">View source</a>



`LinearOperator` acting like a [batch] zero matrix.

Inherits From: [`LinearOperator`](../../tf/linalg/LinearOperator.md), [`Module`](../../tf/Module.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.LinearOperatorZeros`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.LinearOperatorZeros(
    num_rows,
    num_columns=None,
    batch_shape=None,
    dtype=None,
    is_non_singular=False,
    is_self_adjoint=True,
    is_positive_definite=False,
    is_square=True,
    assert_proper_shapes=False,
    name=&#x27;LinearOperatorZeros&#x27;
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operator acts like a [batch] zero matrix `A` with shape
`[B1,...,Bb, N, M]` for some `b >= 0`.  The first `b` indices index a
batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
an `N x M` matrix.  This matrix `A` is not materialized, but for
purposes of broadcasting this shape will be relevant.

`LinearOperatorZeros` is initialized with `num_rows`, and optionally
`num_columns, `batch_shape`, and `dtype` arguments.  If `num_columns` is
`None`, then this operator will be initialized as a square matrix. If
`batch_shape` is `None`, this operator efficiently passes through all
arguments.  If `batch_shape` is provided, broadcasting may occur, which will
require making copies.

```python
# Create a 2 x 2 zero matrix.
operator = LinearOperatorZero(num_rows=2, dtype=tf.float32)

operator.to_dense()
==> [[0., 0.]
     [0., 0.]]

operator.shape
==> [2, 2]

operator.determinant()
==> 0.

x = ... Shape [2, 4] Tensor
operator.matmul(x)
==> Shape [2, 4] Tensor, same as x.

# Create a 2-batch of 2x2 zero matrices
operator = LinearOperatorZeros(num_rows=2, batch_shape=[2])
operator.to_dense()
==> [[[0., 0.]
      [0., 0.]],
     [[0., 0.]
      [0., 0.]]]

# Here, even though the operator has a batch shape, the input is the same as
# the output, so x can be passed through without a copy.  The operator is able
# to detect that no broadcast is necessary because both x and the operator
# have statically defined shape.
x = ... Shape [2, 2, 3]
operator.matmul(x)
==> Shape [2, 2, 3] Tensor, same as tf.zeros_like(x)

# Here the operator and x have different batch_shape, and are broadcast.
# This requires a copy, since the output is different size than the input.
x = ... Shape [1, 2, 3]
operator.matmul(x)
==> Shape [2, 2, 3] Tensor, equal to tf.zeros_like([x, x])
```

### Shape compatibility

This operator acts on [batch] matrix with compatible shape.
`x` is a batch matrix with compatible shape for `matmul` and `solve` if

```
operator.shape = [B1,...,Bb] + [N, M],  with b >= 0
x.shape =   [C1,...,Cc] + [M, R],
and [C1,...,Cc] broadcasts with [B1,...,Bb] to [D1,...,Dd]
```

#### Matrix property hints

This `LinearOperator` is initialized with boolean flags of the form `is_X`,
for `X = non_singular, self_adjoint, positive_definite, square`.
These have the following meaning:

* If `is_X == True`, callers should expect the operator to have the
  property `X`.  This is a promise that should be fulfilled, but is *not* a
  runtime assert.  For example, finite floating point precision may result
  in these promises being violated.
* If `is_X == False`, callers should expect the operator to not have `X`.
* If `is_X == None` (the default), callers should have no expectation either
  way.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_rows`<a id="num_rows"></a>
</td>
<td>
 Scalar non-negative integer `Tensor`.  Number of rows in the
corresponding zero matrix.
</td>
</tr><tr>
<td>
`num_columns`<a id="num_columns"></a>
</td>
<td>
 Scalar non-negative integer `Tensor`.  Number of columns in
the corresponding zero matrix. If `None`, defaults to the value of
`num_rows`.
</td>
</tr><tr>
<td>
`batch_shape`<a id="batch_shape"></a>
</td>
<td>
 Optional `1-D` integer `Tensor`.  The shape of the leading
dimensions.  If `None`, this operator has no leading dimensions.
</td>
</tr><tr>
<td>
`dtype`<a id="dtype"></a>
</td>
<td>
 Data type of the matrix that this operator represents.
</td>
</tr><tr>
<td>
`is_non_singular`<a id="is_non_singular"></a>
</td>
<td>
 Expect that this operator is non-singular.
</td>
</tr><tr>
<td>
`is_self_adjoint`<a id="is_self_adjoint"></a>
</td>
<td>
 Expect that this operator is equal to its hermitian
transpose.
</td>
</tr><tr>
<td>
`is_positive_definite`<a id="is_positive_definite"></a>
</td>
<td>
 Expect that this operator is positive definite,
meaning the quadratic form `x^H A x` has positive real part for all
nonzero `x`.  Note that we do not require the operator to be
self-adjoint to be positive-definite.  See:
https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
</td>
</tr><tr>
<td>
`is_square`<a id="is_square"></a>
</td>
<td>
 Expect that this operator acts like square [batch] matrices.
</td>
</tr><tr>
<td>
`assert_proper_shapes`<a id="assert_proper_shapes"></a>
</td>
<td>
 Python `bool`.  If `False`, only perform static
checks that initialization and method arguments have proper shape.
If `True`, and static checks are inconclusive, add asserts to the graph.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
A name for this `LinearOperator`
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
 If `num_rows` is determined statically to be non-scalar, or
negative.
</td>
</tr><tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
 If `num_columns` is determined statically to be non-scalar,
or negative.
</td>
</tr><tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
 If `batch_shape` is determined statically to not be 1-D, or
negative.
</td>
</tr><tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
 If any of the following is not `True`:
`{is_self_adjoint, is_non_singular, is_positive_definite}`.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`H`<a id="H"></a>
</td>
<td>
Returns the adjoint of the current `LinearOperator`.

Given `A` representing this `LinearOperator`, return `A*`.
Note that calling `self.adjoint()` and `self.H` are equivalent.
</td>
</tr><tr>
<td>
`batch_shape`<a id="batch_shape"></a>
</td>
<td>
`TensorShape` of batch dimensions of this `LinearOperator`.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns
`TensorShape([B1,...,Bb])`, equivalent to `A.shape[:-2]`
</td>
</tr><tr>
<td>
`domain_dimension`<a id="domain_dimension"></a>
</td>
<td>
Dimension (in the sense of vector spaces) of the domain of this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `N`.
</td>
</tr><tr>
<td>
`dtype`<a id="dtype"></a>
</td>
<td>
The `DType` of `Tensor`s handled by this `LinearOperator`.
</td>
</tr><tr>
<td>
`graph_parents`<a id="graph_parents"></a>
</td>
<td>
List of graph dependencies of this `LinearOperator`. (deprecated)

Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Do not call `graph_parents`.
</td>
</tr><tr>
<td>
`is_non_singular`<a id="is_non_singular"></a>
</td>
<td>

</td>
</tr><tr>
<td>
`is_positive_definite`<a id="is_positive_definite"></a>
</td>
<td>

</td>
</tr><tr>
<td>
`is_self_adjoint`<a id="is_self_adjoint"></a>
</td>
<td>

</td>
</tr><tr>
<td>
`is_square`<a id="is_square"></a>
</td>
<td>
Return `True/False` depending on if this operator is square.
</td>
</tr><tr>
<td>
`parameters`<a id="parameters"></a>
</td>
<td>
Dictionary of parameters used to instantiate this `LinearOperator`.
</td>
</tr><tr>
<td>
`range_dimension`<a id="range_dimension"></a>
</td>
<td>
Dimension (in the sense of vector spaces) of the range of this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `M`.
</td>
</tr><tr>
<td>
`shape`<a id="shape"></a>
</td>
<td>
`TensorShape` of this `LinearOperator`.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns
`TensorShape([B1,...,Bb, M, N])`, equivalent to `A.shape`.
</td>
</tr><tr>
<td>
`tensor_rank`<a id="tensor_rank"></a>
</td>
<td>
Rank (in the sense of tensors) of matrix corresponding to this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `b + 2`.
</td>
</tr>
</table>



## Methods

<h3 id="add_to_tensor"><code>add_to_tensor</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator_zeros.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_to_tensor(
    mat, name=&#x27;add_to_tensor&#x27;
)
</code></pre>

Add matrix represented by this operator to `mat`.  Equiv to `I + mat`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`mat`
</td>
<td>
 `Tensor` with same `dtype` and shape broadcastable to `self`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
 A name to give this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with broadcast shape and same `dtype` as `self`.
</td>
</tr>

</table>



<h3 id="adjoint"><code>adjoint</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>adjoint(
    name: str = &#x27;adjoint&#x27;
) -> 'LinearOperator'
</code></pre>

Returns the adjoint of the current `LinearOperator`.

Given `A` representing this `LinearOperator`, return `A*`.
Note that calling `self.adjoint()` and `self.H` are equivalent.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`LinearOperator` which represents the adjoint of this `LinearOperator`.
</td>
</tr>

</table>



<h3 id="assert_non_singular"><code>assert_non_singular</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assert_non_singular(
    name=&#x27;assert_non_singular&#x27;
)
</code></pre>

Returns an `Op` that asserts this operator is non singular.

This operator is considered non-singular if

```
ConditionNumber < max{100, range_dimension, domain_dimension} * eps,
eps := np.finfo(self.dtype.as_numpy_dtype).eps
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A string name to prepend to created ops.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Assert` `Op`, that, when run, will raise an `InvalidArgumentError` if
the operator is singular.
</td>
</tr>

</table>



<h3 id="assert_positive_definite"><code>assert_positive_definite</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assert_positive_definite(
    name=&#x27;assert_positive_definite&#x27;
)
</code></pre>

Returns an `Op` that asserts this operator is positive definite.

Here, positive definite means that the quadratic form `x^H A x` has positive
real part for all nonzero `x`.  Note that we do not require the operator to
be self-adjoint to be positive definite.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name to give this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Assert` `Op`, that, when run, will raise an `InvalidArgumentError` if
the operator is not positive definite.
</td>
</tr>

</table>



<h3 id="assert_self_adjoint"><code>assert_self_adjoint</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>assert_self_adjoint(
    name=&#x27;assert_self_adjoint&#x27;
)
</code></pre>

Returns an `Op` that asserts this operator is self-adjoint.

Here we check that this operator is *exactly* equal to its hermitian
transpose.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A string name to prepend to created ops.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Assert` `Op`, that, when run, will raise an `InvalidArgumentError` if
the operator is not self-adjoint.
</td>
</tr>

</table>



<h3 id="batch_shape_tensor"><code>batch_shape_tensor</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>batch_shape_tensor(
    name=&#x27;batch_shape_tensor&#x27;
)
</code></pre>

Shape of batch dimensions of this operator, determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns a `Tensor` holding
`[B1,...,Bb]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`int32` `Tensor`
</td>
</tr>

</table>



<h3 id="cholesky"><code>cholesky</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>cholesky(
    name: str = &#x27;cholesky&#x27;
) -> 'LinearOperator'
</code></pre>

Returns a Cholesky factor as a `LinearOperator`.

Given `A` representing this `LinearOperator`, if `A` is positive definite
self-adjoint, return `L`, where `A = L L^T`, i.e. the cholesky
decomposition.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`LinearOperator` which represents the lower triangular matrix
in the Cholesky decomposition.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
When the `LinearOperator` is not hinted to be positive
definite and self adjoint.
</td>
</tr>
</table>



<h3 id="cond"><code>cond</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>cond(
    name=&#x27;cond&#x27;
)
</code></pre>

Returns the condition number of this linear operator.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Shape `[B1,...,Bb]` `Tensor` of same `dtype` as `self`.
</td>
</tr>

</table>



<h3 id="determinant"><code>determinant</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>determinant(
    name=&#x27;det&#x27;
)
</code></pre>

Determinant for every batch member.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`Tensor` with shape `self.batch_shape` and same `dtype` as `self`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`NotImplementedError`
</td>
<td>
 If `self.is_square` is `False`.
</td>
</tr>
</table>



<h3 id="diag_part"><code>diag_part</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>diag_part(
    name=&#x27;diag_part&#x27;
)
</code></pre>

Efficiently get the [batch] diagonal part of this operator.

If this operator has shape `[B1,...,Bb, M, N]`, this returns a
`Tensor` `diagonal`, of shape `[B1,...,Bb, min(M, N)]`, where
`diagonal[b1,...,bb, i] = self.to_dense()[b1,...,bb, i, i]`.

```
my_operator = LinearOperatorDiag([1., 2.])

# Efficiently get the diagonal
my_operator.diag_part()
==> [1., 2.]

# Equivalent, but inefficient method
tf.linalg.diag_part(my_operator.to_dense())
==> [1., 2.]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`diag_part`
</td>
<td>
 A `Tensor` of same `dtype` as self.
</td>
</tr>
</table>



<h3 id="domain_dimension_tensor"><code>domain_dimension_tensor</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>domain_dimension_tensor(
    name=&#x27;domain_dimension_tensor&#x27;
)
</code></pre>

Dimension (in the sense of vector spaces) of the domain of this operator.

Determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `N`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`int32` `Tensor`
</td>
</tr>

</table>



<h3 id="eigvals"><code>eigvals</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>eigvals(
    name=&#x27;eigvals&#x27;
)
</code></pre>

Returns the eigenvalues of this linear operator.

If the operator is marked as self-adjoint (via `is_self_adjoint`)
this computation can be more efficient.

Note: This currently only supports self-adjoint operators.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Shape `[B1,...,Bb, N]` `Tensor` of same `dtype` as `self`.
</td>
</tr>

</table>



<h3 id="inverse"><code>inverse</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>inverse(
    name: str = &#x27;inverse&#x27;
) -> 'LinearOperator'
</code></pre>

Returns the Inverse of this `LinearOperator`.

Given `A` representing this `LinearOperator`, return a `LinearOperator`
representing `A^-1`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name scope to use for ops added by this method.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`LinearOperator` representing inverse of this matrix.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
When the `LinearOperator` is not hinted to be `non_singular`.
</td>
</tr>
</table>



<h3 id="log_abs_determinant"><code>log_abs_determinant</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>log_abs_determinant(
    name=&#x27;log_abs_det&#x27;
)
</code></pre>

Log absolute value of determinant for every batch member.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`Tensor` with shape `self.batch_shape` and same `dtype` as `self`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`NotImplementedError`
</td>
<td>
 If `self.is_square` is `False`.
</td>
</tr>
</table>



<h3 id="matmul"><code>matmul</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>matmul(
    x, adjoint=False, adjoint_arg=False, name=&#x27;matmul&#x27;
)
</code></pre>

Transform [batch] matrix `x` with left multiplication:  `x --> Ax`.

```python
# Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
operator = LinearOperator(...)
operator.shape = [..., M, N]

X = ... # shape [..., N, R], batch matrix, R > 0.

Y = operator.matmul(X)
Y.shape
==> [..., M, R]

Y[..., :, r] = sum_j A[..., :, j] X[j, r]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
`LinearOperator` or `Tensor` with compatible shape and same `dtype` as
`self`. See class docstring for definition of compatibility.
</td>
</tr><tr>
<td>
`adjoint`
</td>
<td>
Python `bool`.  If `True`, left multiply by the adjoint: `A^H x`.
</td>
</tr><tr>
<td>
`adjoint_arg`
</td>
<td>
 Python `bool`.  If `True`, compute `A x^H` where `x^H` is
the hermitian transpose (transposition and complex conjugation).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `LinearOperator` or `Tensor` with shape `[..., M, R]` and same `dtype`
as `self`.
</td>
</tr>

</table>



<h3 id="matvec"><code>matvec</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>matvec(
    x, adjoint=False, name=&#x27;matvec&#x27;
)
</code></pre>

Transform [batch] vector `x` with left multiplication:  `x --> Ax`.

```python
# Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
operator = LinearOperator(...)

X = ... # shape [..., N], batch vector

Y = operator.matvec(X)
Y.shape
==> [..., M]

Y[..., :] = sum_j A[..., :, j] X[..., j]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
`Tensor` with compatible shape and same `dtype` as `self`.
`x` is treated as a [batch] vector meaning for every set of leading
dimensions, the last dimension defines a vector.
See class docstring for definition of compatibility.
</td>
</tr><tr>
<td>
`adjoint`
</td>
<td>
Python `bool`.  If `True`, left multiply by the adjoint: `A^H x`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with shape `[..., M]` and same `dtype` as `self`.
</td>
</tr>

</table>



<h3 id="range_dimension_tensor"><code>range_dimension_tensor</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>range_dimension_tensor(
    name=&#x27;range_dimension_tensor&#x27;
)
</code></pre>

Dimension (in the sense of vector spaces) of the range of this operator.

Determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `M`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`int32` `Tensor`
</td>
</tr>

</table>



<h3 id="shape_tensor"><code>shape_tensor</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>shape_tensor(
    name=&#x27;shape_tensor&#x27;
)
</code></pre>

Shape of this `LinearOperator`, determined at runtime.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns a `Tensor` holding
`[B1,...,Bb, M, N]`, equivalent to <a href="../../tf/shape.md"><code>tf.shape(A)</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`int32` `Tensor`
</td>
</tr>

</table>



<h3 id="solve"><code>solve</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>solve(
    rhs, adjoint=False, adjoint_arg=False, name=&#x27;solve&#x27;
)
</code></pre>

Solve (exact or approx) `R` (batch) systems of equations: `A X = rhs`.

The returned `Tensor` will be close to an exact solution if `A` is well
conditioned. Otherwise closeness will vary. See class docstring for details.

#### Examples:



```python
# Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
operator = LinearOperator(...)
operator.shape = [..., M, N]

# Solve R > 0 linear systems for every member of the batch.
RHS = ... # shape [..., M, R]

X = operator.solve(RHS)
# X[..., :, r] is the solution to the r'th linear system
# sum_j A[..., :, j] X[..., j, r] = RHS[..., :, r]

operator.matmul(X)
==> RHS
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`rhs`
</td>
<td>
`Tensor` with same `dtype` as this operator and compatible shape.
`rhs` is treated like a [batch] matrix meaning for every set of leading
dimensions, the last two dimensions defines a matrix.
See class docstring for definition of compatibility.
</td>
</tr><tr>
<td>
`adjoint`
</td>
<td>
Python `bool`.  If `True`, solve the system involving the adjoint
of this `LinearOperator`:  `A^H X = rhs`.
</td>
</tr><tr>
<td>
`adjoint_arg`
</td>
<td>
 Python `bool`.  If `True`, solve `A X = rhs^H` where `rhs^H`
is the hermitian transpose (transposition and complex conjugation).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
 A name scope to use for ops added by this method.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`Tensor` with shape `[...,N, R]` and same `dtype` as `rhs`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`NotImplementedError`
</td>
<td>
 If `self.is_non_singular` or `is_square` is False.
</td>
</tr>
</table>



<h3 id="solvevec"><code>solvevec</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>solvevec(
    rhs, adjoint=False, name=&#x27;solve&#x27;
)
</code></pre>

Solve single equation with best effort: `A X = rhs`.

The returned `Tensor` will be close to an exact solution if `A` is well
conditioned. Otherwise closeness will vary. See class docstring for details.

#### Examples:



```python
# Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
operator = LinearOperator(...)
operator.shape = [..., M, N]

# Solve one linear system for every member of the batch.
RHS = ... # shape [..., M]

X = operator.solvevec(RHS)
# X is the solution to the linear system
# sum_j A[..., :, j] X[..., j] = RHS[..., :]

operator.matvec(X)
==> RHS
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`rhs`
</td>
<td>
`Tensor` with same `dtype` as this operator.
`rhs` is treated like a [batch] vector meaning for every set of leading
dimensions, the last dimension defines a vector.  See class docstring
for definition of compatibility regarding batch dimensions.
</td>
</tr><tr>
<td>
`adjoint`
</td>
<td>
Python `bool`.  If `True`, solve the system involving the adjoint
of this `LinearOperator`:  `A^H X = rhs`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
 A name scope to use for ops added by this method.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`Tensor` with shape `[...,N]` and same `dtype` as `rhs`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`NotImplementedError`
</td>
<td>
 If `self.is_non_singular` or `is_square` is False.
</td>
</tr>
</table>



<h3 id="tensor_rank_tensor"><code>tensor_rank_tensor</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tensor_rank_tensor(
    name=&#x27;tensor_rank_tensor&#x27;
)
</code></pre>

Rank (in the sense of tensors) of matrix corresponding to this operator.

If this operator acts like the batch matrix `A` with
`A.shape = [B1,...,Bb, M, N]`, then this returns `b + 2`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`int32` `Tensor`, determined at runtime.
</td>
</tr>

</table>



<h3 id="to_dense"><code>to_dense</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_dense(
    name=&#x27;to_dense&#x27;
)
</code></pre>

Return a dense (batch) matrix representing this operator.


<h3 id="trace"><code>trace</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>trace(
    name=&#x27;trace&#x27;
)
</code></pre>

Trace of the linear operator, equal to sum of `self.diag_part()`.

If the operator is square, this is also the sum of the eigenvalues.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
 A name for this `Op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Shape `[B1,...,Bb]` `Tensor` of same `dtype` as `self`.
</td>
</tr>

</table>



<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator_zeros.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__getitem__(
    slices
)
</code></pre>




<h3 id="__matmul__"><code>__matmul__</code></h3>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg/linear_operator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__matmul__(
    other
)
</code></pre>






