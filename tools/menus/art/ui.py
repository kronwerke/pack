#!/usr/bin/env python3
"""Logo, buttons, icons and bars of the Kronwerke menus, as pixel art on the same grid as the artwork.

    ui.py <outdir>        writes the PNGs (1 texel = 1 GUI pixel at the menu's scale) and ui_sheet.png
"""
import sys, os
import numpy as np
from PIL import Image
from px import Canvas, cols, hexc
from scene import PAL

P = PAL['dusk']
K = P['brass']
DARK = hexc('#15121f')
NIGHT = cols('#3a3046', '#2d2538', '#231d2c', '#1a1522')
RED = cols('#a8404a', '#86303e', '#662536', '#4a1c2c')
CREAM = hexc('#f2ede3')

GLYPH = {
    'K': 'X...X X..X. X.X.. XX... X.X.. X..X. X...X',
    'R': 'XXXX. X...X X...X XXXX. X.X.. X..X. X...X',
    'O': '.XXX. X...X X...X X...X X...X X...X .XXX.',
    'N': 'X...X XX..X XX..X X.X.X X..XX X..XX X...X',
    'W': 'X...X X...X X...X X.X.X X.X.X XX.XX X...X',
    'E': 'XXXXX X.... X.... XXXX. X.... X.... XXXXX',
}
SMALL = {
    'S': '.XX X.. .X. ..X XX.', 'E': 'XXX X.. XX. X.. XXX', 'A': '.X. X.X XXX X.X X.X', 'O': '.X. X.X X.X X.X .X.',
    'N': 'X..X XX.X X.XX X..X X..X', '2': 'XX. ..X .X. X.. XXX', ' ': '... ... ... ... ...', 'T': 'XXX .X. .X. .X. .X.',
    'F': 'XXX X.. XX. X.. X..', 'L': 'X.. X.. X.. X.. XXX', 'I': 'XXX .X. .X. .X. XXX', 'D': 'XX. X.X X.X X.X XX.',
    'G': '.XX X.. X.X X.X .XX', 'R': 'XX. X.X XX. X.X X.X', 'U': 'X.X X.X X.X X.X XXX', 'C': '.XX X.. X.. X.. .XX',
    'H': 'X.X X.X XXX X.X X.X', 'K': 'X.X X.X XX. X.X X.X', 'W': 'X...X X...X X.X.X XX.XX X...X', 'M': 'X...X XX.XX X.X.X X...X X...X',
    'P': 'XX. X.X XX. X.. X..', 'B': 'XX. X.X XX. X.X XX.', 'V': 'X.X X.X X.X X.X .X.', 'Y': 'X.X X.X .X. .X. .X.',
    'Z': 'XXX ..X .X. X.. XXX', '1': '.X. XX. .X. .X. XXX', '3': 'XX. ..X .X. ..X XX.', '.': '... ... ... ... .X.',
    '0': 'XXX X.X X.X X.X XXX', '%': 'X.X ..X .X. X.. X.X', ':': '... .X. ... .X. ...', '-': '... ... XXX ... ...',
}


def glyph_mask(c, ch, x, y, k, table=GLYPH):
    m = c.none()
    for r, row in enumerate(table[ch].split()):
        for q, v in enumerate(row):
            if v == 'X':
                m |= c.rect(x + q * k, y + r * k, x + q * k + k, y + r * k + k)
    return m


def small_text(c, text, x, y, col, shadow=None):
    for ch in text:
        m = glyph_mask(c, ch, x, y, 1, SMALL)
        if shadow is not None:
            c.fill(c.shift(m, 0, 1), shadow)
        c.fill(m, col)
        x += len(SMALL[ch].split()[0]) + 1
    return x


def text_width(text):
    return sum(len(SMALL[ch].split()[0]) + 1 for ch in text) - 1


