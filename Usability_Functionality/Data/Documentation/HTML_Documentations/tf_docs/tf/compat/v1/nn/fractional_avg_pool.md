description: Performs fractional average pooling on the input. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.fractional_avg_pool" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.fractional_avg_pool

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/nn_ops.py">View source</a>



Performs fractional average pooling on the input. (deprecated)


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.fractional_avg_pool(
    value,
    pooling_ratio,
    pseudo_random=False,
    overlapping=False,
    deterministic=False,
    seed=0,
    seed2=0,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
`seed2` and `deterministic` args are deprecated.  Use fractional_avg_pool_v2.

This is a deprecated version of `fractional_avg_pool`.

Fractional average pooling is similar to Fractional max pooling in the pooling
region generation step. The only difference is that after pooling regions are
generated, a mean operation is performed instead of a max operation in each
pooling region.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`<a id="value"></a>
</td>
<td>
A `Tensor`. 4-D with shape `[batch, height, width, channels]`.
</td>
</tr><tr>
<td>
`pooling_ratio`<a id="pooling_ratio"></a>
</td>
<td>
A list of `floats` that has length >= 4.  Pooling ratio for
each dimension of `value`, currently only supports row and col dimension
and should be >= 1.0. For example, a valid pooling ratio looks like [1.0,
1.44, 1.73, 1.0]. The first and last elements must be 1.0 because we don't
allow pooling on batch and channels dimensions.  1.44 and 1.73 are pooling
ratio on height and width dimensions respectively.
</td>
</tr><tr>
<td>
`pseudo_random`<a id="pseudo_random"></a>
</td>
<td>
An optional `bool`.  Defaults to `False`. When set to `True`,
generates the pooling sequence in a pseudorandom fashion, otherwise, in a
random fashion. Check paper (Graham, 2015) for difference between
pseudorandom and random.
</td>
</tr><tr>
<td>
`overlapping`<a id="overlapping"></a>
</td>
<td>
An optional `bool`.  Defaults to `False`.  When set to `True`,
it means when pooling, the values at the boundary of adjacent pooling
cells are used by both cells. For example:
`index  0  1  2  3  4`
`value  20 5  16 3  7`
If the pooling sequence is [0, 2, 4], then 16, at index 2 will be used
twice.  The result would be [20, 16] for fractional avg pooling.
</td>
</tr><tr>
<td>
`deterministic`<a id="deterministic"></a>
</td>
<td>
An optional `bool`.  Deprecated; use `fractional_avg_pool_v2`
instead.
</td>
</tr><tr>
<td>
`seed`<a id="seed"></a>
</td>
<td>
An optional `int`.  Defaults to `0`.  If set to be non-zero, the
random number generator is seeded by the given seed.  Otherwise it is
seeded by a random seed.
</td>
</tr><tr>
<td>
`seed2`<a id="seed2"></a>
</td>
<td>
An optional `int`.  Deprecated; use `fractional_avg_pool_v2` instead.
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


</table>


A tuple of `Tensor` objects (`output`, `row_pooling_sequence`,
`col_pooling_sequence`).
  output: Output `Tensor` after fractional avg pooling.  Has the same type as
    `value`.
  row_pooling_sequence: A `Tensor` of type `int64`.
  col_pooling_sequence: A `Tensor` of type `int64`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">References</h2></th></tr>
<tr class="alt">
<td colspan="2">
Fractional Max-Pooling:
[Graham, 2015](https://arxiv.org/abs/1412.6071)
([pdf](https://arxiv.org/pdf/1412.6071.pdf))
</td>
</tr>

</table>

