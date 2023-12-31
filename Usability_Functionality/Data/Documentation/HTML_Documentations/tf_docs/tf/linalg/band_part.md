description: Copy a tensor setting everything outside a central band in each innermost matrix to zero.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.band_part" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.band_part

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Copy a tensor setting everything outside a central band in each innermost matrix to zero.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.band_part`, `tf.compat.v1.matrix_band_part`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.band_part(
    input: Annotated[Any, TV_MatrixBandPart_T],
    num_lower: Annotated[Any, TV_MatrixBandPart_Tindex],
    num_upper: Annotated[Any, TV_MatrixBandPart_Tindex],
    name=None
) -> Annotated[Any, TV_MatrixBandPart_T]
</code></pre>



<!-- Placeholder for "Used in" -->

The `band` part is computed as follows:
Assume `input` has `k` dimensions `[I, J, K, ..., M, N]`, then the output is a
tensor with the same shape where

`band[i, j, k, ..., m, n] = in_band(m, n) * input[i, j, k, ..., m, n]`.

The indicator function

`in_band(m, n) = (num_lower < 0 || (m-n) <= num_lower)) &&
                 (num_upper < 0 || (n-m) <= num_upper)`.

#### For example:



```
# if 'input' is [[ 0,  1,  2, 3]
#                [-1,  0,  1, 2]
#                [-2, -1,  0, 1]
#                [-3, -2, -1, 0]],

tf.linalg.band_part(input, 1, -1) ==> [[ 0,  1,  2, 3]
                                       [-1,  0,  1, 2]
                                       [ 0, -1,  0, 1]
                                       [ 0,  0, -1, 0]],

tf.linalg.band_part(input, 2, 1) ==> [[ 0,  1,  0, 0]
                                      [-1,  0,  1, 0]
                                      [-2, -1,  0, 1]
                                      [ 0, -2, -1, 0]]
```

#### Useful special cases:



```
 tf.linalg.band_part(input, 0, -1) ==> Upper triangular part.
 tf.linalg.band_part(input, -1, 0) ==> Lower triangular part.
 tf.linalg.band_part(input, 0, 0) ==> Diagonal.
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`<a id="input"></a>
</td>
<td>
A `Tensor`. Rank `k` tensor.
</td>
</tr><tr>
<td>
`num_lower`<a id="num_lower"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
0-D tensor. Number of subdiagonals to keep. If negative, keep entire
lower triangle.
</td>
</tr><tr>
<td>
`num_upper`<a id="num_upper"></a>
</td>
<td>
A `Tensor`. Must have the same type as `num_lower`.
0-D tensor. Number of superdiagonals to keep. If negative, keep
entire upper triangle.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

