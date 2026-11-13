#!/usr/bin/env python3
"""Rough offline preview of a FancyMenu layout file (v3 format).

    fmrender.py <pack root> <layout.txt> <out.jpg> [gui scale]

The pack root is the folder that holds `config/fancymenu`. It draws the
background, images, buttons, texts and shapes where the layout puts them, on a
1920x1080 window. It does not know vanilla widgets the layout never touched,
animations, placeholders or requirements: every element is drawn as if visible.
"""
import os, re, sys, glob
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
NONE = '-2147483648'


def blocks(text):
    out, name, cur = [], None, None
    for line in text.splitlines():
        s = line.strip()
        if cur is None:
            m = re.match(r'^([\w\-]+)\s*\{$', s)
            if m:
                name, cur = m.group(1), {}
            continue
        if s == '}':
            out.append((name, cur)); cur = None; continue
        if ' = ' in s:
            k, v = s.split(' = ', 1); cur[k] = v
    return out


def font(px):
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',):
        if os.path.exists(p):
            return ImageFont.truetype(p, max(8, int(px)))
    return ImageFont.load_default()


def resolve(root, src):
    if not src:
        return None
    src = re.sub(r'^\[source:\w+\]', '', src).strip()
    if src.startswith('http') or ':' in src.split('/')[0]:
        return None
    src = src.lstrip('/')
    for base in (root, os.path.join(root, 'overrides')):
        p = os.path.join(base, src)
        if os.path.isfile(p):
            return p
        # case-insensitive fallback
        d, f = os.path.split(p)
        if os.path.isdir(d):
            for g in os.listdir(d):
                if g.lower() == f.lower():
                    return os.path.join(d, g)
    return None


def load(path):
    try:
        im = Image.open(path); im.seek(0)
        return im.convert('RGBA')
    except Exception:
        return None


def cover(im, w, h):
    r = max(w / im.width, h / im.height)
    im = im.resize((max(1, round(im.width * r)), max(1, round(im.height * r))), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def color(c, default=(255, 255, 255, 255)):
    m = re.match(r'^#?([0-9a-fA-F]{6})([0-9a-fA-F]{2})?$', (c or '').strip())
    if not m:
        return default
    v = m.group(1); a = m.group(2)
    return (int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16), int(a, 16) if a else 255)


def clean(t):
    t = re.sub(r'\{"placeholder":"(\w+)".*?\}\}+', r'<\1>', t or '')
    t = re.sub(r'%#[0-9A-Fa-f]{6,8}%|%#%|[*_`]|\[([^\]]*)\]\([^)]*\)', lambda m: m.group(1) or '', t)
    t = re.sub(r'[§&][0-9a-fk-or]', '', t)
    return t.replace('%n%', '\n').replace('\\n', '\n')


