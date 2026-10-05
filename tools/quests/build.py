#!/usr/bin/env python3
"""Builds config/ftbquests from the chapters in tools/quests/chapters/.
Usage: build.py [quests out dir] [assets out dir]; defaults: config/ftbquests and kubejs/assets."""
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
assets = sys.argv[2] if len(sys.argv) > 2 else os.path.join(here, "..", "..", "kubejs", "assets")
chapters, quests, tables = ftbq.write(out, assets_dir=assets)

# the theme of the book: colours, quest shapes, dependency lines, background
import theme  # noqa: E402
theme.write(assets)

# banners of removed quests would linger, so drop every picture no chapter uses any more
import re  # noqa: E402
used = set()
for root, _, files in os.walk(out):
    for f in files:
        if f.endswith(".snbt"):
            used |= set(re.findall(r"kronwerke:textures/quests/([a-z0-9_/]+\.png)", open(os.path.join(root, f)).read()))
pics = os.path.join(assets, "kronwerke", "textures", "quests")
for root, _, files in os.walk(pics):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), pics).replace(os.sep, "/")
        if f.endswith(".png") and rel not in used:
            os.remove(os.path.join(root, f))
print(f"{chapters} chapters, {quests} quests, {tables} reward tables -> {os.path.abspath(out)}")
