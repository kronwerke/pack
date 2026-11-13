"""Shot 4 of the trailer: the five stages, each on its own piece of ground, two seconds each.

Every card has the same build: the stage's number and name on the left in its colour, and on
the right an island that shows what the stage is about, with the obelisk on it, one tier
taller each time. card(stage, m) paints frame m (0..23) of stage 0..4; the islands' still
parts are painted once.

    I   Steinwerk    quarry and crane, the mill with its wheel, a drill at the cobblestone generator
    II  Messingwerk  brick workshop, brass wheels, a belt, the Nether portal, a mana pool
    III Stahlwerk    the blast furnace that never sleeps, a pour of steel, the steam hammer
    IV  Sternwerk    end stone, obsidian pillars with crystals, the dragon before the moon
    V   Chaoswerk    black shards, the chaos crystal, lightning, the guardian behind it all

Behind every island stands its own sky (backdrop): bands of colour, clouds, a sea of cloud, far
islets, fading into the night toward the writing.
"""
import math

import numpy as np

import font
from px import Canvas, cols, hexc, noise1d, noise2d

W, H = 480, 270
NIGHT = hexc('#0d0b10')
OUTL = hexc('#15121f')
CREAM = hexc('#f2ede3')
STAGE = cols('#a8b596', '#e5b451', '#8bb6dc', '#bb98f4', '#f06579')
NAMES = ('STEINWERK', 'MESSINGWERK', 'STAHLWERK', 'STERNWERK', 'CHAOSWERK')
GOALS = ('FUNDAMENT DES KRONWERKS', 'DIE MESSINGMASCHINE', 'DER OFEN SCHLÄFT NIE', 'LICHT DES DRACHEN', 'DER CHAOSWÄCHTER')
ROMAN = ('I', 'II', 'III', 'IV', 'V')
STONE = cols('#8a7f97', '#655a73', '#4b4159', '#3a3046', '#2d2538', '#231d2c')
SLATE = cols('#5a5270', '#443c58', '#332c45', '#262034', '#1c1727')
BRASS = cols('#fff3c4', '#f7dc86', '#e5b451', '#b98530', '#8a5a24', '#5c3a1e')
WOOD = cols('#b8865a', '#8d5a3b', '#6b4030', '#4a2c26', '#33201f', '#241718')
MOSS = cols('#c6dc6e', '#8fba4f', '#5d9443', '#3b6f3d', '#285238', '#1c3a31')
EARTH = cols('#6b5247', '#54403a', '#3f2f30', '#2e2228', '#211920')
BRICK = cols('#c9705a', '#a8523f', '#86392f', '#622a2a', '#451f24')
GLOW = cols('#fff1b8', '#ffd27a', '#ffa64d', '#d9662c', '#8f3a22')
CYAN = cols('#e8fbff', '#9fe9f5', '#5fd3e6', '#2f9fc0', '#1c6388')
ENDST = cols('#f1efb5', '#dcd98f', '#b9b673', '#8e8c5c', '#63613f')
OBSID = cols('#4a3a6b', '#33274d', '#221a36', '#150f24')
PURPLE = cols('#f0d5ff', '#d7a8ff', '#bb98f4', '#8a5fd0', '#5a3a96')
CHAOS = cols('#ffd0dc', '#ff8fa8', '#f06579', '#b0344f', '#6e1f38', '#3a1226')

IX, IY = 332, 170              # the middle of an island's top
_STATIC = {}


def rng(seed):
    return np.random.default_rng(seed)


def island_base(c, top_cols, earth, seed, left=212, right=452):
    """A floating piece of ground: flat on top with a coloured turf, ragged rock below."""
    x = np.arange(W)
    span = (x >= left) & (x <= right)
    t = np.clip((x - left) / float(right - left), 0, 1)
    belly = np.sin(t * math.pi) ** 0.55
    under = IY + 5 + belly * (30 + 16 * noise2d(W, 1, seed, period=14, octaves=3)[0]) + 3 * noise2d(W, 1, seed + 1, period=5, octaves=1)[0]
    top = np.round(IY + noise2d(W, 1, seed + 2, period=30, octaves=2)[0] * 3 - 1.5)
    m = (c.yy >= top[None, :]) & (c.yy <= under[None, :]) & span[None, :]
    depth = (c.yy - top[None, :]) / np.maximum(under - top, 1)[None, :]
    n = noise2d(W, H, seed + 3, period=9, octaves=2)
    c.ramp(m, earth, np.clip(depth * 1.1 + (n - 0.5) * 0.25, 0, 1), soft=0.3)
    g = rng(seed + 4)
    for _ in range(9):
        sx, sy = int(g.integers(left + 14, right - 14)), int(g.integers(IY + 8, IY + 24))
        st = c.ellipse(sx, sy, g.integers(3, 7), g.integers(2, 4)) & m
        c.fill(st, tuple(int(v * 0.8) for v in earth[1]))
        c.fill(st & ~c.shift(st, 0, 1), earth[0])
    c.fill(m & (c.yy <= top[None, :] + 2), top_cols[2])
    c.fill(m & (c.yy == top[None, :]), top_cols[1])
    c.fill(m & (c.yy == top[None, :]) & (n > 0.55), top_cols[0])
    for rx in range(left + 18, right - 10, 31):
        ry = int(under[rx])
        ln = int(g.integers(5, 13))
        xx = rx
        for k in range(ln):
            if g.random() < 0.35:
                xx += int(g.integers(-1, 2))
            c.px(xx, ry + k, earth[-1])
    c.fill(c.edge(m, inner=False) & (c.yy > top[None, :]), OUTL)
    return top


def obelisk(c, x, base, tier, glow):
    """The obelisk as it stands after this many stages: taller each time, and from the third
    with a brass band, from the fourth with pylons, at the fifth with a crown of light."""
    h = 34 + tier * 9
    for k, (hw, y0, y1) in enumerate(((11, base - 3, base + 1), (8, base - 6, base - 3))):
        st = c.rect(x - hw, y0, x + hw + 1, y1)
        c.fill(st, SLATE[2])
        c.fill(c.rect(x - hw, y0, x + hw + 1, y0 + 1), SLATE[0])
        c.fill(c.edge(st, inner=False), OUTL)
    top = base - 6 - h
    body = c.poly([(x - 5, base - 6), (x - 4, top + 8), (x, top), (x + 4, top + 8), (x + 5, base - 6)])
    c.ramp(body, [SLATE[0], SLATE[1], SLATE[2], SLATE[3]], np.clip((c.xx - x + 5) / 10.0, 0, 1), soft=0.25)
    for y in range(base - 14, top + 10, -9):
        c.fill(body & (c.yy == y), SLATE[4])
    if tier >= 2:
        c.fill(body & (c.yy >= top + 8) & (c.yy < top + 10), BRASS[2])
    c.fill(body & (c.yy < top + 4), BRASS[1])
    c.fill(c.edge(body, inner=False), OUTL)
    if tier >= 3:
        for sx in (-17, 17):
            post = c.rect(x + sx - 1, base - 16, x + sx + 1, base + 1)
            c.fill(post, SLATE[2])
            c.fill(c.edge(post, inner=False) & (c.yy <= base), OUTL)
            c.fill(c.rect(x + sx - 1, base - 19, x + sx + 1, base - 16), GLOW[1])
    return top


def crystal(a, x, y, m, col, bright, tier):
    """The crystal over the tip with its beam, on the finished array (it bobs)."""
    cy = y - 7 + int(round(math.sin(m / 4.0) * 1))
    yy, xx = np.mgrid[0:H, 0:W]
    dia = (np.abs(xx - x) / 3.0 + np.abs(yy - cy) / 5.0) <= 1.0
    beam = (np.abs(xx - x) <= (1 if tier >= 3 else 0)) & (yy < cy - 5)
    reach = 60 + tier * 18
    fade = np.clip((cy - 5 - yy) / float(reach), 0, 1)
    a[beam & (fade < 0.55)] = bright
    a[beam & (fade >= 0.55) & (fade < 1) & (((yy + m) % 3) != 0) & (fade < 0.8)] = col
    a[beam & (fade >= 0.8) & (fade < 1) & (((yy + m) % 3) == 0)] = col
    a[dia] = col
    a[dia & (xx < x) & (yy <= cy)] = bright
    if tier >= 4:
        for k in range(6):
            ang = m / 5.0 + k * math.pi / 3
            a[int(cy + math.sin(ang) * 3), int(x + math.cos(ang) * 9)] = bright


def planks(c, mask, seed, width=4):
    g = rng(seed)
    lo = int(c.xx[mask].min()) if mask.any() else 0
    idx = (c.xx - lo) // width
    tone = g.integers(0, 3, 200)
    for i in np.unique(idx[mask]):
        pm = mask & (idx == i)
        c.fill(pm, [WOOD[2], WOOD[3], WOOD[2]][int(tone[int(i) % 200])])
        c.fill(pm & (((c.xx - lo) % width) == width - 1), WOOD[4])


