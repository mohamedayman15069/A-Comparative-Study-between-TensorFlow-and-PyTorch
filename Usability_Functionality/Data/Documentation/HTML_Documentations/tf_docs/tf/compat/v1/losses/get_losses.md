description: Gets the list of losses from the loss_collection.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.losses.get_losses" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.losses.get_losses

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/ops/losses/util.py">View source</a>



Gets the list of losses from the loss_collection.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.losses.get_losses(
    scope=None, loss_collection=ops.GraphKeys.LOSSES
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`scope`<a id="scope"></a>
</td>
<td>
An optional scope name for filtering the losses to return.
</td>
</tr><tr>
<td>
`loss_collection`<a id="loss_collection"></a>
</td>
<td>
Optional losses collection.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
a list of loss tensors.
</td>
</tr>

</table>

