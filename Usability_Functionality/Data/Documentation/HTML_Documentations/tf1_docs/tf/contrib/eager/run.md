<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.eager.run" />
<meta itemprop="path" content="Stable" />
</div>

# tf.contrib.eager.run

Runs the program with an optional main function and argv list.

``` python
tf.contrib.eager.run(
    main=None,
    argv=None
)
```

<!-- Placeholder for "Used in" -->

The program will run with eager execution enabled.

#### Example:


```python
import tensorflow as tf
# Import subject to future changes:
from tensorflow.contrib.eager.python import tfe

def main(_):
  u = tf.constant(6.0)
  v = tf.constant(7.0)
  print(u * v)

if __name__ == "__main__":
  tfe.run()
```

#### Args:


* <b>`main`</b>: the main function to run.
* <b>`argv`</b>: the arguments to pass to it.