def crown_mark(c, cx, base, w, h, R=K):
    x0 = cx - w // 2
    pts = [(x0, base - 3), (x0 - 1, base - h + 3), (x0 + w * 0.22, base - h * 0.5), (cx - w * 0.2, base - h + 1),
           (cx - w * 0.08, base - h * 0.5), (cx, base - h - 1), (cx + w * 0.08, base - h * 0.5), (cx + w * 0.2, base - h + 1),
           (x0 + w * 0.78, base - h * 0.5), (x0 + w, base - h + 3), (x0 + w - 1, base - 3)]
    m = c.rect(x0, base - 4, x0 + w, base) | c.poly(pts)
    t = np.clip(0.95 - (c.xx - x0) / float(w) * 0.8 + (c.yy - (base - h)) / float(h) * 0.3, 0, 1)
    c.ramp(m, [R[0], R[1], R[2], R[3]], t, soft=0.3)
    c.fill(c.rect(x0, base - 4, x0 + w, base - 3), R[0])
    c.fill(c.rect(x0, base - 1, x0 + w, base), R[4])
    gems = P['gem']
    for i, gx in enumerate(np.linspace(x0 + 2, x0 + w - 4, 5 if w >= 20 else 3)):
        c.fill(c.rect(gx, base - 3, gx + 2, base - 1), gems[i % len(gems)])
    for px_, py_ in ((x0 - 1, base - h + 2), (cx - w * 0.2, base - h), (cx, base - h - 2), (cx + w * 0.2, base - h), (x0 + w, base - h + 2)):
        b = c.ellipse(px_, py_, 1.5)
        c.fill(b, R[1]); m |= b
    return m


def logo(scale2=True):
    """KRONWERKE in raised brass letters with the crown over the middle W and a SEASON 2 plate."""
    k = 3
    text = 'KRONWERKE'
    lw, gap = 5 * k, 2
    total = len(text) * lw + (len(text) - 1) * gap
    Wc, Hc = total + 12, 62
    c = Canvas(Wc, Hc)
    x0, y0 = 5, 18
    face = c.none()
    for i, ch in enumerate(text):
        face |= glyph_mask(c, ch, x0 + i * (lw + gap), y0, k)
    depth = c.none()
    for d in range(1, 5):
        depth |= c.shift(face, 0, d)
    for d in range(1, 3):
        depth |= c.shift(c.shift(face, 0, 4), d, 0) | c.shift(face, d, d)
    outline = face | depth
    grow = outline.copy()
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        grow |= c.shift(outline, dx, dy)
    c.fill(grow, DARK)
    c.ramp(depth, [K[3], K[4], K[5]], (c.yy - y0 - 12) / 14.0, soft=0.2)
    t = (c.yy - y0) / float(7 * k)
    c.ramp(face, [K[0], K[1], K[2], K[2], K[3]], t * 0.95, soft=0.35)
    c.fill(face & ~c.shift(face, 0, 1), K[0])                # top edge
    c.fill(face & ~c.shift(face, 1, 0) & c.shift(face, 0, 1), K[1])   # left edge
    c.fill(face & ~c.shift(face, 0, -1), K[3])               # bottom edge of the face
    c.fill(face & ~c.shift(face, -1, 0) & c.shift(face, 0, -1), K[3])  # right edge
    # crown over the W
    wx = x0 + 4 * (lw + gap) + lw // 2
    cm = Canvas(Wc, Hc)
    m = crown_mark(cm, wx, y0 - 1, 22, 15)
    ring = m.copy()
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ring |= cm.shift(m, dx, dy)
    c.fill(ring & ~m, DARK)
    c.paste(cm)
    # plate
    label = 'SEASON 2'
    pw = text_width(label) + 16
    px0, py0 = Wc // 2 - pw // 2, y0 + 7 * k + 8
    plate = c.rect(px0, py0, px0 + pw, py0 + 11)
    edge = c.rect(px0 - 1, py0 + 1, px0 + pw + 1, py0 + 10) | plate
    c.fill(edge, DARK)
    c.ramp(c.rect(px0 + 1, py0 + 1, px0 + pw - 1, py0 + 10), [RED[0], RED[1], RED[2]], (c.yy - py0) / 11.0, soft=0.3)
    c.fill(c.rect(px0 + 1, py0 + 1, px0 + pw - 1, py0 + 2), K[2])
    c.fill(c.rect(px0 + 1, py0 + 9, px0 + pw - 1, py0 + 10), K[4])
    for rx in (px0 + 3, px0 + pw - 5):
        c.fill(c.rect(rx, py0 + 4, rx + 2, py0 + 6), K[1]); c.px(rx + 1, py0 + 5, K[4])
    small_text(c, label, px0 + 8, py0 + 3, CREAM, shadow=RED[3])
    return c


