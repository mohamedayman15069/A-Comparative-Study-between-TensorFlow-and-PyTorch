<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.framework.VariableDeviceChooser" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
</div>

# tf.contrib.framework.VariableDeviceChooser

## Class `VariableDeviceChooser`

Device chooser for variables.



<!-- Placeholder for "Used in" -->

When using a parameter server it will assign them in a round-robin fashion.
When not using a parameter server it allows GPU or CPU placement.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_tasks=0,
    job_name='ps',
    device_type='CPU',
    device_index=0,
    replica=None
)
```

Initialize VariableDeviceChooser.


#### Usage:

To use with 2 parameter servers:
  VariableDeviceChooser(2)

To use without parameter servers:
  VariableDeviceChooser()
  VariableDeviceChooser(device_type='GPU') # For GPU placement



#### Args:


* <b>`num_tasks`</b>: number of tasks.
* <b>`job_name`</b>: String, a name for the parameter server job.
* <b>`device_type`</b>: Optional device type string (e.g. "CPU" or "GPU")
* <b>`device_index`</b>: int.  Optional device index.  If left unspecified, device
  represents 'any' device_index.



## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(op)
```

Call self as a function.




