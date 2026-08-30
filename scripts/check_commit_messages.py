#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    raw = subprocess.check_output(
        ["git", "-C", str(ROOT), "log", "--reverse", "--format=%H%x1f%B%x1e"],
        text=True,
    )
    errors: list[str] = []
    count = 0

    for record in raw.split("\x1e"):
        record = record.strip()
        if not record:
            continue
        commit_hash, message = record.split("\x1f", 1)
        lines = message.rstrip().splitlines()
        subject = lines[0].strip() if lines else ""
        bullets = [line for line in lines[1:] if line.startswith("- ") and len(line) > 2]
        count += 1

        if not subject:
            errors.append(f"{commit_hash[:12]}: missing subject")
        if len(bullets) < 2:
            errors.append(
                f"{commit_hash[:12]}: expected at least 2 bullet lines in commit body, found {len(bullets)}"
            )

    if errors:
        print("\n".join(f"[FAIL] {error}" for error in errors))
        return 1

    print(f"[PASS] COMMIT_MESSAGE_BULLETS_VALID commits={count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