def plate(w, h, kind='plain', hover=False, pressed=False):
    """A brass-framed button plate. kind: plain (night inset), main (red inset), flat (disabled)."""
    c = Canvas(w, h)
    R = [K[0], K[0], K[1], K[2], K[3], K[4]] if hover else K
    if kind == 'flat':
        R = [tuple(int(v * 0.55 + 40) for v in col) for col in K]
    body = c.rect(1, 0, w - 1, h) | c.rect(0, 1, w, h - 1)
    c.fill(body, DARK if not hover else K[4])
    f = 3 if h >= 18 else 2
    frame = c.rect(1, 1, w - 1, h - 1)
    c.ramp(frame, [R[1], R[2], R[2], R[3]], (c.yy - 1) / float(h - 2), soft=0.25)
    c.fill(c.rect(1, 1, w - 1, 2), R[0])
    c.fill(c.rect(1, 1, 2, h - 2), R[1])
    c.fill(c.rect(1, h - 2, w - 1, h - 1), R[4])
    c.fill(c.rect(w - 2, 2, w - 1, h - 1), R[3])
    inset = c.rect(f + 1, f + 1, w - f - 1, h - f - 1)
    c.fill(c.rect(f, f, w - f, h - f), R[5])
    I = RED if kind == 'main' else NIGHT
    if hover:
        I = [tuple(min(255, int(v * 1.22 + 8)) for v in col) for col in I]
    c.ramp(inset, [I[1], I[2], I[3]], (c.yy - f) / float(h - 2 * f), soft=0.3)
    c.fill(c.rect(f + 1, f + 1, w - f - 1, f + 2), I[3])
    c.fill(c.rect(f + 1, h - f - 2, w - f - 1, h - f - 1), I[0])
    if f == 3:
        for rx, ry in ((2, 2), (w - 4, 2), (2, h - 4), (w - 4, h - 4)):
            c.px(rx, ry, R[0]); c.px(rx + 1, ry + 1, R[4])
    if kind == 'main':
        # a second, thin brass line inside the red field and a stud at each end
        c.fill(c.rect(f + 3, f + 3, w - f - 3, f + 4), R[3]); c.fill(c.rect(f + 3, h - f - 4, w - f - 3, h - f - 3), R[3])
        c.fill(c.rect(f + 3, f + 3, f + 4, h - f - 3), R[3]); c.fill(c.rect(w - f - 4, f + 3, w - f - 3, h - f - 3), R[3])
        for sx in (f + 7, w - f - 10):
            sy = h // 2 - 2
            c.fill(c.rect(sx, sy, sx + 3, sy + 3), R[1]); c.px(sx, sy, R[0]); c.px(sx + 2, sy + 2, R[4])
    return c


ICONS = {
    'chat': ['..........', '.XXXXXXXX.', 'XXXXXXXXXX', 'XX.XX.XX.X'.replace('.X', '.X'), 'XXXXXXXXXX', 'XXXXXXXXXX', '.XXXXXXXX.', '..XXX.....', '..XX......', '..X.......'],
    'globe': ['...XXXX...', '.XX.XX.XX.', '.X..XX..X.', 'XXXXXXXXXX', 'X...XX...X', 'X...XX...X', 'XXXXXXXXXX', '.X..XX..X.', '.XX.XX.XX.', '...XXXX...'],
    'home': ['....XX....', '...XXXX...', '..XXXXXX..', '.XXXXXXXX.', 'XXXXXXXXXX', '.XXXXXXXX.', '.XXX..XXX.', '.XXX..XXX.', '.XXX..XXX.', '..........'],
    'exit': ['XXXXXX....', 'X....X....', 'X....X..X.', 'X.......XX', 'X...XXXXXX', 'X...XXXXXX', 'X.......XX', 'X....X..X.', 'X....X....', 'XXXXXX....'],
    'cog': ['...XXXX...', '.X.XXXX.X.', '.XXXXXXXX.', 'XXXX..XXXX', 'XXX....XXX', 'XXX....XXX', 'XXXX..XXXX', '.XXXXXXXX.', '.X.XXXX.X.', '...XXXX...'],
    'map': ['XXX....XXX', 'X.XXXXXX.X', 'X.X..X.X.X', 'X.X..X.X.X', 'X.X.XX.X.X', 'X.X.X..X.X', 'X.XXX..X.X', 'X.X....X.X', 'X.XXXXXX.X', 'XXX....XXX'],
    'book': ['.XXXX.XXXX', 'XX..XXX..X', 'X.XX.X.XXX', 'X....X...X', 'X.XX.X.XXX', 'X....X...X', 'X.XX.X.XXX', 'X....X...X', 'XXXXXXXXXX', '....XX....'],
}


