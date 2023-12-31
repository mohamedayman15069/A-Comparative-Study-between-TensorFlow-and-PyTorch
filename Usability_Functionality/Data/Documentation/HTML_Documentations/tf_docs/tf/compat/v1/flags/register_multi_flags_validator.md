description: Adds a constraint to multiple flags.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.register_multi_flags_validator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.register_multi_flags_validator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Adds a constraint to multiple flags.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.register_multi_flags_validator(
    flag_names,
    multi_flags_checker,
    message=&#x27;Flags validation failed&#x27;,
    flag_values=_flagvalues.FLAGS
)
</code></pre>



<!-- Placeholder for "Used in" -->

The constraint is validated when flags are initially parsed, and after each
change of the corresponding flag's value.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`flag_names`<a id="flag_names"></a>
</td>
<td>
[str | FlagHolder], a list of the flag names or holders to be
checked. Positional-only parameter.
</td>
</tr><tr>
<td>
`multi_flags_checker`<a id="multi_flags_checker"></a>
</td>
<td>
callable, a function to validate the flag.

* input - dict, with keys() being flag_names, and value for each key
    being the value of the corresponding flag (string, boolean, etc).
* output - bool, True if validator constraint is satisfied.
    If constraint is not satisfied, it should either return False or
    raise flags.ValidationError.
</td>
</tr><tr>
<td>
`message`<a id="message"></a>
</td>
<td>
str, error text to be shown to the user if checker returns False.
If checker raises flags.ValidationError, message from the raised
error will be shown.
</td>
</tr><tr>
<td>
`flag_values`<a id="flag_values"></a>
</td>
<td>
flags.FlagValues, optional FlagValues instance to validate
against.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`AttributeError`<a id="AttributeError"></a>
</td>
<td>
Raised when a flag is not registered as a valid flag name.
</td>
</tr><tr>
<td>
`ValueError`<a id="ValueError"></a>
</td>
<td>
Raised when multiple FlagValues are used in the same
invocation. This can occur when FlagHolders have different `_flagvalues`
or when str-type flag_names entries are present and the `flag_values`
argument does not match that of provided FlagHolder(s).
</td>
</tr>
</table>

