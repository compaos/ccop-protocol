# Versioning and Compatibility

## Version model

Protocol releases use Semantic Versioning.

- Before 1.0, a minor release may change the conformance surface; patch releases remain backward compatible within that minor line.
- At and after 1.0, a major release is required for an incompatible normative or wire-format change.
- Schema directories use a stable major-line path such as `schemas/v0/`; the exact Protocol version remains encoded in schema identifiers and document envelopes.

## Compatibility rules

An implementation must reject an unsupported major line and any unsupported critical extension. Unknown non-critical extension data may be preserved or ignored only where the applicable schema permits it. A consumer must not silently reinterpret an object from another Protocol version.

Published schema identifiers are immutable. Corrections that change validation behavior require a new Protocol version and new schema identifier. Registries that affect semantics are versioned with the Protocol release.

## Conformance claims

A public claim must state:

- Protocol version;
- conformance profile and test-suite revision;
- implementation name and version;
- execution date and complete pass/fail result; and
- any explicitly permitted exclusions.

Passing one reference core's tests is not, by itself, a conformance claim. The language-neutral conformance suite is authoritative for testing; normative specifications and accepted RFCs are authoritative when artifacts conflict.

## Deprecation

Deprecations are announced in release notes. Before 1.0, maintainers should provide at least one minor release of notice where safety allows. At and after 1.0, a deprecated feature remains supported until the next major release unless retaining it creates a documented security risk.
