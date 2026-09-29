#!/usr/bin/env python3
"""Builds config/ftbquests from the chapters in tools/quests/chapters/. Run from the pack root."""
import importlib
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import ftbq  # noqa: E402

for f in sorted(os.listdir(os.path.join(here, "chapters"))):
    if f.endswith(".py") and not f.startswith("_"):
        importlib.import_module("chapters." + f[:-3])

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "..", "..", "config", "ftbquests")
chapters, quests, tables = ftbq.write(out)
print(f"{chapters} chapters, {quests} quests, {tables} reward tables -> {os.path.abspath(out)}")
