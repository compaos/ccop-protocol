# Verification

**Status:** Normative core in v0.5.3.

Verification determines whether explicit claims about a Task, Run, Operation, Result, or other subject are supported by evidence under a declared method.

## Artifacts

- `VerificationSpec` declares checks, evidence selection, timing, and control requirements.
- `VerificationRun` records a verifier's bounded execution of a specification.
- `VerificationResult` records `VERIFIED`, `PARTIALLY_VERIFIED`, `FAILED`, or `UNABLE_TO_VERIFY`.
- `Evidence` records traceable material and provenance.

Verification MUST remain distinct from execution success. A successful Run or Operation is evidence about execution, not proof that the Task's completion criteria were met. An implementation MUST preserve `FAILED` versus `UNABLE_TO_VERIFY`; absence of evidence is not evidence of failure unless the specification states that rule.

Verifier independence and evidence closure use the `direct_control` and `full_closure` modes defined in the schema. Deadlines and time anchors MUST be evaluated deterministically. Verification records MUST identify the applied specification and subject.
