# Specifications

These documents describe the Protocol's semantic model. The conformance status of a concept is explicit:

| Concept | v0.5.3 status | Canonical serialization |
| --- | --- | --- |
| Company | Conceptual | Not defined |
| Goal | Conceptual | Not defined |
| Task | Normative | `task.schema.json` |
| Capability | Partial | `capability-lease.schema.json`, Tool objects |
| Run | Normative | `run.schema.json` |
| Decision | Partial | `authority-decision.schema.json` |
| Authority | Normative core | Policy, grant, decision, approval, and lease schemas |
| Verification | Normative core | Spec, run, result, and evidence schemas |
| Signal | Future, non-normative | Not defined |

"Conceptual" defines a stable role in the semantic model but does not authorize a v0.5.3 wire-format or conformance claim. Normative serialization is defined by `schemas/v0/`; registries and semantic conformance rules add requirements that JSON Schema cannot express.

The key words `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are to be interpreted as described in RFC 2119 and RFC 8174 when, and only when, they appear in all capitals.
