# Goal

**Status:** Conceptual in v0.5.3; no canonical serialization.

A Goal expresses an intended organizational outcome. It provides context for proposing and evaluating Tasks; it does not itself authorize execution.

A future Goal object should support a stable identifier, outcome statement, accountable principals, measurable criteria, time horizon, parent or related goals, and references to Tasks and evidence. Goal progress should be derived from explicit evidence and verification rather than inferred solely from Run success.

Implementations MAY use local goal models with v0.5.3 objects. They MUST NOT emit or advertise those records as canonical v0.5.3 Goal objects. A future RFC must define lifecycle, measurement, hierarchy, closure, conflict handling, and privacy rules before Goal enters the conformance surface.
