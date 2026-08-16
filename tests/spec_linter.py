#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
SCHEMAS=ROOT/'schemas'/'v0'
REGISTRIES=SCHEMAS/'registries'
errors=[]

def load(p): return json.loads(p.read_text())
# L1: required schema inventory
required=['task','run','result','principal','execution-engine','tool','tool-request','effect','operation','authority-policy','authority-grant','authority-decision','capability-lease','approval','evidence','verification-spec','verification-run','verification-result','event','governance-writer-registry','resource-type-profile']
for n in required:
    if not (SCHEMAS/f'{n}.schema.json').exists(): errors.append(f'L1 missing schema: {n}')
for n in ['object-ref','principal-ref','tool-ref','resource-ref','money','timestamp','decimal','cost','fx-conversion','semantic-hash','json-pointer']:
    if not (SCHEMAS/'shared'/f'{n}.schema.json').exists(): errors.append(f'L1 missing shared schema: {n}')
# L2 task selector targets must be legal transitions
trans={tuple(x) for x in load(REGISTRIES/'task-transitions.json')}
selectors=load(REGISTRIES/'recovery-selectors.json')
source_map={'on_child_failure':['ACTIVE'],'on_authority_denied':['ACTIVE','WAITING_AUTHORITY'],'on_run_failure':['ACTIVE'],'on_run_timeout':['ACTIVE'],'on_run_cancelled':['ACTIVE'],'on_verification_failed':['VERIFYING'],'on_unable_to_verify':['VERIFYING'],'on_budget_exceeded':['ACTIVE'],'on_deadline_exceeded':['ACTIVE']}
for sel,targets in selectors.items():
    for src in source_map[sel]:
        for tgt in targets:
            if src==tgt: continue
            if (src,tgt) not in trans: errors.append(f'L2 missing transition for {sel}: {src}->{tgt}')
# L4 arrays used by protocol registry must be declared
arr=load(REGISTRIES/'array-semantics.json')
for key in ['semantics.domains','ccop.critical_extensions','related_refs','controlled_by','policy.match','policy.rules']:
    if key not in arr: errors.append(f'L4 missing array semantic: {key}')
# L5 event types relied upon by protocol
et=set(load(REGISTRIES/'event-types.json'))
for e in ['lease.issued','lease.consumed','execution.completed','principal.control_changed','governance.writer_registry_changed']:
    if e not in et: errors.append(f'L5 missing event type: {e}')
# Validate JSON schemas syntax using jsonschema
try:
    from jsonschema.validators import validator_for
    for p in list(SCHEMAS.glob('*.json'))+list((SCHEMAS/'shared').glob('*.json')):
        sch=load(p); validator_for(sch).check_schema(sch)
except Exception as e: errors.append('schema syntax: '+str(e))
if errors:
    print('CCOP self-lint FAILED')
    for e in errors: print(' -',e)
    sys.exit(1)
print('CCOP self-lint PASS')
