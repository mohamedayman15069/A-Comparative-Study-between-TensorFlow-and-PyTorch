description: Returns the index with the largest value across dimensions of a tensor.
robots: noindex

# tf.raw_ops.ArgMax

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the index with the largest value across dimensions of a tensor.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ArgMax`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ArgMax(
    input,
    dimension,
    output_type=<a href="../../tf/dtypes.md#int64"><code>tf.dtypes.int64</code></a>,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note that in case of ties the identity of the return value is not guaranteed.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Usage</h2></th></tr>
<tr class="alt">
<td colspan="2">
```python
import tensorflow as tf
a = [1, 10, 26.9, 2.8, 166.32, 62.3]
b = tf.math.argmax(input = a)
c = tf.keras.backend.eval(b)
# c = 4
# here a[4] = 166.32 which is the largest element of a across axis 0
```
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`<a id="input"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`, `qint8`, `quint8`, `qint32`, `qint16`, `quint16`, `bool`.
</td>
</tr><tr>
<td>
`dimension`<a id="dimension"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `int16`, `int32`, `int64`.
int16, int32 or int64, must be in the range `[-rank(input), rank(input))`.
Describes which dimension of the input Tensor to reduce across. For vectors,
use dimension = 0.
</td>
</tr><tr>
<td>
`output_type`<a id="output_type"></a>
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int16, tf.uint16, tf.int32, tf.int64`. Defaults to <a href="../../tf.md#int64"><code>tf.int64</code></a>.
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
A `Tensor` of type `output_type`.
</td>
</tr>

</table>

