#!/usr/bin/env python3
"""Search Modrinth for a name and print top hits that support neoforge + 1.21.1."""
import json, sys, urllib.request, urllib.parse
UA = "kronwerke-pack-tools/0.1"
def search(q):
    facets = json.dumps([["categories:neoforge"], ["versions:1.21.1"], ["project_type:mod"]])
    url = f"https://api.modrinth.com/v2/search?query={urllib.parse.quote(q)}&facets={urllib.parse.quote(facets)}&limit=5"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["hits"]
for q in sys.argv[1:]:
    hits = search(q)
    print(f"== {q}")
    for h in hits:
        print(f"   {h['slug']:35} {h['title'][:40]:40} dl={h['downloads']:>9}  by {h['author']}")