def bricks(c, mask, R, seed, row=3, width=6):
    ys = c.yy[mask]
    if ys.size == 0:
        return
    y0 = int(ys.min())
    r = (c.yy - y0) // row
    shift = np.where(r % 2 == 0, 0, width // 2)
    key = (r * 71 + ((c.xx + shift) // width) * 29) % 499
    tone = rng(seed).integers(0, 10, 499)[key]
    c.fill(mask, R[2])
    c.fill(mask & (tone < 3), R[1])
    c.fill(mask & (tone >= 8), R[3])
    c.fill(mask & ((((c.yy - y0) % row) == row - 1) | (((c.xx + shift) % width) == width - 1)), R[4])


def grass(c, x0, x1, y, seed, R=MOSS, tall=3):
    g = rng(seed)
    for x in range(x0, x1):
        h = int(g.integers(0, tall + 1))
        if g.random() < 0.4:
            continue
        for k in range(h):
            c.px(x, y - 1 - k, R[3] if k < h - 1 else R[1])


def wheel_frame(a, cx, cy, r, m, spokes=8, R=WOOD, speed=0.12):
    """A water wheel or flywheel drawn straight into the array at frame m."""
    yy, xx = np.mgrid[0:H, 0:W]
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    ang = np.arctan2(yy - cy, xx - cx) - m * speed
    rim = (d <= r) & (d >= r - 2.2)
    sp = (np.abs(np.sin(ang * spokes / 2.0)) < 0.16) & (d < r - 1.5) & (d > 2)
    hub = d <= 2.4
    a[rim | sp] = R[2]
    a[rim & (yy < cy) & (d > r - 1.2)] = R[0]
    a[hub] = R[4]
    ring = (d <= r + 1) & (d > r)
    a[ring] = OUTL
    # paddles
    for k in range(spokes):
        an = m * speed + k * 2 * math.pi / spokes
        px_, py_ = cx + math.cos(an) * (r + 1.5), cy + math.sin(an) * (r + 1.5)
        a[int(round(py_)) - 1:int(round(py_)) + 1, int(round(px_)) - 1:int(round(px_)) + 1] = R[1]


def gear_frame(a, cx, cy, r, teeth, m, R=BRASS, speed=0.1):
    yy, xx = np.mgrid[0:H, 0:W]
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    ang = np.arctan2(yy - cy, xx - cx) - m * speed
    step = 2 * math.pi / teeth
    off = np.abs(((ang / step + 0.5) % 1.0) - 0.5)
    tip = r * 0.78 + (r - r * 0.78) * np.clip((0.3 - off) / 0.14, 0, 1)
    g = (d <= tip) & (d >= r * 0.3)
    lit = np.clip(0.5 - ((xx - cx) * 0.6 + (yy - cy) * 0.8) / (2.2 * r), 0, 1)
    a[g] = R[3]
    a[g & (lit > 0.45)] = R[2]
    a[g & (lit > 0.7)] = R[1]
    hole = (d < r * 0.62) & (d > r * 0.42) & (np.abs(np.sin(ang * 2)) > 0.35)
    a[g & hole] = R[5]
    p = np.pad(g, 1)
    a[~g & (p[:-2, 1:-1] | p[2:, 1:-1] | p[1:-1, :-2] | p[1:-1, 2:]) & (d > r * 0.5)] = OUTL


def smoke(a, x, y, m, n=7, rise=30, drift=10, cols_=('#655a73', '#4b4159'), period=40.0):
    for i in range(n):
        life = ((m / period) + i / float(n)) % 1.0
        px_ = int(x + life * drift + math.sin(m / 9.0 + i * 2.1) * (1 + 3 * life))
        py_ = int(y - life * rise)
        s = 2 if life < 0.2 or life > 0.75 else 3
        if life < 0.85 and 2 < py_ < H - 4 and 2 < px_ < W - 4:
            a[py_:py_ + s, px_:px_ + s] = hexc(cols_[i % 2])


# ======================================================================================
# the five islands: still parts once, moving parts per frame

def pine(c, x, base, h, seed=0):
    """A small pine: three tiers of dark green, lit on the left."""
    c.fill(c.rect(x, base - 4, x + 2, base + 1), WOOD[4])
    for k in range(3):
        w = 4 + (2 - k) * 3 - (h < 20)
        y1 = base - 3 - k * (h // 4)
        tri = c.poly([(x + 0.5, y1 - h // 2.2), (x - w, y1), (x + w + 1, y1)])
        c.fill(tri, MOSS[4])
        c.fill(tri & (c.xx <= x) & ~c.shift(tri, 1, 1), MOSS[3])
        c.fill(tri & ~c.shift(tri, 0, 1) & (c.xx < x), MOSS[2])
        c.fill(c.edge(tri, inner=False), OUTL)


def lamp(c, x, base, h=12):
    c.fill(c.rect(x, base - h, x + 1, base + 1), SLATE[1])
    c.fill(c.rect(x - 1, base - h - 3, x + 2, base - h), GLOW[1])
    c.px(x, base - h - 2, GLOW[0])
    c.fill(c.rect(x - 1, base - h - 4, x + 2, base - h - 3), BRASS[3])


def stage1_static(c):
    top = island_base(c, MOSS[1:4], [EARTH[1], EARTH[2], EARTH[3], EARTH[4]], 101)
    # the quarry on the right: a cliff cut in steps, a ladder, a scaffold, a crane with a block
    steps = ((384, 452, IY - 30), (398, 452, IY - 52), (414, 452, IY - 72), (432, 452, IY - 86))
    cliff = c.none()
    for k, (x0, x1, y0) in enumerate(steps):
        y1 = IY + 1 if k == 0 else steps[k - 1][2]
        blk = c.rect(x0, y0, x1, y1)
        bricks(c, blk, [STONE[0], STONE[1], STONE[2], STONE[3], STONE[4]], 110 + k, row=6, width=10)
        c.fill(c.rect(x0, y0, x1, y0 + 1), STONE[0])
        c.fill(c.rect(x0, y0 + 1, x0 + 1, y1), STONE[1])
        cliff |= blk
    # fresh cuts: lighter squares where blocks were taken, drill holes
    for bx_, by_ in ((402, IY - 46), (420, IY - 64), (388, IY - 20), (440, IY - 80)):
        c.fill(c.rect(bx_, by_, bx_ + 7, by_ + 6), STONE[0])
        c.fill(c.rect(bx_, by_ + 5, bx_ + 7, by_ + 6), STONE[2])
    c.fill(c.edge(cliff, inner=False) & (c.yy <= IY), OUTL)
    for y in range(IY - 30, IY, 3):                                   # the ladder
        c.fill(c.rect(378, y, 384, y + 1), WOOD[1])
    c.fill(c.rect(378, IY - 32, 379, IY + 1) | c.rect(383, IY - 32, 384, IY + 1), WOOD[3])
    moss = cliff & ~c.shift(cliff, 0, 1) & (noise2d(W, H, 115, period=5, octaves=1) > 0.45)
    c.fill(moss, MOSS[2])
    c.fill(c.shift(moss, 0, 1) & cliff & (noise2d(W, H, 116, period=3, octaves=1) > 0.4), MOSS[3])
    crane = c.line(444, IY - 86, 444, IY - 118, width=3) | c.line(444, IY - 117, 410, IY - 108, width=2) | c.line(444, IY - 100, 432, IY - 112, width=1)
    c.fill(crane, WOOD[2])
    c.fill(crane & ~c.shift(crane, 0, 1), WOOD[0])
    c.fill(c.edge(crane, inner=False), OUTL)
    # cobblestone in stacks by the cliff's foot
    for px_, n_ in ((350, 5), (332, 3)):
        for j in range(n_):
            for i in range(n_ - j):
                bx_, by_ = px_ + i * 6 + j * 3, IY - 5 - j * 5
                c.fill(c.rect(bx_, by_, bx_ + 6, by_ + 5), STONE[2 + (i + j) % 2])
                c.fill(c.rect(bx_, by_, bx_ + 6, by_ + 1), STONE[0])
                c.fill(c.rect(bx_ + 5, by_, bx_ + 6, by_ + 5), STONE[4])
                c.px(bx_ + 2, by_ + 2, STONE[4])
    c.fill(c.line(346, IY, 338, IY - 18, width=1), WOOD[1])                       # a pickaxe against the pile
    c.fill(c.line(333, IY - 16, 343, IY - 19, width=2), STONE[0])
    # the mill: a stone house with a mossy roof, its wheel in a race of water
    house = c.rect(222, IY - 34, 262, IY + 1)
    bricks(c, house, [STONE[0], STONE[1], STONE[2], STONE[3], STONE[4]], 120, row=5, width=9)
    upper = c.rect(222, IY - 34, 262, IY - 22)
    planks(c, upper, 121, width=5)
    roof = c.poly([(216, IY - 34), (228, IY - 54), (258, IY - 54), (268, IY - 34)])
    c.fill(roof, hexc('#553a56'))
    for ry in range(IY - 54, IY - 34, 4):
        c.fill(roof & (c.yy == ry + 3), hexc('#3f2b43'))
        c.fill(roof & (c.yy == ry) & ((c.xx + ry) % 6 < 4), hexc('#8d6a86'))
    rm = roof & (noise2d(W, H, 122, period=8, octaves=2) > 0.6)
    c.fill(rm, MOSS[3])
    c.fill(rm & ~c.shift(rm, 0, 1), MOSS[1])
    chim = c.rect(250, IY - 64, 256, IY - 54)
    bricks(c, chim, [STONE[0], STONE[1], STONE[2], STONE[3], STONE[4]], 123, row=3, width=5)
    c.fill(c.rect(232, IY - 16, 242, IY + 1), OUTL)
    c.fill(c.rect(233, IY - 15, 236, IY + 1), GLOW[2])
    c.fill(c.rect(233, IY - 15, 234, IY + 1), GLOW[1])
    c.fill(c.rect(248, IY - 30, 256, IY - 24), GLOW[1])
    c.fill(c.rect(251, IY - 30, 252, IY - 24), WOOD[4])
    c.fill(c.edge(house | roof | chim, inner=False) & (c.yy <= IY), OUTL)
    race = c.rect(262, IY - 4, 304, IY + 1)
    c.fill(race, CYAN[4])
    c.fill(c.rect(262, IY - 4, 304, IY - 3), CYAN[2])
    c.fill(c.rect(262, IY - 2, 264, IY + 1) | c.rect(302, IY - 2, 304, IY + 1), STONE[2])
    # the cobblestone generator: lava left, water right, the stone between them, a drill over it
    gen = c.rect(304, IY - 14, 330, IY + 1)
    c.fill(gen, STONE[3])
    c.fill(c.rect(304, IY - 14, 330, IY - 13), STONE[1])
    c.fill(c.rect(306, IY - 11, 312, IY - 2), GLOW[3])
    c.fill(c.rect(306, IY - 11, 312, IY - 9), GLOW[1])
    c.fill(c.rect(322, IY - 11, 328, IY - 2), CYAN[3])
    c.fill(c.rect(322, IY - 11, 328, IY - 10), CYAN[1])
    c.fill(c.rect(314, IY - 11, 320, IY - 2), STONE[1])
    c.fill(c.edge(gen, inner=False) & (c.yy <= IY), OUTL)
    post = c.rect(316, IY - 30, 318, IY - 14) | c.rect(310, IY - 31, 324, IY - 29)
    c.fill(post, WOOD[2])
    pine(c, 214 + 4, IY, 26)
    pine(c, 298, IY, 20)
    lamp(c, 272, IY)
    grass(c, 214, 450, IY, 130)
    for fx, col in ((268, '#f2ede3'), (294, '#f06579'), (346, '#f2ede3'), (376, '#e5b451'), (226, '#bb98f4')):
        c.px(fx, IY - 4, hexc(col))


def stage1_move(a, m):
    wheel_frame(a, 282, IY - 18, 16, m, 8, WOOD, 0.14)
    for k in range(8):                                                  # water running off the wheel
        y = IY - 12 + ((m + k * 3) % 11)
        if y < IY - 2:
            a[y, 297 + (k % 3)] = CYAN[1]
    for k in range(4):                                                  # glitter on the race
        a[IY - 4, 264 + ((m * 2 + k * 11) % 38)] = CYAN[0]
    # the drill: a bit that turns over the stone, and a block that hops onto the pile
    bx = 316
    a[IY - 21:IY - 14, bx - 1:bx + 3] = STONE[1]
    a[IY - 14, bx - 1 + ((m // 2) % 4)] = BRASS[1]
    a[IY - 17, bx - 1 + ((m // 2 + 2) % 4)] = STONE[4]
    t = m % 12
    if t < 8:
        x = 320 + t * 5
        y = IY - 14 - int(math.sin(t / 8.0 * math.pi) * 14)
        a[y:y + 5, x:x + 5] = STONE[2]
        a[y, x:x + 5] = STONE[0]
    # the crane lifts its block out of the quarry
    lift = int((m % 24) / 23.0 * 18)
    sw = int(round(math.sin(m / 4.0) * 1.5))
    a[IY - 107:IY - 78 - lift, 411 + sw] = WOOD[4]
    a[IY - 78 - lift:IY - 71 - lift, 407 + sw:416 + sw] = STONE[1]
    a[IY - 78 - lift, 407 + sw:416 + sw] = STONE[0]
    a[IY - 72 - lift, 407 + sw:416 + sw] = STONE[3]
    smoke(a, 252, IY - 66, m, n=5, rise=22, drift=7)
    # the obelisk's first stone: only the foot stands yet, the crystal waits over it
    for k, (hw, y0, y1) in enumerate(((11, IY - 3, IY + 1), (8, IY - 6, IY - 3))):
        a[y0:y1, 364 - hw:364 + hw + 1] = SLATE[2]
        a[y0, 364 - hw:364 + hw + 1] = SLATE[0]
    a[IY - 16:IY - 6, 364 - 5:364 + 6] = SLATE[2]
    a[IY - 16:IY - 6, 364 - 5] = SLATE[0]
    a[IY - 17, 364 - 5:364 + 6] = OUTL
    crystal(a, 364, IY - 22, m, STAGE[0], hexc('#e8f0d8'), 0)


def stage2_static(c):
    top = island_base(c, MOSS[1:4], [EARTH[1], EARTH[2], EARTH[3], EARTH[4]], 201)
    # the brass works: a brick hall with tall arched windows, a big wheel on its gable
    hall = c.rect(222, IY - 48, 296, IY + 1)
    bricks(c, hall, BRICK, 210, row=4, width=8)
    c.fill(c.rect(222, IY - 6, 296, IY + 1), STONE[3])
    c.fill(c.rect(222, IY - 6, 296, IY - 5), STONE[1])
    roof = c.poly([(216, IY - 48), (228, IY - 66), (290, IY - 66), (302, IY - 48)])
    c.fill(roof, hexc('#3f2b43'))
    for ry in range(IY - 66, IY - 48, 4):
        c.fill(roof & (c.yy == ry + 3), hexc('#2c1f31'))
        c.fill(roof & (c.yy == ry) & ((c.xx + ry) % 7 < 5), hexc('#6f4f6c'))
    c.fill(c.rect(216, IY - 49, 302, IY - 47), BRASS[3])
    c.fill(c.rect(216, IY - 49, 302, IY - 48), BRASS[1])
    for wx in (230, 244, 274, 284):
        win = c.rect(wx, IY - 38, wx + 6, IY - 20) | c.ellipse(wx + 2.5, IY - 38, 3, 3)
        c.fill(win & hall, GLOW[1])
        c.fill(win & hall & (c.yy > IY - 28), GLOW[2])
        c.fill(c.rect(wx + 2, IY - 40, wx + 3, IY - 20) | c.rect(wx, IY - 30, wx + 6, IY - 29), BRICK[4])
    door = c.rect(254, IY - 20, 268, IY + 1) | c.ellipse(261, IY - 20, 7, 6)
    c.fill(door & hall, GLOW[2])
    c.fill(door & hall & (np.abs(c.xx - 261) > 3), GLOW[3])
    c.fill(c.edge(door & hall, inner=True), BRASS[3])
    chim = c.poly([(282, IY - 66), (283, IY - 96), (289, IY - 96), (290, IY - 66)])
    bricks(c, chim, BRICK, 211)
    c.fill(c.rect(282, IY - 98, 291, IY - 96), BRASS[3])
    c.fill(c.rect(282, IY - 98, 291, IY - 97), BRASS[1])
    tank = c.rect(302, IY - 26, 316, IY + 1) | c.ellipse(309, IY - 26, 7, 4)
    c.ramp(tank, [BRASS[1], BRASS[2], BRASS[3], BRASS[4]], np.clip((c.xx - 302) / 14.0, 0, 1), soft=0.25)
    for ty in (IY - 20, IY - 10):
        c.fill(tank & (c.yy == ty), BRASS[5])
    c.fill(c.line(296, IY - 30, 304, IY - 30) | c.line(296, IY - 30, 296, IY - 24), BRASS[2])
    c.fill(c.edge(hall | roof | chim | tank, inner=False) & (c.yy <= IY), OUTL)
    # the belt on trestles, from the hall to a crate
    c.fill(c.rect(318, IY - 13, 372, IY - 10), SLATE[3])
    c.fill(c.rect(318, IY - 13, 372, IY - 12), SLATE[1])
    for tx in (324, 346, 368):
        c.fill(c.rect(tx, IY - 10, tx + 2, IY + 1), WOOD[3])
    crate = c.rect(372, IY - 9, 384, IY + 1)
    planks(c, crate, 212, width=4)
    c.fill(c.rect(372, IY - 9, 384, IY - 8), WOOD[0])
    c.fill(c.edge(crate, inner=False) & (c.yy <= IY), OUTL)
    # the Nether portal: an obsidian frame, netherrack creeping out at its foot
    px0 = 408
    full = c.rect(px0, IY - 56, px0 + 38, IY + 1)
    frame = full & ~c.rect(px0 + 6, IY - 50, px0 + 32, IY - 4)
    c.fill(frame, OBSID[2])
    c.fill(frame & (noise2d(W, H, 213, period=4, octaves=1) > 0.62), OBSID[0])
    c.fill(frame & ~c.shift(frame, 0, 1), OBSID[0])
    c.fill(c.edge(full, inner=False) & (c.yy <= IY), OUTL)
    for nx in range(398, 452, 3):
        if (nx * 7) % 5 < 2:
            c.fill(c.rect(nx, IY, nx + 3, IY + 2), CHAOS[4])
    # a mana pool with its flowers
    pool = c.rect(388, IY - 6, 406, IY + 1)
    c.fill(pool, STONE[1])
    c.fill(c.rect(390, IY - 5, 404, IY - 1), CYAN[2])
    c.fill(c.rect(390, IY - 5, 404, IY - 4), CYAN[0])
    c.fill(c.edge(pool, inner=False) & (c.yy <= IY), OUTL)
    for fx, col in ((386, '#f06579'), (320, '#bb98f4'), (452 - 4, '#8bb6dc'), (216 + 2, '#f2ede3')):
        c.fill(c.line(fx, IY, fx, IY - 6), MOSS[3])
        c.fill(c.rect(fx - 1, IY - 8, fx + 2, IY - 6), hexc(col))
    lamp(c, 334, IY - 0)
    obelisk(c, 352, IY, 1, CYAN[2])
    grass(c, 214, 450, IY, 230)


def stage2_move(a, m):
    gear_frame(a, 259, IY - 58, 13, 10, m, BRASS, 0.12)
    gear_frame(a, 240, IY - 70, 7, 6, -m, BRASS, 0.20)
    for k in range(4):                                                  # ingots ride the belt
        x = 320 + ((m * 2 + k * 14) % 52)
        a[IY - 16:IY - 13, x:x + 4] = BRASS[2]
        a[IY - 16, x:x + 4] = BRASS[0]
    yy, xx = np.mgrid[0:H, 0:W]
    inside = (xx >= 414) & (xx < 440) & (yy >= IY - 50) & (yy < IY - 4)
    sw = np.sin(xx * 0.9 + yy * 0.6 + m * 0.7) + np.sin(yy * 0.5 - m * 0.4)
    a[inside] = PURPLE[4]
    a[inside & (sw > 0.2)] = PURPLE[3]
    a[inside & (sw > 1.2)] = PURPLE[1]
    for k in range(7):                                                  # motes drift out of the portal
        life = ((m / 14.0) + k / 7.0) % 1.0
        a[int(IY - 28 - life * 30 + math.sin(k) * 10), int(427 + math.sin(m / 3.0 + k * 2) * (10 + life * 10))] = PURPLE[1]
    for k in range(3):
        life = ((m / 10.0) + k / 3.0) % 1.0
        a[int(IY - 7 - life * 10), 392 + k * 5] = CYAN[0]
    if (m // 6) % 2 == 0:                                               # the tank lets off steam
        for k in range(3):
            a[IY - 34 - k * 2 - (m % 6), 309 + (k % 2) * 2] = hexc('#c9c6d4')
    smoke(a, 285, IY - 100, m, n=7, rise=30, drift=12, cols_=('#8a7f97', '#655a73'))
    crystal(a, 352, IY - 6 - 43, m, STAGE[1], BRASS[0], 1)


STEEL = cols('#e6e3ee', '#c9c6d4', '#8a8799', '#5c586b', '#3d3a4a', '#2a2733')
PURPUR = cols('#c79ad0', '#a57aa5', '#7d5a80', '#5a3f62', '#3c2a45')


def stage3_static(c):
    dark = [hexc('#57505c'), hexc('#3f3844'), hexc('#2a242f')]
    top = island_base(c, dark, [EARTH[2], EARTH[3], EARTH[4], hexc('#1a1319')], 301)
    # the rolling hall behind: a saw roof with skylights, a dark wall with tall windows
    hall = c.rect(322, IY - 50, 402, IY + 1)
    c.fill(hall, hexc('#2c1a22'))
    bricks(c, hall & (c.yy > IY - 50), [BRICK[3], BRICK[4], hexc('#3a1a20'), hexc('#2c1418'), hexc('#1e0e12')], 305, row=4, width=8)
    for k in range(4):
        x0 = 322 + k * 20
        saw = c.poly([(x0, IY - 50), (x0, IY - 64), (x0 + 20, IY - 50)])
        c.fill(saw, SLATE[3])
        c.fill(saw & ~c.shift(saw, 1, -1) & (c.xx > x0), SLATE[1])
        sky = c.rect(x0 + 1, IY - 61, x0 + 3, IY - 52)
        c.fill(sky, GLOW[2])
        c.fill(c.rect(x0 + 1, IY - 61, x0 + 3, IY - 58), GLOW[1])
        c.fill(c.edge(saw, inner=False) & (c.yy < IY - 49), OUTL)
    for wx in (336, 352, 368, 384):
        c.fill(c.rect(wx, IY - 40, wx + 6, IY - 18), GLOW[4])
        c.fill(c.rect(wx + 1, IY - 39, wx + 5, IY - 19), GLOW[3])
        c.fill(c.rect(wx + 1, IY - 30, wx + 5, IY - 19), hexc('#b3501f'))
        c.fill(c.rect(wx + 3, IY - 40, wx + 4, IY - 18) | c.rect(wx, IY - 29, wx + 6, IY - 28), hexc('#2c1418'))
    c.fill(c.edge(hall, inner=False) & (c.yy <= IY) & (c.yy >= IY - 50), OUTL)
    # the blast furnace: a tall brick tower banded with iron, a hopper on top, a glowing mouth
    fur = c.poly([(234, IY + 1), (239, IY - 64), (271, IY - 64), (276, IY + 1)])
    bricks(c, fur, [BRICK[1], BRICK[2], BRICK[3], BRICK[4], hexc('#2c1418')], 310)
    c.fill(fur & (c.xx > 266), BRICK[4])
    for by in (IY - 16, IY - 34, IY - 52):
        c.fill(fur & (c.yy >= by) & (c.yy < by + 2), STEEL[3])
        c.fill(fur & (c.yy == by), STEEL[2])
        c.fill(fur & (c.yy == by + 2), OUTL)
        for rx in range(238, 274, 6):
            c.px(rx, by + 1, STEEL[1])
    top_ring = c.rect(237, IY - 68, 274, IY - 64)
    c.fill(top_ring, STEEL[4])
    c.fill(c.rect(237, IY - 68, 274, IY - 67), STEEL[2])
    hop = c.poly([(244, IY - 68), (248, IY - 78), (263, IY - 78), (267, IY - 68)])
    c.fill(hop, STEEL[4])
    c.fill(hop & (c.xx < 252), STEEL[3])
    c.fill(c.rect(248, IY - 79, 264, IY - 78), STEEL[1])
    arch = c.ellipse(255, IY - 6, 10, 9) & (c.yy <= IY)
    c.fill(arch, hexc('#2c1418'))
    c.fill(c.ellipse(255, IY - 5, 8, 7) & (c.yy <= IY), GLOW[2])
    c.fill(c.ellipse(255, IY - 4, 5, 4) & (c.yy <= IY), GLOW[0])
    for ly in range(IY - 62, IY - 18, 4):                                # the ladder up the furnace
        c.fill(c.rect(240, ly, 245, ly + 1), STEEL[3])
    c.fill(c.rect(240, IY - 64, 241, IY - 18) | c.rect(244, IY - 64, 245, IY - 18), STEEL[4])
    c.fill(c.edge(fur | top_ring | hop, inner=False) & (c.yy <= IY), OUTL)
    # the hot blast stove: an iron cylinder with a dome, a pipe down from the furnace's top
    stove = c.rect(282, IY - 40, 296, IY + 1) | c.ellipse(288.5, IY - 40, 7, 6)
    c.ramp(stove, [STEEL[2], STEEL[3], STEEL[4], STEEL[5]], np.clip((c.xx - 282) / 14.0, 0, 1), soft=0.25)
    for ty in (IY - 30, IY - 18, IY - 6):
        c.fill(stove & (c.yy == ty), STEEL[5])
        for rx in (284, 288, 292):
            c.px(rx, ty - 1, STEEL[1])
    pipe = c.line(271, IY - 66, 288, IY - 48, width=3)
    c.fill(pipe, STEEL[3])
    c.fill(pipe & ~c.shift(pipe, 0, 1), STEEL[1])
    c.fill(c.edge(stove | pipe, inner=False) & (c.yy <= IY), OUTL)
    # the tall chimney and a second, shorter one, each with rings
    for cx_, ct in ((306, IY - 104), (317, IY - 76)):
        ch = c.poly([(cx_ - 4, IY + 1), (cx_ - 3, ct), (cx_ + 3, ct), (cx_ + 4, IY + 1)])
        bricks(c, ch, [BRICK[2], BRICK[3], BRICK[4], hexc('#3a1a20'), hexc('#2c1418')], 311 + cx_)
        c.fill(ch & (c.xx <= cx_ - 2), BRICK[2])
        c.fill(c.rect(cx_ - 4, ct - 2, cx_ + 5, ct), STEEL[3])
        c.fill(c.rect(cx_ - 4, ct - 2, cx_ + 5, ct - 1), STEEL[1])
        for ry in range(ct + 14, IY - 6, 22):
            c.fill(ch & (c.yy == ry), STEEL[4])
        c.fill(c.edge(ch, inner=False) & (c.yy <= IY), OUTL)
    c.fill(c.rect(305, IY - 100, 307, IY - 97), hexc('#f06579'))           # a warning light
    # the casting bed in front of the hall, its gantry of iron
    bed = c.rect(330, IY - 4, 394, IY + 1)
    c.fill(bed, STEEL[4])
    c.fill(c.rect(330, IY - 4, 394, IY - 3), STEEL[2])
    gantry = c.rect(326, IY - 44, 329, IY + 1) | c.rect(395, IY - 44, 398, IY + 1) | c.rect(323, IY - 47, 401, IY - 44)
    c.fill(gantry, STEEL[4])
    c.fill(c.rect(323, IY - 47, 401, IY - 46), STEEL[1])
    c.fill(c.rect(326, IY - 44, 327, IY + 1) | c.rect(395, IY - 44, 396, IY + 1), STEEL[2])
    for gx in range(331, 394, 6):                                        # the truss under the beam
        c.px(gx, IY - 43, STEEL[3])
        c.px(gx + 1, IY - 42, STEEL[3])
    c.fill(c.edge(gantry | bed, inner=False) & (c.yy <= IY), OUTL)
    # the steam hammer's frame, its anvil
    frame = c.rect(408, IY - 34, 410, IY + 1) | c.rect(422, IY - 34, 424, IY + 1) | c.rect(406, IY - 37, 426, IY - 34)
    c.fill(frame, STEEL[4])
    c.fill(c.rect(406, IY - 37, 426, IY - 36), STEEL[1])
    anvil = c.rect(411, IY - 5, 422, IY + 1)
    c.fill(anvil, STEEL[5])
    c.fill(c.rect(411, IY - 5, 422, IY - 4), STEEL[2])
    c.fill(c.edge(frame | anvil, inner=False) & (c.yy <= IY), OUTL)
    # ingots in a stack, a heap of coal, a lamp
    for j in range(3):
        for i in range(3 - j):
            bx_, by_ = 428 + i * 7 + j * 3, IY - 3 - j * 3
            c.fill(c.rect(bx_, by_, bx_ + 6, by_ + 3), STEEL[3 + (i + j) % 2])
            c.fill(c.rect(bx_, by_, bx_ + 6, by_ + 1), STEEL[0])
    heap = c.poly([(220 + 8, IY + 1), (229 + 4, IY - 6), (240, IY + 1)])
    c.fill(heap, hexc('#1c1727'))
    c.fill(heap & (noise2d(W, H, 320, period=3, octaves=1) > 0.6), hexc('#3a3046'))
    # the warm light of the mouth on the ground
    warm = (((c.xx - 255) / 26.0) ** 2 + ((c.yy - IY - 1) / 5.0) ** 2 <= 1) & (c.yy >= IY - 1) & c.alpha & ~arch
    c.fill(warm & (((c.xx + c.yy) % 2) == 0), GLOW[4])
    c.fill(warm & (np.abs(c.xx - 255) < 12) & (c.yy == IY), GLOW[3])
    obelisk(c, 220, IY, 2, CYAN[2])


def stage3_move(a, m):
    yy, xx = np.mgrid[0:H, 0:W]
    pulse = 0.5 + 0.5 * math.sin(m / 2.5)
    mouth = (((xx - 255) / 5.0) ** 2 + ((yy - (IY - 4)) / 4.0) ** 2 <= 1) & (yy <= IY)
    a[mouth] = GLOW[0] if pulse > 0.4 else GLOW[1]
    # the ladle runs along the gantry and pours into the moulds, one after the other
    lx = 338 + int((m / 23.0) * 44)
    a[IY - 44:IY - 34, lx] = STEEL[3]
    a[IY - 46:IY - 44, lx - 2:lx + 3] = STEEL[2]
    a[IY - 34:IY - 26, lx - 4:lx + 5] = STEEL[4]
    a[IY - 34:IY - 26, lx - 4] = STEEL[2]
    a[IY - 34, lx - 4:lx + 5] = GLOW[1]
    a[IY - 26:IY - 4, lx + 3] = GLOW[0]
    a[IY - 26:IY - 4:2, lx + 4] = GLOW[2]
    a[IY - 26:IY - 4:3, lx + 2] = GLOW[2]
    for k in range(9):
        mx = 332 + k * 7
        if mx < lx + 3:
            a[IY - 6:IY - 4, mx:mx + 5] = GLOW[1] if lx + 3 - mx < 9 else (GLOW[3] if lx + 3 - mx < 23 else STEEL[1])
    for k in range(8):                                                    # sparks where it lands
        life = ((m / 5.0) + k / 8.0) % 1.0
        sx = lx + 3 + int(math.cos(k * 2.2) * life * 10)
        sy = IY - 6 - int(math.sin(life * math.pi) * 9)
        a[sy, sx] = GLOW[0] if life < 0.5 else GLOW[2]
    # the steam hammer falls on every beat (six frames), sparks fly from the anvil
    t = m % 6
    lift = (0, 6, 12, 17, 20, 21)[t]                                      # 0 at the strike, then it rises
    hy = IY - 12 - lift
    a[IY - 34:hy, 415:418] = STEEL[2]
    a[IY - 34:hy, 415] = STEEL[0]
    a[hy:hy + 6, 412:421] = STEEL[3]
    a[hy, 412:421] = STEEL[1]
    a[hy + 5, 412:421] = STEEL[5]
    a[IY - 7:IY - 5, 413:420] = GLOW[1] if t < 3 else GLOW[2]            # the glowing bloom on the anvil
    if t < 2:
        for k in range(7):
            ang = k * 0.55 + 0.4
            r = 5 + t * 6
            a[int(IY - 7 - math.sin(ang) * r), int(416 + math.cos(ang) * r * 1.3)] = GLOW[0] if t == 0 else GLOW[2]
    smoke(a, 305, IY - 108, m, n=10, rise=44, drift=20, cols_=('#4b4159', '#3a3046'), period=36.0)
    smoke(a, 316, IY - 80, m + 9, n=6, rise=28, drift=12, cols_=('#655a73', '#4b4159'), period=30.0)
    if (m // 6) % 2 == 0:                                                 # the warning light blinks
        a[IY - 100:IY - 97, 305:307] = hexc('#ffd0dc')
    for k in range(7):                                                    # embers out of the furnace's top
        life = ((m / 12.0) + k / 7.0) % 1.0
        a[int(IY - 80 - life * 26), int(256 + math.sin(m / 3.0 + k * 1.9) * (3 + life * 8))] = GLOW[2] if k % 2 else GLOW[1]
    for k in range(3):                                                    # steam off the stove
        life = ((m / 9.0) + k / 3.0) % 1.0
        a[int(IY - 48 - life * 10), 288 + k * 2 - 2] = hexc('#c9c6d4')
    crystal(a, 220, IY - 6 - 52, m, STAGE[2], hexc('#e2f0fc'), 2)


def enderman(c, x, base, carries=None):
    """Tall, thin and black, two purple eyes; one of them carries a block of grass."""
    black = hexc('#0d0918')
    c.fill(c.rect(x, base - 9, x + 1, base + 1) | c.rect(x + 2, base - 9, x + 3, base + 1), black)
    c.fill(c.rect(x - 1, base - 16, x + 4, base - 9), black)
    c.fill(c.rect(x - 2, base - 15, x - 1, base - 6) | c.rect(x + 4, base - 15, x + 5, base - 6), black)
    c.fill(c.rect(x - 1, base - 21, x + 4, base - 16), black)
    c.px(x - 1, base - 19, PURPLE[1]); c.px(x, base - 19, PURPLE[0])
    c.px(x + 2, base - 19, PURPLE[0]); c.px(x + 3, base - 19, PURPLE[1])
    if carries:
        c.fill(c.rect(x - 1, base - 11, x + 4, base - 7), EARTH[1])
        c.fill(c.rect(x - 1, base - 12, x + 4, base - 10), MOSS[1])
        c.fill(c.rect(x - 2, base - 10, x - 1, base - 8) | c.rect(x + 4, base - 10, x + 5, base - 8), black)


def chorus(c, x, base, h, seed):
    g = rng(seed)
    c.fill(c.rect(x, base - h, x + 2, base + 1), PURPLE[4])
    c.fill(c.rect(x, base - h, x + 1, base + 1), PURPLE[3])
    y = base - 5
    side = 1
    while y > base - h + 3:
        ln = int(g.integers(3, 6))
        up = int(g.integers(3, 7))
        x0 = x + (2 if side > 0 else -ln)
        c.fill(c.rect(x0, y, x0 + ln, y + 2), PURPLE[4])
        bx = x + (ln if side > 0 else -ln)
        c.fill(c.rect(bx, y - up, bx + 2, y + 1), PURPLE[4])
        c.fill(c.rect(bx - 1, y - up - 3, bx + 3, y - up), PURPLE[1])
        c.px(bx - 1, y - up - 3, PURPLE[0])
        c.px(bx + 2, y - up - 1, PURPLE[2])
        y -= int(g.integers(5, 9))
        side = -side
    c.fill(c.rect(x - 1, base - h - 3, x + 3, base - h), PURPLE[1])
    c.px(x - 1, base - h - 3, PURPLE[0])
    c.px(x + 2, base - h - 1, PURPLE[2])


def stage4_back(b):
    """The sky of the End: the moon the dragon crosses, far islands, a city with its ship."""
    mo = b.ellipse(318, 60, 24)
    b.fill(mo, hexc('#cfc4ea'))
    b.fill(mo & (np.sqrt((b.xx - 311) ** 2 + (b.yy - 54) ** 2) <= 17), hexc('#ebe3ff'))
    for cx_, cy_, r in ((327, 56, 3.4), (311, 71, 2.6), (323, 69, 1.8), (304, 52, 2), (331, 70, 1.4)):
        cr = b.ellipse(cx_, cy_, r)
        b.fill(cr, hexc('#b3a6d6'))
        b.fill(cr & ~b.shift(cr, -1, -1), hexc('#9d8fc4'))
    far = hexc('#2f2749')
    far2 = hexc('#3d3360')
    for ix, iy, iw in ((250, 40, 20), (446, 96, 28), (388, 28, 12)):
        isl = b.poly([(ix - iw, iy), (ix + iw, iy), (ix + iw * 0.4, iy + iw * 0.5), (ix - iw * 0.3, iy + iw * 0.6)])
        b.fill(isl, far)
        b.fill(isl & (b.yy <= iy + 1), far2)
    # the city on the island to the right: towers of purpur, a banner, a bridge, the ship
    for tx, th, tw in ((436, 26, 6), (450, 40, 5), (444, 14, 12)):
        tow = b.rect(tx, 96 - th, tx + tw, 96)
        b.fill(tow, hexc('#4a3a6b'))
        b.fill(b.rect(tx, 96 - th, tx + 1, 96), hexc('#6a5590'))
        b.fill(b.rect(tx - 1, 96 - th - 2, tx + tw + 1, 96 - th), hexc('#6a5590'))
        for wy in range(96 - th + 4, 94, 7):
            b.px(tx + tw // 2, wy, PURPLE[1])
    b.fill(b.rect(454, 60, 455, 70) | b.rect(455, 60, 458, 64), hexc('#8a5fd0'))
    ship = b.poly([(462, 70), (478, 70), (475, 75), (465, 75)])
    b.fill(ship, hexc('#3d3360'))
    b.fill(b.rect(469, 60, 470, 70), hexc('#3d3360'))
    b.fill(b.poly([(470, 61), (477, 65), (470, 68)]), hexc('#5a4a80'))
    b.fill(b.rect(456, 71, 462, 72), hexc('#4a3a6b'))


def stage4_static(c):
    top = island_base(c, [ENDST[0], ENDST[1], ENDST[2]], [ENDST[2], ENDST[3], ENDST[4], hexc('#3f3e2a')], 401)
    # the blocks of end stone show on top
    for bx_ in range(214, 450, 9):
        c.px(bx_ + (bx_ * 7) % 4, IY + 2, ENDST[3])
        c.fill(c.rect(bx_ + 3, IY + 4, bx_ + 7, IY + 5) & c.alpha, ENDST[3])
    # obsidian pillars of different heights, the tall ones with a cage for their crystal
    for i, (px_, ph, pw) in enumerate(((248, 44, 9), (276, 82, 11), (404, 70, 11), (434, 36, 8))):
        pil = c.rect(px_ - pw // 2, IY - ph, px_ + pw // 2 + 1, IY + 1)
        c.ramp(pil, [OBSID[0], OBSID[1], OBSID[2], OBSID[3]], np.clip((c.xx - px_ + pw / 2.0) / pw, 0, 1), soft=0.3)
        n = noise2d(W, H, 410 + i, period=5, octaves=1)
        c.fill(pil & (n > 0.72), OBSID[0])
        c.fill(pil & (n < 0.2), OBSID[3])
        c.fill(pil & (c.yy == IY - ph), PURPLE[3])
        c.fill(c.edge(pil, inner=False) & (c.yy <= IY), OUTL)
        if i in (1, 2):
            cage = c.rect(px_ - 5, IY - ph - 11, px_ + 6, IY - ph)
            bars = cage & (((c.xx - px_) % 3 == 1) | (c.yy == IY - ph - 11))
            c.fill(bars, STEEL[3])
            c.fill(bars & (c.yy == IY - ph - 11), STEEL[2])
        else:
            c.fill(c.rect(px_ - 2, IY - ph - 2, px_ + 3, IY - ph), STONE[4])     # bedrock under the crystal
    # the exit fountain of bedrock in the middle: a bowl, the pillar with four torches, the egg on top
    bowl = c.rect(328, IY - 4, 376, IY + 1) | c.rect(332, IY - 6, 372, IY - 4)
    c.fill(bowl, STONE[4])
    c.fill(bowl & ~c.shift(bowl, 0, 1), STONE[2])
    c.fill(bowl & (noise2d(W, H, 420, period=3, octaves=1) > 0.62), STONE[5])
    inner = c.rect(335, IY - 5, 369, IY - 3)
    c.fill(inner, hexc('#07060b'))
    for sx in (338, 343, 349, 358, 362, 366):
        c.px(sx, IY - 5 + (sx % 2), hexc('#9fe9f5') if sx % 3 else PURPLE[1])
    post = c.rect(349, IY - 20, 355, IY - 4)
    c.fill(post, STONE[4])
    c.fill(c.rect(349, IY - 20, 350, IY - 4), STONE[2])
    c.fill(post & (noise2d(W, H, 421, period=3, octaves=1) > 0.6), STONE[5])
    for tx in (346, 356):
        c.fill(c.rect(tx, IY - 14, tx + 2, IY - 10), WOOD[1])
        c.fill(c.rect(tx, IY - 16, tx + 2, IY - 14), GLOW[1])
    egg = c.ellipse(352, IY - 25, 4, 5) & (c.yy <= IY - 20)
    c.fill(egg, hexc('#1a1230'))
    c.fill(egg & (c.xx < 351) & (c.yy < IY - 24), PURPLE[4])
    c.px(350, IY - 27, PURPLE[2]); c.px(353, IY - 23, PURPLE[3])
    c.fill(c.edge(bowl | post | egg, inner=False) & (c.yy <= IY), OUTL)
    chorus(c, 300, IY, 26, 430)
    chorus(c, 316, IY, 15, 431)
    chorus(c, 386, IY, 21, 432)
    chorus(c, 446, IY, 13, 433)
    chorus(c, 262, IY, 11, 434)
    enderman(c, 290, IY)
    enderman(c, 420, IY, carries=True)
    obelisk(c, 224, IY, 3, PURPLE[2])


def dragon(a, x, y, m):
    """The dragon before the moon: head and horns, a long neck and tail, two wings that beat."""
    c = Canvas(W, H)
    up = math.sin(m * 0.9)
    dark, mid, lite = hexc('#0d0918'), hexc('#2a2145'), hexc('#5a4a80')
    body = c.ellipse(x, y, 9, 4)
    neck = c.line(x - 7, y - 1, x - 19, y - 5, width=3)
    head = c.poly([(x - 18, y - 9), (x - 27, y - 6), (x - 28, y - 4), (x - 19, y - 3)])
    horn = c.line(x - 18, y - 8, x - 14, y - 11, width=1) | c.line(x - 19, y - 8, x - 16, y - 12, width=1)
    tail = c.line(x + 7, y, x + 19, y + 2, width=3) | c.line(x + 19, y + 2, x + 30, y + 5, width=2) | c.line(x + 30, y + 5, x + 36, y + 4, width=1)
    spade = c.poly([(x + 35, y + 1), (x + 40, y + 4), (x + 35, y + 7)])
    # wings like a bat's: shoulder, elbow, tip, and a trailing edge with two notches; the far one
    # a little behind and paler, the near one in front
    def wing(ox, amp):
        ty = -20 * up * amp
        return c.poly([(x - 5 + ox, y - 1), (x - 1 + ox, y - 1 + ty * 0.6), (x + 11 + ox, y - 1 + ty), (x + 12 + ox, y - 1 + ty * 0.62),
                       (x + 9 + ox, y + ty * 0.5), (x + 15 + ox, y + ty * 0.3), (x + 10 + ox, y + ty * 0.2), (x + 13 + ox, y + 1), (x + 6 + ox, y + 1)])

    far = wing(-4, 0.85)
    near = wing(0, 1.0)
    ty = -20 * up
    c.fill(far, mid)
    c.fill(body | neck | head | horn | tail | spade, dark)
    c.fill(near, dark)
    bone = c.line(x - 5, y - 1, x - 1, y - 1 + ty * 0.6) | c.line(x - 1, y - 1 + ty * 0.6, x + 11, y - 1 + ty)
    c.fill(bone, lite)
    c.fill(c.line(x - 1, y - 1 + ty * 0.6, x + 15, y + ty * 0.3) & near, mid)
    c.fill((body | neck | tail) & ~c.shift(body | neck | tail, 0, 1) & ~near, mid)
    for k in range(4):                                                  # spikes along the back
        c.px(x + 9 + k * 5, y - 1 + k // 2, lite)
    c.px(x - 23, y - 6, PURPLE[0])
    c.px(x - 22, y - 6, PURPLE[1])
    m_ = c.alpha
    # a pale rim where it flies before the dark sky, none before the moon
    p = np.pad(m_, 1)
    rim = ~m_ & (p[:-2, 1:-1] | p[2:, 1:-1] | p[1:-1, :-2] | p[1:-1, 2:]) & (a.astype(int).sum(axis=2) < 330)
    a[rim] = hexc('#4a3a6b')
    a[m_] = c.a[m_]


def stage4_move(a, m):
    yy, xx = np.mgrid[0:H, 0:W]
    dx, dy = 424 - int(m * 8.2), 62 + int(round(math.sin(m / 4.0) * 5))
    # the crystals turn in their cages and send their beams to the dragon
    for px_, ph, caged in ((276, 82, True), (404, 70, True), (248, 44, False), (434, 36, False)):
        cy = IY - ph - (6 if caged else 7) + int(round(math.sin(m / 3.0 + px_) * 1))
        wide = 2 if ((m // 3) + px_) % 2 == 0 else 1
        a[cy - 2:cy + 3, px_ - wide + 1:px_ + wide] = PURPLE[1]
        a[cy - 1:cy + 2, px_] = PURPLE[0]
        a[cy - 3, px_] = PURPLE[0]
        a[cy + 3, px_] = PURPLE[3]
        if caged:
            n = 18
            for k in range(1, n):
                if (k + m) % 2 == 0:
                    bx, by = px_ + (dx - px_) * k / n, (cy - 4) + (dy + 2 - cy) * k / n
                    if 0 <= int(bx) < W and 0 <= int(by) < H:
                        a[int(by), int(bx)] = PURPLE[0]
    dragon(a, dx, dy, m)
    # somebody glides over the island on elytra, a rocket's sparks behind
    gx, gy = 216 + int(m * 4.6), 128 - int(m * 1.6)
    a[gy, gx:gx + 3] = hexc('#c9c6d4')
    a[gy - 1, gx + 1:gx + 4] = hexc('#8a8799')
    a[gy + 1, gx + 1] = hexc('#5fd3e6')
    for k in range(1, 5):
        if (k + m) % 2:
            a[gy + k // 2 + 1, gx - k * 2] = GLOW[1] if k < 3 else GLOW[3]
    # one enderman is gone in a puff and stands somewhere else
    if 10 <= m < 13:
        for k in range(8):
            a[IY - 4 - (k * 5) % 18 - (m - 10) * 2, 289 + (k * 3) % 6 - 1] = PURPLE[1 + k % 3]
    # end motes drifting up
    for k in range(18):
        life = ((m / 30.0) + k / 18.0) % 1.0
        x = 220 + (k * 53) % 228
        a[int(IY - 4 - life * 64), x + int(math.sin(m / 5.0 + k) * 2)] = PURPLE[2] if k % 2 else ENDST[0]
    # portal stars glint
    for k, sx in enumerate((338, 343, 349, 358, 362, 366)):
        if (m + k * 2) % 5 == 0:
            a[IY - 5 + (sx % 2), sx] = CREAM
    crystal(a, 224, IY - 6 - 61, m, PURPLE[2], PURPLE[0], 3)


def stage5_back(b):
    """The Chaos Guardian in the dark behind the island: a head, a neck, two wings spread wide."""
    sil = hexc('#12060d')
    rim = hexc('#4a1830')
    hx, hy = 396, 70
    neck = b.poly([(hx - 7, hy + 6), (hx + 7, hy + 6), (hx + 16, 170), (hx - 16, 170)])
    head = b.poly([(hx - 8, hy - 8), (hx + 8, hy - 8), (hx + 10, hy + 2), (hx + 5, hy + 12), (hx - 5, hy + 12), (hx - 10, hy + 2)])
    horns = b.poly([(hx - 8, hy - 7), (hx - 15, hy - 22), (hx - 4, hy - 8)]) | b.poly([(hx + 8, hy - 7), (hx + 15, hy - 22), (hx + 4, hy - 8)])
    horns |= b.poly([(hx - 10, hy - 2), (hx - 19, hy - 9), (hx - 9, hy + 2)]) | b.poly([(hx + 10, hy - 2), (hx + 19, hy - 9), (hx + 9, hy + 2)])
    wing_l = b.poly([(hx - 12, 120), (hx - 44, 66), (hx - 98, 34), (hx - 86, 62), (hx - 96, 84), (hx - 70, 82), (hx - 74, 106), (hx - 50, 100), (hx - 48, 126), (hx - 28, 122), (hx - 20, 150)])
    wing_r = b.poly([(hx + 12, 120), (hx + 40, 62), (hx + 84, 30), (hx + 84, 60), (hx + 84, 84), (hx + 66, 82), (hx + 70, 106), (hx + 48, 100), (hx + 46, 126), (hx + 28, 122), (hx + 20, 150)])
    shoulders = b.ellipse(hx, 150, 34, 30)
    whole = neck | head | horns | wing_l | wing_r | shoulders
    b.fill(whole, sil)
    lit = whole & ~b.shift(whole, 0, 1)
    b.fill(lit, rim)
    b.fill(lit & (((b.xx * 3 + b.yy) % 7) == 0), CHAOS[4])
    for (x0, y0, x1, y1) in ((hx - 44, 66, hx - 86, 62), (hx - 44, 66, hx - 70, 82), (hx - 44, 66, hx - 50, 100), (hx + 40, 62, hx + 84, 60), (hx + 40, 62, hx + 66, 82), (hx + 40, 62, hx + 48, 100)):
        b.fill(b.line(x0, y0, x1, y1) & whole, hexc('#2a0e1c'))                       # the fingers of the wings
    for k in range(5):                                                               # scales down the neck
        b.fill(b.line(hx - 5 - k, hy + 18 + k * 12, hx, hy + 22 + k * 12) | b.line(hx, hy + 22 + k * 12, hx + 5 + k, hy + 18 + k * 12), hexc('#2a0e1c'))


def injector(c, x, base, h, to_left):
    """A fusion injector on its post, its tip toward the crystal."""
    c.fill(c.rect(x, base - h, x + 3, base + 1), OBSID[1])
    c.fill(c.rect(x, base - h, x + 1, base + 1), OBSID[0])
    head = c.rect(x - 1, base - h - 4, x + 4, base - h)
    c.fill(head, STEEL[4])
    c.fill(c.rect(x - 1, base - h - 4, x + 4, base - h - 3), STEEL[2])
    c.px(x + (-2 if to_left else 4), base - h - 2, CHAOS[1])
    c.fill(c.edge(head | c.rect(x, base - h, x + 3, base + 1), inner=False) & (c.yy <= base), OUTL)


def stage5_static(c):
    top = island_base(c, [OBSID[0], OBSID[1], OBSID[2]], [OBSID[1], OBSID[2], OBSID[3], hexc('#0d0918')], 501)
    # shards of black crystal leaning every way, a red vein in each
    for i, (sx, sw, sh, lean) in enumerate(((232, 9, 34, -6), (247, 6, 18, 3), (292, 7, 22, -3), (384, 6, 16, 4), (440, 9, 38, 6), (428, 6, 20, -3), (372, 5, 12, -3))):
        sh_m = c.poly([(sx - sw / 2.0, IY + 1), (sx + lean - 1, IY - sh), (sx + lean + 1, IY - sh), (sx + sw / 2.0, IY + 1)])
        c.ramp(sh_m, [OBSID[0], OBSID[1], OBSID[2], OBSID[3]], np.clip((c.xx - sx + sw / 2.0) / sw, 0, 1), soft=0.25)
        c.fill(sh_m & ~c.shift(sh_m, 1, 0), PURPLE[4])
        vein = c.line(sx, IY - 1, sx + lean * 0.7, IY - sh * 0.7) & sh_m
        c.fill(vein & ((c.yy % 3) != 0), CHAOS[3])
        c.fill(c.edge(sh_m, inner=False) & (c.yy <= IY), OUTL)
    # cracks in the ground that glow, the turf broken by them
    n = noise2d(W, H, 510, period=6, octaves=2)
    crack = (c.yy > IY + 1) & (c.yy < IY + 22) & (np.abs(n - 0.5) < 0.02) & (c.xx > 222) & (c.xx < 444)
    c.fill(crack & c.alpha, CHAOS[3])
    c.fill(crack & c.alpha & (c.yy < IY + 8), CHAOS[2])
    for gx in range(226, 440, 13):
        c.px(gx + (gx * 5) % 7, IY, CHAOS[3])
    # draconium in the rock: a few purple glints
    g = rng(511)
    for _ in range(12):
        ox, oy = int(g.integers(230, 436)), int(g.integers(IY + 6, IY + 26))
        if c.alpha[oy, ox]:
            c.px(ox, oy, PURPLE[3]); c.px(ox + 1, oy, PURPLE[2])
    # the altar under the chaos crystal: three steps, runes, four injectors round it
    alt = c.rect(318, IY - 4, 360, IY + 1) | c.rect(324, IY - 8, 354, IY - 4) | c.rect(330, IY - 12, 348, IY - 8)
    c.fill(alt, OBSID[2])
    c.fill(alt & ~c.shift(alt, 0, 1), OBSID[0])
    c.fill(alt & ~c.shift(alt, 1, 0), OBSID[1])
    for rx in range(326, 354, 4):
        c.px(rx, IY - 6, CHAOS[2])
    for rx in range(320, 360, 5):
        c.px(rx, IY - 2, CHAOS[3])
    c.fill(c.rect(333, IY - 11, 345, IY - 10), CHAOS[2])
    c.fill(c.edge(alt, inner=False) & (c.yy <= IY), OUTL)
    injector(c, 306, IY, 20, False)
    injector(c, 368, IY, 20, True)
    injector(c, 298, IY, 10, False)
    injector(c, 376, IY, 10, True)
    # the energy core on the right: two stabilisers, the ball of light between them comes in the moving part
    for sx in (398, 418):
        st = c.rect(sx, IY - 26, sx + 4, IY + 1)
        c.fill(st, STEEL[4])
        c.fill(c.rect(sx, IY - 26, sx + 1, IY + 1), STEEL[2])
        c.fill(c.rect(sx - 1, IY - 29, sx + 5, IY - 26), STEEL[3])
        c.fill(c.rect(sx + 1, IY - 20, sx + 3, IY - 8), GLOW[3])
        c.fill(c.edge(st | c.rect(sx - 1, IY - 29, sx + 5, IY - 26), inner=False) & (c.yy <= IY), OUTL)
    obelisk(c, 264, IY, 4, CHAOS[2])


def stage5_move(a, m):
    yy, xx = np.mgrid[0:H, 0:W]
    # the guardian's eyes open
    hx, hy = 396, 70
    open_ = min(1.0, m / 7.0)
    if open_ > 0.25:
        tall = 1 if open_ < 0.6 else (2 if open_ < 0.9 else 3)
        for sx in (-7, 3):
            a[hy - 1:hy - 1 + tall, hx + sx:hx + sx + 5] = CHAOS[2]
            a[hy - 1:hy - 1 + tall, hx + sx + 1:hx + sx + 4] = CHAOS[1]
            a[hy - 1 + tall // 2, hx + sx + 2] = CHAOS[0]
        if open_ >= 1.0 and (m // 2) % 2 == 0:                           # a breath of fire starts in its mouth
            a[hy + 8:hy + 10, hx - 2:hx + 3] = CHAOS[3]
            a[hy + 9, hx - 1:hx + 2] = CHAOS[1]
    cx, cy = 339, IY - 46 + int(round(math.sin(m / 4.0) * 2))
    # beams from the injectors to the crystal
    for ix, iy in ((306, IY - 22), (371, IY - 22), (298, IY - 12), (379, IY - 12)):
        n = int(math.hypot(cx - ix, cy + 12 - iy))
        for k in range(n):
            if (k - m * 2) % 5 < 3:
                bx, by = ix + (cx - ix) * k / n, iy + (cy + 12 - iy) * k / n
                a[int(by), int(bx)] = CHAOS[2] if (k - m * 2) % 5 else CHAOS[0]
    # the chaos crystal: a tall dark diamond, its core beats
    dia = (np.abs(xx - cx) / 10.0 + np.abs(yy - cy) / 22.0) <= 1.0
    beat = 0.5 + 0.5 * math.sin(m * math.pi / 3.0)
    a[dia] = CHAOS[4]
    a[dia & (xx < cx) & (yy < cy)] = CHAOS[3]
    a[dia & (xx >= cx) & (yy >= cy)] = CHAOS[5]
    core = (np.abs(xx - cx) / 5.0 + np.abs(yy - cy) / 11.0) <= (0.7 + 0.3 * beat)
    a[core] = CHAOS[2]
    a[(np.abs(xx - cx) / 2.0 + np.abs(yy - cy) / 5.0) <= 1.0] = CHAOS[0] if beat > 0.5 else CHAOS[1]
    a[dia & (xx == cx - 1) & (yy < cy - 12)] = CHAOS[1]
    p = np.pad(dia, 1)
    a[~dia & (p[:-2, 1:-1] | p[2:, 1:-1] | p[1:-1, :-2] | p[1:-1, 2:])] = OUTL
    for k in range(4):                                                    # splinters circle the crystal
        ang = m / 4.0 + k * math.pi / 2
        sx, sy = int(cx + math.cos(ang) * 17), int(cy + math.sin(ang) * 6)
        if math.sin(ang) > -0.2 or abs(sx - cx) > 10:
            a[sy - 1:sy + 2, sx] = CHAOS[1]
            a[sy, sx - 1:sx + 2] = CHAOS[2]
    # lightning from the crystal to the shards, a new fork every two frames
    g = rng(520 + m // 2)
    for tx, ty in ((227, IY - 34), (446, IY - 38), (290, IY - 22), (426, IY - 20)):
        if g.random() < 0.6:
            x, y = float(cx), float(cy)
            for k in range(12):
                nx = x + (tx - x) / (12 - k) + g.uniform(-3, 3)
                ny = y + (ty - y) / (12 - k) + g.uniform(-3, 3)
                steps = int(max(abs(nx - x), abs(ny - y))) + 1
                for s in range(steps):
                    px_, py_ = int(x + (nx - x) * s / steps), int(y + (ny - y) * s / steps)
                    if 0 <= px_ < W and 0 <= py_ < H:
                        a[py_, px_] = CHAOS[0] if (k + m) % 3 else CHAOS[1]
                x, y = nx, ny
    # the energy core between its stabilisers
    ex, ey = 410, IY - 16
    r = 5.0 + 0.8 * math.sin(m / 2.0)
    d = np.sqrt((xx - ex) ** 2 + (yy - ey) ** 2)
    a[d <= r + 1] = GLOW[3]
    a[d <= r] = GLOW[2]
    a[(d <= r - 1.5)] = GLOW[1]
    a[np.sqrt((xx - ex + 1) ** 2 + (yy - ey + 1) ** 2) <= r - 3.4] = GLOW[0]
    for k in range(6):
        ang = m / 3.0 + k * math.pi / 3
        a[int(ey + math.sin(ang) * 3), int(ex + math.cos(ang) * 9)] = GLOW[1]
    for sx in (402, 417):
        if (m + sx) % 3:
            a[ey, min(sx, ex - 6) if sx < ex else ex + 6:max(sx, ex - 5) if sx < ex else sx + 1] = GLOW[1]
    # ash and sparks rising
    for k in range(20):
        life = ((m / 26.0) + k / 20.0) % 1.0
        x = 222 + (k * 47) % 224
        a[int(IY - 2 - life * 74), x + int(math.sin(m / 4.0 + k) * 3)] = CHAOS[2] if k % 3 else CHAOS[0]
    crystal(a, 264, IY - 6 - 70, m, CHAOS[2], CHAOS[0], 4)


STATICS = (stage1_static, stage2_static, stage3_static, stage4_static, stage5_static)
MOVES = (stage1_move, stage2_move, stage3_move, stage4_move, stage5_move)
SHIFT = 18                     # the islands stand this far to the right of where they were painted
TX = 20                        # the writing's left edge

# the sky of every stage, from the top of the picture to its bottom, and its clouds from shade to light
SKY = (
    cols('#1b2438', '#243450', '#32506a', '#4a7082', '#739892', '#a9bf9e', '#dcd8a8'),      # a cool morning
    cols('#2b2350', '#473270', '#78467e', '#b45c78', '#de8460', '#f2ae62', '#fbd98a'),      # the golden evening
    cols('#0f0e18', '#17141f', '#231926', '#391d29', '#5c262b', '#8c3b2b', '#bd5c2d'),      # night over the furnaces
    cols('#0c0a16', '#110e20', '#17122c', '#1d1738', '#241c44', '#2b2150', '#33265a'),      # the End
    cols('#0d0810', '#160912', '#220b18', '#330e1f', '#481327', '#621a2f', '#822338'),      # the storm of chaos
)
CLOUD = (
    cols('#4f7080', '#7c9c9c', '#b6c8aa', '#eee8c4'),
    cols('#84568a', '#bc6c7a', '#ee9c6e', '#fcd48e'),
    cols('#241c2a', '#372631', '#522f33', '#7c4332'),
    cols('#1d1738', '#241c44', '#2b2150', '#3a2c66'),
    cols('#200a16', '#3a1122', '#5c1a30', '#8c2a42'),
)
BAYER4 = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]) / 16.0 + 1 / 32.0


def islet(b, x, y, w, turf, rock, seed):
    """A small piece of ground far off; returns its top's mask so that things can stand on it."""
    g = rng(seed)
    pts = [(x - w, y), (x + w, y)]
    n = 5
    for k in range(n, -1, -1):
        f = k / float(n)
        pts.append((x - w + 2 * w * f + g.uniform(-1, 1), y + (w * 0.75) * math.sin(f * math.pi) ** 0.7 * g.uniform(0.7, 1.1) + 1))
    m = b.poly(pts)
    b.fill(m, rock[1])
    b.fill(m & (b.xx > x + w * 0.2), rock[2])
    b.fill(m & (b.yy <= y + 1), turf[1])
    b.fill(m & (b.yy == y), turf[0])
    return m


def far_pine(b, x, base, h, col, lit):
    for k in range(h):
        hw = (k * 2) // 5 + (1 if k % 3 == 2 else 0)
        b.fill(b.rect(x - hw, base - h + k, x + hw + 1, base - h + k + 1), col)
        b.px(x - hw, base - h + k, lit)


def backdrop(stage):
    """The sky behind an island: bands of colour, clouds, a sea of cloud below, far islets with
    something of the stage on them, then all of it fading into the night toward the edges."""
    import scene
    b = Canvas(W, H)
    P = {'cloud': list(CLOUD[stage])}
    n = noise2d(W, H, 700 + stage, period=60, octaves=2)
    b.ramp(b.rect(0, 0, W, H), list(SKY[stage]), np.clip((b.yy - 6) / 236.0 + (n - 0.5) * 0.12, 0, 1), soft=0.5)
    g = rng(600 + stage)
    if stage >= 2:
        for _ in range(110):
            x, y = int(g.integers(0, W)), int(g.integers(0, 150))
            b.px(x, y, hexc('#f2ede3') if g.random() < 0.2 else hexc('#6a5f80'))
    if stage == 0:
        # a pale sun low behind the island, far ranges
        for r, col in ((30, '#e6dcae'), (22, '#f4eec8'), (16, '#fffbe0')):
            b.fill(b.ellipse(400, 196, r), hexc(col))
        for base, amp, col, lit, seed in ((206, 26, '#5d8088', '#8fb0a4', 11), (220, 18, '#46666f', '#6f9690', 12)):
            ys = base - amp * (noise2d(W, 1, 720 + seed, period=70, octaves=3)[0])
            m = b.yy >= np.round(ys)[None, :]
            b.fill(m, hexc(col))
            b.fill(m & ~b.shift(m, 0, 1), hexc(lit))
            b.fill(m & ~b.shift(m, 1, 1) & ~b.shift(m, 0, 2), hexc(lit))
    if stage == 1:
        for r, col in ((34, '#fbd98a'), (26, '#fde9ae'), (20, '#fff6d0')):
            b.fill(b.ellipse(428, 204, r), hexc(col))
    if stage == 2:
        # far works on the horizon: chimneys in a row, their smoke lit from below
        for cx_, top in ((236, 232), (250, 224), (300, 236), (366, 230), (402, 222), (452, 234), (468, 226)):
            b.fill(b.rect(cx_, top, cx_ + 3, 256), hexc('#1c1420'))
            b.px(cx_ + 1, top - 1, hexc('#f06579'))
            for k in range(7):
                b.fill(b.ellipse(cx_ + 2 + k * 3, top - 4 - k * 3, 2 + k * 0.5, 1.5 + k * 0.3), hexc('#372631') if k % 2 else hexc('#2c2029'))
        for hx_, hw_, hh_ in ((258, 34, 8), (410, 40, 11), (322, 30, 6)):
            b.fill(b.rect(hx_, 250 - hh_, hx_ + hw_, 258), hexc('#1c1420'))
            for wx in range(hx_ + 3, hx_ + hw_ - 2, 5):
                b.px(wx, 250 - hh_ + 3, GLOW[2])
    if stage == 4:
        stage5_back(b)
    # clouds: a few in the open sky, lit from below where the light is
    spots = {0: ((250, 60, 60), (430, 44, 52), (330, 28, 40), (464, 110, 44)),
             1: ((244, 52, 64), (420, 36, 56), (336, 22, 36), (462, 96, 48), (286, 100, 30)),
             2: ((260, 70, 70), (420, 52, 80), (340, 100, 50)),
             3: (),
             4: ((250, 40, 80), (440, 30, 90), (330, 20, 60), (236, 96, 50), (470, 120, 40))}[stage]
    for k, (cx_, base, width) in enumerate(spots):
        scene.cloud(b, P, cx_, base, width, 740 + stage * 10 + k, flat=(stage in (0, 1) and k % 2 == 1))
    if stage == 3:
        stage4_back(b)
    # far islets with something of the stage on them
    turf = ([MOSS[2], MOSS[3]], [MOSS[2], MOSS[3]], [hexc('#3a333f'), hexc('#2a242f')], [ENDST[2], ENDST[3]], [OBSID[1], OBSID[2]])[stage]
    rock = ([hexc('#6f8f90'), hexc('#4f6f78'), hexc('#3e5a66')], [hexc('#9a5a70'), hexc('#74466a'), hexc('#5a3860')],
            [hexc('#2a1c24'), hexc('#20161d'), hexc('#181018')], [ENDST[3], ENDST[4], hexc('#3f3e2a')], [hexc('#2a1226'), hexc('#1e0c1c'), hexc('#150814')])[stage]
    if stage != 3:
        for k, (ix, iy, iw) in enumerate(((230, 92, 8), (462, 136, 11), (286, 228, 7), (392, 28, 6))):
            islet(b, ix, iy, iw, turf, rock, 760 + stage * 10 + k)
            if stage == 0:
                far_pine(b, ix - 2, iy, 9, hexc('#2f5a50'), hexc('#4f8a60'))
                if iw > 8:
                    far_pine(b, ix + 4, iy, 6, hexc('#2f5a50'), hexc('#4f8a60'))
            elif stage == 1:
                b.fill(b.rect(ix - 3, iy - 6, ix + 3, iy), BRICK[2])
                b.fill(b.poly([(ix - 4, iy - 6), (ix, iy - 10), (ix + 4, iy - 6)]), hexc('#3f2b43'))
                b.px(ix, iy - 3, GLOW[1])
                if iw > 8:
                    b.fill(b.ellipse(ix + 6, iy - 5, 3), BRASS[3])
                    b.fill(b.ellipse(ix + 6, iy - 5, 1.2), hexc('#5c3a1e'))
            elif stage == 2:
                b.fill(b.rect(ix - 1, iy - 12, ix + 2, iy), hexc('#3a1a20'))
                b.px(ix, iy - 13, GLOW[2])
                b.fill(b.rect(ix + 3, iy - 5, ix + 8, iy), hexc('#2c1418'))
                b.px(ix + 5, iy - 3, GLOW[2])
            elif stage == 4:
                sh = b.poly([(ix - 3, iy), (ix + 1, iy - 12 - iw), (ix + 3, iy)])
                b.fill(sh, OBSID[2])
                b.fill(sh & ~b.shift(sh, 1, 0), CHAOS[4])
    # a sea of cloud under everything, two rows deep
    if stage != 3:
        sea = [tuple(int(v * 0.72) for v in col) for col in CLOUD[stage]]
        for k in range(9):
            scene.cloud(b, {'cloud': sea}, 190 + k * 38 + int(g.integers(-8, 8)), 262 + (k % 2) * 4, 70 + int(g.integers(0, 30)), 780 + stage * 10 + k)
        front = [tuple(int(v * 0.5) for v in col) for col in CLOUD[stage]]
        for k in range(7):
            scene.cloud(b, {'cloud': front}, 200 + k * 50 + int(g.integers(-10, 10)), 276, 80 + int(g.integers(0, 30)), 795 + stage * 10 + k)
    # the picture fades into the night toward the writing and the corners, in steps, dithered
    d = np.sqrt(((b.xx - (IX + 4)) / 1.25) ** 2 + ((b.yy - (IY - 36)) / 1.0) ** 2)
    k = np.clip((d - 92) / 124.0, 0, 1)
    level = np.clip(np.floor(k * 6 + BAYER4[b.yy % 4, b.xx % 4]) / 6.0, 0, 1)
    out = b.a.astype(float) * (1 - level[..., None]) + np.array(NIGHT, float) * level[..., None]
    b.a[:] = out.astype(np.uint8)
    return b


def static(stage):
    if stage in _STATIC:
        return _STATIC[stage]
    back = backdrop(stage)
    c = Canvas(W, H)
    STATICS[stage](c)
    back.paste(c)
    _STATIC[stage] = back.a.copy()
    return _STATIC[stage]


def card(stage, m):
    a = static(stage).copy()
    MOVES[stage](a, m)
    # the island comes in from the right as the writing comes in from the left
    sh = SHIFT + int(round(max(0, 4 - m) ** 2 * 3))
    a[:, sh:] = a[:, :-sh].copy()
    a[:, :sh] = NIGHT
    col = STAGE[stage]
    # the writing slides in from the left in the first frames
    slide = int(round(max(0, 5 - m) ** 2 * 2.2))
    x = TX - slide
    font.draw(a, 'STUFE ' + ROMAN[stage], x, 92, CREAM, 2)
    font.draw(a, NAMES[stage], x, 114, col, 3)
    a[142:144, max(0, x):max(0, x) + min(170, 12 + m * 14)] = col
    a[144, max(0, x):max(0, x) + min(170, 12 + m * 14)] = OUTL
    if m >= 5:
        font.draw(a, GOALS[stage], TX, 152, CREAM, 1)
    # five pips: which stage of the five this is
    for k in range(5):
        px_ = TX + k * 12
        a[170:176, px_:px_ + 8] = OUTL
        a[171:175, px_ + 1:px_ + 7] = STAGE[k] if k <= stage else hexc('#2d2538')
    return a
