# Company

**Status:** Conceptual in v0.5.3; no canonical serialization.

A Company is an organizational governance boundary within which goals, tasks, principals, authority, execution, and verification are interpreted. It is not a tenant record, billing account, legal opinion, or product workspace.

## Semantics

A future canonical Company object should provide a stable identifier, issuer or trust anchor, applicable policy domains, and references to principals authorized to govern the Company. It should support federation without assuming a central registry or hosted control plane.

In v0.5.3, organization identity is represented only indirectly through `Principal` objects, issuer identifiers, and `on_behalf_of` relationships. Implementations MAY maintain richer company records locally, but MUST NOT claim that a private record is a v0.5.3 Company object.

## Interoperability requirements for a future RFC

A Company RFC must define identifier ownership, cross-company references, issuer discovery, governance transfer, privacy boundaries, and conformance behavior. It must not prescribe incorporation jurisdiction, organizational chart, deployment topology, or commercial provider.
