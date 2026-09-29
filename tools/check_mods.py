#!/usr/bin/env python3
"""Check which Modrinth slugs have a NeoForge 1.21.1 version. Writes a report."""
import json, sys, time, urllib.request, urllib.parse, concurrent.futures as cf

API = "https://api.modrinth.com/v2"
UA = "kronwerke-pack-tools/0.1 (pack tooling)"
MC = "1.21.1"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for i in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return 404, None
            if e.code == 429:
                time.sleep(2 + i * 2); continue
            return e.code, None
        except Exception:
            time.sleep(1)
    return 0, None

def check(slug):
    q = urllib.parse.quote
    st, proj = get(f"{API}/project/{q(slug)}")
    if st != 200:
        return slug, {"status": "missing", "http": st}
    st, vers = get(f"{API}/project/{q(slug)}/version?loaders={q(json.dumps(['neoforge']))}&game_versions={q(json.dumps([MC]))}")
    if st != 200 or not vers:
        # find what it does support
        loaders = proj.get("loaders", []); gv = proj.get("game_versions", [])
        return slug, {"status": "no-neoforge-1.21.1", "title": proj["title"], "loaders": loaders, "latest_gv": gv[-3:], "side": (proj.get("client_side"), proj.get("server_side"))}
    v = vers[0]
    return slug, {"status": "ok", "title": proj["title"], "version": v["version_number"], "type": v["version_type"], "date": v["date_published"][:10], "side": (proj.get("client_side"), proj.get("server_side")), "downloads": proj.get("downloads")}

def main():
    slugs = []
    for line in open(sys.argv[1]):
        line = line.split("#", 1)[0].strip()
        if line:
            slugs.append(line.split()[0])
    slugs = list(dict.fromkeys(slugs))
    res = {}
    with cf.ThreadPoolExecutor(6) as ex:
        for slug, r in ex.map(check, slugs):
            res[slug] = r
    json.dump(res, open(sys.argv[2], "w"), indent=1)
    ok = [s for s in slugs if res[s]["status"] == "ok"]
    bad = [s for s in slugs if res[s]["status"] != "ok"]
    print(f"OK: {len(ok)}   NOT OK: {len(bad)}\n")
    for s in bad:
        r = res[s]
        print(f"  {s:35} {r['status']:22} {r.get('title','')}  loaders={r.get('loaders')} gv={r.get('latest_gv')}")

if __name__ == "__main__":
    main()
