description: Computes the eigen decomposition of a batch of self-adjoint matrices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.eigh" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.eigh

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/linalg_ops.py">View source</a>



Computes the eigen decomposition of a batch of self-adjoint matrices.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.eigh`, `tf.compat.v1.self_adjoint_eig`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.eigh(
    tensor, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the eigenvalues and eigenvectors of the innermost N-by-N matrices
in `tensor` such that
`tensor[...,:,:] * v[..., :,i] = e[..., i] * v[...,:,i]`, for i=0...N-1.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`<a id="tensor"></a>
</td>
<td>
`Tensor` of shape `[..., N, N]`. Only the lower triangular part of
each inner inner matrix is referenced.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
string, optional name of the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`e`<a id="e"></a>
</td>
<td>
Eigenvalues. Shape is `[..., N]`. Sorted in non-decreasing order.
</td>
</tr><tr>
<td>
`v`<a id="v"></a>
</td>
<td>
Eigenvectors. Shape is `[..., N, N]`. The columns of the inner most
matrices contain eigenvectors of the corresponding matrices in `tensor`
</td>
</tr>
</table>

