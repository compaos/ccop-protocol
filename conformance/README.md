# Conformance

The conformance corpus is implementation-neutral. Stable fixture identifiers and expected canonical values are normative for the conformance revision in which they are released; runners and reports are non-normative tooling.

## Contents

- `fixtures/valid` and `fixtures/invalid` cover structural cases.
- `fixtures/canonicalization` and `fixtures/hashing` lock deterministic representations.
- `fixtures/differential` drive cross-language reference checks.
- `fixtures/security` exercise high-risk semantic rules.
- `negative/N01.json` through `negative/N65.json` are the stable negative-test inventory.
- `differential/` contains runner adapters for the bundled reference cores.

The inventory is complete, but v0.5.3 does not yet execute every semantic negative case end to end. Conformance claims must state the exact profile and suite revision and must not imply coverage that was not run.
