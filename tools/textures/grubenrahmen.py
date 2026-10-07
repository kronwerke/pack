#!/usr/bin/env python3
"""The Grubenrahmen and the Minenportal: textures with depth.

The frame is dark slate bound in riveted iron, with blue crystal veins carved into it that
run on across neighbouring blocks (the veins are periodic, so every tile joins every other).
Every texture comes with labPBR maps for shader packs: _n (normal, ambient occlusion, height
for parallax) and _s (smoothness, iron as metal, crystal veins as light). Without a shader the
depth is baked into the colours: light from the top left.

Connected textures through Athena like the obelisk (see ctm.py): the iron band only runs
along the outline of a group of frame blocks. The tiles go into this pack's
assets/kronwerke/textures/block/ctm/grubenrahmen and a client script writes the model into
KubeJS's 'last' pack. The plain textures (a lone block, and the animated portal) go into
Kronwerke Core, whose path is the first argument.

    python3 tools/textures/grubenrahmen.py ../core-repo
"""
import json
import os
import sys

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.join(HERE, "..", "..")
S = 32  # pixels per block
RNG = np.random.default_rng(1871)


def periodic_noise(size, falloff, seed, lo=1, hi=None):
    """Noise that tiles: random phases in the frequency domain, power falling with frequency."""
    rng = np.random.default_rng(seed)
    f = np.fft.fftfreq(size) * size
    fx, fy = np.meshgrid(f, f)
    r = np.sqrt(fx ** 2 + fy ** 2)
    amp = np.where(r < lo, 0, 1 / np.maximum(r, 1) ** falloff)
    if hi is not None:
        amp = np.where(r > hi, 0, amp)
    spec = amp * np.exp(2j * np.pi * rng.random((size, size)))
    n = np.real(np.fft.ifft2(spec))
    n -= n.mean()
    return n / (np.abs(n).max() + 1e-9)


def smooth(a, b, x):
    t = np.clip((x - a) / (b - a), 0, 1)
    return t * t * (3 - 2 * t)


# ---- the frame ----------------------------------------------------------------------------

def surface():
    """Stone and veins, the same for every tile so the quarters join."""
    fine = periodic_noise(S, 1.1, 11, lo=3)
    coarse = periodic_noise(S, 2.0, 12, lo=1, hi=6)
    stone_h = 0.58 + 0.10 * fine + 0.07 * coarse
    # veins: ridges of a low frequency noise, warped a little so they branch
    warp = periodic_noise(S, 2.0, 13, lo=1, hi=4)
    v = periodic_noise(S, 2.2, 14, lo=1, hi=5)
    yy, xx = np.mgrid[0:S, 0:S]
    sx = (xx + 3 * warp).astype(int) % S
    v = v[yy, sx]
    ridge = 1 - np.abs(v) * 2.2
    core = smooth(0.80, 0.93, ridge)
    halo = smooth(0.45, 0.85, ridge)
    # a second, thinner set of veins
    v2 = periodic_noise(S, 1.6, 15, lo=2, hi=8)
    ridge2 = 1 - np.abs(v2) * 3.0
    core = np.maximum(core, 0.8 * smooth(0.93, 0.99, ridge2))
    halo = np.maximum(halo, 0.5 * smooth(0.8, 0.97, ridge2))
    h = stone_h - 0.22 * halo + 0.12 * core  # carved channels, crystal standing in them
    return h, core, halo, fine


BAND = 5  # the iron band's width in pixels


def band_mask(top, bottom, left, right):
    """Where the iron band is (1), with its inner seam (separately)."""
    m = np.zeros((S, S))
    seam = np.zeros((S, S))
    yy, xx = np.mgrid[0:S, 0:S]
    for on, d in ((top, yy), (bottom, S - 1 - yy), (left, xx), (right, S - 1 - xx)):
        if not on:
            continue
        m = np.maximum(m, (d < BAND).astype(float))
        seam = np.maximum(seam, (d == BAND).astype(float))
    seam = seam * (1 - m)
    return m, seam


