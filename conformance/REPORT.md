# v0.5.3 Reference Core Conformance Report

**Artifact status:** Non-normative report

**Protocol baseline:** v0.5.3

**Generated:** 2026-08-16

## Current result

- Specification self-linter: PASS
- Structural fixture validator: PASS
- Canonicalization and hash-vector validator: PASS
- N1–N65 negative-conformance inventory: COMPLETE (65/65 descriptors)
- Executable high-risk negative-core checks: PASS
- Python/TypeScript differential runner: PASS
- Differential vectors executed: 11

## Scope limitation

The N1–N65 descriptor inventory is complete, but not every negative descriptor is wired to an end-to-end semantic handler. The current executable core covers the highest-risk deterministic and security primitives: timestamp normalization, Effect and Event hashing, glob and operator behavior, exact-decimal Money and FX, event-writer authorization, governance counters, and trusted control assertions.

Remaining descriptors require Authority, state-machine, reconciliation, Verification, and policy-enforcement-point black-box handlers. Their stable N1–N65 identifiers must not change when those handlers are added.

This report does not certify any product or independent implementation.
