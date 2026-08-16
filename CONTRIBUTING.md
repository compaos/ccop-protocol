# Contributing

Contributions from independent implementers, researchers, users, and vendors are welcome.

## Before opening a change

- Use an issue for defects and focused clarifications.
- Use an RFC for canonical objects, wire formats, lifecycle rules, security semantics, compatibility policy, or conformance requirements.
- Keep public content in English.
- Do not submit customer data, credentials, private configuration, product-only behavior, commercial strategy, or proprietary business documents.

## Pull requests

A change should be small enough to review and should include the tests or fixtures that prove its behavior. Normative requirements use `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` in the sense of RFC 2119 and RFC 8174.

Run:

```bash
python tests/spec_linter.py
python tests/validate_fixtures.py
python tests/validate_vectors.py
python tests/run_negative_core.py
python tests/run_differential.py
```

Explain compatibility impact, security impact, conformance impact, and any behavior not tested. By submitting a contribution, you agree that it is licensed under Apache License 2.0.
