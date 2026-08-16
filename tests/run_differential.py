#!/usr/bin/env python3
import shutil,subprocess,json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
local_tsc=R/'reference/typescript/node_modules/.bin/tsc'
tsc=shutil.which('tsc') or (str(local_tsc) if local_tsc.exists() else None)
if tsc:
 subprocess.run([tsc,'-p',str(R/'reference/typescript/tsconfig.json')],check=True,cwd=R)
elif not (R/'reference/typescript/dist/index.js').exists():
 raise SystemExit('TypeScript compiler unavailable and no prebuilt reference core found')
p=json.loads(subprocess.check_output([sys.executable,str(R/'conformance/differential/run_python.py')],text=True,cwd=R))
t=json.loads(subprocess.check_output(['node',str(R/'conformance/differential/run_typescript.mjs')],text=True,cwd=R))
if p!=t:
 print('DIFFERENTIAL FAIL')
 print('PY',json.dumps(p,indent=2));print('TS',json.dumps(t,indent=2));sys.exit(1)
print(f'DIFFERENTIAL PASS: {len(p)} vectors')
for x in p: print(' ',x['id'],x.get('result',x.get('error')))
