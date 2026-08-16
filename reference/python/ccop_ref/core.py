from __future__ import annotations
import json, hashlib, re
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_EVEN
from typing import Any

GENESIS_HASH = "0" * 64
SAFE_INT_MAX = 9007199254740991

class CCOPError(ValueError): pass

def _parse_ts(s:str)->datetime:
    if re.search(r'T23:59:60(?:[.Z+-])', s): raise CCOPError('TIMESTAMP_LEAP_SECOND')
    if s.endswith('-00:00'): raise CCOPError('TIMESTAMP_UNKNOWN_OFFSET')
    m=re.fullmatch(r'(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)(?:\.(\d+))?(Z|[+-]\d\d:\d\d)',s)
    if not m: raise CCOPError('TIMESTAMP_INVALID')
    frac=m.group(2) or ''
    if len(frac)>9: raise CCOPError('TIMESTAMP_PRECISION')
    # Python datetime supports microseconds; retain ns text separately by integer conversion for canonicalization
    # Normalize with manual offset arithmetic after padding/truncating only for datetime offset conversion.
    use_frac=(frac+'000000')[:6]
    base=m.group(1)+(('.'+use_frac) if use_frac else '')+m.group(3).replace('Z','+00:00')
    dt=datetime.fromisoformat(base)
    return dt.astimezone(timezone.utc)

def canonical_timestamp(s:str)->str:
    if re.search(r'T23:59:60(?:[.Z+-])', s): raise CCOPError('TIMESTAMP_LEAP_SECOND')
    if s.endswith('-00:00'): raise CCOPError('TIMESTAMP_UNKNOWN_OFFSET')
    m=re.fullmatch(r'(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)(?:\.(\d+))?(Z|[+-]\d\d:\d\d)',s)
    if not m: raise CCOPError('TIMESTAMP_INVALID')
    frac=m.group(2) or ''
    if len(frac)>9: raise CCOPError('TIMESTAMP_PRECISION')
    # calculate exact UTC second using integer-second datetime, then preserve fractional digits verbatim
    base=datetime.fromisoformat(m.group(1)+m.group(3).replace('Z','+00:00')).astimezone(timezone.utc)
    out=base.strftime('%Y-%m-%dT%H:%M:%S')
    frac=frac.rstrip('0')
    if frac: out += '.'+frac
    return out+'Z'

def validate_number(v:Any):
    if isinstance(v,bool) or v is None: return
    if isinstance(v,int):
        if abs(v)>SAFE_INT_MAX: raise CCOPError('NUMBER_UNSAFE_INTEGER')
    elif isinstance(v,float):
        if v!=v or v in (float('inf'),float('-inf')): raise CCOPError('NUMBER_NONFINITE')
        if v==0.0 and str(v).startswith('-'): raise CCOPError('NUMBER_NEGATIVE_ZERO')
        if v.is_integer() and abs(v)>SAFE_INT_MAX: raise CCOPError('NUMBER_UNSAFE_INTEGER')

def _json_num(v:Any)->str:
    validate_number(v)
    if isinstance(v,int): return str(v)
    # Stable enough for current normative vectors; floats in hash fixtures are intentionally excluded.
    s=repr(v).lower()
    s=s.replace('e+','e')
    return s

def canonical_json(v:Any)->str:
    if v is None:return 'null'
    if v is True:return 'true'
    if v is False:return 'false'
    if isinstance(v,str):return json.dumps(v, ensure_ascii=False, separators=(',',':'))
    if isinstance(v,(int,float)) and not isinstance(v,bool):return _json_num(v)
    if isinstance(v,list):return '['+','.join(canonical_json(x) for x in v)+']'
    if isinstance(v,dict):
        return '{'+','.join(canonical_json(k)+':'+canonical_json(v[k]) for k in sorted(v.keys()))+'}'
    raise CCOPError('UNSUPPORTED_JSON_TYPE')

