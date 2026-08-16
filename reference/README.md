# Reference Cores

The Python and TypeScript reference cores demonstrate deterministic v0.5.3 behavior and support differential testing. They are non-normative and have no privileged status over independent implementations. The TypeScript directory includes prebuilt JavaScript so the differential suite can run without installing a compiler; maintainers must rebuild it whenever `src/` changes.

Protocol behavior is determined by released specifications, schemas, registries, accepted RFCs, and the language-neutral conformance corpus. A discrepancy in a reference core is an implementation defect unless a release process determines that the normative artifacts themselves require a new version.

The cores remain in this repository while the Protocol is pre-1.0. Separate language SDK repositories should be created only when stable external demand and independent release needs justify them.
