description: Computes the exponential linear function.
robots: noindex

# tf.raw_ops.Elu

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the exponential linear function.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Elu`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Elu(
    features, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The ELU function is defined as:

 * $ e ^ x - 1 $ if $ x < 0 $
 * $ x $ if $ x >= 0 $

#### Examples:



```
>>> tf.nn.elu(1.0)
<tf.Tensor: shape=(), dtype=float32, numpy=1.0>
>>> tf.nn.elu(0.0)
<tf.Tensor: shape=(), dtype=float32, numpy=0.0>
>>> tf.nn.elu(-1000.0)
<tf.Tensor: shape=(), dtype=float32, numpy=-1.0>
```

See [Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs)
](http://arxiv.org/abs/1511.07289)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`features`<a id="features"></a>
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
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

