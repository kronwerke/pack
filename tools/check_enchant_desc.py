"""Every enchantment of the pack needs a description for Enchantment Descriptions, in English and German.

usage: check_enchant_desc.py <mods folder of an installed server or client>
Reads the enchantments from the mod jars and the pack's kubejs data, the texts from the jars and the pack's lang files
(kubejs/assets/kronwerke/lang). Enchantments with a literal description (mob equipment of structure mods) are left out.
"""
import zipfile, json, glob, os, re, sys
mods = sorted(glob.glob(sys.argv[1].rstrip('/') + '/*.jar'))
ench = {}   # id -> (jar, description component)
lang = {'en_us': {}, 'de_de': {}}
def scan(zf, jar, depth=0):
    for n in zf.namelist():
        m = re.match(r'data/([^/]+)/enchantment/(.+)\.json$', n)
        if m:
            try: d = json.loads(zf.read(n).decode('utf-8', 'replace'))
            except Exception: d = {}
            ench[m.group(1) + ':' + m.group(2)] = (os.path.basename(jar), d.get('description'))
        m = re.match(r'assets/[^/]+/lang/(en_us|de_de)\.json$', n)
        if m:
            try:
                d = json.loads(zf.read(n).decode('utf-8', 'replace'), strict=False)
                for k, v in d.items():
                    if k.startswith('enchantment.') and isinstance(v, str): lang[m.group(1)].setdefault(k, v)
            except Exception as e: pass
        if depth == 0 and n.startswith('META-INF/jarjar/') and n.endswith('.jar'):
            import io
            try: scan(zipfile.ZipFile(io.BytesIO(zf.read(n))), jar, 1)
            except Exception: pass
for jar in mods:
    try: scan(zipfile.ZipFile(jar), jar)
    except Exception as e: print('ERR', jar, e, file=sys.stderr)
# pack's own
pk = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kubejs')
for f in glob.glob(pk + '/data/*/enchantment/*.json'):
    ns = f.split('/data/')[1].split('/')[0]
    ench[ns + ':' + os.path.basename(f)[:-5]] = ('pack', json.load(open(f)).get('description'))
packlang = {'en_us': {}, 'de_de': {}}
for f in glob.glob(pk + '/assets/*/lang/*.json'):
    l = os.path.basename(f)[:-5]
    if l in packlang:
        for k, v in json.load(open(f)).items():
            if k.startswith('enchantment.'): packlang[l][k] = v
print(len(ench), 'enchantments', len(mods), 'jars')
from collections import Counter
c = Counter(); miss_en = []; miss_de = []
for e, (jar, desc) in sorted(ench.items()):
    ns, p = e.split(':')
    if isinstance(desc, str): continue
    key = desc.get('translate') if isinstance(desc, dict) and 'translate' in desc else 'enchantment.%s.%s' % (ns, p.replace('/', '.'))
    en = packlang['en_us'].get(key + '.desc') or lang['en_us'].get(key + '.desc')
    de = packlang['de_de'].get(key + '.desc') or lang['de_de'].get(key + '.desc')
    c[ns] += 1
    if not en: miss_en.append((e, key, jar))
    if not de: miss_de.append((e, key, jar))
print(dict(c))
print('missing en', len(miss_en), 'missing de', len(miss_de))
for e, key, jar in miss_en: print('EN', e, key, jar[:40])
for e, key, jar in miss_de: print('DE', e, key, jar[:40])
sys.exit(1 if miss_en or miss_de else 0)
