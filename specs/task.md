# Task

**Status:** Normative in v0.5.3.

A Task is a bounded, accountable unit of work undertaken to achieve or advance an outcome. It is the sole canonical work object in the Protocol.

## Lifecycle

The canonical states are `DRAFT`, `READY`, `ACTIVE`, `WAITING_AUTHORITY`, `VERIFYING`, `NEEDS_DECISION`, `VERIFIED`, `FAILED`, and `CANCELLED`. Implementations MUST enforce the transitions in `schemas/v0/registries/task-transitions.json`; a structurally valid but illegal transition is non-conformant.

Task owns business lifecycle and completion. Execution is represented by one or more Runs. A Task MUST NOT enter `VERIFIED` solely because a Run succeeded. Applicable verification requirements and completion policy govern that transition.

## Composition and recovery

Tasks may contain child Task references. Completion semantics are either `first_success` or `explicit` as defined by the schema. Recovery selectors and their permitted targets are normative registry entries. Implementations MUST NOT invent a recovery selector inside the v0.5.3 namespace.

## Serialization

Canonical structure is defined by `schemas/v0/task.schema.json` together with shared schemas and registries. Semantic constraints that are not expressible in JSON Schema remain conformance requirements.
