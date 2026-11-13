#!/usr/bin/env python3 -I
"""List the top Modrinth modpacks and pull only their menu config (FancyMenu, Drippy) out of the .mrpack via HTTP range requests."""
import io, json, os, sys, urllib.request, urllib.parse, zipfile, re, time

UA = {'User-Agent': 'kronwerke-pack-research/1.0 (github@elchi.dev)'}

def get(url, headers=None):
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read(), r.headers

class Ranged(io.RawIOBase):
    def __init__(self, url, size):
        self.url, self.size, self.pos, self.cache = url, size, 0, {}
    def seekable(self): return True
    def readable(self): return True
    def tell(self): return self.pos
    def seek(self, off, whence=0):
        self.pos = off if whence == 0 else self.pos + off if whence == 1 else self.size + off
        return self.pos
    def readinto(self, b):
        d = self.read(len(b)); b[:len(d)] = d; return len(d)
    def read(self, n=-1):
        if n < 0: n = self.size - self.pos
        if n == 0 or self.pos >= self.size: return b''
        end = min(self.pos + n, self.size) - 1
        # read in 256k aligned chunks, cached
        C = 1 << 18
        out = b''
        p = self.pos
        while p <= end:
            ci = p // C
            if ci not in self.cache:
                a, b = ci * C, min((ci + 1) * C, self.size) - 1
                data, _ = get(self.url, {'Range': f'bytes={a}-{b}'})
                self.cache[ci] = data
            chunk = self.cache[ci]
            s = p - ci * C
            take = min(len(chunk) - s, end - p + 1)
            out += chunk[s:s + take]
            p += take
        self.pos = p
        return out

def main(outdir, limit, offset=0):
    facets = urllib.parse.quote('[["project_type:modpack"]]')
    data, _ = get(f'https://api.modrinth.com/v2/search?facets={facets}&index=downloads&limit={limit}&offset={offset}')
    hits = json.loads(data)['hits']
    res = []
    for h in hits:
        slug = h['slug']
        try:
            vs, _ = get(f'https://api.modrinth.com/v2/project/{slug}/version')
            vs = json.loads(vs)
            v = vs[0]
            f = next((x for x in v['files'] if x.get('primary')), v['files'][0])
            z = zipfile.ZipFile(io.BufferedReader(Ranged(f['url'], f['size']), 1 << 16))
            names = z.namelist()
            menu = [n for n in names if re.search(r'fancymenu|drippy', n, re.I) and not n.endswith('/')]
            other = sorted({n.split('/')[2] for n in names if re.search(r'^overrides/config/(custommainmenu|isxander-main-menu-credits|bettermodsbutton|mainmenu|panorama|seamless|puzzle|titlescreen)', n, re.I) and n.count('/') >= 2})
            idx = json.loads(z.read('modrinth.index.json'))
            mods = [os.path.basename(x['path']).lower() for x in idx.get('files', [])]
            menumods = sorted({m.split('-')[0].split('_')[0] for m in mods if re.search(r'fancymenu|drippy|custommainmenu|panorama|spiffy|loadingscreen|titlescreen|main.?menu|modmenu|essential|bettertitle|mcef|watermedia', m)})
            layouts = [n for n in menu if '/customization/' in n]
            got = 0
            if menu:
                d = os.path.join(outdir, slug)
                for n in menu:
                    if re.search(r'\.(ogg|mp4|wav|mp3|webm|mov)$', n, re.I): continue
                    if z.getinfo(n).file_size > 12_000_000: continue
                    p = os.path.normpath(os.path.join(d, n))
                    if not p.startswith(d): continue
                    os.makedirs(os.path.dirname(p), exist_ok=True)
                    open(p, 'wb').write(z.read(n)); got += 1
            row = dict(slug=slug, title=h['title'], downloads=h['downloads'], loaders=v.get('loaders'), mc=v.get('game_versions', [])[-1:], size=f['size'], menu_files=len(menu), layouts=len(layouts), saved=got, menumods=menumods, other=other)
        except Exception as e:
            row = dict(slug=slug, title=h['title'], downloads=h['downloads'], error=repr(e)[:160])
        res.append(row)
        print(json.dumps(row), flush=True)
        time.sleep(0.3)
    json.dump(res, open(os.path.join(outdir, f'scan_{offset}.json'), 'w'), indent=1)

main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 0)
