<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary.tensor_summary" />
<meta itemprop="path" content="Stable" />
</div>

# tf.summary.tensor_summary

Outputs a `Summary` protocol buffer with a serialized tensor.proto.

### Aliases:

* `tf.compat.v1.summary.tensor_summary`
* `tf.compat.v2.compat.v1.summary.tensor_summary`
* `tf.summary.tensor_summary`

``` python
tf.summary.tensor_summary(
    name,
    tensor,
    summary_description=None,
    collections=None,
    summary_metadata=None,
    family=None,
    display_name=None
)
```

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`name`</b>: A name for the generated node. If display_name is not set, it will
  also serve as the tag name in TensorBoard. (In that case, the tag
  name will inherit tf name scopes.)
* <b>`tensor`</b>: A tensor of any type and shape to serialize.
* <b>`summary_description`</b>: A long description of the summary sequence. Markdown
  is supported.
* <b>`collections`</b>: Optional list of graph collections keys. The new summary op is
  added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
* <b>`summary_metadata`</b>: Optional SummaryMetadata proto (which describes which
  plugins may use the summary value).
* <b>`family`</b>: Optional; if provided, used as the prefix of the summary tag,
  which controls the name used for display on TensorBoard when
  display_name is not set.
* <b>`display_name`</b>: A string used to name this data in TensorBoard. If this is
  not set, then the node name will be used instead.


#### Returns:

A scalar `Tensor` of type `string`. The serialized `Summary` protocol
buffer.
