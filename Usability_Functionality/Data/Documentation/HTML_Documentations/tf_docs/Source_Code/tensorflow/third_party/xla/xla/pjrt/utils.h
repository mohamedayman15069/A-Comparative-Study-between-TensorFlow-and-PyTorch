/* Copyright 2020 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#ifndef XLA_PJRT_UTILS_H_
#define XLA_PJRT_UTILS_H_

#include <cstdint>
#include <functional>
#include <memory>
#include <optional>
#include <vector>

#include "absl/container/flat_hash_map.h"
#include "absl/types/span.h"
#include "mlir/IR/BuiltinOps.h"  // from @llvm-project
#include "xla/client/executable_build_options.h"
#include "xla/client/xla_computation.h"
#include "xla/hlo/ir/hlo_module.h"
#include "xla/pjrt/layout_mode.h"
#include "xla/service/computation_placer.h"
#include "xla/shape.h"
#include "xla/status.h"
#include "xla/statusor.h"
#include "xla/xla_data.pb.h"

namespace xla {

// Returns the num_replicas, num_partitions and device assignment given a
// ExecutableBuildOptions and whether we want a portable executable.
Status ParseDeviceAssignmentCompileOptions(
    bool compile_portable_executable, ExecutableBuildOptions* build_options,
    std::function<StatusOr<DeviceAssignment>(int, int)>
        GetDefaultDeviceAssignmentFunction,
    int* num_replicas, int* num_partitions,
    std::shared_ptr<DeviceAssignment>* device_assignment);

// Returns the LayoutMode for each argument of the main function in the
// module. Checks for the "mhlo.layout_mode" attr, and if not present, assumes
// LayoutMode::Mode::kDefault.
StatusOr<std::vector<LayoutMode>> GetArgLayoutModes(mlir::ModuleOp module);
// Returns the LayoutMode for each output of the main function in the
// module. Checks for the "mhlo.layout_mode" attr, and if not present, assumes
// LayoutMode::Mode::kDefault.
StatusOr<std::vector<LayoutMode>> GetOutputLayoutModes(mlir::ModuleOp module);

// Populates the frontend attributes "arg_layout_mode" and "out_layout_mode" in
// xla_computation based on `module`. This function must be called before the
// LayoutMode getters below work correctly on `computation`.
Status AddLayoutModesToFrontendAttrs(mlir::ModuleOp module,
                                     XlaComputation& xla_computation);
// Returns the LayoutMode for each argument of the computations. Checks for the
// "arg_layout_mode" frontend attribute, and if not present, assumes
// LayoutMode::Mode::kDefault.
StatusOr<std::vector<LayoutMode>> GetArgLayoutModes(
    const XlaComputation& computation);
// Returns the LayoutMode for each argument of the computations. Checks for the
// "out_layout_mode" frontend attribute, and if not present, assumes
// LayoutMode::Mode::kDefault.
StatusOr<std::vector<LayoutMode>> GetOutputLayoutModes(
    const XlaComputation& computation);

// Returns (arg shapes, output shape) with properly-set Layouts that can
// be passed to XLA to reflect arg_layout_modes and out_layout_modes.
StatusOr<std::pair<std::vector<Shape>, Shape>> LayoutModesToXlaShapes(
    const XlaComputation& computation, std::vector<LayoutMode> arg_layout_modes,
    std::vector<LayoutMode> out_layout_modes,
    std::function<StatusOr<Shape>(Shape)>
        choose_compact_layout_for_shape_function);

// Generates useful data structures for communciating desired layouts to XLA:
// * Returns a vector of argument xla::Shapes with properly-set Layouts
// * Returns vector of pointers to those Shapes to create HloModuleConfig
// * Modifies `build_options` to have the correct result_layout set or unset
StatusOr<std::pair<std::vector<Shape>, std::vector<const Shape*>>>
LayoutModesToXla(const XlaComputation& computation,
                 std::vector<LayoutMode> arg_layout_modes,
                 std::vector<LayoutMode> out_layout_modes,
                 std::function<StatusOr<Shape>(Shape)>
                     choose_compact_layout_for_shape_function,
                 ExecutableBuildOptions& build_options);

// Returns pointers to the argument layouts given an XlaComputation and
// ExecutableBuildOptions.
Status DetermineArgumentLayoutsFromCompileOptions(
    const XlaComputation& computation,
    std::function<StatusOr<Shape>(Shape)>
        choose_compact_layout_for_shape_function,
    std::optional<std::vector<Shape>>& argument_layouts,
    ExecutableBuildOptions* build_options,
    std::vector<const Shape*>* argument_layout_pointers);

// Executables can donate buffers so that buffers can be aliased from inputs
// to outputs. This function returns a sorted vector of parameters that must be
// donated when executable is run. tuple_inputs reflects the option that
// executable was compiled with.
StatusOr<std::vector<int>> ComputeParametersThatMustBeDonated(
    const HloModule& hlo_module, bool tuple_inputs);

// Return max parallelism level.
int DefaultThreadPoolSize();

// Returns true if the striding of an array corresponds to a major-to-minor
// layout.
bool HasMajorToMinorLayout(PrimitiveType type, absl::Span<int64_t const> dims,
                           absl::Span<int64_t const> byte_strides);

// Constructs a new dense array shape with the given byte strides. Supports only
// trivial (compact) byte_strides that represents a transposition of a dense
// buffer.
StatusOr<Shape> MakeShapeWithTrivialByteStrides(
    PrimitiveType element_type, absl::Span<const int64_t> dimensions,
    absl::Span<const int64_t> byte_strides);

// If a buffer `is_donated`, then it can only be used once. This function
// records the use into donation_clashes and tests for incompatible uses.
// Multiple uses are valid iff they are all not donations.  The provided map
// stores the opaque buffer identity, a bool to denote if the previous use is a
// donation, and the index of the previous use for better error messages.
Status TestBufferDonationClashes(
    void* opaque_key,
    absl::flat_hash_map<const void*, std::pair<bool, int>>& donation_clashes,
    bool is_donated, int arg_idx, int replica, int partition);

}  // namespace xla

#endif  // XLA_PJRT_UTILS_H_