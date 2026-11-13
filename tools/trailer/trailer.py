#!/usr/bin/env python3
"""The Kronwerke Season 2 trailer: thirty seconds of pixel art, painted frame by frame.

    trailer.py frames <dir> [from to]   paints the frames (480x270 PNGs, 12 a second)
    trailer.py still <dir> <second>...  single frames enlarged four times, to look at
    trailer.py video <dir> <out.mp4>    frames plus music.wav from <dir> to a 1080p video

The pictures stand on the grid of the menus (480 by 270, one texel is four pixels of a 1080p
screen). The cut follows the music (music.py, 120 beats a minute, a bar is two seconds):

     0 -  4 s   down from the stars to the old works, ticking        "Etwas tickt noch."
     4 - 10 s   the valley at dusk, the train comes in               "Die Werke laufen wieder an."
    10 - 16 s   the obelisk at spawn, everybody gives                "Ein Ziel. Alle zusammen."
    16 - 26 s   the five stages, two seconds each                    Steinwerk ... Chaoswerk
    26 - 30 s   the name, the date, the address

The first shot uses the layers of Core's join picture (give the Core checkout with KW_CORE,
default ../../../core next to the pack), the second the title picture of tools/menus/art, the
last the logo of the menus. To build everything:

    python3 trailer.py frames out && python3 music.py out/music.wav && python3 trailer.py video out trailer.mp4
"""
import math
import os
import subprocess
import sys

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'menus', 'art'))
import font  # noqa: E402
from px import Canvas, cols, hexc, noise1d, noise2d  # noqa: E402

W, H, FPS = 480, 270, 12
TOTAL = 30 * FPS
CORE = os.environ.get('KW_CORE', os.path.join(HERE, '..', '..', '..', 'core'))
NIGHT = hexc('#0d0b10')
CREAM = hexc('#f2ede3')
BRASS = cols('#fff3c4', '#f7dc86', '#e5b451', '#b98530', '#8a5a24', '#5c3a1e')
STAGE = cols('#a8b596', '#e5b451', '#8bb6dc', '#bb98f4', '#f06579')
OUTL = hexc('#15121f')
BAYER8 = None


def bayer8():
    global BAYER8
    if BAYER8 is None:
        b = np.array([[0, 2], [3, 1]])
        for _ in range(2):
            b = np.block([[4 * b, 4 * b + 2], [4 * b + 3, 4 * b + 1]])
        yy, xx = np.mgrid[0:H, 0:W]
        BAYER8 = (b[yy % 8, xx % 8] + 0.5) / 64.0
    return BAYER8


def blank(col=NIGHT):
    a = np.zeros((H, W, 3), np.uint8)
    a[:] = col
    return a


def over(a, rgba, x, y):
    """Lays an RGBA array over the frame with its top left at x, y (may reach outside)."""
    h, w = rgba.shape[:2]
    x0, y0, x1, y1 = max(0, x), max(0, y), min(W, x + w), min(H, y + h)
    if x1 <= x0 or y1 <= y0:
        return
    part = rgba[y0 - y:y1 - y, x0 - x:x1 - x]
    m = part[..., 3] > 127
    a[y0:y1, x0:x1][m] = part[..., :3][m]


def scale2(rgba, k):
    return np.repeat(np.repeat(rgba, k, axis=0), k, axis=1)


def dissolve(a, b, k):
    """A pixel dissolve from a to b: at k the share k of the pixels (by the Bayer pattern) show b."""
    out = a.copy()
    m = bayer8() < k
    out[m] = b[m]
    return out


def darken(a, k):
    return (a.astype(float) * (1 - k) + np.array(NIGHT) * k).astype(np.uint8)


