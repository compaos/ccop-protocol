# Signal

**Status:** Future, non-normative guidance. Signal is not a canonical v0.5.3 object.

A future Signal would be an immutable, structured observation of a potentially relevant change, condition, occurrence, or input in an organization's operating domain that may cause organizational evaluation or governed work to be proposed.

A Signal would describe what was observed. It would not by itself authorize, require, prioritize, or execute an action.

```text
Domain -> Source Evidence -> Signal -> Evaluation -> Task Proposal
       -> Governed Acceptance -> Task -> Run -> Effect -> Authority
       -> Operation -> Verification
```

Signal must remain distinct from Event and Evidence. Event records a lifecycle fact about Protocol governance objects. Evidence is traceable material that can support a Signal, Decision, or Verification.

A future RFC should define source and subject references, typed observation, `occurred_at`, `observed_at`, `received_at`, reported severity, confidence, trust, fingerprinting, correlation, related Signal references, Evidence references, supersession, extension rules, schemas, fixtures, and tests. Severity must remain observation metadata and must not create authority or immediate execution.

Implementations MUST NOT claim v0.5.3 Signal conformance.
