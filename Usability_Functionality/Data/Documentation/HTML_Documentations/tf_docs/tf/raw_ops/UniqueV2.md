description: Finds unique elements along an axis of a tensor.
robots: noindex

# tf.raw_ops.UniqueV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Finds unique elements along an axis of a tensor.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.UniqueV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.UniqueV2(
    x,
    axis,
    out_idx=<a href="../../tf/dtypes.md#int32"><code>tf.dtypes.int32</code></a>,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation either returns a tensor `y` containing unique elements
along the `axis` of a tensor. The returned unique elements is sorted
in the same order as they occur along `axis` in `x`.
This operation also returns a tensor `idx` that is the same size as
the number of the elements in `x` along the `axis` dimension. It
contains the index in the unique output `y`.
In other words, for an `1-D` tensor `x` with `axis = None:

`y[idx[i]] = x[i] for i in [0, 1,...,rank(x) - 1]`

#### For example:



```
# tensor 'x' is [1, 1, 2, 4, 4, 4, 7, 8, 8]
y, idx = unique(x)
y ==> [1, 2, 4, 7, 8]
idx ==> [0, 0, 1, 2, 2, 2, 3, 4, 4]
```

For an `2-D` tensor `x` with `axis = 0`:

```
# tensor 'x' is [[1, 0, 0],
#                [1, 0, 0],
#                [2, 0, 0]]
y, idx = unique(x, axis=0)
y ==> [[1, 0, 0],
       [2, 0, 0]]
idx ==> [0, 0, 1]
```

For an `2-D` tensor `x` with `axis = 1`:

```
# tensor 'x' is [[1, 0, 0],
#                [1, 0, 0],
#                [2, 0, 0]]
y, idx = unique(x, axis=1)
y ==> [[1, 0],
       [1, 0],
       [2, 0]]
idx ==> [0, 1, 1]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`<a id="x"></a>
</td>
<td>
A `Tensor`. A `Tensor`.
</td>
</tr><tr>
<td>
`axis`<a id="axis"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A `Tensor` of type `int32` (default: None). The axis of the Tensor to
find the unique elements.
</td>
</tr><tr>
<td>
`out_idx`<a id="out_idx"></a>
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../../tf.md#int32"><code>tf.int32</code></a>.
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
A tuple of `Tensor` objects (y, idx).
</td>
</tr>
<tr>
<td>
`y`<a id="y"></a>
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`idx`<a id="idx"></a>
</td>
<td>
A `Tensor` of type `out_idx`.
</td>
</tr>
</table>

