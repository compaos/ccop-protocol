# Terminology

## Task, not Work

Task is the canonical Protocol object for a bounded, accountable unit of work. The Protocol does not define a parallel `Work` object.

`Work` may be used as an ordinary domain word. Protocol object names, identifiers, schemas, events, and conformance surfaces use `Task`, including `task_id`, `task.schema.json`, and Task lifecycle events.

The word "Work" in the Apache License retains its legal meaning and is unrelated to the Protocol object model.

## Task and Run

A Task owns the governed business lifecycle. A Run is one governed execution instance and correlation envelope of a Task. One Task may have multiple Runs.

A Run may associate an execution engine, context, decisions, effects, operations, evidence, verification, costs, and results. It does not replace those objects. A successful Run does not complete a Task unless the applicable verification and completion policy also permits Task completion.

## Signal, Event, and Evidence

A future Signal would describe an observed change or condition in an organization's operating domain. Event records a lifecycle fact about Protocol governance objects. Evidence is traceable material that may support a Signal, Decision, or Verification.

Signal is not a canonical v0.5.3 object.
