"""The Kronwerk itself: halls, tower with the crown, chimneys, obelisk. Drawn on its own layer."""
import numpy as np
from px import Canvas

BASE = 173


def blend(a, col, k):
    return (a.astype(float) * (1 - k) + np.array(col, float) * k).astype(np.uint8)


def brick(b, m, P, seed=0, key='brick', bw=7, bh=3, lit_from=None):
    """Brick or stone courses inside a mask, lighter towards the right."""
    R = P[key]
    xs = np.where(m.any(axis=0))[0]
    if len(xs) == 0:
        return
    x0, x1 = xs.min(), xs.max() + 1
    t = 1 - (b.xx - x0) / max(1.0, x1 - x0)
    if lit_from is not None:
        t = 1 - np.clip((b.xx - lit_from) / max(1.0, x1 - lit_from), 0, 1)
    b.ramp(m, [R[1], R[2], R[2], R[3]], t * 0.9 + 0.05, soft=0.5)
    row = b.yy // bh
    joint = ((b.yy % bh) == bh - 1) | (((b.xx + (row % 2) * (bw // 2)) % bw) == 0)
    b.a[m & joint] = blend(b.a[m & joint], R[4], 0.55)
    rng = np.random.default_rng(seed)
    cell = (row * 131 + (b.xx + (row % 2) * (bw // 2)) // bw * 17) % 97
    pick = rng.permutation(97)
    light = m & ~joint & (pick[cell] < 9)
    dark = m & ~joint & (pick[cell] > 86)
    b.a[light] = blend(b.a[light], R[0], 0.5)
    b.a[dark] = blend(b.a[dark], R[4], 0.4)


def slate(b, m, P):
    R = P['roof']
    ys = np.where(m.any(axis=1))[0]
    xs = np.where(m.any(axis=0))[0]
    if len(ys) == 0:
        return
    y0, x0, x1 = ys.min(), xs.min(), xs.max() + 1
    row = (b.yy - y0) // 3
    t = 0.85 - (b.xx - x0) / float(x1 - x0) * 0.75 + (b.yy - y0) / max(1.0, ys.max() - y0) * 0.15
    b.ramp(m, [R[0], R[1], R[2], R[3]], t, soft=0.45)
    line = m & (((b.yy - y0) % 3) == 2)
    b.a[line] = blend(b.a[line], R[4], 0.5)
    tick = m & (((b.xx + (row % 2) * 2) % 5) == 0) & ~line
    b.a[tick] = blend(b.a[tick], R[4], 0.3)
    b.fill(m & ~b.shift(m, 0, 1), P['brass'][2])


def window(b, P, x, y, w, h, night, arch=True, lit=True):
    """Arched window with a warm glow; x, y is the top left of the frame."""
    frame = b.rect(x, y + (w // 2 if arch else 0), x + w, y + h)
    if arch:
        frame |= b.ellipse(x + (w - 1) / 2.0, y + w / 2.0, w / 2.0 + 0.2) & (b.yy <= y + w // 2)
    b.fill(frame, P['brick'][4])
    glass = b.rect(x + 1, y + (w // 2 if arch else 1), x + w - 1, y + h - 1)
    if arch:
        glass |= b.ellipse(x + (w - 1) / 2.0, y + w / 2.0, w / 2.0 - 0.9) & (b.yy <= y + w // 2)
    G = P['glow']
    if lit:
        d = np.hypot((b.xx - (x + w / 2.0)) / (w / 2.0), (b.yy - (y + h * 0.62)) / (h * 0.6))
        b.ramp(glass, [G[0], G[1], G[2], G[3]], d * 0.75, soft=0.5)
    else:
        b.ramp(glass, [P['roof'][1], P['roof'][2], P['roof'][3]], (b.yy - y) / float(h), soft=0.3)
    mx = x + w // 2
    b.fill(glass & ((b.xx == mx) | (b.yy == y + h // 2 + (1 if arch else 0))), P['brick'][4])
    b.fill(b.rect(x - 1, y + h, x + w + 1, y + h + 1), P['stone'][1])
    return frame


def gear(b, P, cx, cy, r, teeth=10, hole=True, phase=0.0):
    ang = np.arctan2(b.yy - cy, b.xx - cx) + phase
    d = np.hypot(b.xx - cx, b.yy - cy)
    tooth = ((ang * teeth / (2 * np.pi)) % 1.0) < 0.5
    m = (d <= r) | ((d <= r + 2.2) & tooth)
    R = P['brass']
    t = np.clip(0.5 - ((b.xx - cx) - (b.yy - cy)) / (2.8 * r), 0, 1)
    b.ramp(m, [R[1], R[2], R[3], R[4]], t, soft=0.3)
    if hole and r >= 5:
        hub = max(1.7, r * 0.3)
        inner = (d <= r - 2.2) & (d > hub)
        spoke = (np.abs(b.xx - cx) < 0.9) | (np.abs(b.yy - cy) < 0.9)
        b.fill(inner & ~spoke, P['dark'])
        b.fill(d <= hub, R[1])
        b.fill(d <= 0.8, R[4])
    b.fill(b.edge(m) & (b.xx - cx < b.yy - cy - 1), R[5])
    return m


def crown(b, P, cx, base, w, h):
    """The Kronwerke crown: a band with five points, the middle one tallest."""
    R = P['brass']
    x0 = cx - w // 2
    band = b.rect(x0, base - 5, x0 + w, base)
    pts = [(x0, base - 5), (x0 - 2, base - h + 5), (x0 + w * 0.2, base - h * 0.52), (cx - w * 0.2, base - h + 2),
           (cx - w * 0.07, base - h * 0.5), (cx, base - h - 1), (cx + w * 0.07, base - h * 0.5), (cx + w * 0.2, base - h + 2),
           (x0 + w * 0.8, base - h * 0.52), (x0 + w + 1, base - h + 5), (x0 + w - 1, base - 5)]
    m = band | b.poly(pts)
    t = np.clip(1 - (b.xx - x0) / float(w) * 0.9 + (b.yy - (base - h)) / float(h) * 0.25 - 0.1, 0, 1)
    b.ramp(m, [R[0], R[1], R[2], R[3], R[4]], t, soft=0.35)
    b.fill(b.rect(x0, base - 5, x0 + w, base - 4), R[1])
    b.fill(b.rect(x0, base - 1, x0 + w, base), R[4])
    for i, gx in enumerate(np.linspace(x0 + 3, x0 + w - 4, 5)):
        b.fill(b.rect(gx, base - 4, gx + 2, base - 2), P['gem'][i % len(P['gem'])])
    b.fill(b.edge(m) & (b.xx < cx - w * 0.3), R[5])
    for px_, py_ in ((x0 - 2, base - h + 4), (cx - w * 0.2, base - h + 1), (cx, base - h - 2), (cx + w * 0.2, base - h + 1), (x0 + w + 1, base - h + 4)):
        ball = b.ellipse(px_, py_, 1.6)
        b.fill(ball, R[1])
        b.px(int(px_) + 1, int(py_) - 1, R[0])
        m |= ball
    return m


def smoke(c, P, x, y, seed, n=7, drift=-3.4, rise=6.0, size=1.0):
    rng = np.random.default_rng(seed)
    S = P['smoke']
    body = c.none()
    puffs = []
    for i in range(n):
        f = i / float(n - 1)
        cx = x + drift * i * (0.6 + f) + rng.uniform(-1.5, 1.5)
        cy = y - rise * i - rng.uniform(0, 2)
        r = (2.4 + 7.5 * f ** 0.9) * size
        for _ in range(3):
            puffs.append((cx + rng.uniform(-r * 0.5, r * 0.5), cy + rng.uniform(-r * 0.3, r * 0.3), r * rng.uniform(0.55, 0.85)))
    for cx, cy, r in puffs:
        body |= c.ellipse(cx, cy, r * 1.2, r)
    c.fill(body, S[2])
    core = body & c.shift(body, 2, -2) & c.shift(body, 4, -3)
    c.fill(core, S[3])
    lit = body & ~c.shift(body, -2, 1) & ~c.shift(body, -1, 2)
    c.fill(body & ~c.shift(body, -3, 2), S[1])
    c.fill(lit, S[0])


def chimney(b, P, x, top, base, w=6):
    m = b.rect(x, top, x + w, base)
    brick(b, m, P, seed=x, bw=4, bh=3)
    b.fill(b.rect(x - 1, top, x + w + 1, top + 2), P['brass'][3])
    b.fill(b.rect(x - 1, top, x + w + 1, top + 1), P['brass'][1])
    b.fill(b.rect(x, top + 8, x + w, top + 9), P['brass'][3])
    b.fill(b.rect(x + 1, top - 1, x + w - 1, top), P['dark'])


def obelisk(c, P, x, base, h, night):
    S = P['stone']
    # the beam first, so the stone covers its foot
    for y in range(base - h - 1, 8, -1):
        f = (base - h - y) / float(base - h - 8)
        if f < 0.3 or c.bayer[y, x] < 1.25 - f * 1.3:
            c.px(x, y, P['beam'])
        for dx in (-1, 1):
            if f < 0.12 or c.bayer[y, x + dx] < 0.3 - f * 0.9:
                c.px(x + dx, y, P['glow'][2])
    m = c.poly([(x - 6, base), (x - 4, base - h + 8), (x, base - h), (x + 4, base - h + 8), (x + 6, base)])
    c.ramp(m, [S[2], S[3], S[4]], 1 - (c.xx - (x - 6)) / 13.0 + 0.2, soft=0.25)
    c.fill(m & ~c.shift(m, -1, 0), P['sun'][1])
    c.fill(m & ~c.shift(m, 1, 0), P['dark'])
    cap = c.poly([(x - 4, base - h + 8), (x, base - h), (x + 4, base - h + 8)])
    c.fill(cap, P['brass'][3]); c.fill(cap & (c.xx >= x), P['brass'][1]); c.fill(cap & ~c.shift(cap, -1, 0), P['brass'][0])
    c.fill(c.rect(x - 4, base - h + 8, x + 5, base - h + 9), P['brass'][4])
    for i, y in enumerate(range(base - h + 13, base - 8, 6)):
        pat = ((0, 0), (1, 0), (-1, 1), (0, 2), (1, 3)) if i % 2 == 0 else ((-1, 0), (0, 0), (1, 1), (0, 2), (-1, 3))
        for dx, dy in pat:
            c.px(x + dx, y + dy, P['rune'])
    for x0, x1, y0, y1, k in ((x - 8, x + 9, base - 3, base, 2), (x - 11, x + 12, base, base + 3, 3)):
        c.fill(c.rect(x0, y0, x1, y1), S[k]); c.fill(c.rect(x0, y0, x1, y0 + 1), S[0]); c.fill(c.rect(x1 - 1, y0, x1, y1), P['sun'][1])


def halo(c, cx, cy, r, col, only=None, k=(0.07, 0.16, 0.3)):
    """Soft light in three flat rings; only limits it to a mask."""
    d = np.hypot(c.xx - cx, (c.yy - cy) * 1.25)
    for i, kk in enumerate(k):
        m = d <= r * (1 - i / 3.0)
        if only is not None:
            m &= only
        c.a[m] = blend(c.a[m], col, kk if i == 0 else kk - k[i - 1])


def train(c, P, x, y):
    """A small steam engine with two wagons, heading right; x, y is the rail under the rear wagon."""
    K, B, Wd, D = P['brass'], P['brick'], P['wood'], P['dark']

    def wheel(wx, wy, r=2.6):
        c.fill(c.ellipse(wx, wy, r), D); c.fill(c.ellipse(wx, wy, r - 1.2), K[3]); c.px(int(wx), int(wy), K[1])

    def wagon(wx, wy, load):
        c.fill(c.rect(wx, wy - 9, wx + 18, wy - 3), Wd[1]); c.fill(c.rect(wx, wy - 9, wx + 18, wy - 8), Wd[0])
        for i in range(wx + 4, wx + 18, 5):
            c.fill(c.rect(i, wy - 8, i + 1, wy - 3), Wd[2])
        c.fill(c.rect(wx - 1, wy - 4, wx + 19, wy - 2), K[3]); c.fill(c.rect(wx - 1, wy - 4, wx + 19, wy - 3), K[1])
        c.fill(c.rect(wx + 17, wy - 9, wx + 18, wy - 4), P['sun'][1])
        if load == 'ore':
            for i, (lx, ly, col) in enumerate(((2, -11, K[2]), (6, -12, K[1]), (10, -11, K[2]), (13, -12, K[1]), (4, -10, K[3]), (8, -10, K[2]), (15, -10, K[3]))):
                c.fill(c.rect(wx + lx, wy + ly, wx + lx + 3, wy + ly + 3), col)
        else:
            c.fill(c.rect(wx + 2, wy - 14, wx + 9, wy - 9), Wd[0]); c.fill(c.rect(wx + 2, wy - 14, wx + 9, wy - 13), K[1]); c.fill(c.rect(wx + 5, wy - 14, wx + 6, wy - 9), Wd[2])
            c.fill(c.rect(wx + 10, wy - 13, wx + 16, wy - 9), Wd[1]); c.fill(c.rect(wx + 10, wy - 13, wx + 16, wy - 12), Wd[0])
        wheel(wx + 4, wy - 1); wheel(wx + 14, wy - 1)

    wagon(x, y, 'crates')
    wagon(x + 21, y + 1, 'ore')
    lx, ly = x + 42, y + 2
    c.fill(c.rect(lx - 2, ly - 5, lx, ly - 4), D); c.fill(c.rect(x + 19, y - 4, x + 21, y - 3), D)
    # cab
    c.fill(c.rect(lx, ly - 16, lx + 10, ly - 3), B[2]); c.fill(c.rect(lx, ly - 16, lx + 10, ly - 15), B[0]); c.fill(c.rect(lx + 9, ly - 16, lx + 10, ly - 3), B[1])
    c.fill(c.rect(lx - 1, ly - 18, lx + 11, ly - 16), P['roof'][2]); c.fill(c.rect(lx - 1, ly - 18, lx + 11, ly - 17), P['roof'][0])
    c.fill(c.rect(lx + 2, ly - 13, lx + 8, ly - 8), P['glow'][1]); c.fill(c.rect(lx + 5, ly - 13, lx + 6, ly - 8), B[4])
    # boiler
    boiler = c.rect(lx + 10, ly - 12, lx + 27, ly - 4)
    c.ramp(boiler, [K[1], K[2], K[3], K[4]], (c.yy - (ly - 12)) / 8.0, soft=0.3)
    for i in (lx + 15, lx + 21):
        c.fill(c.rect(i, ly - 12, i + 1, ly - 4), K[4])
    c.fill(c.rect(lx + 26, ly - 12, lx + 28, ly - 4), K[0])
    c.fill(c.rect(lx + 21, ly - 18, lx + 25, ly - 12), D); c.fill(c.rect(lx + 20, ly - 19, lx + 26, ly - 17), K[3]); c.fill(c.rect(lx + 20, ly - 19, lx + 26, ly - 18), K[1])
    c.fill(c.ellipse(lx + 14, ly - 13, 2.2, 1.6), K[2])
    c.fill(c.poly([(lx + 28, ly - 5), (lx + 33, ly - 1), (lx + 28, ly - 1)]), D)
    c.fill(c.rect(lx + 28, ly - 9, lx + 30, ly - 7), P['glow'][0])
    c.fill(c.rect(lx - 1, ly - 4, lx + 29, ly - 2), D)
    wheel(lx + 4, ly - 1, 3.4); wheel(lx + 13, ly - 1, 3.4); wheel(lx + 22, ly - 1, 2.6)
    c.fill(c.rect(lx + 4, ly - 2, lx + 14, ly - 1), K[1])
    return lx + 23, ly - 19


def rails(c, P, g, f):
    """A track across the lower slope, from the left edge to the right: bed, sleepers, two rails."""
    xs = np.arange(c.w)
    ys = np.round(207 + xs * 0.058 + np.sin(xs / 70.0) * 2.0).astype(int)
    S = P['stone']
    for x in xs:
        c.fill(c.rect(x, ys[x] - 1, x + 1, ys[x] + 5), P['path'][2])
        c.px(x, ys[x] + 5, P['grass'][5])
    for x in range(1, c.w, 5):
        c.fill(c.rect(x, ys[x] - 1, x + 2, ys[x] + 5), P['wood'][2])
        c.fill(c.rect(x, ys[x] - 1, x + 2, ys[x]), P['wood'][1])
    for x in xs:
        c.px(x, ys[x], S[0]); c.px(x, ys[x] + 1, S[3])
        c.px(x, ys[x] + 3, S[1]); c.px(x, ys[x] + 4, S[4])
    return ys


def birds(c, P):
    for x, y, s in ((92, 62, 1), (104, 56, 1), (84, 72, 0), (228, 96, 0), (310, 44, 1), (322, 50, 0), (40, 128, 0)):
        col = P['dark']
        c.px(x, y, col); c.px(x - 1, y - 1, col); c.px(x + 1, y - 1, col)
        if s:
            c.px(x - 2, y - 1, col); c.px(x + 2, y - 1, col); c.px(x - 3, y, col); c.px(x + 3, y, col)


def lantern(c, P, x, base, h=11):
    c.fill(c.rect(x, base - h, x + 1, base), P['wood'][3])
    c.fill(c.rect(x, base - h, x + 4, base - h + 1), P['wood'][3])
    c.fill(c.rect(x + 2, base - h + 1, x + 5, base - h + 5), P['brass'][4])
    c.fill(c.rect(x + 3, base - h + 2, x + 4, base - h + 4), P['glow'][0])
    c.px(x + 2, base - h + 2, P['glow'][2]); c.px(x + 4, base - h + 3, P['glow'][2])


def draw(c, P, g, night):
    b = Canvas(c.w, c.h)
    B, K, S = P['brick'], P['brass'], P['stone']

    # long evening shadow on the grass, falling to the left
    G = P['grass']
    sh = c.poly([(44, BASE + 1), (236, BASE + 1), (226, BASE + 18), (-40, BASE + 30)]) & c.below(g + 1)
    for i in range(len(G) - 1, -1, -1):
        hit = sh & (c.a == np.array(G[i], np.uint8)).all(axis=2)
        c.fill(hit, G[min(len(G) - 1, i + 2)])

    # ---- west workshop -------------------------------------------------------
    wx0, wx1, wy = 64, 112, 143
    brick(b, b.rect(wx0, wy, wx1, BASE), P, seed=1)
    roof = b.poly([(wx0 - 4, wy), (wx0 + 8, wy - 14), (wx1 + 2, wy - 14), (wx1 + 2, wy)])
    slate(b, roof, P)
    b.fill(b.rect(wx0 - 4, wy, wx1, wy + 2), K[3]); b.fill(b.rect(wx0 - 4, wy, wx1, wy + 1), K[1])
    for x in (71, 85, 99):
        window(b, P, x, 151, 7, 14, night)
    # tank on the far left
    tank = b.rect(46, 150, 62, BASE)
    b.ramp(tank, [K[4], K[3], K[2], K[1], K[2]], (b.xx - 46) / 16.0, soft=0.4)
    b.fill(b.ellipse(53.5, 150, 8, 3) & (b.yy <= 150), K[2])
    b.fill(b.rect(46, 157, 62, 158), K[5]); b.fill(b.rect(46, 166, 62, 167), K[5])
    b.fill(b.rect(52, 141, 55, 148), K[3]); b.fill(b.rect(52, 141, 70, 143), K[3]); b.fill(b.rect(52, 141, 70, 142), K[1])

    # ---- main hall -----------------------------------------------------------
    hx0, hx1, hy = 108, 184, 121
    brick(b, b.rect(hx0, hy, hx1, BASE), P, seed=2)
    roof = b.poly([(hx0 - 4, hy), (hx0 + 14, hy - 24), (hx1 - 6, hy - 24), (hx1 + 3, hy)])
    slate(b, roof, P)
    b.fill(b.rect(hx0 - 4, hy, hx1 + 3, hy + 2), K[3]); b.fill(b.rect(hx0 - 4, hy, hx1 + 3, hy + 1), K[1])
    b.fill(b.rect(hx0, hy + 2, hx1, hy + 4), B[4])
    # stone plinth
    brick(b, b.rect(hx0 - 1, BASE - 6, hx1 + 1, BASE), P, seed=3, key='stone', bw=9, bh=3)
    # gate
    gx0, gx1, gy = 136, 158, 143
    arch = b.rect(gx0, gy + 10, gx1, BASE) | (b.ellipse((gx0 + gx1 - 1) / 2.0, gy + 11, 11.2) & (b.yy <= gy + 11))
    b.fill(arch, K[3])
    b.fill(arch & ~b.shift(arch, 1, 1), K[1])
    inner = b.rect(gx0 + 2, gy + 11, gx1 - 2, BASE) | (b.ellipse((gx0 + gx1 - 1) / 2.0, gy + 11, 9.0) & (b.yy <= gy + 11))
    d = np.hypot((b.xx - 147) / 11.0, (b.yy - (BASE - 4)) / 26.0)
    G = P['glow']
    b.ramp(inner, [G[0], G[1], G[2], G[3], B[3]], d * 0.95, soft=0.6)
    b.fill(inner & (b.xx == 147), B[4])
    b.fill(inner & (b.yy == gy + 11), B[4])
    for x in (139, 143, 151, 155):
        b.fill(inner & (b.xx == x) & (b.yy < gy + 11), B[4])
    # hall windows and the big wheel over the gate
    for x in (114, 125, 163, 174):
        window(b, P, x, 141, 7, 20, night)
    gear(b, P, 147, 131, 7, teeth=10)
    # dormers on the roof
    for x in (124, 164):
        b.fill(b.poly([(x - 1, 112), (x + 4, 106), (x + 9, 112)]), P['roof'][3])
        b.fill(b.rect(x, 112, x + 9, 119), B[3])
        b.fill(b.rect(x + 2, 113, x + 7, 118), G[1]); b.fill(b.rect(x + 4, 113, x + 5, 118), B[4])
    chimney(b, P, 117, 76, 100)
    chimney(b, P, 170, 84, 100, w=5)

    # ---- tower ---------------------------------------------------------------
    tx0, tx1, ty = 184, 210, 66
    brick(b, b.rect(tx0, ty, tx1, BASE), P, seed=4, lit_from=tx0 - 6)
    for y in range(ty, BASE, 6):
        b.fill(b.rect(tx0, y, tx0 + 3, y + 3), S[2]); b.fill(b.rect(tx1 - 3, y + 3, tx1, y + 6), S[1])
    brick(b, b.rect(tx0 - 1, BASE - 8, tx1 + 1, BASE), P, seed=5, key='stone', bw=9, bh=3)
    # platform and battlement
    b.fill(b.rect(tx0 - 3, ty - 4, tx1 + 3, ty), S[2]); b.fill(b.rect(tx0 - 3, ty - 4, tx1 + 3, ty - 3), S[0])
    b.fill(b.rect(tx0 - 3, ty - 1, tx1 + 3, ty), S[4])
    for x in range(tx0 - 3, tx1 + 3, 6):
        b.fill(b.rect(x, ty - 8, x + 4, ty - 4), S[2]); b.fill(b.rect(x, ty - 8, x + 4, ty - 7), S[0]); b.fill(b.rect(x + 3, ty - 8, x + 4, ty - 4), S[0])
    # the crown on top
    crown(b, P, 197, ty - 8, 30, 24)
    # clock wheel, windows, door
    b.fill(b.ellipse(197, 92, 11.5), S[3]); b.fill(b.ellipse(197, 92, 10.3), P['dark'])
    gear(b, P, 197, 92, 7, teeth=12, phase=0.3)
    window(b, P, 193, 112, 8, 16, night)
    window(b, P, 193, 136, 8, 14, night)
    door = b.rect(193, 158, 202, BASE) | (b.ellipse(197, 158, 4.6) & (b.yy <= 158))
    b.fill(door, P['wood'][3]); b.fill(b.rect(194, 158, 201, BASE), P['wood'][2]); b.fill(b.rect(197, 156, 198, BASE), P['wood'][3])
    b.px(199, 166, K[1])
    b.fill(b.rect(tx0, 106, tx1, 108), K[3]); b.fill(b.rect(tx0, 106, tx1, 107), K[1])
    b.fill(b.rect(tx0, 130, tx1, 132), K[3]); b.fill(b.rect(tx0, 130, tx1, 131), K[1])

    # ---- east wing with the half wheel --------------------------------------
    ex0, ex1, ey = 210, 234, 148
    brick(b, b.rect(ex0, ey, ex1, BASE), P, seed=6, key='stone', bw=8, bh=4, lit_from=ex0 - 10)
    roof = b.poly([(ex0, ey), (ex0, ey - 9), (ex1 - 3, ey - 9), (ex1 + 3, ey)])
    slate(b, roof, P)
    b.fill(b.rect(ex0, ey, ex1 + 3, ey + 1), K[1])
    window(b, P, 216, 155, 7, 12, night)
    gear(b, P, 236, 166, 9, teeth=12, phase=0.1)

    # pipes across the front
    b.fill(b.rect(62, 146, 64, BASE), K[3]); b.fill(b.rect(63, 146, 64, BASE), K[1])
    b.fill(b.rect(104, 126, 108, 128), K[3]); b.fill(b.rect(104, 126, 106, 146), K[3]); b.fill(b.rect(105, 126, 106, 146), K[1])

    # rim light from the sun on every right-hand edge, cool shade on the left
    rim = b.alpha & ~b.shift(b.alpha, -1, 0)
    b.a[rim] = blend(b.a[rim], P['sun'][1], 0.6)
    lee = b.alpha & ~b.shift(b.alpha, 1, 0)
    b.a[lee] = blend(b.a[lee], P['dark'], 0.45)

    # smoke goes behind the buildings, so draw it on the scene first
    smoke(c, P, 120, 74, 5)
    smoke(c, P, 172, 82, 6, n=8, drift=-2.2)
    birds(c, P)
    c.paste(b)

    # ---- things in front -----------------------------------------------------
    obelisk(c, P, 256, int(g[256]) + 1, 56, night)
    path = c.poly([(140, BASE), (155, BASE), (176, 196), (214, 222), (262, 252), (222, 252), (176, 226), (146, 198)])
    c.ramp(path, P['path'], (c.yy - BASE) / 80.0 + (c.bayer - 0.5) * 0.3, soft=0.6)
    c.fill(path & ~c.shift(path, 1, 0), P['path'][2])
    ry = rails(c, P, g, None)
    for x, y in ((132, BASE + 2), (164, BASE + 4), (146, 198), (232, 232)):
        lantern(c, P, x, y)
    cx, cy = train(c, P, 28, int(ry[40]) + 3)
    smoke(c, P, cx, cy, 12, n=5, drift=-3.2, rise=3.4, size=0.55)
    # warm light: the gate on the path, the lanterns, the windows at night
    halo(c, 147, BASE + 6, 30 if night else 22, P['glow'][2], only=c.below(g))
    for x, y in ((135, BASE - 7), (167, BASE - 5), (149, 189), (235, 223)):
        halo(c, x, y, 13 if night else 8, P['glow'][2])
    # low stone wall along the terrace
    for x0, x1 in ((58, 130), (166, 242)):
        wall = c.rect(x0, BASE - 1, x1, BASE + 4) & c.below(g - 2)
        brick(c, wall, P, seed=9, key='stone', bw=6, bh=3)
        c.fill(c.rect(x0, BASE - 1, x1, BASE) & wall, S[0])
