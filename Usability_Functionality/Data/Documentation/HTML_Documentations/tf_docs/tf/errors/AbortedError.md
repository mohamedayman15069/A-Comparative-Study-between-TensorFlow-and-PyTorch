description: Raised when an operation was aborted, typically due to a concurrent action.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.errors.AbortedError" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.errors.AbortedError

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/framework/errors_impl.py">View source</a>



Raised when an operation was aborted, typically due to a concurrent action.

Inherits From: [`OpError`](../../tf/errors/OpError.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.errors.AbortedError`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.errors.AbortedError(
    node_def, op, message, *args
)
</code></pre>



<!-- Placeholder for "Used in" -->

For example, running a
<a href="../../tf/queue/QueueBase.md#enqueue"><code>tf.queue.QueueBase.enqueue</code></a>
operation may raise `AbortedError` if a
<a href="../../tf/queue/QueueBase.md#close"><code>tf.queue.QueueBase.close</code></a> operation
previously ran.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`error_code`<a id="error_code"></a>
</td>
<td>
The integer error code that describes the error.
</td>
</tr><tr>
<td>
`experimental_payloads`<a id="experimental_payloads"></a>
</td>
<td>
A dictionary describing the details of the error.
</td>
</tr><tr>
<td>
`message`<a id="message"></a>
</td>
<td>
The error message that describes the error.
</td>
</tr><tr>
<td>
`node_def`<a id="node_def"></a>
</td>
<td>
The `NodeDef` proto representing the op that failed.
</td>
</tr><tr>
<td>
`op`<a id="op"></a>
</td>
<td>
The operation that failed, if known.

*N.B.* If the failed op was synthesized at runtime, e.g. a `Send`
or `Recv` op, there will be no corresponding
<a href="../../tf/Operation.md"><code>tf.Operation</code></a>
object.  In that case, this will return `None`, and you should
instead use the <a href="../../tf/errors/OpError.md#node_def"><code>tf.errors.OpError.node_def</code></a> to
discover information about the op.
</td>
</tr>
</table>



