"""Shot 3 of the trailer: the obelisk at spawn at nightfall, and everybody brings something.

The plaza is painted once (static()); frame(m) adds what moves: the crystal and its shards, the
beam, the runes running up the trunk, the little people who walk up, raise what they carry and
walk off again, the gifts that fly into the crystal, the lanterns, and the goal's bar at the top,
which fills while they give. m is the frame within the shot (0..71).
"""
import math

import numpy as np

import font
from px import Canvas, cols, hexc, noise1d, noise2d

W, H = 480, 270
GY = 206                       # the ground line at the obelisk's foot
CX = 240
OUTL = hexc('#15121f')
SKY = cols('#2b2147', '#3a2a57', '#5a3566', '#8f4a6b', '#d0705f', '#f2a765')      # top to horizon
STONE = cols('#8a7f97', '#655a73', '#4b4159', '#3a3046', '#2d2538', '#231d2c')
SLATE = cols('#5a5270', '#443c58', '#332c45', '#262034', '#1c1727')              # the obelisk's own dark stone
BRASS = cols('#fff3c4', '#f7dc86', '#e5b451', '#b98530', '#8a5a24', '#5c3a1e')
CYAN = cols('#e8fbff', '#9fe9f5', '#5fd3e6', '#2f9fc0', '#1c6388')
GOLD = cols('#fff7d0', '#ffe28a', '#f7c14e')
MOSS = cols('#8fba4f', '#5d9443', '#3b6f3d', '#285238', '#1c3a31')
WOOD = cols('#8d5a3b', '#6b4030', '#4a2c26', '#33201f')
GLOW = cols('#fff1b8', '#ffd27a', '#ffa64d', '#d9662c')
PAVE = cols('#544a66', '#463d58', '#3a3249', '#2f283c', '#251f30')
NIGHT = hexc('#0d0b10')
STAGE = cols('#a8b596', '#e5b451', '#8bb6dc', '#bb98f4', '#f06579')
SHIRTS = cols('#f06579', '#8bb6dc', '#bb98f4', '#a8b596', '#e5b451', '#f2ede3', '#63a88f', '#d9662c')
SKIN = cols('#f1c9a5', '#d9a57d', '#a8744f', '#f5d7b8')
GIFTS = cols('#8a7f97', '#e5b451', '#bb98f4', '#d9c98f', '#8a7f97', '#63a88f')

_STATIC = None


def trunk_half(y):
    """Half the obelisk's width at height y: the trunk tapers, the tip is a pyramid."""
    if y >= 72:
        return 11.0 + (y - 72) / (GY - 19 - 72.0) * 5.0
    return max(0.0, 11.0 * (y - 46) / 26.0)


