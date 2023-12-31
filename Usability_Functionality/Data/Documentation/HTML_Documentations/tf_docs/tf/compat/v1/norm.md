description: Computes the norm of vectors, matrices, and tensors. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.norm" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.norm

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg_ops.py">View source</a>



Computes the norm of vectors, matrices, and tensors. (deprecated arguments)


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.norm`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.norm(
    tensor,
    ord=&#x27;euclidean&#x27;,
    axis=None,
    keepdims=None,
    name=None,
    keep_dims=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Deprecated: SOME ARGUMENTS ARE DEPRECATED: `(keep_dims)`. They will be removed in a future version.
Instructions for updating:
keep_dims is deprecated, use keepdims instead

This function can compute several different vector norms (the 1-norm, the
Euclidean or 2-norm, the inf-norm, and in general the p-norm for p > 0) and
matrix norms (Frobenius, 1-norm, 2-norm and inf-norm).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`<a id="tensor"></a>
</td>
<td>
`Tensor` of types `float32`, `float64`, `complex64`, `complex128`
</td>
</tr><tr>
<td>
`ord`<a id="ord"></a>
</td>
<td>
Order of the norm. Supported values are 'fro', 'euclidean',
`1`, `2`, `np.inf` and any positive real number yielding the corresponding
p-norm. Default is 'euclidean' which is equivalent to Frobenius norm if
`tensor` is a matrix and equivalent to 2-norm for vectors.
Some restrictions apply:
  a) The Frobenius norm `fro` is not defined for vectors,
  b) If axis is a 2-tuple (matrix norm), only 'euclidean', 'fro', `1`,
     `2`, `np.inf` are supported.
See the description of `axis` on how to compute norms for a batch of
vectors or matrices stored in a tensor.
</td>
</tr><tr>
<td>
`axis`<a id="axis"></a>
</td>
<td>
If `axis` is `None` (the default), the input is considered a vector
and a single vector norm is computed over the entire set of values in the
tensor, i.e. `norm(tensor, ord=ord)` is equivalent to
`norm(reshape(tensor, [-1]), ord=ord)`.
If `axis` is a Python integer, the input is considered a batch of vectors,
and `axis` determines the axis in `tensor` over which to compute vector
norms.
If `axis` is a 2-tuple of Python integers it is considered a batch of
matrices and `axis` determines the axes in `tensor` over which to compute
a matrix norm.
Negative indices are supported. Example: If you are passing a tensor that
can be either a matrix or a batch of matrices at runtime, pass
`axis=[-2,-1]` instead of `axis=None` to make sure that matrix norms are
computed.
</td>
</tr><tr>
<td>
`keepdims`<a id="keepdims"></a>
</td>
<td>
If True, the axis indicated in `axis` are kept with size 1.
Otherwise, the dimensions in `axis` are removed from the output shape.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
The name of the op.
</td>
</tr><tr>
<td>
`keep_dims`<a id="keep_dims"></a>
</td>
<td>
Deprecated alias for `keepdims`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`output`<a id="output"></a>
</td>
<td>
A `Tensor` of the same type as tensor, containing the vector or
matrix norms. If `keepdims` is True then the rank of output is equal to
the rank of `tensor`. Otherwise, if `axis` is none the output is a scalar,
if `axis` is an integer, the rank of `output` is one less than the rank
of `tensor`, if `axis` is a 2-tuple the rank of `output` is two less
than the rank of `tensor`.
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
If `ord` or `axis` is invalid.
</td>
</tr>
</table>




 <section><devsite-expandable expanded>
 <h2 class="showalways">numpy compatibility</h2>

Mostly equivalent to numpy.linalg.norm.
Not supported: ord <= 0, 2-norm for matrices, nuclear norm.
Other differences:
  a) If axis is `None`, treats the flattened `tensor` as a vector
   regardless of rank.
  b) Explicitly supports 'euclidean' norm as the default, including for
   higher order tensors.

 </devsite-expandable></section>

