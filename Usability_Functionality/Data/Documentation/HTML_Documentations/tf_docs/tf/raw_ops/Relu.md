description: Computes rectified linear: max(features, 0).
robots: noindex

# tf.raw_ops.Relu

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes rectified linear: `max(features, 0)`.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Relu`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Relu(
    features, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See: https://en.wikipedia.org/wiki/Rectifier_(neural_networks)
Example usage:
```
>>> tf.nn.relu([-2., 0., 3.]).numpy()
array([0., 0., 3.], dtype=float32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`features`<a id="features"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`, `qint8`.
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
A `Tensor`. Has the same type as `features`.
</td>
</tr>

</table>

