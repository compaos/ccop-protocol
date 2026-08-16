#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "reference" / "python"))

from ccop_ref.core import canonical_json, deep_normalize, effect_hash, event_hash


def load(path: Path):
    return json.loads(path.read_text())


failures = []
hashing = ROOT / "conformance" / "fixtures" / "hashing"

effect = load(hashing / "effect-hash.vector.json")
effect_canonical = canonical_json(deep_normalize(effect["input"]))
if effect_canonical != effect["canonical_json"]:
    failures.append("effect canonical JSON")
if effect_hash(effect["input"]) != effect["sha256"]:
    failures.append("effect SHA-256")

event = load(hashing / "event-hash.vector.json")
event_canonical = canonical_json(deep_normalize(event["input"]))
if event_canonical != event["canonical_json"]:
    failures.append("event canonical JSON")
if event_hash(event["input"]) != event["sha256"]:
    failures.append("event SHA-256")

ordering = load(
    ROOT / "conformance" / "fixtures" / "canonicalization" / "set-order.vector.json"
)
canonical_a = canonical_json(deep_normalize(ordering["input_a"]))
canonical_b = canonical_json(deep_normalize(ordering["input_b"]))
if canonical_a != ordering["canonical_a"] or canonical_b != ordering["canonical_b"]:
    failures.append("set ordering canonical JSON")
if effect_hash(ordering["input_a"]) != ordering["hash_a"]:
    failures.append("set ordering hash A")
if effect_hash(ordering["input_b"]) != ordering["hash_b"]:
    failures.append("set ordering hash B")
if ordering["same"] is not True or canonical_a != canonical_b:
    failures.append("set ordering equivalence")

if failures:
    print("VECTOR VALIDATION FAILED")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("VECTOR VALIDATION PASS: effect, event, and set-order vectors")
