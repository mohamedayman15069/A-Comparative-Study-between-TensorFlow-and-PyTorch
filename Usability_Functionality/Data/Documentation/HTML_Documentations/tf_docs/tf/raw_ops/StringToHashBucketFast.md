description: Converts each string in the input Tensor to its hash mod by a number of buckets.
robots: noindex

# tf.raw_ops.StringToHashBucketFast

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Converts each string in the input Tensor to its hash mod by a number of buckets.


<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StringToHashBucketFast`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StringToHashBucketFast(
    input, num_buckets, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The hash function is deterministic on the content of the string within the
process and will never change. However, it is not suitable for cryptography.
This function may be used when CPU time is scarce and inputs are trusted or
unimportant. There is a risk of adversaries constructing inputs that all hash
to the same bucket. To prevent this problem, use a strong hash function with
`tf.string_to_hash_bucket_strong`.

#### Examples:



```
>>> tf.strings.to_hash_bucket_fast(["Hello", "TensorFlow", "2.x"], 3).numpy()
array([0, 2, 2])
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
A `Tensor` of type `string`. The strings to assign a hash bucket.
</td>
</tr><tr>
<td>
`num_buckets`<a id="num_buckets"></a>
</td>
<td>
An `int` that is `>= 1`. The number of buckets.
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
A `Tensor` of type `int64`.
</td>
</tr>

</table>