def band_height(top, bottom, left, right):
    """The band: a raised flat strip with a bevel on both sides and domed rivets every 8 px."""
    yy, xx = np.mgrid[0:S, 0:S]
    h = np.zeros((S, S))
    for on, d, along in ((top, yy, xx), (bottom, S - 1 - yy, xx), (left, xx, yy), (right, S - 1 - xx, yy)):
        if not on:
            continue
        inside = d < BAND
        prof = np.where(d == 0, 0.80, np.where(d == BAND - 1, 0.78, 0.92))
        # rivets on the band's middle line, every 8 px
        rd = np.sqrt((d - 2) ** 2 + ((along % 8) - 3.5) ** 2)
        rivet = np.where(rd < 1.8, 0.14 * np.sqrt(np.clip(1 - (rd / 1.8) ** 2, 0, 1)), 0)
        h = np.where(inside, np.maximum(h, prof + rivet), h)
    return h


def normals(h, strength=3.2):
    gx = (np.roll(h, -1, 1) - np.roll(h, 1, 1)) / 2
    gy = (np.roll(h, -1, 0) - np.roll(h, 1, 0)) / 2
    n = np.dstack((-gx * strength, -gy * strength, np.ones_like(h)))
    n /= np.linalg.norm(n, axis=2, keepdims=True)
    return n


def occlusion(h):
    blur = sum(np.roll(np.roll(h, dy, 0), dx, 1) for dy in range(-2, 3) for dx in range(-2, 3)) / 25
    return np.clip(1 - np.maximum(0, blur - h) * 4, 0.55, 1)


def frame_tile(top, bottom, left, right):
    stone_h, core, halo, fine = surface()
    band, seam = band_mask(top, bottom, left, right)
    bh = band_height(top, bottom, left, right)
    h = np.where(band > 0, bh, stone_h)
    h = np.where(seam > 0, 0.38, h)
    core = core * (1 - band) * (1 - seam)
    halo = halo * (1 - band) * (1 - seam)

    # colours
    slate = np.dstack([46 + 18 * fine, 49 + 18 * fine, 62 + 20 * fine])
    tint = np.array([34, 92, 160])
    stone = slate * (1 - 0.55 * halo[..., None]) + tint * (0.55 * halo[..., None])
    crystal = np.array([132, 214, 255])
    stone = stone * (1 - core[..., None]) + crystal * core[..., None]
    brushed = periodic_noise(S, 0.6, 21, lo=4)
    iron = np.dstack([92 + 12 * brushed, 95 + 12 * brushed, 106 + 12 * brushed])
    riv = (bh > 0.95) & (band > 0)
    iron = np.where(riv[..., None], np.array([150, 150, 160]), iron)
    col = np.where(band[..., None] > 0, iron, stone)
    col = np.where(seam[..., None] > 0, np.array([18, 18, 24]), col)

    # depth baked in: light from the top left, crystal glows and is not shaded
    n = normals(h, 4.5)
    light = np.array([-0.55, -0.6, 0.58])
    light /= np.linalg.norm(light)
    lam = np.clip((n * light).sum(axis=2), 0, 1)
    ao = occlusion(h)
    shade = (0.45 + 0.85 * lam) * ao
    shade = shade * (1 - core) + 1.0 * core
    rgb = np.clip(col * shade[..., None], 0, 255).astype(np.uint8)
    albedo = Image.fromarray(np.dstack([rgb, np.full((S, S), 255, np.uint8)]), "RGBA")

    # labPBR normal: RG normal, B ambient occlusion, A height
    nrm = np.dstack([(n[..., 0] * 0.5 + 0.5) * 255, (n[..., 1] * 0.5 + 0.5) * 255, ao * 255, np.clip(h, 0.004, 1) * 255])
    normal = Image.fromarray(nrm.astype(np.uint8), "RGBA")

    # labPBR specular: R smoothness, G f0 or metal (230 is iron), B porosity, A emission (255 none)
    smooth_ = np.where(band > 0, 150, np.where(core > 0.3, 215, 45 + 20 * halo))
    f0 = np.where(band > 0, 230, np.where(core > 0.3, 28, 10))
    por = np.where(band > 0, 0, np.where(core > 0.3, 0, 45))
    emis = np.where(core > 0.05, np.clip(254 * core, 1, 254), np.where(halo > 0.3, 60 * halo, 255))
    spec = Image.fromarray(np.dstack([smooth_, f0, por, emis]).astype(np.uint8), "RGBA")
    return albedo, normal, spec


