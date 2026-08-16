# Governance

## Purpose

This project governs the Company Coordination and Operations Protocol (CCOP) as an implementation-neutral public standard. Governance decisions must protect interoperability and the ability of independent implementations to participate on equal terms.

## Roles

- **Contributors** submit issues, RFCs, specifications, schemas, tests, or reference code.
- **Maintainers** review contributions, operate releases, and apply this policy.
- **Editors** maintain normative text and ensure that accepted decisions are represented consistently.

The current maintainer list and public contact information are recorded in `MAINTAINERS.md`. Maintainer affiliation does not grant an implementation special status. Governance inquiries may be sent to [protocol@compaos.ai](mailto:protocol@compaos.ai).

## Decision process

Routine corrections may be merged after maintainer review. Any change that alters canonical objects, wire format, lifecycle semantics, security properties, compatibility, or conformance requires an RFC.

RFCs progress through Draft, Review, Accepted or Rejected, and Implemented. Acceptance requires:

1. a public review period of at least 14 calendar days;
2. evidence that at least two independent implementations can implement the proposal, or a documented reason for a temporary exception before 1.0;
3. corresponding schema and conformance changes where applicable; and
4. maintainer consensus. If consensus is impossible, a two-thirds majority of non-recused maintainers decides.

Material conflicts of interest must be disclosed. A maintainer must recuse from a decision that uniquely advantages an implementation or commercial service with which that maintainer is affiliated.

## Neutrality requirements

Normative material must not require a named product, vendor, hosted service, model provider, programming language, transport, or deployment topology unless the dependency is itself part of the accepted Protocol. Examples use reserved or clearly fictional identifiers. Product marketing and private business strategy do not belong in this repository.

Reference implementations are explanatory and testable artifacts. They do not override normative specifications, schemas, registries, or accepted RFCs.

## Releases

Maintainers publish signed version tags, release notes, schema manifests, and conformance-suite revisions. A release candidate must pass all repository checks and a language-neutrality scan. See `VERSIONING.md`.

## Amendments

Changing this governance policy requires an RFC and the same review period as a normative Protocol change.
