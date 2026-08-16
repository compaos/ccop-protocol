import json,sys,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'reference/python'))
from ccop_ref.core import *
def call(op,args):
    return {'canonical_timestamp':canonical_timestamp,'glob':ccop_glob,'eval_op':eval_op,'money_add':money_add,'fx_settle':fx_settle}[op](*args)
vec=json.loads((ROOT/'conformance/fixtures/differential/core-vectors.json').read_text())
out=[]
for v in vec:
    try:r=call(v['op'],v['args']);out.append({'id':v['id'],'result':r})
    except Exception as e:out.append({'id':v['id'],'error':str(e)})
effect=json.loads((ROOT/'conformance/fixtures/differential/effect.self-contained.json').read_text()); event=json.loads((ROOT/'conformance/fixtures/differential/event.self-contained.json').read_text())
out += [{'id':'effect-hash','result':effect_hash(effect)},{'id':'event-hash','result':event_hash(event)}]
print(json.dumps(out,sort_keys=True,separators=(',',':')))
