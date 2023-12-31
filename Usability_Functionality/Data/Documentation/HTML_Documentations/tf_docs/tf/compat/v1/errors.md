description: Public API for tf._api.v2.errors namespace

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.errors" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="ABORTED"/>
<meta itemprop="property" content="ALREADY_EXISTS"/>
<meta itemprop="property" content="CANCELLED"/>
<meta itemprop="property" content="DATA_LOSS"/>
<meta itemprop="property" content="DEADLINE_EXCEEDED"/>
<meta itemprop="property" content="FAILED_PRECONDITION"/>
<meta itemprop="property" content="INTERNAL"/>
<meta itemprop="property" content="INVALID_ARGUMENT"/>
<meta itemprop="property" content="NOT_FOUND"/>
<meta itemprop="property" content="OK"/>
<meta itemprop="property" content="OUT_OF_RANGE"/>
<meta itemprop="property" content="PERMISSION_DENIED"/>
<meta itemprop="property" content="RESOURCE_EXHAUSTED"/>
<meta itemprop="property" content="UNAUTHENTICATED"/>
<meta itemprop="property" content="UNAVAILABLE"/>
<meta itemprop="property" content="UNIMPLEMENTED"/>
<meta itemprop="property" content="UNKNOWN"/>
</div>

# Module: tf.compat.v1.errors

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf._api.v2.errors namespace



## Classes

[`class AbortedError`](../../../tf/errors/AbortedError.md): Raised when an operation was aborted, typically due to a concurrent action.

[`class AlreadyExistsError`](../../../tf/errors/AlreadyExistsError.md): Raised when an entity that we attempted to create already exists.

[`class CancelledError`](../../../tf/errors/CancelledError.md): Raised when an operation is cancelled.

[`class DataLossError`](../../../tf/errors/DataLossError.md): Raised when unrecoverable data loss or corruption is encountered.

[`class DeadlineExceededError`](../../../tf/errors/DeadlineExceededError.md): Raised when a deadline expires before an operation could complete.

[`class FailedPreconditionError`](../../../tf/errors/FailedPreconditionError.md): Raised when some prerequisites are not met when running an operation.

[`class InternalError`](../../../tf/errors/InternalError.md): Raised when the system experiences an internal error.

[`class InvalidArgumentError`](../../../tf/errors/InvalidArgumentError.md): Raised when an operation receives an invalid argument.

[`class NotFoundError`](../../../tf/errors/NotFoundError.md): Raised when a requested entity (e.g., a file or directory) was not found.

[`class OpError`](../../../tf/errors/OpError.md): The base class for TensorFlow exceptions.

[`class OutOfRangeError`](../../../tf/errors/OutOfRangeError.md): Raised when an operation iterates past the valid range.

[`class PermissionDeniedError`](../../../tf/errors/PermissionDeniedError.md): Raised when the caller does not have permission to run an operation.

[`class ResourceExhaustedError`](../../../tf/errors/ResourceExhaustedError.md): Raised when some resource has been exhausted while running operation.

[`class UnauthenticatedError`](../../../tf/errors/UnauthenticatedError.md): Raised when the request does not have valid authentication credentials.

[`class UnavailableError`](../../../tf/errors/UnavailableError.md): Raised when the runtime is currently unavailable.

[`class UnimplementedError`](../../../tf/errors/UnimplementedError.md): Raised when an operation has not been implemented.

[`class UnknownError`](../../../tf/errors/UnknownError.md): Unknown error.

[`class raise_exception_on_not_ok_status`](../../../tf/compat/v1/errors/raise_exception_on_not_ok_status.md): Context manager to check for C API status.

## Functions

[`error_code_from_exception_type(...)`](../../../tf/compat/v1/errors/error_code_from_exception_type.md)

[`exception_type_from_error_code(...)`](../../../tf/compat/v1/errors/exception_type_from_error_code.md)



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Other Members</h2></th></tr>

<tr>
<td>
ABORTED<a id="ABORTED"></a>
</td>
<td>
`10`
</td>
</tr><tr>
<td>
ALREADY_EXISTS<a id="ALREADY_EXISTS"></a>
</td>
<td>
`6`
</td>
</tr><tr>
<td>
CANCELLED<a id="CANCELLED"></a>
</td>
<td>
`1`
</td>
</tr><tr>
<td>
DATA_LOSS<a id="DATA_LOSS"></a>
</td>
<td>
`15`
</td>
</tr><tr>
<td>
DEADLINE_EXCEEDED<a id="DEADLINE_EXCEEDED"></a>
</td>
<td>
`4`
</td>
</tr><tr>
<td>
FAILED_PRECONDITION<a id="FAILED_PRECONDITION"></a>
</td>
<td>
`9`
</td>
</tr><tr>
<td>
INTERNAL<a id="INTERNAL"></a>
</td>
<td>
`13`
</td>
</tr><tr>
<td>
INVALID_ARGUMENT<a id="INVALID_ARGUMENT"></a>
</td>
<td>
`3`
</td>
</tr><tr>
<td>
NOT_FOUND<a id="NOT_FOUND"></a>
</td>
<td>
`5`
</td>
</tr><tr>
<td>
OK<a id="OK"></a>
</td>
<td>
`0`
</td>
</tr><tr>
<td>
OUT_OF_RANGE<a id="OUT_OF_RANGE"></a>
</td>
<td>
`11`
</td>
</tr><tr>
<td>
PERMISSION_DENIED<a id="PERMISSION_DENIED"></a>
</td>
<td>
`7`
</td>
</tr><tr>
<td>
RESOURCE_EXHAUSTED<a id="RESOURCE_EXHAUSTED"></a>
</td>
<td>
`8`
</td>
</tr><tr>
<td>
UNAUTHENTICATED<a id="UNAUTHENTICATED"></a>
</td>
<td>
`16`
</td>
</tr><tr>
<td>
UNAVAILABLE<a id="UNAVAILABLE"></a>
</td>
<td>
`14`
</td>
</tr><tr>
<td>
UNIMPLEMENTED<a id="UNIMPLEMENTED"></a>
</td>
<td>
`12`
</td>
</tr><tr>
<td>
UNKNOWN<a id="UNKNOWN"></a>
</td>
<td>
`2`
</td>
</tr>
</table>