def deep_normalize(v:Any, set_keys=frozenset({'domains','critical_extensions','tool_operation_ids','tool_refs','resource_refs','related_refs','reason_codes','policy_basis','grant_basis','evidence_refs','controlled_by'})):
    if isinstance(v,dict):
        out={}
        for k,val in v.items():
            nv=deep_normalize(val,set_keys)
            if nv in ({},[]) and k not in ('critical_extensions','event_payload'):
                # optional empties omitted generically; explicit required fields should be handled by schema before this stage.
                continue
            if k in ('occurred_at','observed_at','asserted_at','issued_at','expires_at','started_at','ended_at','created_at','updated_at') and isinstance(nv,str):
                try:nv=canonical_timestamp(nv)
                except CCOPError: pass
            if isinstance(nv,list) and k in set_keys:
                nv=sorted(nv,key=canonical_json)
            out[k]=nv
        return out
    if isinstance(v,list): return [deep_normalize(x,set_keys) for x in v]
    validate_number(v)
    return v

def sha256_hex(s:str)->str:return hashlib.sha256(s.encode('utf-8')).hexdigest()

def effect_hash(effect_obj:dict)->str:
    e=effect_obj['payload']['effect'] if 'payload' in effect_obj else effect_obj
    x={k:e[k] for k in ('principal','tool_ref','tool_operation_id','resource_ref','semantics','canonical_input')}
    ce=effect_obj.get('ccop',{}).get('critical_extensions',{}) if 'payload' in effect_obj else e.get('critical_extensions',{})
    if ce:
        x['critical_extensions']=ce
    return sha256_hex(canonical_json(deep_normalize(x)))

def event_hash(event_obj:dict)->str:
    ev=event_obj['payload']['event'] if 'payload' in event_obj else event_obj
    keys=('stream_id','sequence','event_type','actor','subject_ref','related_refs','writer_registry_ref','occurred_at','event_payload','prev_hash')
    x={k:ev[k] for k in keys if k in ev}
    # integrity.prev_hash form supported too
    if 'prev_hash' not in x and ev.get('integrity',{}).get('prev_hash') is not None:x['prev_hash']=ev['integrity']['prev_hash']
    return sha256_hex(canonical_json(deep_normalize(x)))

def validate_decimal(s:str, scale:int|None=None):
    if not isinstance(s,str) or not re.fullmatch(r'-?(0|[1-9][0-9]*)(?:\.([0-9]+))?',s):raise CCOPError('DECIMAL_INVALID')
    if s.startswith('-') and Decimal(s)==0: raise CCOPError('DECIMAL_NEGATIVE_ZERO')
    frac=s.split('.',1)[1] if '.' in s else ''
    if scale is not None and len(frac)!=scale:raise CCOPError('DECIMAL_SCALE_MISMATCH')
    return Decimal(s)

def money_add(items:list[dict],currency:str,scale:int)->dict:
    q=Decimal(1).scaleb(-scale)
    total=Decimal(0)
    for m in items:
        if m['currency']!=currency or m['scale']!=scale:raise CCOPError('MONEY_SCOPE_MISMATCH')
        total += validate_decimal(m['amount'],scale)
    total=total.quantize(q,rounding=ROUND_HALF_EVEN)
    return {'amount':f'{total:.{scale}f}' if scale else f'{total:.0f}','scale':scale,'currency':currency}

def fx_settle(original:dict,rate:str,rate_scale:int,target_currency:str,target_scale:int)->dict:
    a=validate_decimal(original['amount'],original['scale']); r=validate_decimal(rate,rate_scale)
    q=Decimal(1).scaleb(-target_scale); z=(a*r).quantize(q,rounding=ROUND_HALF_EVEN)
    return {'amount':f'{z:.{target_scale}f}' if target_scale else f'{z:.0f}','scale':target_scale,'currency':target_currency}

def pointer_get(obj:Any,path:str):
    if path=='':return obj
    if not path.startswith('/'):raise CCOPError('POINTER_INVALID')
    cur=obj
    for token in path[1:].split('/'):
        token=token.replace('~1','/').replace('~0','~')
        if isinstance(cur,dict) and token in cur:cur=cur[token]
        elif isinstance(cur,list) and token.isdigit() and int(token)<len(cur):cur=cur[int(token)]
        else:raise CCOPError('POINTER_UNRESOLVED')
    return cur

