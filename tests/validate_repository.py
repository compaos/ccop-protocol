#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {
    "",
    ".d.ts",
    ".js",
    ".json",
    ".md",
    ".mjs",
    ".py",
    ".toml",
    ".ts",
    ".txt",
    ".yml",
    ".yaml",
}


def repository_files():
    output = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        text=True,
    )
    return [ROOT / line for line in output.splitlines() if line]


errors = []
private_business_name = "pay" + "tend"
for path in repository_files():
    relative = path.relative_to(ROOT).as_posix()
    try:
        relative.encode("ascii")
    except UnicodeEncodeError:
        errors.append(f"non-ASCII public path: {relative}")
    suffix = ".d.ts" if relative.endswith(".d.ts") else path.suffix
    if suffix not in TEXT_SUFFIXES:
        continue
    try:
        content = path.read_text()
    except UnicodeDecodeError:
        continue
    for number, line in enumerate(content.splitlines(), 1):
        if any("\u4e00" <= char <= "\u9fff" for char in line):
            errors.append(f"non-English public content: {relative}:{number}")
        if private_business_name in line.lower():
            errors.append(f"private business reference: {relative}:{number}")

if errors:
    print("REPOSITORY POLICY FAILED")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)

print("REPOSITORY POLICY PASS: English-only public content and paths")
