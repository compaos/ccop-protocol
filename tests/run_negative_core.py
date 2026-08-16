#!/usr/bin/env python3
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'reference/python'))
from ccop_ref.core import *
inv=sorted((R/'conformance/negative').glob('N*.json'))
assert len(inv)==65, f'expected 65 negative fixtures, got {len(inv)}'
reg=json.loads((R/'conformance/fixtures/security/writer-registry.json').read_text())
engine={'issuer':'urn:example:company:acme','type':'execution_engine','id':'engine_1'}
orch={'issuer':'urn:example:company:acme','type':'service_account','id':'orchestrator'}
lease={'issuer':'urn:example:company:acme','id':'lease_1','revision':1}; approval={'issuer':'urn:example:company:acme','id':'approval_1','revision':1}; op={'issuer':'urn:example:company:acme','id':'operation_1','revision':1}
events=[{'event_type':'lease.issued','subject_ref':lease,'related_refs':[approval]},{'event_type':'lease.consumed','subject_ref':lease,'related_refs':[op]}]
checks=[]
def ck(name,cond): checks.append((name,bool(cond)))
ck('N38/N43 engine writer rejected',not writer_allowed(reg,engine,'execution.completed'))
ck('authorized writer accepted',writer_allowed(reg,orch,'execution.completed'))
ck('N42 lease counter',lease_consumed(events,lease)==1 and approval_leases(events,approval)==1)
p=json.loads((R/'conformance/fixtures/security/principal-self-control.json').read_text());ck('N56 self-control untrusted',not control_assertion_trusted(engine,p))
try: validate_decimal('-0.00',2); ck('N61 negative zero',False)
except CCOPError: ck('N61 negative zero',True)
for ts in ['2016-12-31T23:59:60Z','2026-01-01T00:00:00-00:00']:
 try: canonical_timestamp(ts);ck('timestamp reject '+ts,False)
 except CCOPError:ck('timestamp reject '+ts,True)
ck('N54 decimal',eval_op('0.9963','decimal_gte','0.99'))
fail=[n for n,v in checks if not v]
print(f'NEGATIVE INVENTORY: {len(inv)}/65 present')
for n,v in checks: print(('PASS ' if v else 'FAIL ')+n)
if fail: sys.exit(1)
