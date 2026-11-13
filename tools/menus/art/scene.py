#!/usr/bin/env python3
"""The Kronwerke menu artwork: the works in the valley, drawn as pixel art on a 480x270 grid.

    scene.py <outdir>            writes title_dusk.png and title_night.png (1920x1080) and previews

Everything is drawn by this script, nothing is traced or imported. Light comes from the right.
"""
import sys, os
import numpy as np
from px import Canvas, cols, hexc, noise1d, noise2d, smooth

W, H = 480, 270
HORIZON = 150

PAL = {
    'dusk': dict(
        sky=cols('#232c5a', '#33407a', '#4d4d8c', '#7a5a95', '#b06a86', '#de8870', '#f2ab66', '#f8cf7e', '#fde9ae'),
        sun=cols('#fff6d0', '#fde9ae', '#f8cf7e'),
        cloud=cols('#8a6a9c', '#b77d95', '#ee9f7a', '#fbd08c'),
        far=cols('#8d76a6', '#74669c', '#5f5a90'), far_lit=hexc('#c58fa0'), snow=hexc('#f3c9b0'),
        mid=cols('#5a5488', '#484577', '#3a3a68'), mid_lit=hexc('#8f6f92'),
        lake=cols('#f6c67c', '#e59a73', '#b9708a', '#7d5c94', '#544f8a', '#3c4379'), glint=hexc('#fdebad'),
        forest=cols('#1b2740', '#22344a', '#2c4652'), forest_lit=hexc('#5e7a5c'),
        grass=cols('#d4d86e', '#9cc25c', '#62a054', '#3f7d50', '#2f6049', '#234840'),
        fore=cols('#2c5a4c', '#234a45', '#1b3a3c', '#152c33'), leaf=hexc('#3f7d58'),
        path=cols('#e9c98a', '#c99a66', '#9a6c50'),
        stone=cols('#b9b6c4', '#8c8ba6', '#646686', '#474a69', '#30324d'),
        brick=cols('#e39a5c', '#c26a44', '#9a4a3c', '#733538', '#4f2634'),
        brass=cols('#fff3c4', '#f7dc86', '#e5b451', '#b98530', '#8a5a24', '#5c3a1e'),
        roof=cols('#6e78a4', '#4d5682', '#363d62', '#252a47', '#1a1d33'),
        wood=cols('#b98a52', '#8f6238', '#6a4530', '#472c26'),
        glow=cols('#fff8dc', '#fde9ae', '#f9c860', '#f08a3c'),
        smoke=cols('#e7ad98', '#b98da0', '#8a739a', '#64598a'),
        dark=hexc('#1a1830'), rune=hexc('#fde9ae'), beam=hexc('#fde9ae'),
    ),
}


def lerp_pts(pts, n):
    xs, ys = zip(*pts)
    return np.interp(np.arange(n), xs, ys)


def sky(c, P, night):
    t = c.yy / float(HORIZON)
    sx, sy = 268, 122
    d = np.hypot((c.xx - sx) / 1.6, c.yy - sy)
    t = np.clip(t * 0.96 + 0.22 * np.exp(-(d / 70.0) ** 2), 0, 1)
    c.ramp(c.rect(0, 0, W, HORIZON + 2), P['sky'], t, soft=0.5)
    if night:
        rng = np.random.default_rng(7)
        for _ in range(150):
            x, y = int(rng.integers(0, W)), int(rng.integers(0, HORIZON - 15))
            c.px(x, y, P['star'][int(rng.integers(0, 2))])
        for x, y in ((60, 30), (150, 58), (232, 22), (318, 70), (410, 40), (455, 96), (26, 92)):
            for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
                c.px(x + dx, y + dy, P['star'][0])
            c.px(x + 2, y, P['star'][1]); c.px(x - 2, y, P['star'][1]); c.px(x, y + 2, P['star'][1]); c.px(x, y - 2, P['star'][1])
    return sx, sy


def sun(c, P, sx, sy, night):
    if night:
        mx, my, r = 286, 58, 15
        halo = c.ellipse(mx, my, r + 7) & ~c.ellipse(mx, my, r)
        c.dither(halo, P['sky'][3], P['sky'][5], 0.5)
        c.fill(c.ellipse(mx, my, r), P['moon'][1])
        c.fill(c.ellipse(mx - 2, my - 2, r - 3), P['moon'][0])
        for cx, cy, cr in ((mx - 6, my - 4, 3), (mx + 5, my + 3, 4), (mx + 2, my - 8, 2), (mx - 4, my + 7, 2)):
            c.fill(c.ellipse(cx, cy, cr), P['moon'][2])
        return
    for r, t in ((40, 0.3), (31, 0.55), (25, 0.85)):
        ring = c.ellipse(sx, sy, r) & (c.yy < HORIZON + 2)
        c.dither(ring, P['sky'][7], P['sky'][8], t)
    c.fill(c.ellipse(sx, sy, 19) & (c.yy < HORIZON + 2), P['sun'][1])
    c.fill(c.ellipse(sx, sy, 17) & (c.yy < HORIZON + 2), P['sun'][0])