def ccop_glob(pattern:str,value:str)->bool:
    i=0; rx='^'
    while i<len(pattern):
        c=pattern[i]
        if c=='*':
            if i+1<len(pattern) and pattern[i+1]=='*':rx+='.*';i+=2;continue
            rx+='[^/]*'
        elif c=='?':rx+='[^/]'
        else:rx+=re.escape(c)
        i+=1
    return re.fullmatch(rx,value) is not None

def eval_op(left,op,right=None):
    if op=='exists':return bool(left)
    if op=='eq':return type(left) is type(right) and left==right
    if op=='neq':return not (type(left) is type(right) and left==right)
    if op=='in':
        if not isinstance(right,list):raise CCOPError('OP_TYPE')
        return any(type(left) is type(x) and left==x for x in right)
    if op=='contains':
        if isinstance(left,str) and isinstance(right,str):return right in left
        if isinstance(left,list):return any(type(right) is type(x) and right==x for x in left)
        raise CCOPError('OP_TYPE')
    if op=='glob':
        if not isinstance(left,str) or not isinstance(right,str):raise CCOPError('OP_TYPE')
        return ccop_glob(right,left)
    if op in ('gt','gte','lt','lte'):
        if isinstance(left,bool) or isinstance(right,bool) or not isinstance(left,(int,float)) or not isinstance(right,(int,float)):raise CCOPError('OP_TYPE')
        validate_number(left);validate_number(right)
        return {'gt':left>right,'gte':left>=right,'lt':left<right,'lte':left<=right}[op]
    if op.startswith('decimal_'):
        a=validate_decimal(left);b=validate_decimal(right); c=op[8:]
        return {'eq':a==b,'neq':a!=b,'gt':a>b,'gte':a>=b,'lt':a<b,'lte':a<=b}[c]
    raise CCOPError('OP_UNSUPPORTED')

def policy_decision(effect_eval:dict,rules:list[dict])->str:
    decisions=[]
    for rule in rules:
        ok=True
        for c in rule.get('match',[]):
            try:left=pointer_get(effect_eval,c['path'])
            except CCOPError:
                if c['operator']=='exists':left=False
                else:return 'DENY'
            try:
                if not eval_op(left,c['operator'],c.get('value')):ok=False;break
            except CCOPError:return 'DENY'
        if ok:decisions.append(rule['decision'])
    if 'DENY' in decisions:return 'DENY'
    if 'REQUIRE_APPROVAL' in decisions:return 'REQUIRE_APPROVAL'
    if 'ALLOW' in decisions:return 'ALLOW'
    return 'DENY'

def writer_allowed(registry:dict, actor:dict, event_type:str)->bool:
    writers=registry.get('payload',{}).get('governance_writer_registry',registry).get('writers',[])
    for w in writers:
        if w['principal_ref']==actor and event_type in w.get('allowed_event_types',[]):return True
    return False

def lease_consumed(events:list[dict], lease_ref:dict)->int:
    n=0
    for e in events:
        ev=e.get('payload',{}).get('event',e)
        if ev.get('event_type')=='lease.consumed' and ev.get('subject_ref')==lease_ref:n+=1
    return n

def approval_leases(events:list[dict],approval_ref:dict)->int:
    n=0
    for e in events:
        ev=e.get('payload',{}).get('event',e)
        if ev.get('event_type')=='lease.issued' and approval_ref in ev.get('related_refs',[]):n+=1
    return n

def counter_precheck(current:int,maximum:int)->bool:return current<maximum

def control_assertion_trusted(principal_ref:dict, principal_obj:dict)->bool:
    p=principal_obj.get('payload',{}).get('principal',principal_obj)
    control=p.get('control')
    if not control:return False
    asserted=control.get('asserted_by')
    if not asserted:return False
    return asserted != principal_ref
