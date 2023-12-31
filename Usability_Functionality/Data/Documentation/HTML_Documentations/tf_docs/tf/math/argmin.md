description: Returns the index with the smallest value across axes of a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.argmin" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.argmin

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/math_ops.py">View source</a>



Returns the index with the smallest value across axes of a tensor.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.argmin`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.argmin(
    input,
    axis=None,
    output_type=<a href="../../tf/dtypes.md#int64"><code>tf.dtypes.int64</code></a>,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns the smallest index in case of ties.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`<a id="input"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`,
`int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`,
`quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`,
`uint64`.
</td>
</tr><tr>
<td>
`axis`<a id="axis"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
int32 or int64, must be in the range `-rank(input), rank(input))`.
Describes which axis of the input Tensor to reduce across. For vectors,
use axis = 0.
</td>
</tr><tr>
<td>
`output_type`<a id="output_type"></a>
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to
<a href="../../tf.md#int64"><code>tf.int64</code></a>.
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



#### Usage:


```python
import tensorflow as tf
a = [1, 10, 26.9, 2.8, 166.32, 62.3]
b = tf.math.argmin(input = a)
c = tf.keras.backend.eval(b)
# c = 0
# here a[0] = 1 which is the smallest element of a across axis 0
```