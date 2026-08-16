# Repository Checks

Run all checks from the repository root:

```bash
python tests/spec_linter.py
python tests/validate_fixtures.py
python tests/validate_vectors.py
python tests/run_negative_core.py
python tests/run_differential.py
```

Install dependencies from the repository root with:

```bash
python -m pip install -r requirements-dev.txt
npm ci --prefix reference/typescript
```

The differential check uses the locally installed TypeScript compiler when present and otherwise checks the bundled prebuilt reference core.
