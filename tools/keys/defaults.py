"""Kronwerke sets no keys of its own (since 15.11.2026): every mod keeps its default.

Instances that ran an earlier pack layout still carry its keys in their options. This writes
the Core resource assets/kronwerke/keys.tsv, which moves every key that still sits where that
layout put it back to the mod's default (a key the player chose is left alone).

    python3 tools/keys/defaults.py keys-dump.tsv old-keybindings.txt ../core/src/main/resources/assets/kronwerke/keys.tsv

keys-dump.tsv: every key mapping of the client (name, category, default key and modifier,
current key and modifier, conflict context), made by Kronwerke Core with
-Dkronwerke.dumpKeys=<file>. old-keybindings.txt: config/defaultoptions/keybindings.txt of the
earlier layout (the last one is in the pack's history at v0.24.45).
"""
import csv
import sys

# bump when this is written again for another earlier layout, so Core applies it once more
VERSION = 2


def main(dump, old, tsv):
    default = {r[0]: (r[2], r[3]) for r in csv.reader(open(dump), delimiter="\t") if r}
    earlier = {}
    for line in open(old):
        line = line.strip()
        if line.startswith("key_") and line.count(":") >= 2:
            name, key, mod = line[4:].rsplit(":", 2)
            earlier[name] = (key, mod or "NONE")
    moved = 0
    with open(tsv, "w") as f:
        f.write("# Kronwerke sets no keys of its own since layout 2 (15.11.2026): every key that still sits where an earlier "
                "pack layout put it goes back to its mod's default. name, the earlier pack key and modifier, the mod "
                "default key and modifier. Written by the pack's tools/keys/defaults.py.\n")
        f.write(f"version\t{VERSION}\n")
        for name in sorted(earlier):
            if name in default and earlier[name] != default[name]:
                f.write("\t".join([name, *earlier[name], *default[name]]) + "\n")
                moved += 1
    print(f"{moved} keys go back to their mod default")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
