# Authority

**Status:** Normative core in v0.5.3.

Authority determines whether a principal may cause an Effect under specified conditions. Capability answers whether an action can be performed; Authority answers whether it may be performed.

## Core artifacts

- `AuthorityPolicy` defines ordered matching rules and outcomes.
- `AuthorityDecision` records evaluation for an exact Effect semantic hash.
- `AuthorityGrant` delegates bounded authority to a principal.
- `Approval` records a required approval.
- `CapabilityLease` binds permission to a concrete execution context and use limit.
- `GovernanceWriterRegistry` restricts which principals may write sensitive lifecycle events.

Policy outcomes are `ALLOW`, `DENY`, and `REQUIRE_APPROVAL`. Implementations MUST apply ceiling rules, grant boundaries, validity intervals, counters, exact subject and resource semantics, and authorized-writer rules. An execution engine MUST NOT self-assert trusted control. Structural schema validity does not satisfy these semantic requirements.

Authority artifacts MUST be auditable and attributable. Implementations MUST NOT treat a hosted account, API access, technical capability, or successful operation as implicit authority.
