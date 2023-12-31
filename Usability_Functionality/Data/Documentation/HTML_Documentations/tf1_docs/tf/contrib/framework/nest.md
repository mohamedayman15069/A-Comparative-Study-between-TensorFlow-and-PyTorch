<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.contrib.framework.nest" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.contrib.framework.nest

## Functions for working with arbitrarily nested sequences of elements.

<!-- Placeholder for "Used in" -->

This module can perform operations on nested structures. A nested structure is a
Python sequence, tuple (including `namedtuple`), or dict that can contain
further sequences, tuples, and dicts.

attr.s decorated classes (http://www.attrs.org) are also supported, in the
same way as `namedtuple`.

The utilities here assume (and do not check) that the nested structures form a
'tree', i.e., no references in the structure of the input of these functions
should be recursive.

Example structures: `((3, 4), 5, (6, 7, (9, 10), 8))`, `(np.array(0),
  (np.array([3, 4]), tf.constant([3, 4])))`

## Functions

[`assert_same_structure(...)`](../../../tf/nest/assert_same_structure.md): Asserts that two structures are nested in the same way.

[`assert_shallow_structure(...)`](../../../tf/contrib/framework/nest/assert_shallow_structure.md): Asserts that `shallow_tree` is a shallow structure of `input_tree`.

[`flatten(...)`](../../../tf/nest/flatten.md): Returns a flat list from a given nested structure.

[`flatten_dict_items(...)`](../../../tf/contrib/framework/nest/flatten_dict_items.md): Returns a dictionary with flattened keys and values.

[`flatten_up_to(...)`](../../../tf/contrib/framework/nest/flatten_up_to.md): Flattens `input_tree` up to `shallow_tree`.

[`flatten_with_joined_string_paths(...)`](../../../tf/contrib/framework/nest/flatten_with_joined_string_paths.md): Returns a list of (string path, data element) tuples.

[`flatten_with_tuple_paths(...)`](../../../tf/contrib/framework/nest/flatten_with_tuple_paths.md): Returns a list of `(tuple_path, leaf_element)` tuples.

[`flatten_with_tuple_paths_up_to(...)`](../../../tf/contrib/framework/nest/flatten_with_tuple_paths_up_to.md): Flattens `input_tree` up to `shallow_tree`.

[`get_traverse_shallow_structure(...)`](../../../tf/contrib/framework/nest/get_traverse_shallow_structure.md): Generates a shallow structure from a `traverse_fn` and `structure`.

[`is_nested(...)`](../../../tf/nest/is_nested.md): Returns true if its input is a collections.abc.Sequence (except strings).

[`is_sequence(...)`](../../../tf/contrib/framework/nest/is_sequence.md): Returns true if its input is a collections.Sequence (except strings).

[`is_sequence_or_composite(...)`](../../../tf/contrib/framework/nest/is_sequence_or_composite.md): Returns true if its input is a sequence or a `CompositeTensor`.

[`map_structure(...)`](../../../tf/nest/map_structure.md): Applies `func` to each entry in `structure` and returns a new structure.

[`map_structure_up_to(...)`](../../../tf/contrib/framework/nest/map_structure_up_to.md): Applies a function or op to a number of partially flattened inputs.

[`map_structure_with_paths(...)`](../../../tf/contrib/framework/nest/map_structure_with_paths.md): Applies `func` to each entry in `structure` and returns a new structure.

[`map_structure_with_tuple_paths(...)`](../../../tf/contrib/framework/nest/map_structure_with_tuple_paths.md): Applies `func` to each entry in `structure` and returns a new structure.

[`map_structure_with_tuple_paths_up_to(...)`](../../../tf/contrib/framework/nest/map_structure_with_tuple_paths_up_to.md): Applies a function or op to a number of partially flattened inputs.

[`pack_sequence_as(...)`](../../../tf/nest/pack_sequence_as.md): Returns a given flattened sequence packed into a given structure.

[`yield_flat_paths(...)`](../../../tf/contrib/framework/nest/yield_flat_paths.md): Yields paths for some nested structure.