def caption(a, text, y=236, k=2, colour=CREAM, shown=1.0, cx=W // 2):
    """A line of writing under the picture; shown < 1 types it letter by letter."""
    n = int(round(len(text) * min(1.0, shown)))
    x = cx - font.width(text, k) // 2
    if n > 0:
        font.draw(a, text[:n], x, y, colour, k)


# ======================================================================================
# shot 1: the old works (the layers of Core's join picture)

_JOIN = {}


def join_layers():
    if not _JOIN:
        d = os.path.join(CORE, 'src', 'main', 'resources', 'assets', 'kronwerke', 'textures', 'gui', 'join')
        for n in ('back', 'scene', 'front', 'light', 'gear_big', 'gear_mid', 'gear_small', 'pendulum'):
            _JOIN[n] = np.array(Image.open(os.path.join(d, n + '.png')).convert('RGBA'))
    return _JOIN


def island(f, lamps=1.0):
    """The join picture at frame f of its gears, as an RGBA array of 320 by 200, clear where nothing is."""
    L = join_layers()
    a = np.zeros((200, 320, 4), np.uint8)

    def put(img, x, y):
        h, w = img.shape[:2]
        m = img[..., 3] > 127
        a[y:y + h, x:x + w][m] = img[m]

    put(L['scene'], 0, 0)
    # smoke from the chimney
    for i in range(9):
        life = ((f / 62.0) + i / 9.0) % 1.0
        x = int(70 + life * 22 + math.sin(f / 17.0 + i * 2.1) * (1.5 + 4 * life))
        y = int(58 - life * 34)
        size = 2 if life < 0.25 or life > 0.7 else 3
        if life < 0.8 and 0 <= y < 198:
            a[y:y + size, x:x + size] = (hexc('#655a73') if i % 2 == 0 else hexc('#4b4159')) + (255,)
    sw = math.sin(f * math.pi / 16.0)
    pf = int(round((sw * 0.5 + 0.5) * 12))
    put(L['pendulum'][:, pf * 40:pf * 40 + 40], 222, 65)
    for name, x, y, s, columns, n in (('gear_small', 128, 98, 46, 8, 48), ('gear_mid', 212, 32, 58, 8, 64), ('gear_big', 154, 54, 84, 12, 96)):
        i = f % n
        put(L[name][(i // columns) * s:(i // columns) * s + s, (i % columns) * s:(i % columns) * s + s], x, y)
    put(L['front'], 0, 0)
    if lamps > 0.5:
        put(L['light'], 0, 0)
    # fireflies
    for i in range(11):
        bx, by = 44 + ((i * 97) % 240), 112 + ((i * 53) % 34)
        x = int(bx + math.sin(f / 23.0 + i) * 9)
        y = int(by + math.sin(f / 15.0 + i * 1.7) * 5)
        if math.sin(f / 6.0 + i * 2.3) > -0.2:
            a[y, x] = hexc('#c6dc6e') + (255,)
    return a


def tick_frame(n):
    """The gears' frame at trailer frame n: they tick, a tooth every half second (the beat), fast then still."""
    beat = n / (FPS / 2.0)                       # half seconds
    whole = math.floor(beat)
    part = beat - whole
    eased = min(1.0, part / 0.45)
    eased = 1 - (1 - eased) ** 2
    return int(round((whole + eased) * 8))


TALL = 390                     # the first shot's sky is taller than the picture: the view comes down it
CROWN = ((300, 78), (306, 60), (316, 70), (326, 52), (336, 70), (346, 60), (352, 78))
_NIGHT = {}


def night_back():
    """The sky over the old works, the far islets with what was left on them, a sea of cloud below."""
    if 'a' in _NIGHT:
        return _NIGHT['a']
    import scene
    c = Canvas(W, TALL)
    n = noise2d(W, TALL, 31, period=70, octaves=2)
    c.ramp(c.rect(0, 0, W, TALL), cols('#0d0b10', '#100e17', '#14111f', '#191528', '#1f1a33'), np.clip(c.yy / float(TALL) * 1.05 + (n - 0.5) * 0.2, 0, 1), soft=0.5)
    # a faint band of far stars across the sky
    gb = np.random.default_rng(32)
    for _ in range(900):
        x, y = int(gb.integers(0, W)), int(gb.integers(0, TALL - 70))
        off = abs((y - 40) - (x - 60) * 0.32)
        if off < 34 and gb.random() < (1 - off / 34.0) ** 1.5:
            c.px(x, y, hexc('#2c2744') if gb.random() < 0.75 else hexc('#48426a'))
    # the moon behind the works, dim, with a ring of haze
    mx, my = 203, TALL - 246 + 50
    for r, col in ((27, '#15121f'), (22, '#1a1628')):
        ring = c.ellipse(mx, my, r)
        c.fill(ring & (((c.xx + c.yy) % 2) == 0), hexc(col))
    c.fill(c.ellipse(mx, my, 17), hexc('#3d3655'))
    c.fill(c.ellipse(mx - 2, my - 2, 14), hexc('#4a4266'))
    c.fill(c.ellipse(mx - 4, my - 4, 9), hexc('#564d76'))
    for cx_, cy_, r in ((mx + 5, my - 5, 3), (mx - 5, my + 6, 2.4), (mx + 6, my + 6, 2), (mx - 8, my - 3, 1.6)):
        cr = c.ellipse(cx_, cy_, r)
        c.fill(cr, hexc('#332d4a'))
        c.fill(cr & ~c.shift(cr, 1, 1), hexc('#2a2540'))
    # thin clouds the moon catches
    P = {'cloud': cols('#17142a', '#1f1c38', '#2a2648', '#3d3862')}
    for k, (cx, base, width) in enumerate(((70, 120, 80), (410, 96, 96), (250, 30, 60), (30, 250, 70), (450, 262, 80), (150, 186, 50))):
        scene.cloud(c, P, cx, base, width, 40 + k, flat=True)
    # far islets, dark, with what was left on them
    dark, lit, turf = hexc('#1a1629'), hexc('#2c2748'), hexc('#2c4438')
    gi = np.random.default_rng(36)

    def islet(x, y, w):
        pts = [(x - w, y), (x + w, y)]
        for k in range(6, -1, -1):
            f = k / 6.0
            pts.append((x - w + 2 * w * f + gi.uniform(-1, 1), y + 1 + w * 0.7 * math.sin(f * math.pi) ** 0.6 * gi.uniform(0.7, 1.15)))
        m = c.poly(pts)
        c.fill(m, dark)
        c.fill(m & (c.xx < x - w * 0.2), lit)
        c.fill(m & (c.yy <= y + 1), hexc('#22352e'))
        c.fill(m & (c.yy == y), turf)
        for k in range(3):
            rx = int(x - w // 2 + k * (w // 2))
            for q in range(int(gi.integers(2, 6))):
                c.px(rx, y + w * 0.6 + 2 + q, dark)

    islet(40, 262, 16)                                   # a dead tree and a leaning post
    tree = c.line(38, 262, 38, 244, width=2) | c.line(38, 250, 32, 243) | c.line(38, 247, 44, 240) | c.line(44, 240, 46, 236) | c.line(32, 243, 30, 239)
    c.fill(tree, dark)
    c.fill(tree & ~c.shift(tree, 1, 0), lit)
    c.fill(c.line(50, 262, 53, 252), dark)
    islet(446, 226, 20)                                  # a wheel half sunk into the ground, a lamp that still burns
    wheel = (c.ellipse(444, 226, 11) & ~c.ellipse(444, 226, 7) & (c.yy < 226)) | (c.rect(443, 215, 445, 226)) | c.line(436, 219, 452, 219)
    c.fill(wheel, hexc('#3a2c22'))
    c.fill(wheel & ~c.shift(wheel, 0, 1), hexc('#6b4f2a'))
    c.fill(c.rect(460, 216, 461, 226), dark)
    c.px(460, 215, hexc('#ffd27a'))
    islet(404, 344, 12)                                  # a broken chimney
    c.fill(c.poly([(399, 344), (400, 326), (403, 330), (405, 324), (406, 344)]), dark)
    c.fill(c.rect(400, 326, 401, 344), lit)
    islet(96, 352, 14)                                   # two pines
    for px_, h in ((90, 12), (100, 9)):
        for k in range(h):
            hw = (k * 2) // 5
            c.fill(c.rect(px_ - hw, 352 - h + k, px_ + hw + 1, 353 - h + k), hexc('#17231f'))
    islet(214, 68, 9)
    # a sea of cloud under everything
    sea = {'cloud': cols('#100e18', '#15121f', '#1b172a', '#252038')}
    for k in range(10):
        scene.cloud(c, sea, 20 + k * 50, 384 + (k % 2) * 5, 90, 60 + k)
    _NIGHT['a'] = c.a.copy()
    g = np.random.default_rng(35)
    _NIGHT['stars'] = [(int(g.integers(0, W)), int(g.integers(0, TALL - 60)), int(g.integers(0, 4)), g.random() < 0.22) for _ in range(230)]
    return _NIGHT['a']


def night_sky(n):
    """The tall sky at frame n: the stars twinkle, the crown stands among them, one star falls."""
    a = night_back().copy()
    for x, y, phase, bright in _NIGHT['stars']:
        if (n // 5 + phase) % 4 != 0 and tuple(a[y, x]) < (60, 60, 90):
            a[y, x] = CREAM if bright else hexc('#5d5470')
    for k in range(len(CROWN) - 1):                      # the crown: seven stars and the faint lines between them
        (x0, y0), (x1, y1) = CROWN[k], CROWN[k + 1]
        steps = max(abs(x1 - x0), abs(y1 - y0))
        for q in range(2, steps - 1, 3):
            a[y0 + (y1 - y0) * q // steps, x0 + (x1 - x0) * q // steps] = hexc('#3a3558')
    for k, (x, y) in enumerate(CROWN):
        a[y, x] = hexc('#fff3c4')
        if (n // 4 + k) % 3:
            a[y - 1, x] = a[y + 1, x] = a[y, x - 1] = a[y, x + 1] = BRASS[2]
    if 6 <= n < 13:                                      # a falling star
        q = n - 6
        for d in range(7):
            x, y = 120 + q * 13 - d * 3, 96 + q * 6 - d * 1.4
            a[int(y), int(x)] = (CREAM, CREAM, hexc('#c9c4e8'), hexc('#8a84b0'), hexc('#5d5470'), hexc('#3a3558'), hexc('#2a2540'))[d]
    return a


def shot_works(n):
    """0 to 4 s. The view comes down from the stars to the old works, which tick; then the line."""
    f = tick_frame(n)
    lamps = 1.0 if (n % 7) != 3 else 0.0         # the lamps flicker now and then
    sky = night_sky(n)
    isl = island(f, lamps)
    h, w = isl.shape[:2]
    mk = isl[..., 3] > 127
    sky[TALL - 246:TALL - 246 + h, 80:80 + w][mk] = isl[..., :3][mk]
    u = min(1.0, n / 21.0)
    u = u * u * (3 - 2 * u)
    vy = int(round((TALL - H) * u))
    a = sky[vy:vy + H].copy()
    caption(a, 'ETWAS TICKT NOCH.', y=240, k=2, shown=(n - 26) / 9.0)
    return a


# ======================================================================================
# shot 2: the valley (the title picture)

_VALLEY = {}


def valley(t):
    if t not in _VALLEY:
        import scene
        _VALLEY[t] = np.array(scene.build('dusk', t).image(1))
    return _VALLEY[t]


def shot_valley(n):
    """4 to 10 s. The train comes in from the left and stops at the works; the line types itself."""
    m = n - 4 * FPS
    t = min(79, int(m * 10 / 12.0 * 1.25))       # the picture's own clock runs a little faster than at home
    a = valley(t).copy()
    caption(a, 'DIE WERKE LAUFEN WIEDER AN.', y=244, k=2, shown=(m - 18) / 14.0)
    return a


# ======================================================================================
# shot 3: the obelisk at spawn

def shot_obelisk(n):
    """10 to 16 s. Everybody brings something; the bar fills and the stage is done on the last beat."""
    import obelisk_shot
    m = n - 10 * FPS
    a, pct = obelisk_shot.frame(m)
    a = a.copy()
    obelisk_shot.foreground(a, m)
    caption(a, 'EIN ZIEL. ALLE ZUSAMMEN.', y=247, k=2, shown=(m - 12) / 12.0)
    return a


# ======================================================================================
# shot 4: the five stages

def shot_stage(n):
    """16 to 26 s. Two seconds a stage; every cut lands on a bar."""
    import stages_shot
    m = n - 16 * FPS
    stage, k = m // (2 * FPS), m % (2 * FPS)
    a = stages_shot.card(stage, k)
    if k < 2:                                      # a short light on the cut, the stage's colour in it
        light = tuple((int(v) + 2 * c) // 3 for v, c in zip(STAGE[stage], CREAM))
        a = tint(a, light, (0.3, 0.1)[k])
    return a


def tint(a, col, k):
    return (a.astype(float) * (1 - k) + np.array(col, float) * k).astype(np.uint8)


# ======================================================================================
# shot 5: the name, the date, the address

_FINAL = {}


def final_back():
    if 'back' not in _FINAL:
        c = Canvas(W, H)
        d = np.sqrt(((c.xx - W / 2) / 1.7) ** 2 + (c.yy - 96) ** 2)
        c.ramp(c.rect(0, 0, W, H), cols('#33243a', '#261b2e', '#1a1422', '#120f18') + [NIGHT], np.clip(d / 150.0, 0, 1), soft=0.5)
        g = np.random.default_rng(77)
        for _ in range(110):
            x, y = int(g.integers(0, W)), int(g.integers(0, H))
            c.px(x, y, CREAM if g.random() < 0.18 else hexc('#5d5470'))
        _FINAL['back'] = c.a.copy()
        import ui
        _FINAL['logo'] = np.array(ui.logo().image(2, rgba=True))
    return _FINAL['back']


def gear_sprite(name, f):
    L = join_layers()
    s, columns, n = {'gear_small': (46, 8, 48), 'gear_mid': (58, 8, 64), 'gear_big': (84, 12, 96)}[name]
    i = f % n
    return L[name][(i // columns) * s:(i // columns) * s + s, (i % columns) * s:(i % columns) * s + s]


def shot_final(n):
    """26 to 30 s. The wheels tick on behind; the name comes with the bar, then the date, then where."""
    m = n - 26 * FPS
    a = final_back().copy()
    f = tick_frame(n)
    # the three wheels of the works, large and in the dark, half out of the picture
    lay = np.zeros((H, W, 4), np.uint8)
    for name, x, y, k, turn in (('gear_big', -52, 132, 2, 1), ('gear_mid', 84, 196, 2, -1), ('gear_mid', 392, -44, 2, -1), ('gear_small', 372, 40, 2, 1), ('gear_big', 366, 150, 2, 1), ('gear_small', -30, -28, 2, 1)):
        sp = scale2(gear_sprite(name, f if turn > 0 else -f), k)
        h, w = sp.shape[:2]
        x0, y0, x1, y1 = max(0, x), max(0, y), min(W, x + w), min(H, y + h)
        part = sp[y0 - y:y1 - y, x0 - x:x1 - x]
        mk = part[..., 3] > 127
        lay[y0:y1, x0:x1][mk] = part[mk]
    mk = lay[..., 3] > 127
    bright = lay[..., :3].astype(int).sum(axis=2)
    a[mk] = hexc('#1d1727')
    a[mk & (bright > 430)] = hexc('#2a2135')
    a[mk & (bright > 600)] = hexc('#4a3a3c')
    a[mk & (bright < 150)] = hexc('#15111d')
    # sparks rising
    for k in range(26):
        life = ((n / 50.0) + k / 26.0) % 1.0
        x = (k * 61 + 17) % W + int(math.sin(n / 7.0 + k) * 4)
        y = int(H - 4 - life * 150)
        if 0 <= x < W - 1 and 0 <= y < H:
            a[y, x] = BRASS[1] if k % 3 else BRASS[3]
    logo = _FINAL['logo']
    lh, lw = logo.shape[:2]
    drop = (10, 4, 1, 0)[m] if m < 4 else 0
    over(a, logo, W // 2 - lw // 2, 22 - drop)
    if m >= 9:
        caption(a, '16. JANUAR 2027, 18 UHR', y=168, k=2, shown=(m - 9) / 10.0)
    if m >= 24:
        text = 'KRONWERKE.NET'
        x = W // 2 - font.width(text, 2) // 2
        pad = a[196:220, x - 12:x + font.width(text, 2) + 12]
        pad[:] = hexc('#15121f')
        pad[0, :] = BRASS[3]
        pad[-1, :] = BRASS[4]
        font.draw(a, text, x, 201, BRASS[1], 2)
        # the five stages as pips under it, one more with every frame
        for k in range(5):
            if m >= 27 + k * 2:
                px_ = W // 2 - 34 + k * 14
                a[232:240, px_:px_ + 10] = OUTL
                a[233:239, px_ + 1:px_ + 9] = STAGE[k]
                a[233, px_ + 1:px_ + 9] = np.minimum(255, np.array(STAGE[k], int) + 40)
    if m < 3:
        a = tint(a, BRASS[0], (0.45, 0.2, 0.07)[m])
    if 24 <= m < 26:
        a = tint(a, BRASS[0], (0.2, 0.07)[m - 24])
    return a


# ======================================================================================
# the cut

CUTS = (0, 4, 10, 16, 26, 30)


def raw(n):
    if n < 4 * FPS:
        return shot_works(n)
    if n < 10 * FPS:
        return shot_valley(n)
    if n < 16 * FPS:
        return shot_obelisk(n)
    if n < 26 * FPS:
        return shot_stage(n)
    return shot_final(min(n, TOTAL - 1))


def frame(n):
    a = raw(n)
    # the first two cuts dissolve pixel by pixel over the last three frames before the bar
    for cut in (4 * FPS, 10 * FPS):
        if cut - 3 <= n < cut:
            a = dissolve(a, raw(cut), (n - (cut - 4)) / 4.0)
    # the stage is done: the picture goes white with the last beat before the stages
    if 16 * FPS - 5 <= n < 16 * FPS:
        a = tint(a, CREAM, (0.12, 0.25, 0.4, 0.6, 0.8)[n - (16 * FPS - 5)])
    return a


def main():
    mode = sys.argv[1]
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    if mode == 'frames':
        lo = int(sys.argv[3]) if len(sys.argv) > 3 else 0
        hi = int(sys.argv[4]) if len(sys.argv) > 4 else TOTAL
        for n in range(lo, hi):
            Image.fromarray(frame(n)).save(os.path.join(out, 'f%04d.png' % n))
            if n % 24 == 0:
                print('frame', n, flush=True)
    elif mode == 'still':
        for s in sys.argv[3:]:
            n = int(round(float(s) * FPS))
            Image.fromarray(frame(n)).resize((W * 4, H * 4), Image.NEAREST).save(os.path.join(out, 'still_%s.png' % s.replace('.', '_')))
    elif mode == 'video':
        target = sys.argv[3]
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', os.path.join(out, 'f%04d.png')]
        music = os.path.join(out, 'music.wav')
        if os.path.exists(music):
            cmd += ['-i', music, '-c:a', 'aac', '-b:a', '192k', '-shortest']
        cmd += ['-vf', 'scale=1920:1080:flags=neighbor,fps=24', '-c:v', 'libx264', '-preset', 'slow', '-crf', '14', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', target]
        subprocess.check_call(cmd)
    print('ok')


if __name__ == '__main__':
    main()
