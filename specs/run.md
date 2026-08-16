# Run

**Status:** Normative in v0.5.3.

A Run is one governed execution instance and correlation envelope of a Task. One Task may have zero, one, or many Runs.

## Lifecycle

The canonical states are `QUEUED`, `RUNNING`, `WAITING_AUTHORITY`, `WAITING_DECISION`, `PAUSED`, `CANCELLING`, `SUCCEEDED`, `FAILED`, `DENIED`, `CANCELLED`, and `TIMED_OUT`. Implementations MUST enforce `schemas/v0/registries/run-transitions.json`.

Terminal reasons are `EXECUTION_TIMEOUT`, `QUEUE_TIMEOUT`, `PAUSE_TIMEOUT`, `CANCELLATION_TIMEOUT`, `AUTHORITY_DENIED`, and `TECHNICAL_FAILURE`. Implementations MUST preserve the distinction between denial, cancellation, timeout, and technical failure.

## Boundaries

Run identifies the Task and execution engine and may aggregate costs. Effect records intended external mutation; Operation records an actual execution attempt for an Effect. A Run may contain multiple Effects and Operations. Run MUST NOT be used as a substitute for decision, evidence, authority, operation, result, or verification records.

Serialization is defined by `schemas/v0/run.schema.json`.
