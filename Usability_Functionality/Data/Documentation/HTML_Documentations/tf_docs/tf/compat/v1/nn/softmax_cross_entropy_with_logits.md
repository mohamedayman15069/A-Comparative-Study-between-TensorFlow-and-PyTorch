description: Computes softmax cross entropy between logits and labels. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.softmax_cross_entropy_with_logits" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.softmax_cross_entropy_with_logits

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/nn_ops.py">View source</a>



Computes softmax cross entropy between `logits` and `labels`. (deprecated)


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.softmax_cross_entropy_with_logits(
    labels=None, logits=None, dim=-1, name=None, axis=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Deprecated: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:

Future major versions of TensorFlow will allow gradients to flow
into the labels input on backprop by default.

See `tf.nn.softmax_cross_entropy_with_logits_v2`.


Measures the probability error in discrete classification tasks in which the
classes are mutually exclusive (each entry is in exactly one class).  For
example, each CIFAR-10 image is labeled with one and only one label: an image
can be a dog or a truck, but not both.

**NOTE:**  While the classes are mutually exclusive, their probabilities
need not be.  All that is required is that each row of `labels` is
a valid probability distribution.  If they are not, the computation of the
gradient will be incorrect.

If using exclusive `labels` (wherein one and only
one class is true at a time), see `sparse_softmax_cross_entropy_with_logits`.

**WARNING:** This op expects unscaled logits, since it performs a `softmax`
on `logits` internally for efficiency.  Do not call this op with the
output of `softmax`, as it will produce incorrect results.

A common use case is to have logits and labels of shape
`[batch_size, num_classes]`, but higher dimensions are supported, with
the `dim` argument specifying the class dimension.

Backpropagation will happen only into `logits`.  To calculate a cross entropy
loss that allows backpropagation into both `logits` and `labels`, see
`tf.nn.softmax_cross_entropy_with_logits_v2`.

**Note that to avoid confusion, it is required to pass only named arguments to
this function.**

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`labels`<a id="labels"></a>
</td>
<td>
Each vector along the class dimension should hold a valid
probability distribution e.g. for the case in which labels are of shape
`[batch_size, num_classes]`, each row of `labels[i]` must be a valid
probability distribution.
</td>
</tr><tr>
<td>
`logits`<a id="logits"></a>
</td>
<td>
Per-label activations, typically a linear output. These activation
energies are interpreted as unnormalized log probabilities.
</td>
</tr><tr>
<td>
`dim`<a id="dim"></a>
</td>
<td>
The class dimension. Defaulted to -1 which is the last dimension.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`axis`<a id="axis"></a>
</td>
<td>
Alias for dim.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` that contains the softmax cross entropy loss. Its type is the
same as `logits` and its shape is the same as `labels` except that it does
not have the last dimension of `labels`.
</td>
</tr>

</table>