def save_set(folder, name, imgs):
    os.makedirs(folder, exist_ok=True)
    a, n, s = imgs
    a.save(os.path.join(folder, name + ".png"))
    n.save(os.path.join(folder, name + "_n.png"))
    s.save(os.path.join(folder, name + "_s.png"))


# ---- the portal ---------------------------------------------------------------------------

FRAMES = 32


def portal():
    """Blue light that flows and turns, gold sparks; tiles and loops."""
    rng = np.random.default_rng(31)
    f = np.fft.fftfreq(S) * S
    fx, fy = np.meshgrid(f, f)
    r = np.sqrt(fx ** 2 + fy ** 2)
    amp = np.where((r < 1) | (r > 9), 0, 1 / np.maximum(r, 1) ** 1.6)
    phase0 = 2 * np.pi * rng.random((S, S))
    speed = rng.integers(1, 3, (S, S)) * np.sign(rng.random((S, S)) - 0.5)
    frames = []
    yy, xx = np.mgrid[0:S, 0:S]
    sparks = [(rng.integers(0, S), rng.integers(0, S), rng.integers(0, FRAMES)) for _ in range(9)]
    for k in range(FRAMES):
        t = 2 * np.pi * k / FRAMES
        field = np.real(np.fft.ifft2(amp * np.exp(1j * (phase0 + speed * t))))
        field = (field - field.min()) / (field.max() - field.min() + 1e-9)
        # bands that rise: the field moved up over the loop
        shift = int(round(k * S / FRAMES))
        rise = np.roll(field, -shift, axis=0)
        v = 0.55 * field + 0.45 * rise
        v = v ** 1.6
        deep = np.array([10, 22, 78])
        mid = np.array([38, 104, 214])
        hi = np.array([150, 216, 255])
        c = np.where(v[..., None] < 0.5, deep + (mid - deep) * (v[..., None] / 0.5),
                     mid + (hi - mid) * ((v[..., None] - 0.5) / 0.5))
        alpha = 170 + 70 * v
        img = np.dstack([c, alpha])
        for sx, sy, born in sparks:
            age = (k - born) % FRAMES
            if age < 6:
                y = (sy - age * 2) % S
                glow = 1 - age / 6
                img[y, sx, :3] = img[y, sx, :3] * (1 - glow) + np.array([255, 205, 110]) * glow
                img[y, sx, 3] = 255
        frames.append(np.clip(img, 0, 255).astype(np.uint8))
    sheet = np.concatenate(frames, axis=0)
    return Image.fromarray(sheet, "RGBA")


def write_script(models):
    out = os.path.join(PACK, "kubejs", "client_scripts")
    lines = ["// Connected textures for the Grubenrahmen through Athena. Written by",
             "// tools/textures/grubenrahmen.py; the tiles are in assets/kronwerke/textures/block/ctm.",
             "ClientEvents.generateAssets('last', event => {"]
    for name, m in models.items():
        lines.append(f"    event.json('kronwerke:models/block/{name}', {json.dumps(m)})")
    lines.append("})")
    with open(os.path.join(out, "grubenrahmen_ctm.js"), "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    core = sys.argv[1] if len(sys.argv) > 1 else os.path.join(PACK, "..", "core-repo")
    tiles = os.path.join(PACK, "kubejs", "assets", "kronwerke", "textures", "block", "ctm", "grubenrahmen")
    save_set(tiles, "center", frame_tile(True, True, True, True))
    save_set(tiles, "horizontal", frame_tile(True, True, False, False))
    save_set(tiles, "vertical", frame_tile(False, False, True, True))
    save_set(tiles, "empty", frame_tile(False, False, False, False))
    prefix = "kronwerke:block/ctm/grubenrahmen"
    t = {k: f"{prefix}/{k}" for k in ("center", "empty", "horizontal", "vertical")}
    t["particle"] = f"{prefix}/center"
    write_script({"grubenrahmen": {"loader": "athena:athena", "athena:loader": "athena:ctm", "ctm_textures": t}})

    core_tex = os.path.join(core, "src", "main", "resources", "assets", "kronwerke", "textures", "block")
    save_set(core_tex, "grubenrahmen", frame_tile(True, True, True, True))
    portal().save(os.path.join(core_tex, "minenportal.png"))
    with open(os.path.join(core_tex, "minenportal.png.mcmeta"), "w") as f:
        json.dump({"animation": {"frametime": 2, "interpolate": True}}, f)
    print("ok")
