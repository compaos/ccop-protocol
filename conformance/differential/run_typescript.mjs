import fs from "node:fs";import path from "node:path";import {fileURLToPath} from "node:url";import * as c from "../../reference/typescript/dist/index.js";
const here=path.dirname(fileURLToPath(import.meta.url)), root=path.resolve(here,"../..");
const vec=JSON.parse(fs.readFileSync(path.join(root,"conformance/fixtures/differential/core-vectors.json"),"utf8"));
const f={canonical_timestamp:c.canonicalTimestamp,glob:c.ccopGlob,eval_op:c.evalOp,money_add:c.moneyAdd,fx_settle:c.fxSettle};
let out=[];for(const v of vec){try{out.push({id:v.id,result:f[v.op](...v.args)})}catch(e){out.push({id:v.id,error:e.message})}}
const effect=JSON.parse(fs.readFileSync(path.join(root,"conformance/fixtures/differential/effect.self-contained.json"),"utf8"));const event=JSON.parse(fs.readFileSync(path.join(root,"conformance/fixtures/differential/event.self-contained.json"),"utf8"));
out.push({id:"effect-hash",result:c.effectHash(effect)},{id:"event-hash",result:c.eventHash(event)});console.log(JSON.stringify(out));