def icon(name, hover=False):
    c = plate(20, 20, 'plain', hover)
    rows = ICONS[name]
    for y, row in enumerate(rows):
        for x, v in enumerate(row):
            if v == 'X':
                c.px(5 + x, 5 + y, CREAM if not hover else K[0])
    return c


def bar_frame(w, h):
    c = plate(w, h, 'plain')
    return c


def bar_fill(w, h):
    c = Canvas(w, h)
    c.ramp(c.rect(0, 0, w, h), [K[0], K[1], K[2], K[3]], c.yy / float(h), soft=0.3)
    c.fill(c.rect(0, 0, w, 1), K[0])
    for x in range(0, w, 6):
        c.fill(c.rect(x, 1, x + 1, h), K[3])
    return c


def tag(w, h):
    """A small dark tag with a brass edge, for a line of text under a button."""
    c = Canvas(w, h)
    c.fill(c.rect(1, 0, w - 1, h) | c.rect(0, 0, w, h - 1), DARK)
    c.fill(c.rect(1, 0, w - 1, h - 1), K[4])
    c.ramp(c.rect(2, 0, w - 2, h - 2), [NIGHT[2], NIGHT[3]], c.yy / float(h), soft=0.3)
    c.fill(c.rect(2, h - 3, w - 2, h - 2), NIGHT[1])
    return c


def window_icon(size):
    """The crown on the night ground, for the window and the task bar."""
    c = Canvas(size, size)
    body = c.rect(1, 0, size - 1, size) | c.rect(0, 1, size, size - 1)
    c.fill(body, hexc('#0d0b10'))
    m = Canvas(size, size)
    if size >= 32:
        crown_mark(m, size // 2, size - 7, 22, 16)
    else:
        crown_mark(m, size // 2, size - 3, 12, 9)
    c.paste(m)
    return c


def save(c, path, rgba=True):
    c.image(1, rgba=rgba).save(path, optimize=True)


def build(out):
    os.makedirs(out, exist_ok=True)
    items = {'logo': logo()}
    for name, (w, h, kind) in {'btn_main': (148, 32, 'main'), 'btn_wide': (148, 20, 'plain'), 'btn_half': (72, 20, 'plain'),
                               'btn_80': (80, 20, 'plain'), 'btn_64': (64, 20, 'plain'),
                               'btn_vanilla': (200, 20, 'plain'), 'btn_small': (98, 20, 'plain')}.items():
        items[name] = plate(w, h, kind)
        items[name + '_hover'] = plate(w, h, kind, hover=True)
    items['btn_vanilla_off'] = plate(200, 20, 'flat')
    for n in ICONS:
        items['icon_' + n] = icon(n)
        items['icon_' + n + '_hover'] = icon(n, hover=True)
    items['btn_join'] = plate(148, 24, 'main')
    items['btn_join_hover'] = plate(148, 24, 'main', hover=True)
    items['tag'] = tag(104, 14)
    items['tip'] = tag(220, 26)
    items['bar_frame'] = bar_frame(148, 20)
    items['bar_fill'] = bar_fill(140, 12)
    for k, c in items.items():
        save(c, os.path.join(out, k + '.png'))
    # contact sheet for looking at them
    sheet = Image.new('RGBA', (1500, 900), (70, 100, 90, 255))
    x = y = 10
    rowh = 0
    for k, c in items.items():
        im = c.image(4, rgba=True)
        if x + im.width > 1490:
            x, y, rowh = 10, y + rowh + 10, 0
        sheet.paste(im, (x, y), im)
        x += im.width + 10; rowh = max(rowh, im.height)
    sheet.convert('RGB').save(os.path.join(out, 'ui_sheet.png'))
    return items


if __name__ == '__main__':
    build(sys.argv[1])
    print('ui written')
