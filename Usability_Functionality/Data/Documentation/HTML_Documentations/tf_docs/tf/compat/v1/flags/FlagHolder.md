description: Holds a defined flag.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.FlagHolder" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__bool__"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__nonzero__"/>
</div>

# tf.compat.v1.flags.FlagHolder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Holds a defined flag.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.FlagHolder(
    flag_values: <a href="../../../../tf/compat/v1/flags/FlagValues.md"><code>tf.compat.v1.flags.FlagValues</code></a>,
    flag: Flag[_T],
    ensure_non_none_value: bool = False
)
</code></pre>



<!-- Placeholder for "Used in" -->

This facilitates a cleaner api around global state. Instead of::

    flags.DEFINE_integer('foo', ...)
    flags.DEFINE_integer('bar', ...)

    def method():
      # prints parsed value of 'bar' flag
      print(flags.FLAGS.foo)
      # runtime error due to typo or possibly bad coding style.
      print(flags.FLAGS.baz)

it encourages code like::

    _FOO_FLAG = flags.DEFINE_integer('foo', ...)
    _BAR_FLAG = flags.DEFINE_integer('bar', ...)

    def method():
      print(_FOO_FLAG.value)
      print(_BAR_FLAG.value)

since the name of the flag appears only once in the source code.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`flag_values`<a id="flag_values"></a>
</td>
<td>
The container the flag is registered to.
</td>
</tr><tr>
<td>
`flag`<a id="flag"></a>
</td>
<td>
The flag object for this flag.
</td>
</tr><tr>
<td>
`ensure_non_none_value`<a id="ensure_non_none_value"></a>
</td>
<td>
Is the value of the flag allowed to be None.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`default`<a id="default"></a>
</td>
<td>
Returns the default value of the flag.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>

</td>
</tr><tr>
<td>
`present`<a id="present"></a>
</td>
<td>
Returns True if the flag was parsed from command-line flags.
</td>
</tr><tr>
<td>
`value`<a id="value"></a>
</td>
<td>
Returns the value of the flag.

If ``_ensure_non_none_value`` is ``True``, then return value is not
``None``.
</td>
</tr>
</table>



## Methods

<h3 id="__bool__"><code>__bool__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__bool__()
</code></pre>




<h3 id="__eq__"><code>__eq__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Return self==value.


<h3 id="__nonzero__"><code>__nonzero__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__nonzero__()
</code></pre>