def static():
    global _STATIC
    if _STATIC is not None:
        return _STATIC
    c = Canvas(W, H)
    # ---- sky: night above, the last light at the horizon ----
    hor = 176
    c.ramp(c.rect(0, 0, W, hor), SKY, np.clip(c.yy / float(hor), 0, 1) ** 1.6, soft=0.5)
    g = np.random.default_rng(3)
    for _ in range(90):
        x, y = int(g.integers(0, W)), int(g.integers(0, 110))
        c.px(x, y, hexc('#f2ede3') if g.random() < 0.25 else hexc('#8d7fae'))
    # thin clouds lit from below
    for cx_, cy_, w_ in ((70, 96, 70), (180, 118, 54), (350, 104, 80), (430, 128, 46), (270, 84, 40)):
        m = c.ellipse(cx_, cy_, w_ / 2.0, 3.2) | c.ellipse(cx_ + w_ * 0.2, cy_ - 2, w_ / 3.2, 2.4)
        c.fill(m, hexc('#6b4a72'))
        c.fill(m & ~c.shift(m, 0, -1), hexc('#e08a6a'))
        c.fill(m & ~c.shift(m, 0, 1), hexc('#4a3560'))
    # ---- far: mountains, the works with its crown tower and lit windows, a forest line ----
    far = c.below(150 + noise1d(W, 4, octaves=((60, 1.0), (23, 0.5), (9, 0.2))) * 16)
    c.fill(far & (c.yy < hor + 6), hexc('#4a3a66'))
    c.fill(far & ~c.shift(far, 0, 1), hexc('#7a5a86'))
    near = c.below(166 + noise1d(W, 5, octaves=((40, 1.0), (13, 0.5))) * 8)
    c.fill(near & (c.yy < hor + 6), hexc('#33284d'))
    c.fill(c.rect(0, 176, W, 191), hexc('#1c1730'))
    c.fill(near & (c.yy < hor + 6), hexc('#33284d'))
    # the works on the left, small: hall, tower, crown, chimney, windows alight
    wx = 58
    hall = c.rect(wx, 160, wx + 34, 178) | c.poly([(wx - 2, 160), (wx + 17, 151), (wx + 36, 160)])
    tower = c.rect(wx + 36, 140, wx + 46, 178)
    chim = c.rect(wx + 6, 144, wx + 9, 158)
    works = hall | tower | chim
    c.fill(works, hexc('#241c36'))
    c.fill(works & ~c.shift(works, 1, 0), hexc('#3a2e52'))
    crown = c.poly([(wx + 35, 140), (wx + 34, 133), (wx + 38, 137), (wx + 41, 131), (wx + 44, 137), (wx + 48, 133), (wx + 47, 140)])
    c.fill(crown, BRASS[3])
    c.fill(crown & ~c.shift(crown, 1, 0), BRASS[1])
    for x, y in ((wx + 5, 166), (wx + 11, 166), (wx + 17, 166), (wx + 23, 166), (wx + 29, 166), (wx + 39, 148), (wx + 39, 158), (wx + 42, 168)):
        c.fill(c.rect(x, y, x + 2, y + 3), GLOW[1])
    gearm = c.ellipse(wx + 41, 153, 2.6)
    c.fill(gearm, BRASS[3])
    c.fill(c.ellipse(wx + 41, 153, 1.2), hexc('#241c36'))   # the tower's gear, a ring from afar
    # forest: pines in two rows
    for row, (base, tone, hi, step, hmin, hmax) in enumerate(((182, '#1f1a33', '#2c2545', 9, 12, 24), (190, '#17132a', '#231c3a', 12, 16, 30))):
        gg = np.random.default_rng(6 + row)
        x = -6
        while x < W + 6:
            h = int(gg.integers(hmin, hmax))
            if not (CX - 110 < x < CX + 110) or row == 0:
                tri = c.poly([(x, base - h), (x - h * 0.28 - 2, base), (x + h * 0.28 + 2, base)])
                c.fill(tri, hexc(tone))
                c.fill(tri & ~c.shift(tri, 1, 0) & (c.xx < x), hexc(hi))
            x += int(gg.integers(step - 3, step + 4))
    # ---- the plaza: paving in rings round the obelisk, seen flat ----
    ground = c.rect(0, 190, W, H)
    depth = np.clip((c.yy - 190) / 80.0, 0, 1)
    c.ramp(ground, [PAVE[2], PAVE[3], PAVE[4], hexc('#1c1727')], depth, soft=0.35)
    # rings: ellipses round the foot; the slabs' joints as short radial strokes
    dxn, dyn = (c.xx - CX) / 1.0, (c.yy - GY) * 3.2
    rad = np.sqrt(dxn * dxn + dyn * dyn)
    ang = np.arctan2(dyn, dxn)
    for r0 in (54, 92, 134, 182, 236):
        ring = (np.abs(rad - r0) < 0.9) & ground
        c.fill(ring, PAVE[4])
        c.fill(c.shift(ring, 0, 1) & ground & ~ring, PAVE[1])
    for i, (r0, r1, n) in enumerate(((54, 92, 14), (92, 134, 20), (134, 182, 26), (182, 236, 34))):
        joint = ground & (rad > r0 + 1) & (rad < r1 - 1) & (np.abs(((ang / (2 * math.pi) * n + (i % 2) * 0.5) % 1.0) - 0.5) < 0.012 * n / 8.0)
        c.fill(joint, PAVE[4])
    # moss and grass in the joints here and there, and at the plaza's far edge
    n2 = noise2d(W, H, 7, period=9, octaves=2)
    c.fill(ground & (np.abs(rad - 134) < 1.6) & (n2 > 0.62), MOSS[3])
    c.fill(ground & (np.abs(rad - 236) < 2.0) & (n2 > 0.5), MOSS[3])
    edge = ground & (c.yy < 193)
    c.fill(edge, MOSS[4])
    c.fill(ground & (c.yy == 190) & (n2 > 0.4), MOSS[2])
    # ---- the leaderboard wall on the right: dark stone, brass frame, lines of names ----
    bx0, by0 = 392, 150
    wall = c.rect(bx0, by0, bx0 + 52, 198)
    c.fill(wall, SLATE[3])
    c.fill(c.rect(bx0, by0, bx0 + 52, by0 + 2) | c.rect(bx0, by0, bx0 + 2, 198), SLATE[1])
    c.fill(c.rect(bx0 + 3, by0 + 3, bx0 + 49, by0 + 5), BRASS[3])
    c.fill(c.rect(bx0 + 3, by0 + 3, bx0 + 49, by0 + 4), BRASS[1])
    for i in range(6):
        y = by0 + 10 + i * 6
        wd = [34, 28, 30, 22, 26, 18][i]
        c.fill(c.rect(bx0 + 6, y, bx0 + 8, y + 2), BRASS[2] if i < 3 else STONE[1])
        c.fill(c.rect(bx0 + 11, y, bx0 + 11 + wd, y + 1), hexc('#f2ede3') if i == 0 else STONE[0])
        c.fill(c.rect(bx0 + 11, y + 2, bx0 + 11 + int(wd * 0.7), y + 3), BRASS[4])
    c.fill(c.edge(wall, inner=False) & (c.yy < 198), OUTL)
    # ---- a waystone on the left ----
    wsx = 118
    ws = c.rect(wsx, 176, wsx + 8, 198) | c.rect(wsx - 2, 194, wsx + 10, 198) | c.rect(wsx - 1, 173, wsx + 9, 176)
    c.fill(ws, STONE[2])
    c.fill(ws & ~c.shift(ws, 1, 0), STONE[0])
    c.fill(c.rect(wsx + 3, 180, wsx + 5, 190), CYAN[2])
    c.fill(c.edge(ws, inner=False) & (c.yy < 198), OUTL)
    # ---- pylons with lanterns and a flag in each stage's colour, two on each side ----
    for i, px_ in enumerate((158, 196, 284, 322)):
        base = 201 + (0 if i in (1, 2) else 3)
        top = base - (44 if i in (1, 2) else 52)
        post = c.rect(px_ - 1, top, px_ + 2, base) | c.rect(px_ - 3, base - 3, px_ + 4, base)
        c.fill(post, SLATE[2])
        c.fill(c.rect(px_ - 1, top, px_, base), SLATE[0])
        c.fill(c.rect(px_ - 2, top - 2, px_ + 3, top), BRASS[3])
        c.fill(c.rect(px_ - 2, top - 2, px_ + 3, top - 1), BRASS[1])
        c.fill(c.edge(post, inner=False) & (c.yy < base), OUTL)
    # ---- pedestals for the three pillars and the last gift ----
    for i, px_ in enumerate((176, 210, 270, 304)):
        base = 204 + (2 if i in (0, 3) else 0)
        ped = c.rect(px_ - 5, base - 9, px_ + 6, base) | c.rect(px_ - 6, base - 11, px_ + 7, base - 9) | c.rect(px_ - 6, base - 2, px_ + 7, base)
        c.fill(ped, SLATE[2])
        c.fill(ped & ~c.shift(ped, 0, 1), SLATE[0])
        c.fill(c.rect(px_ - 4, base - 7, px_ + 5, base - 6), BRASS[3])
        c.fill(c.edge(ped, inner=False) & (c.yy < base), OUTL)
    # ---- the obelisk: three steps, the trunk in panels with brass pins, a brass band, the tip ----
    for k, (hw, y0, y1) in enumerate(((36, GY - 5, GY + 1), (29, GY - 12, GY - 5), (22, GY - 19, GY - 12))):
        st = c.rect(CX - hw, y0, CX + hw + 1, y1)
        c.ramp(st, [SLATE[1], SLATE[2], SLATE[3]], np.clip((c.xx - CX + hw) / (2.0 * hw), 0, 1), soft=0.3)
        c.fill(c.rect(CX - hw, y0, CX + hw + 1, y0 + 1), SLATE[0])
        c.fill(c.rect(CX - hw, y1 - 1, CX + hw + 1, y1), SLATE[4])
        # carved panels on the riser
        for px_ in range(CX - hw + 4, CX + hw - 3, 8):
            c.fill(c.rect(px_, y0 + 2, px_ + 5, y1 - 2), SLATE[3])
        c.fill(c.edge(st, inner=False), OUTL)
    c.fill(c.rect(CX - 22, GY - 20, CX + 23, GY - 19), BRASS[2])
    half = np.vectorize(trunk_half)(np.arange(H))[:, None]
    body = (np.abs(c.xx - CX) <= half) & (c.yy >= 46) & (c.yy < GY - 19)
    lit = np.clip((c.xx - CX + half) / np.maximum(2 * half, 1), 0, 1)
    c.ramp(body, [SLATE[0], SLATE[1], SLATE[2], SLATE[3], SLATE[4]], lit * 0.9 + 0.05, soft=0.25)
    # panels: a mortar line every 22 px, pins in the corners
    for y in range(GY - 19 - 22, 72, -22):
        line = body & (c.yy == y)
        c.fill(line, SLATE[4])
        c.fill(c.shift(line, 0, 1) & body, SLATE[0])
        hw = int(trunk_half(y))
        for sx in (-1, 1):
            c.px(CX + sx * (hw - 3), y + 4, BRASS[2])
            c.px(CX + sx * (hw - 3), y - 3, BRASS[3])
    # the brass band under the tip and the cap
    band = body & (c.yy >= 72) & (c.yy < 76)
    c.ramp(band, [BRASS[1], BRASS[2], BRASS[3], BRASS[4]], lit, soft=0.25)
    c.fill(body & (c.yy == 72), BRASS[0])
    cap = body & (c.yy < 52)
    c.ramp(cap, [BRASS[0], BRASS[2], BRASS[3]], lit, soft=0.25)
    c.fill(c.edge(body, inner=False) & (c.yy < GY - 19), OUTL)
    plaza_life(c)
    _STATIC = (c.a.copy(), body)
    return _STATIC


