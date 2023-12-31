description: Log 'msg % args' at level 'level' only first 'n' times.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.logging.log_first_n" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.logging.log_first_n

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" class="external" href="/code/stable/tensorflow/python/platform/tf_logging.py">View source</a>



Log 'msg % args' at level 'level' only first 'n' times.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.logging.log_first_n(
    level, msg, n, *args
)
</code></pre>



<!-- Placeholder for "Used in" -->

Not threadsafe.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`level`<a id="level"></a>
</td>
<td>
The level at which to log.
</td>
</tr><tr>
<td>
`msg`<a id="msg"></a>
</td>
<td>
The message to be logged.
</td>
</tr><tr>
<td>
`n`<a id="n"></a>
</td>
<td>
The number of times this should be called before it is logged.
</td>
</tr><tr>
<td>
`*args`<a id="*args"></a>
</td>
<td>
The args to be substituted into the msg.
</td>
</tr>
</table>