def cloud(c, P, cx, base, width, seed, flat=False):
    rng = np.random.default_rng(seed)
    m = c.none()
    n = max(3, width // 9)
    for i in range(n):
        f = (i + 0.5) / n
        r = (3 + 9 * np.sin(np.pi * f) ** 0.8 * rng.uniform(0.7, 1.1)) * (0.55 if flat else 1.0)
        x = cx - width / 2 + f * width + rng.uniform(-2, 2)
        m |= c.ellipse(x, base - r * 0.55, r * 1.25, r)
    m &= c.yy < base
    m |= c.rect(cx - width // 2 + 3, base - 2, cx + width // 2 - 3, base)
    ys = np.where(m, c.yy, 10 ** 6).min(axis=0)
    top = np.where(ys < 10 ** 6, ys, base)[None, :]
    t = np.clip((c.yy - top) / np.maximum(1.0, base - top), 0, 1)
    c.ramp(m, P['cloud'], t ** 1.4, soft=0.0)
    c.fill(m & ~c.shift(m, 0, -1) & (c.yy >= base - 1), P['cloud'][-1])


def ridge(c, P, key, base, amp, seed, lit, snow=None, sharp=0.0):
    n = noise1d(W, seed) * 0.5 + 0.5
    peaks = 1 - np.abs(noise1d(W, seed + 1, ((27, 1.0), (11, 0.4))))
    ys = HORIZON - (base + amp * ((1 - sharp) * n + sharp * n * peaks))
    ys = np.round(ys).astype(int)
    m = c.below(ys) & (c.yy < HORIZON + 2)
    depth = (c.yy - ys[None, :]) / 34.0
    c.ramp(m, P[key], depth, soft=0.3)
    slope = smooth(np.gradient(smooth(ys, 1)), 2)
    th = np.clip(slope * 16.0, 0, 13)[None, :]
    d = c.yy - ys[None, :]
    face = m & (d < th)
    c.fill(face, lit)
    c.dither(m & (d >= th) & (d < th + 3) & (th > 1), P[key][0], lit, 0.45)
    if snow is not None:
        high = ys[None, :] < HORIZON - base - amp * 0.6
        c.fill(face & high & (d < th * 0.55), snow)
        c.fill(m & high & (d < 2), snow)
    return ys


def lake(c, P, sx, night):
    m = c.rect(0, HORIZON, W, 236)
    t = (c.yy - HORIZON) / 55.0
    c.ramp(m, P['lake'], t, soft=0.45)
    rng = np.random.default_rng(11)
    for _ in range(170):
        y = int(rng.integers(HORIZON + 2, 212))
        x = int(rng.integers(0, W))
        ln = int(rng.integers(3, 14))
        k = min(len(P['lake']) - 1, int((y - HORIZON) / 55.0 * (len(P['lake']) - 1)))
        col = P['lake'][max(0, k - 1)] if rng.random() < 0.6 else P['lake'][min(len(P['lake']) - 1, k + 1)]
        c.fill(c.rect(x, y, x + ln, y + 1), col)
    gx = 286 if night else sx
    for y in range(HORIZON + 1, 212, 2):
        half = 3 + (y - HORIZON) * 0.38
        for _ in range(3):
            x = int(gx + rng.uniform(-half, half))
            ln = int(rng.integers(2, 4 + (y - HORIZON) // 6))
            c.fill(c.rect(x - ln // 2, y, x + ln // 2 + 1, y + 1), P['glint'])


def pine(c, P, x, base, h, tone, lit=True):
    m = c.none()
    w = max(3, int(h * 0.42))
    tiers = max(3, h // 5)
    for i in range(tiers):
        f = i / tiers
        ty = base - h + int(f * (h - 3))
        tw = int(2 + (w - 2) * (f + 1.0 / tiers))
        th = int(h / tiers) + 3
        m |= c.poly([(x, ty), (x + tw, ty + th), (x - tw, ty + th)])
    m |= c.rect(x, base - 3, x + 1, base)
    c.fill(m, P['forest'][tone])
    if lit:
        right = m & ~c.shift(m, -1, 0) & (c.xx > x)
        c.fill(right, P['forest_lit'])
        c.dither(m & (c.xx > x) & ~right, P['forest'][tone], P['forest'][min(2, tone + 1)], 0.35)


def far_shore(c, P):
    top = lerp_pts([(276, 152), (300, 149), (330, 144), (372, 136), (420, 126), (480, 114)], W)
    top = np.round(top + noise1d(W, 5, ((23, 1.0), (9, 0.5))) * 2.2).astype(int)
    shore = np.round(lerp_pts([(276, 153), (330, 160), (400, 172), (480, 188)], W) + noise1d(W, 6, ((29, 1.0), (10, 0.5))) * 1.5).astype(int)
    m = c.below(top) & ~c.below(shore) & (c.xx >= 276)
    c.ramp(m, [P['forest'][2], P['forest'][1], P['forest'][0]], (c.yy - top[None, :]) / 24.0, soft=0.4)
    rng = np.random.default_rng(3)
    for row, (off, tone, lo, hi) in enumerate(((2, 1, 12, 19), (9, 1, 12, 20), (18, 0, 13, 21), (28, 0, 14, 22), (40, 0, 14, 23))):
        for x in range(282 + row * 3, W + 8, 7):
            xx = x + int(rng.integers(-2, 3))
            k = min(W - 1, xx)
            base = int(top[k]) + off
            if base > shore[k] + 1 or base - 4 < top[k]:
                continue
            pine(c, P, xx, min(base, int(shore[k])), int(rng.integers(lo, hi)), tone)
    # dark bank and its reflection in the water
    bank = c.below(shore - 2) & ~c.below(shore + 1) & (c.xx >= 276)
    c.fill(bank, P['forest'][0])
    refl = c.below(shore + 1) & ~c.below(shore + 9) & (c.xx >= 276)
    c.dither(refl, P['lake'][-1], P['forest'][0], np.clip(1 - (c.yy - shore[None, :]) / 9.0, 0, 1) * 0.9)
    return top


def ground(c, P):
    g = lerp_pts([(0, 181), (30, 176), (58, 172), (240, 172), (268, 180), (300, 195), (340, 207), (400, 216), (480, 222)], W)
    g = np.round(g + noise1d(W, 21, ((31, 1.0), (11, 0.4))) * 1.2).astype(int)
    g[58:240] = 172
    m = c.below(g)
    depth = np.clip(c.yy - g[None, :], 0, None) / 64.0
    patch = noise2d(W, H, 77, period=30, octaves=3)
    sunny = np.clip((c.xx - 150) / 330.0, 0, 1) * 0.12
    t = 0.12 + depth ** 0.85 * 0.62 + (patch - 0.5) * 0.42 - sunny
    c.ramp(m, P['grass'], t, soft=0.28)
    c.fill(m & (c.yy == g[None, :]), P['grass'][0])
    c.fill(m & (c.yy == g[None, :] + 1), P['grass'][1])
    rng = np.random.default_rng(31)
    n = len(P['grass'])
    for _ in range(300):
        x = int(rng.integers(0, W)); y = int(g[x] + rng.integers(4, 74))
        if y >= H or x >= W - 1:
            continue
        cur = tuple(int(v) for v in c.a[y, x])
        k = P['grass'].index(cur) if cur in P['grass'] else 3
        col = P['grass'][max(0, k - 1)]
        c.px(x, y, col); c.px(x + 1, y - 1, col)
        if rng.random() < 0.4:
            c.px(x - 1, y - 1, col)
    return g


def foreground(c, P):
    f = lerp_pts([(0, 226), (60, 236), (140, 246), (260, 252), (360, 250), (430, 242), (480, 232)], W)
    f = np.round(f + noise1d(W, 41, ((19, 1.0), (7, 0.5))) * 1.5).astype(int)
    m = c.below(f)
    c.ramp(m, P['fore'], (c.yy - f[None, :]) / 30.0, soft=0.5)
    c.fill(m & (c.yy == f[None, :]), P['grass'][3])
    rng = np.random.default_rng(43)

    def bush(cx, cy, r, n):
        b = c.none()
        for _ in range(n):
            a, d = rng.uniform(0, 6.28), rng.uniform(0, r * 0.7)
            b |= c.ellipse(cx + np.cos(a) * d * 1.5, cy + np.sin(a) * d * 0.7, rng.uniform(r * 0.35, r * 0.6))
        c.fill(b, P['fore'][2])
        c.fill(b & c.shift(b, 2, 3), P['fore'][3])
        top = b & ~c.shift(b, 0, 1)
        c.fill(top, P['fore'][0])
        for _ in range(int(r * 2.2)):
            x, y = int(cx + rng.uniform(-r * 1.4, r * 1.4)), int(cy + rng.uniform(-r * 0.8, r * 0.6))
            if 0 <= x < W - 2 and 0 <= y < H - 1 and b[y, x]:
                c.px(x, y, P['leaf']); c.px(x + 1, y, P['leaf']); c.px(x + 1, y - 1, P['fore'][0])

    bush(22, 262, 30, 16); bush(86, 272, 22, 12); bush(455, 262, 34, 18); bush(392, 274, 20, 10); bush(250, 280, 18, 8)
    for _ in range(26):
        x = int(rng.integers(100, 390)); y = int(f[x] + rng.integers(4, 22))
        if y < H - 1:
            col = P['flower'][int(rng.integers(0, len(P['flower'])))]
            c.px(x, y, col); c.px(x + 1, y, col); c.px(x, y - 1, col)
            c.px(x, y + 1, P['fore'][0])
    return f


PAL['dusk']['flower'] = cols('#fde9ae', '#f08a8a', '#c9a4f0', '#fff8dc')
PAL['dusk']['star'] = cols('#fff8dc', '#c9c4e8')
PAL['dusk']['moon'] = cols('#fff8dc', '#e4e0ee', '#c2bfd8')
PAL['dusk']['gem'] = cols('#f06579', '#8bb6dc', '#bb98f4', '#8bb6dc', '#f06579')


def night_palette(D):
    tint = np.array(hexc('#16204e'), float)

    def cool(col, k=0.5, mul=0.62):
        v = np.array(col, float) * mul
        return tuple(int(x) for x in (v * (1 - k) + tint * k))

    N = {}
    for key, val in D.items():
        if key in ('glow', 'rune', 'beam', 'star', 'moon', 'gem'):
            N[key] = val
        elif isinstance(val, list):
            N[key] = [cool(v) for v in val]
        else:
            N[key] = cool(val)
    N['sky'] = cols('#0c0f2c', '#11163c', '#171f4d', '#1e2a60', '#273872', '#324784', '#415a96', '#5a74aa', '#7f95c0')
    N['cloud'] = cols('#b4bfe2', '#8794c2', '#5d6aa2', '#404b80')
    N['lake'] = cols('#5a74aa', '#415a96', '#2c3f80', '#1e2a60', '#161e4a', '#10163a')
    N['glint'] = hexc('#dfe6ff')
    N['sun'] = cols('#eef2ff', '#c4d0f4', '#9aa8d8')
    N['far_lit'] = hexc('#6f7fb4'); N['snow'] = hexc('#c4d0f4'); N['mid_lit'] = hexc('#4d5c96')
    N['forest_lit'] = hexc('#3a5a70')
    N['smoke'] = cols('#aab4d8', '#7c88b4', '#56608e', '#3c446e')
    N['brass'] = [cool(v, 0.3, 0.8) for v in D['brass']]
    return N


PAL['night'] = night_palette(PAL['dusk'])


def build(mode='dusk', stage=99):
    P = PAL[mode]
    night = mode == 'night'
    c = Canvas(W, H)
    sx, sy = sky(c, P, night)
    sun(c, P, sx, sy, night)
    for cx, base, w, seed, flat in ((70, 44, 84, 1, False), (205, 30, 60, 2, False), (372, 58, 96, 3, False), (150, 84, 70, 4, True),
                                    (430, 24, 50, 5, False), (318, 104, 80, 6, True), (20, 108, 60, 8, True), (240, 66, 40, 9, True)):
        cloud(c, P, cx, base, w, seed, flat)
    ridge(c, P, 'far', 14, 44, 100, P['far_lit'], P['snow'])
    ridge(c, P, 'mid', 4, 24, 200, P['mid_lit'])
    lake(c, P, sx, night)
    far_shore(c, P)
    g = ground(c, P)
    if stage > 0:
        import works
        works.draw(c, P, g, night)
    foreground(c, P)
    return c


if __name__ == '__main__':
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    stage = int(sys.argv[2]) if len(sys.argv) > 2 else 99
    for mode in PAL:
        c = build(mode, stage)
        c.image(4).save(os.path.join(out, f'title_{mode}.png'), optimize=True)
        c.image(3).save(os.path.join(out, f'preview_{mode}.png'))
        print('wrote', mode)