def plaza_life(c):
    """What stands about the square: two market stalls, crates and barrels, a cart of ore, and
    the warm light of the lamps on the paving."""
    def stall(x, base, stripe):
        c.fill(c.rect(x, base - 15, x + 1, base + 1) | c.rect(x + 27, base - 15, x + 28, base + 1), WOOD[1])
        counter = c.rect(x - 1, base - 6, x + 29, base + 1)
        c.fill(counter, WOOD[2])
        c.fill(c.rect(x - 1, base - 6, x + 29, base - 5), WOOD[0])
        for k in range(0, 30, 5):
            c.fill(c.rect(x - 1 + k, base - 4, x + k, base + 1), WOOD[3])
        roof = c.poly([(x - 3, base - 14), (x + 1, base - 20), (x + 27, base - 20), (x + 31, base - 14)])
        c.fill(roof, stripe)
        c.fill(roof & (((c.xx - x + 3) // 4) % 2 == 0), hexc('#f2ede3'))
        c.fill(roof & (c.yy >= base - 15), tuple(int(v * 0.7) for v in stripe))
        for k in range(-3, 32, 4):
            c.px(x + k, base - 13, stripe)
        c.fill(c.edge(roof | counter, inner=False) & (c.yy <= base), OUTL)
        for k, col in enumerate(('#e5b451', '#8a7f97', '#63a88f', '#f06579', '#bb98f4', '#d9c98f')):   # the goods
            c.fill(c.rect(x + 2 + k * 4, base - 8, x + 5 + k * 4, base - 6), hexc(col))
            c.px(x + 2 + k * 4, base - 8, hexc('#fff3c4'))
        c.fill(c.rect(x + 13, base - 13, x + 15, base - 11), GLOW[1])                                 # its lamp
        c.px(x + 14, base - 14, WOOD[2])

    stall(22, 200, hexc('#f06579'))
    stall(346, 200, hexc('#8bb6dc'))
    # crates and barrels in small heaps
    for x, base, n in ((66, 201, 3), (136, 203, 2), (330, 203, 2), (452, 202, 3)):
        for k in range(n):
            bx, by = x + k * 7 - (k // 2) * 3, base - (k // 2) * 6
            box = c.rect(bx, by - 6, bx + 6, by + 1)
            c.fill(box, WOOD[1 + k % 2])
            c.fill(c.rect(bx, by - 6, bx + 6, by - 5), WOOD[0])
            c.fill(c.rect(bx + 2, by - 5, bx + 3, by + 1) | c.rect(bx, by - 3, bx + 6, by - 2), WOOD[3])
            c.fill(c.edge(box, inner=False) & (c.yy <= by), OUTL)
    # a cart of ore that somebody left by the board
    cart = c.rect(456, 208, 474, 216)
    c.fill(cart, WOOD[1])
    c.fill(c.rect(456, 208, 474, 209), WOOD[0])
    for k in range(5):
        c.fill(c.ellipse(459 + k * 3.4, 207 - (k % 2), 2.2, 2), STONE[1 + k % 2])
        c.px(459 + k * 3, 206 - (k % 2), BRASS[1] if k % 2 else CYAN[1])
    for wx in (460, 470):
        wh = c.ellipse(wx, 217, 2.6)
        c.fill(wh, STONE[3])
        c.px(wx, 217, STONE[0])
    c.fill(c.edge(cart, inner=False), OUTL)
    # the lamps' light on the ground: warm, dithered, wider than tall
    for lx, ly, rx, ry in ((158, 207, 18, 4), (196, 207, 18, 4), (284, 207, 18, 4), (322, 207, 18, 4), (36, 204, 16, 3), (360, 204, 16, 3)):
        d = ((c.xx - lx) / float(rx)) ** 2 + ((c.yy - ly) / float(ry)) ** 2
        pool = (d <= 1) & c.alpha & (c.a.astype(int).sum(axis=2) < 250) & (c.yy > 200)
        c.fill(pool & (d <= 0.5), hexc('#4d4054'))
        c.fill(pool & (d > 0.5) & (((c.xx + c.yy) % 2) == 0), hexc('#4d4054'))
        c.fill(pool & (d <= 0.16), hexc('#5c4a5a'))


FRONT = ((22, 0, 2, 1, 'torch'), (50, 3, 0, 0, None), (78, 5, 1, 3, 'pick'), (404, 1, 4, 2, None), (432, 6, 3, 1, 'crate'), (458, 4, 0, 0, 'torch'))


def foreground(a, m):
    """The people nearest to us, seen from behind, at the picture's lower corners: they watch,
    they bob on the beat, one holds a torch, one a pickaxe, one brings a crate."""
    for x, shirt_i, hair_i, skin_i, item in FRONT:
        bob = 1 if ((m + x) // 6) % 2 == 0 else 0
        base = 278 - bob
        shirt = SHIRTS[shirt_i]
        dark = tuple(int(v * 0.65) for v in shirt)
        hair = [hexc('#3a2a22'), hexc('#d9b25a'), hexc('#5a3a2a'), hexc('#1c1727'), hexc('#a8744f')][hair_i]
        hair_d = tuple(int(v * 0.7) for v in hair)
        skin = SKIN[skin_i]
        up = item in ('torch', 'pick') or (item is None and ((m + x) // 12) % 2 == 0)

        def box(x0, y0, x1, y1, col):
            x0, x1, y0, y1 = max(0, x0), min(W, x1), max(0, y0), min(H, y1)
            if x1 > x0 and y1 > y0:
                a[y0:y1, x0:x1] = col

        top = base - 34
        box(x - 6, top - 1, x + 6, top + 11, OUTL)                           # head, from behind: hair
        box(x - 5, top, x + 5, top + 10, hair)
        box(x + 2, top, x + 5, top + 10, hair_d)
        box(x - 5, top, x + 5, top + 2, tuple(min(255, int(v * 1.25)) for v in hair))
        box(x - 3, top + 9, x + 3, top + 11, skin)                           # the neck
        box(x - 7, top + 11, x + 7, base, OUTL)                               # the body
        box(x - 6, top + 11, x + 6, base, shirt)
        box(x + 2, top + 11, x + 6, base, dark)
        box(x - 6, top + 11, x + 6, top + 12, tuple(min(255, int(v * 1.2)) for v in shirt))
        if item == 'crate':
            for side in (-1, 1):                                              # both arms up, the crate over the head
                ax = x + side * 8
                box(ax - 2, top - 3, ax + 2, top + 15, OUTL)
                box(ax - 1, top - 2, ax + 1, top + 14, shirt if side < 0 else dark)
                box(ax - 1, top - 2, ax + 1, top + 1, skin)
            box(x - 10, top - 14, x + 10, top - 2, OUTL)
            box(x - 9, top - 13, x + 9, top - 3, WOOD[1])
            box(x - 9, top - 13, x + 9, top - 12, WOOD[0])
            box(x - 1, top - 13, x + 1, top - 3, WOOD[3])
            box(x - 9, top - 8, x + 9, top - 7, WOOD[3])
            for k, col in enumerate((BRASS[1], CYAN[1], BRASS[2], STAGE[3])):
                box(x - 7 + k * 4, top - 16, x - 4 + k * 4, top - 13, col)
        else:
            for side in (-1, 1):
                raised = up and (side == 1 or item is None)
                ax = x + side * 8
                if raised:
                    box(ax - 2, top + 1, ax + 2, top + 15, OUTL)
                    box(ax - 1, top + 2, ax + 1, top + 14, shirt if side < 0 else dark)
                    box(ax - 1, top + 2, ax + 1, top + 5, skin)
                    if item == 'torch' and side == 1:
                        box(ax - 1, top - 8, ax + 1, top + 3, WOOD[1])
                        fl = (m // 2) % 3
                        box(ax - 2, top - 13 - (fl == 1), ax + 2, top - 8, GLOW[2])
                        box(ax - 1, top - 12 - (fl == 1), ax + 1, top - 8, GLOW[0])
                        if fl == 2:
                            box(ax + 1, top - 15, ax + 2, top - 13, GLOW[1])
                    if item == 'pick' and side == 1:
                        box(ax - 1, top - 12, ax + 1, top + 3, WOOD[1])
                        box(ax - 6, top - 14, ax + 6, top - 11, OUTL)
                        box(ax - 5, top - 13, ax + 5, top - 12, STONE[0])
                        box(ax - 6, top - 12, ax - 4, top - 10, STONE[1]); box(ax + 4, top - 12, ax + 6, top - 10, STONE[1])
                else:
                    box(ax - 2, top + 11, ax + 2, top + 26, OUTL)
                    box(ax - 1, top + 12, ax + 1, top + 25, shirt if side < 0 else dark)


RUNES = ['X.X XXX .X.', 'XXX X.. XXX', '.X. XXX X.X', 'X.. XXX ..X', 'XXX .X. XXX', 'X.X .X. X.X', '.XX XX. .XX']


def walkers(m):
    """The little people: where each one is at frame m, what they do, and their gift in flight.

    Each comes in from an edge, walks to a place at the foot, raises what they carry, the
    gift flies up into the crystal, and they walk off the way they came."""
    out = []
    for i in range(24):
        side = -1 if i % 2 == 0 else 1
        start = -26 + i * 3 + (i % 3) * 2                      # the frame they appear at
        stand = CX + side * (42 + (i * 17) % 78)                # where they stop
        row = GY + 5 + (i * 7) % 30                             # nearer rows are lower on the screen
        edge = -8 if side < 0 else W + 8
        reach = abs(stand - edge)
        speed = 4.2 + (i % 3) * 0.5
        walk_in = reach / speed
        t = m - start
        if t < 0:
            continue
        gift_at = start + walk_in + 3
        if t < walk_in:
            x, state = edge + (stand - edge) * (t / walk_in), 'walk'
        elif t < walk_in + 12:
            x, state = stand, 'give' if t < walk_in + 9 else 'stand'
        else:
            back = (t - walk_in - 12) * speed
            x, state = stand - side * back * -1, 'walk'
            x = stand + (edge - stand) * min(1.0, back / reach)
            side = -side
        out.append(dict(i=i, x=x, y=row, side=side, state=state, t=t, gift_at=gift_at, stand=stand))
    return out


def person(a, w, m):
    """A person of ten pixels: head, shirt, legs that step; the one who gives lifts an arm."""
    i, x, y = w['i'], int(round(w['x'])), int(w['y'])
    skin, shirt = SKIN[i % 4], SHIRTS[i % 8]
    dark = tuple(int(v * 0.6) for v in shirt)
    hair = [hexc('#3a2a22'), hexc('#d9b25a'), hexc('#5a3a2a'), hexc('#1c1727'), hexc('#a8744f')][i % 5]
    step = (int(w['t']) // 2) % 2 if w['state'] == 'walk' else 0

    def px(dx, dy, col):
        xx, yy = x + dx, y + dy
        if 0 <= xx < W and 0 <= yy < H:
            a[yy, xx] = col

    for dx in (-1, 0, 1):                                       # an outline's worth of shadow at the feet
        px(dx, 0, hexc('#1c1727'))
    # legs
    px(-1 + step, -1, hexc('#2d2538')); px(-1 + step, -2, hexc('#2d2538'))
    px(1 - step, -1, hexc('#3a3046')); px(1 - step, -2, hexc('#3a3046'))
    # body
    for dy in (-3, -4, -5, -6):
        px(-1, dy, dark); px(0, dy, shirt); px(1, dy, shirt)
    # head
    for dy in (-7, -8):
        px(-1, dy, skin); px(0, dy, skin); px(1, dy, skin)
    px(-1, -9, hair); px(0, -9, hair); px(1, -9, hair)
    px(-w['side'], -8, hair)
    # the arm, and what it carries until it has flown
    if w['state'] == 'give':
        px(w['side'] * 2, -7, skin); px(w['side'] * 2, -8, skin)
    elif w['state'] == 'walk' and m < w['gift_at']:
        px(w['side'] * 2, -5, GIFTS[i % 6]); px(w['side'] * 2, -4, tuple(int(v * 0.7) for v in GIFTS[i % 6]))


def frame(m):
    base, body = static()
    a = base.copy()
    yy, xx = np.mgrid[0:H, 0:W]
    ws = walkers(m)
    # ---- gifts in flight and the moments they arrive ----
    arrivals = []
    flights = []
    for w in ws:
        ft = m - w['gift_at']
        if 0 <= ft < 10:
            u = ft / 10.0
            sx, sy = w['stand'] + (2 if w['stand'] < CX else -2), w['y'] - 9
            x = sx + (CX - sx) * u
            y = sy + (36 - sy) * u - math.sin(u * math.pi) * 34
            flights.append((x, y, GIFTS[w['i'] % 6], u))
        if 10 <= ft < 16:
            arrivals.append(ft - 10)
    flare = max([1 - t / 6.0 for t in arrivals], default=0.0)
    # how full the goal is: it climbs with every gift and is full at the end
    pct = min(100.0, 81 + 19 * (m / 66.0) ** 1.15)
    warm = (pct / 100.0) ** 4
    crystal = tuple(int(CYAN[2][k] * (1 - warm ** 3) + GOLD[2][k] * warm ** 3) for k in range(3))
    bright = tuple(int(CYAN[0][k] * (1 - warm ** 3) + GOLD[0][k] * warm ** 3) for k in range(3))
    # ---- the beam: a thin column into the sky, wider while a gift arrives ----
    bw = 1 + (2 if flare > 0.4 else 1 if flare > 0 else 0)
    beam = (np.abs(xx - CX) <= bw) & (yy < 30)
    a[beam] = bright
    halo = (np.abs(xx - CX) <= bw + 3) & (yy < 30) & ~beam & (((xx + yy + m) % 3) == 0)
    a[halo] = crystal
    # ---- the crystal over the tip: a long diamond that bobs, shards circling it ----
    cy = 36 + int(round(math.sin(m / 5.0) * 1.5))
    size = 1.0 + 0.35 * flare
    dia = (np.abs(xx - CX) / (5.0 * size) + np.abs(yy - cy) / (10.0 * size)) <= 1.0
    a[dia] = crystal
    a[dia & (xx < CX) & (yy < cy)] = bright
    a[dia & (xx > CX) & (yy > cy)] = tuple(int(v * 0.6) for v in crystal)
    ring = np.zeros((H, W), bool)
    p = np.pad(dia, 1)
    ring = ~dia & (p[:-2, 1:-1] | p[2:, 1:-1] | p[1:-1, :-2] | p[1:-1, 2:])
    a[ring] = OUTL
    for k in range(5):
        ang = m / 6.0 + k * 2 * math.pi / 5
        sx, sy = CX + math.cos(ang) * 13, cy + math.sin(ang) * 4 + math.sin(ang * 2) * 1
        if math.sin(ang) > -0.3 or abs(sx - CX) > 6:
            a[int(sy) - 1:int(sy) + 2, int(sx)] = crystal
            a[int(sy), int(sx)] = bright
    # ---- runes run up the trunk: each lights in turn, all of them when a gift lands ----
    for r in range(6):
        ry = GY - 19 - 14 - r * 16
        on = ((m // 3) % 9 == r) or flare > 0.3
        col = bright if on else tuple(int(crystal[k] * 0.6 + 20) for k in range(3))
        for j, row in enumerate(RUNES[r % 7].split()):
            for q, v in enumerate(row):
                if v == 'X':
                    a[ry + j, CX - 1 + q] = col
    # ---- the ring of light on the paving that runs outwards with each gift ----
    dxn, dyn = (xx - CX) / 1.0, (yy - GY) * 3.2
    rad = np.sqrt(dxn * dxn + dyn * dyn)
    for t in arrivals:
        r0 = 40 + t * 30
        wave = (np.abs(rad - r0) < 2.0) & (yy > 190) & (((xx + yy) % 2) == 0)
        a[wave] = crystal
    # ---- lanterns on the pylons (they flicker), flags in the stages' colours (they wave) ----
    for i, px_ in enumerate((158, 196, 284, 322)):
        base = 201 + (0 if i in (1, 2) else 3)
        top = base - (44 if i in (1, 2) else 52)
        fl = (m + i * 5) % 9 != 0
        a[top - 7:top - 2, px_ - 1:px_ + 2] = GLOW[1] if fl else GLOW[2]
        a[top - 5, px_] = GLOW[0]
        a[top - 8, px_ - 1:px_ + 2] = BRASS[3]
        if fl:
            for dx, dy in ((-3, -5), (3, -5), (0, -10), (-2, -3), (2, -7)):
                if ((dx + dy + m // 2) % 2) == 0:
                    a[top + dy, px_ + dx] = GLOW[3]
        col = STAGE[i if i < 2 else i + 1]
        side = 1 if i < 2 else -1
        for k in range(7):
            wy = int(round(math.sin((m / 2.5) + k * 0.9 + i) * (k / 6.0) * 1.6))
            x = px_ + side * (2 + k)
            a[top + 6 + wy:top + 6 + wy + 8 - (k // 3), x] = col if k % 3 else tuple(int(v * 0.75) for v in col)
    # ---- what the pedestals show: an item that turns (two frames) and a gauge ----
    for i, px_ in enumerate((176, 210, 270, 304)):
        base = 204 + (2 if i in (0, 3) else 0)
        col = [STONE[0], BRASS[2], hexc('#bb98f4'), hexc('#63a88f')][i]
        bob = int(round(math.sin(m / 4.0 + i) * 1))
        wide = 2 if ((m // 4) + i) % 2 == 0 else 1
        a[base - 19 + bob:base - 14 + bob, px_ - wide + 1:px_ + wide] = col
        a[base - 19 + bob, px_ - wide + 1:px_ + wide] = tuple(min(255, int(v * 1.25)) for v in col)
        fillw = int(round(9 * min(1.0, (pct + [6, -4, 2, 0][i]) / 100.0)))
        a[base - 4, px_ - 4:px_ + 5] = OUTL
        a[base - 4, px_ - 4:px_ - 4 + fillw] = col
    # ---- people, sorted so the near ones cover the far ones; gifts over them ----
    for w in sorted(ws, key=lambda w: w['y']):
        person(a, w, m)
    for x, y, col, u in flights:
        x, y = int(round(x)), int(round(y))
        a[y:y + 2, x:x + 2] = col
        a[y, x] = tuple(min(255, int(v * 1.3)) for v in col)
        if u > 0.2:
            a[y + 3, x - (1 if x > CX else -1)] = crystal            # a spark trailing behind
    # ---- fireflies ----
    for i in range(12):
        bx, by = 20 + (i * 131) % 440, 150 + (i * 37) % 40
        x = int(bx + math.sin(m / 9.0 + i) * 7)
        y = int(by + math.sin(m / 6.0 + i * 1.7) * 4)
        if math.sin(m / 3.0 + i * 2.3) > 0 and abs(x - CX) > 30:
            a[y, x] = hexc('#c6dc6e')
    # ---- the goal's bar, the way the game shows it: name, then a notched bar ----
    name = 'FUNDAMENT DES KRONWERKS  %d%%' % int(pct)
    a[4:29, CX - 100:CX + 100] = hexc('#1c1727')
    a[4, CX - 100:CX + 100] = BRASS[4]
    a[28, CX - 100:CX + 100] = OUTL
    font.centred(a, name, CX, 8, BRASS[1], 1)
    bx0, bx1, by = CX - 92, CX + 92, 20
    a[by - 1:by + 6, bx0 - 1:bx1 + 1] = OUTL
    a[by:by + 5, bx0:bx1] = hexc('#3a3046')
    fw = int(round((bx1 - bx0) * pct / 100.0))
    a[by:by + 5, bx0:bx0 + fw] = BRASS[2]
    a[by, bx0:bx0 + fw] = BRASS[0]
    a[by + 4, bx0:bx0 + fw] = BRASS[4]
    for k in range(1, 10):
        nx = bx0 + (bx1 - bx0) * k // 10
        a[by:by + 5, nx] = OUTL
    return a, pct
