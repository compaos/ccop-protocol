# Capability

**Status:** Partial in v0.5.3.

A Capability describes what a principal, engine, tool, or integration can perform. It is distinct from a Task, which describes what is to be done, and from Authority, which determines what is permitted.

v0.5.3 does not define a standalone canonical Capability object. Operational capability is expressed through Tool and ToolRequest objects and through a CapabilityLease that binds a principal, task, run, effect, resource, tool, operation, authority decision, validity interval, and use limits.

A CapabilityLease MUST be treated as a constrained, auditable authorization artifact, not as proof that an operation is safe or successful. Possessing technical ability does not imply authority. Implementations MUST apply the linked policy, decision, grant, approval, and lease-consumption rules.

A future standalone Capability RFC must define discovery, versioning, input and output contracts, provider independence, compatibility, and lifecycle without privileging a marketplace or runtime.