def main(root, layout, out, force_scale=None):
    text = open(layout, encoding='utf-8', errors='replace').read()
    bl = blocks(text)
    meta = next((b for n, b in bl if n == 'layout-meta'), {})
    scale, base = None, None
    for n, b in bl:
        if n == 'customization' and b.get('action') == 'setscale':
            scale = float(b.get('scale', 2))
        if n == 'customization' and b.get('action') == 'autoscale':
            base = (float(b.get('basewidth', W)), float(b.get('baseheight', H)))
    guessed = False
    if scale is None:
        scale, guessed = 2.0, True
        for n, b in bl:
            if n == 'vanilla_button' and b.get('anchor_point') == 'vanilla' and 'singleplayer' in b.get('instance_identifier', ''):
                gw = 2 * (float(b['x']) + 100)
                if gw > 100:
                    scale = round(W / gw * 2) / 2
    if base:
        scale = scale * min(W / base[0], H / base[1])
    if force_scale:
        scale = float(force_scale)
    gw, gh = W / scale, H / scale
    canvas = Image.new('RGBA', (W, H), (38, 36, 44, 255))
    notes = []

    # background
    bgs = [b for n, b in bl if n == 'menu_background' and b.get('show_background', 'true') != 'false']
    keep = any(b.get('keepaspectratio') == 'true' for n, b in bl if n == 'customization' and b.get('action') == 'backgroundoptions')
    bg_note = 'no custom background (vanilla panorama or blur)'
    for b in bgs:
        t = b.get('background_type', '')
        im = None
        if t == 'image':
            p = resolve(root, b.get('image_path'))
            im = load(p) if p else None
        elif t == 'slideshow':
            for base_dir in (root, os.path.join(root, 'overrides')):
                g = sorted(glob.glob(os.path.join(base_dir, 'config/fancymenu/slideshows', b.get('slideshow_name', ''), 'images', '*')))
                if g:
                    im = load(g[0]); break
        elif t == 'panorama':
            for base_dir in (root, os.path.join(root, 'overrides')):
                g = glob.glob(os.path.join(base_dir, 'config/fancymenu/panoramas', b.get('panorama_name', ''), 'panorama', 'panorama_0.png'))
                if g:
                    im = load(g[0]); break
        elif 'color' in t:
            canvas.paste(color(b.get('color'), (0, 0, 0, 255)), (0, 0, W, H)); bg_note = f'{t} {b.get("color")}'
            continue
        if im is not None:
            canvas.paste(cover(im, W, H) if keep or t != 'image' else im.resize((W, H), Image.LANCZOS), (0, 0))
            bg_note = f'{t}: {b.get("image_path") or b.get("slideshow_name") or b.get("panorama_name")}'
            break
        elif t:
            bg_note = f'{t} (not drawn)'
    notes.append('background ' + bg_note)

    els = [(n, b) for n, b in bl if n in ('element', 'vanilla_button')]
    byid = {b.get('instance_identifier'): b for n, b in els}
    pos = {}

    def place(b, depth=0):
        i = b.get('instance_identifier')
        if i in pos:
            return pos[i]
        try:
            x, y = float(b.get('x', 0)), float(b.get('y', 0))
            w, h = float(b.get('width', 0)), float(b.get('height', 0))
        except ValueError:
            return None
        a = b.get('anchor_point', 'top-left')
        ox = oy = 0
        if a == 'element':
            other = byid.get(b.get('anchor_point_element'))
            o = place(other, depth + 1) if other is not None and depth < 8 else None
            if o is None:
                return None
            ox, oy = o[0], o[1]
        elif a != 'vanilla':
            if 'right' in a: ox = gw
            elif 'centered' in a: ox = gw / 2
            if a.startswith('bottom'): oy = gh
            elif a.startswith('mid'): oy = gh / 2
        if b.get('advanced_posx', NONE) != NONE or b.get('advanced_posy', NONE) != NONE:
            return None
        x, y = ox + x, oy + y
        if b.get('stretch_x') == 'true': x, w = 0, gw
        if b.get('stretch_y') == 'true': y, h = 0, gh
        pos[i] = (x, y, w, h)
        return pos[i]

    d = ImageDraw.Draw(canvas, 'RGBA')
    behind = meta.get('render_custom_elements_behind_vanilla') == 'true'
    order = [e for e in els if e[0] == ('element' if behind else 'vanilla_button')] + [e for e in els if e[0] == ('vanilla_button' if behind else 'element')]
    skipped = 0
    for n, b in order:
        t = b.get('element_type', n)
        if b.get('is_hidden') == 'true':
            continue
        if n == 'vanilla_button' and b.get('anchor_point') == 'vanilla' and force_scale is None and guessed and False:
            continue
        p = place(b)
        if p is None or p[2] <= 0 or p[3] <= 0:
            skipped += 1; continue
        x, y, w, h = [round(v * scale) for v in p]
        if w > W * 3 or h > H * 3:
            skipped += 1; continue
        op = float(b.get('base_opacity', 1) or 1)
        if t == 'image' or t == 'slideshow':
            src = resolve(root, b.get('source'))
            im = load(src) if src else None
            if im is None:
                d.rectangle((x, y, x + w, y + h), outline=(255, 200, 0, 255)); d.text((x + 3, y + 3), t, font=font(18), fill=(255, 200, 0, 255))
            else:
                im = im.resize((max(1, w), max(1, h)), Image.NEAREST if im.width < w / 2 else Image.LANCZOS)
                if op < 1:
                    im.putalpha(im.getchannel('A').point(lambda v: int(v * op)))
                canvas.alpha_composite(im, (max(-im.width, x), max(-im.height, y))) if x >= 0 and y >= 0 else canvas.paste(im, (x, y), im)
        elif t in ('custom_button', 'vanilla_button'):
            src = resolve(root, b.get('backgroundnormal'))
            im = load(src) if src else None
            if im is not None:
                im = im.resize((max(1, w), max(1, h)), Image.NEAREST if im.width < w / 2 else Image.LANCZOS)
                canvas.paste(im, (x, y), im)
            elif b.get('transparent_background') != 'true':
                d.rectangle((x, y, x + w, y + h), fill=(90, 90, 96, 235), outline=(0, 0, 0, 255), width=max(1, round(scale)))
            label = clean(b.get('label', ''))
            if not label and t == 'vanilla_button' and im is None:
                label = b.get('instance_identifier', '').replace('mc_titlescreen_', '').replace('_button', '').replace('pause_', '')[:22]
            if label:
                f = font(8 * scale * float(b.get('label_scale', 1) or 1))
                tw = d.textlength(label, font=f)
                d.text((x + (w - tw) / 2, y + (h - f.size) / 2 - 1), label, font=f, fill=(255, 255, 255, 255))
        elif t in ('text_v2', 'fancymenu_customization_item_text', 'splash_text'):
            s = clean(b.get('source') or b.get('value') or b.get('splash_text') or ('Splash!' if t == 'splash_text' else ''))[:400]
            f = font(8 * scale * float(b.get('scale', 1) or 1))
            col = (255, 235, 60, 255) if t == 'splash_text' else color(b.get('base_color'))
            yy = y
            for line in s.split('\n')[:14]:
                d.text((x + 2, yy + 2), line[:120], font=f, fill=col); yy += f.size + 3
        elif t == 'shape':
            c = color(b.get('color'), (0, 0, 0, 160))
            ov = Image.new('RGBA', (max(1, w), max(1, h)), c)
            canvas.alpha_composite(ov, (max(0, x), max(0, y)))
            d = ImageDraw.Draw(canvas, 'RGBA')
        elif t in ('progress_bar', 'drippy_vanilla_bar'):
            d.rectangle((x, y, x + w, y + h), fill=color(b.get('background_color'), (40, 40, 40, 255)))
            d.rectangle((x, y, x + int(w * 0.6), y + h), fill=color(b.get('bar_color'), (230, 230, 230, 255)))
        elif t in ('audio_v2', 'animation_controller', 'cursor', 'tooltip', 'ticker', 'music_controller', 'drippy_custom_bar'):
            notes.append('has ' + t)
        else:
            d.rectangle((x, y, x + w, y + h), outline=(0, 220, 255, 255), width=2)
            d.text((x + 4, y + 4), t, font=font(18), fill=(0, 220, 255, 255))
    notes.append(f'gui scale {scale:.2f}' + (' (guessed)' if guessed and not base and not force_scale else '') + f', gui {gw:.0f}x{gh:.0f}, not placed {skipped}')
    canvas = canvas.convert('RGB')
    d = ImageDraw.Draw(canvas)
    label = f"{os.path.basename(root)} | {os.path.basename(layout)} | {meta.get('identifier')} | " + '; '.join(dict.fromkeys(notes))
    d.rectangle((0, H - 34, W, H), fill=(0, 0, 0))
    d.text((8, H - 30), label[:230], font=font(20), fill=(255, 255, 255))
    canvas.resize((1280, 720), Image.LANCZOS).save(out, quality=88)
    print(out, '|', label)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)
