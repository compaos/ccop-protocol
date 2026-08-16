# Compaos Protocol

Compaos Protocol is an open, implementation-neutral standard for describing governed organizational work. It defines interoperable objects, lifecycle rules, authority boundaries, verification semantics, canonicalization rules, and conformance tests without requiring a particular product, deployment model, programming language, AI provider, or commercial service.

This repository is the home of the standard. Compaos OS and every other compatible system are implementations of the Protocol; no implementation is the Protocol itself.

## Current release

The current engineering baseline is **v0.5.3**. It includes:

- JSON Schema Draft 2020-12 definitions for the locked canonical core
- normative lifecycle and array-semantics registries
- valid, invalid, hashing, canonicalization, and differential fixtures
- a complete N1–N65 negative-conformance inventory
- zero-dependency Python and TypeScript reference cores
- executable schema, security, and cross-language checks

The v0.5.3 baseline is pre-1.0. Some concepts described in `specs/` do not yet have a canonical serialization. Each specification states its conformance status explicitly.

## Semantic model

```text
Company -> Goal -> Task -> Run -> Effect -> Authority -> Operation -> Verification
                         |                              |
                         +-> Decision / Evidence <------+
```

`Task` is the sole canonical object for a bounded, accountable unit of work. `Work` is ordinary domain language, not a parallel Protocol object. A `Run` is one governed execution instance of a Task. A future `Signal` may describe an observation upstream of governed work, but Signal is not part of the v0.5.3 canonical object set.

## Repository map

- `specs/` — semantic specifications and terminology
- `schemas/v0/` — the v0 schema line and normative registries
- `examples/` — non-normative example documents
- `rfcs/` — proposed changes to the standard
- `conformance/` — test vectors, fixtures, and conformance inventory
- `reference/` — reference cores, not privileged implementations
- `tests/` — repository verification entry points

## Verify the baseline

Python 3.11+ is required for the reference and conformance checks. Node.js 16.20+ is required only for building and checking the TypeScript reference core.

Install the development dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
npm ci --prefix reference/typescript
```

Then run:

```bash
python tests/spec_linter.py
python tests/validate_fixtures.py
python tests/validate_vectors.py
python tests/run_negative_core.py
python tests/run_differential.py
```

The TypeScript package is intentionally marked `private`: it is a bundled non-normative reference core, not a published npm SDK. A public npm package should be introduced only through an explicit release decision after the Protocol API stabilizes.

## Compatibility

Implementations conform to a named Protocol version and conformance profile, never to an unspecified "latest" version. A conformance claim must identify the tested version, profile, test-suite revision, implementation version, and result. See [VERSIONING.md](VERSIONING.md) and [conformance/README.md](conformance/README.md).

## Independence and neutrality

Protocol changes are evaluated on interoperability, safety, implementability, and ecosystem impact. Product roadmaps, hosted services, private configuration, customer data, and commercial documents are out of scope. No implementation receives normative privileges.

The intended canonical repository is `github.com/compaos/compaos-protocol`.

## Participation

See [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), and [SECURITY.md](SECURITY.md). The project is licensed under Apache License 2.0.
