description: Elementwise computes the bitwise OR of x and y.
robots: noindex

# tf.raw_ops.BitwiseOr

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Elementwise computes the bitwise OR of `x` and `y`.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BitwiseOr`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BitwiseOr(
    x, y, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The result will have those bits set, that are set in `x`, `y` or both. The
computation is performed on the underlying representations of `x` and `y`.

#### For example:



```python
import tensorflow as tf
from tensorflow.python.ops import bitwise_ops
dtype_list = [tf.int8, tf.int16, tf.int32, tf.int64,
              tf.uint8, tf.uint16, tf.uint32, tf.uint64]

for dtype in dtype_list:
  lhs = tf.constant([0, 5, 3, 14], dtype=dtype)
  rhs = tf.constant([5, 0, 7, 11], dtype=dtype)
  exp = tf.constant([5, 5, 7, 15], dtype=tf.float32)

  res = bitwise_ops.bitwise_or(lhs, rhs)
  tf.assert_equal(tf.cast(res,  tf.float32), exp)  # TRUE
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
A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`.
</td>
</tr><tr>
<td>
`y`<a id="y"></a>
</td>
<td>
A `Tensor`. Must have the same type as `x`.
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
A `Tensor`. Has the same type as `x`.
</td>
</tr>

</table>

