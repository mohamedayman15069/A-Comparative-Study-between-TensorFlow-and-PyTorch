description: Public API for tf._api.v2.sparse namespace

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.sparse" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.sparse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf._api.v2.sparse namespace



## Classes

[`class SparseConditionalAccumulator`](../../../tf/compat/v1/SparseConditionalAccumulator.md): A conditional accumulator for aggregating sparse gradients.

[`class SparseTensor`](../../../tf/sparse/SparseTensor.md): Represents a sparse tensor.

## Functions

[`add(...)`](../../../tf/compat/v1/sparse_add.md): Adds two tensors, at least one of each is a `SparseTensor`. (deprecated arguments)

[`bincount(...)`](../../../tf/sparse/bincount.md): Count the number of times an integer value appears in a tensor.

[`concat(...)`](../../../tf/compat/v1/sparse_concat.md): Concatenates a list of `SparseTensor` along the specified dimension. (deprecated arguments)

[`cross(...)`](../../../tf/sparse/cross.md): Generates sparse cross from a list of sparse and dense tensors.

[`cross_hashed(...)`](../../../tf/sparse/cross_hashed.md): Generates hashed sparse cross from a list of sparse and dense tensors.

[`expand_dims(...)`](../../../tf/sparse/expand_dims.md): Returns a tensor with an length 1 axis inserted at index `axis`.

[`eye(...)`](../../../tf/sparse/eye.md): Creates a two-dimensional sparse tensor with ones along the diagonal.

[`fill_empty_rows(...)`](../../../tf/sparse/fill_empty_rows.md): Fills empty rows in the input 2-D `SparseTensor` with a default value.

[`from_dense(...)`](../../../tf/sparse/from_dense.md): Converts a dense tensor into a sparse tensor.

[`mask(...)`](../../../tf/sparse/mask.md): Masks elements of `IndexedSlices`.

[`matmul(...)`](../../../tf/sparse/sparse_dense_matmul.md): Multiply SparseTensor (or dense Matrix) (of rank 2) "A" by dense matrix

[`maximum(...)`](../../../tf/sparse/maximum.md): Returns the element-wise max of two SparseTensors.

[`merge(...)`](../../../tf/compat/v1/sparse_merge.md): Combines a batch of feature ids and values into a single `SparseTensor`. (deprecated)

[`minimum(...)`](../../../tf/sparse/minimum.md): Returns the element-wise min of two SparseTensors.

[`placeholder(...)`](../../../tf/compat/v1/sparse_placeholder.md): Inserts a placeholder for a sparse tensor that will be always fed.

[`reduce_max(...)`](../../../tf/compat/v1/sparse_reduce_max.md): Computes <a href="../../../tf/sparse/maximum.md"><code>tf.sparse.maximum</code></a> of elements across dimensions of a SparseTensor. (deprecated arguments) (deprecated arguments)

[`reduce_max_sparse(...)`](../../../tf/compat/v1/sparse_reduce_max_sparse.md): Computes the max of elements across dimensions of a SparseTensor. (deprecated arguments)

[`reduce_sum(...)`](../../../tf/compat/v1/sparse_reduce_sum.md): Computes <a href="../../../tf/sparse/add.md"><code>tf.sparse.add</code></a> of elements across dimensions of a SparseTensor. (deprecated arguments) (deprecated arguments)

[`reduce_sum_sparse(...)`](../../../tf/compat/v1/sparse_reduce_sum_sparse.md): Computes the sum of elements across dimensions of a SparseTensor. (deprecated arguments)

[`reorder(...)`](../../../tf/sparse/reorder.md): Reorders a `SparseTensor` into the canonical, row-major ordering.

[`reset_shape(...)`](../../../tf/sparse/reset_shape.md): Resets the shape of a `SparseTensor` with indices and values unchanged.

[`reshape(...)`](../../../tf/sparse/reshape.md): Reshapes a `SparseTensor` to represent values in a new dense shape.

[`retain(...)`](../../../tf/sparse/retain.md): Retains specified non-empty values within a `SparseTensor`.

[`segment_mean(...)`](../../../tf/compat/v1/sparse_segment_mean.md): Computes the mean along sparse segments of a tensor.

[`segment_sqrt_n(...)`](../../../tf/compat/v1/sparse_segment_sqrt_n.md): Computes the sum along sparse segments of a tensor divided by the sqrt(N).

[`segment_sum(...)`](../../../tf/compat/v1/sparse_segment_sum.md): Computes the sum along sparse segments of a tensor.

[`slice(...)`](../../../tf/sparse/slice.md): Slice a `SparseTensor` based on the `start` and `size`.

[`softmax(...)`](../../../tf/sparse/softmax.md): Applies softmax to a batched N-D `SparseTensor`.

[`sparse_dense_matmul(...)`](../../../tf/sparse/sparse_dense_matmul.md): Multiply SparseTensor (or dense Matrix) (of rank 2) "A" by dense matrix

[`split(...)`](../../../tf/compat/v1/sparse_split.md): Split a `SparseTensor` into `num_split` tensors along `axis`. (deprecated arguments)

[`to_dense(...)`](../../../tf/sparse/to_dense.md): Converts a `SparseTensor` into a dense tensor.

[`to_indicator(...)`](../../../tf/sparse/to_indicator.md): Converts a `SparseTensor` of ids into a dense bool indicator tensor.

[`transpose(...)`](../../../tf/sparse/transpose.md): Transposes a `SparseTensor`.

