# Decision

**Status:** Partial in v0.5.3.

A Decision records a governed evaluation that influences work or execution. In the v0.5.3 canonical surface, the serialized decision object is specifically an AuthorityDecision; a general-purpose organizational Decision object is not defined.

An AuthorityDecision binds an Effect's semantic hash, a subject principal, a decision of `ALLOW`, `DENY`, or `REQUIRE_APPROVAL`, matched policy references, optional approval references, a reason, and a decision timestamp. Implementations MUST evaluate the decision against the exact Effect semantics and MUST NOT reuse it for a materially different Effect.

Decision records are audit facts, not mutable policy. Re-evaluation produces a new decision. A future general Decision RFC must define provenance, inputs, alternatives, rationale, supersession, and relationship to Task proposals without weakening AuthorityDecision requirements.
