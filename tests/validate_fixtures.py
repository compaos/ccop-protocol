#!/usr/bin/env python3
from pathlib import Path
import json, sys
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
ROOT=Path(__file__).resolve().parents[1]
BASE='https://ccop.dev/schemas/v0.5.3/'
SCHEMAS=ROOT/'schemas'/'v0'
FIXTURES=ROOT/'conformance'/'fixtures'
store={}
for p in list(SCHEMAS.glob('*.json'))+list((SCHEMAS/'shared').glob('*.json')):
    s=json.loads(p.read_text());
    if '$id' in s: store[s['$id']]=s
registry=Registry().with_resources(
    (schema_id, Resource.from_contents(schema)) for schema_id, schema in store.items()
)

def validate(schema_name, obj):
    sch=json.loads((SCHEMAS/schema_name).read_text())
    v=Draft202012Validator(sch, registry=registry)
    return list(v.iter_errors(obj))

cases=[('task.schema.json','fixtures/valid/task.valid.json',True),('principal.schema.json','fixtures/valid/principal.valid.json',True),('governance-writer-registry.schema.json','fixtures/valid/governance-writer-registry.valid.json',True),('task.schema.json','fixtures/invalid/task.unknown-recovery.json',False),('principal.schema.json','fixtures/invalid/principal.self-asserted-control.json',True)]
# note self-asserted control is semantic-invalid, structurally valid; self-linter/conformance handles it.
failed=0
for schema,path,should in cases:
    obj=json.loads((FIXTURES/Path(path).relative_to('fixtures')).read_text()); errs=validate(schema,obj); ok=not errs
    if ok!=should:
        failed+=1; print('FAIL',path,'expected',should,'errors',[e.message for e in errs[:3]])
    else: print('PASS',path,'schema_valid=',ok)
if failed: sys.exit(1)
