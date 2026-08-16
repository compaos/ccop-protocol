# v0 Schema Line

This directory contains the v0.5.3 JSON Schema Draft 2020-12 definitions and normative registries. Schema `$id` values remain under the published `https://ccop.dev/schemas/v0.5.3/` namespace for wire compatibility; renaming the repository does not rewrite released identifiers.

`MANIFEST.json` defines the shipped schema inventory. Files in `shared/` define reusable types. Files in `registries/` define lifecycle, recovery, event-type, and array semantics that implementations must enforce in addition to structural validation.

Published schema identifiers and registry semantics are immutable within a patch line. See `VERSIONING.md`.
