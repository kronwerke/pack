"""Small pixel-art toolkit: masks, dithered ramps, outlines. No anti-aliasing anywhere."""
import numpy as np
from PIL import Image, ImageDraw

BAYER4 = (np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]) + 0.5) / 16.0


def hexc(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def cols(*hs):
    return [hexc(h) for h in hs]


class Canvas:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.a = np.zeros((h, w, 3), np.uint8)
        self.alpha = np.zeros((h, w), bool)
        self.yy, self.xx = np.mgrid[0:h, 0:w]
        self.bayer = BAYER4[self.yy % 4, self.xx % 4]

    # masks
    def none(self):
        return np.zeros((self.h, self.w), bool)

    def rect(self, x0, y0, x1, y1):
        """Half-open rectangle [x0, x1) x [y0, y1)."""
        m = self.none()
        m[max(0, int(y0)):max(0, int(y1)), max(0, int(x0)):max(0, int(x1))] = True
        return m

    def ellipse(self, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        return ((self.xx - cx) / rx) ** 2 + ((self.yy - cy) / ry) ** 2 <= 1.0

    def poly(self, pts):
        im = Image.new('1', (self.w, self.h), 0)
        ImageDraw.Draw(im).polygon([(int(round(x)), int(round(y))) for x, y in pts], fill=1)
        return np.array(im, bool)

    def line(self, x0, y0, x1, y1, width=1):
        im = Image.new('1', (self.w, self.h), 0)
        ImageDraw.Draw(im).line([(int(round(x0)), int(round(y0))), (int(round(x1)), int(round(y1)))], fill=1, width=width)
        return np.array(im, bool)

    def below(self, ys):
        """Mask of everything at or below a per-column height array."""
        return self.yy >= np.asarray(ys)[None, :]

    # painting
    def fill(self, mask, col):
        self.a[mask] = col
        self.alpha |= mask

    def px(self, x, y, col):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.a[int(y), int(x)] = col
            self.alpha[int(y), int(x)] = True

    def dither(self, mask, c1, c2, t):
        """c2 where t beats the Bayer threshold, else c1. t is a number or an array in 0..1."""
        t = np.broadcast_to(np.asarray(t, float), (self.h, self.w))
        pick = t > self.bayer
        self.a[mask & ~pick] = c1
        self.a[mask & pick] = c2
        self.alpha |= mask

    def ramp(self, mask, colors, t, soft=0.35):
        """Banded ramp over a list of colours; soft is the share of each band that dithers into the next."""
        t = np.clip(np.broadcast_to(np.asarray(t, float), (self.h, self.w)), 0, 1)
        n = len(colors)
        f = t * (n - 1)
        lo = np.clip(np.floor(f).astype(int), 0, n - 1)
        frac = f - lo
        if soft <= 0:
            up = frac >= 0.5
        else:
            up = np.clip((frac - 0.5) / soft + 0.5, 0, 1) > self.bayer
        idx = np.clip(lo + up, 0, n - 1)
        pal = np.array(colors, np.uint8)
        self.a[mask] = pal[idx][mask]
        self.alpha |= mask

    def edge(self, mask, inner=True):
        """Border pixels of a mask (inside the mask when inner, else just outside)."""
        p = np.pad(mask, 1)
        allin = p[:-2, 1:-1] & p[2:, 1:-1] & p[1:-1, :-2] & p[1:-1, 2:]
        anyin = p[:-2, 1:-1] | p[2:, 1:-1] | p[1:-1, :-2] | p[1:-1, 2:]
        return (mask & ~allin) if inner else (~mask & anyin)

    def shift(self, mask, dx, dy):
        out = self.none()
        h, w = self.h, self.w
        ys0, ys1 = max(0, dy), min(h, h + dy)
        xs0, xs1 = max(0, dx), min(w, w + dx)
        out[ys0:ys1, xs0:xs1] = mask[ys0 - dy:ys1 - dy, xs0 - dx:xs1 - dx]
        return out

    def paste(self, other, dx=0, dy=0):
        """Draw another canvas (same size) over this one where it has alpha."""
        m = self.shift(other.alpha, dx, dy)
        src = np.roll(other.a, (dy, dx), axis=(0, 1))
        self.a[m] = src[m]
        self.alpha |= m

    def image(self, scale=1, rgba=False):
        if rgba:
            arr = np.dstack([self.a, np.where(self.alpha, 255, 0).astype(np.uint8)])
            im = Image.fromarray(arr, 'RGBA')
        else:
            im = Image.fromarray(self.a, 'RGB')
        return im.resize((self.w * scale, self.h * scale), Image.NEAREST) if scale != 1 else im


def noise1d(n, seed, octaves=((40, 1.0), (17, 0.45), (7, 0.2))):
    """Smooth 1D value noise in about -1..1 for ridge lines."""
    rng = np.random.default_rng(seed)
    x = np.arange(n)
    out = np.zeros(n)
    for period, amp in octaves:
        k = n // period + 3
        v = rng.uniform(-1, 1, k)
        i = x / period
        i0 = np.floor(i).astype(int)
        f = i - i0
        f = f * f * (3 - 2 * f)
        out += amp * (v[i0] * (1 - f) + v[i0 + 1] * f)
    return out / sum(a for _, a in octaves)


def noise2d(w, h, seed, period=24, octaves=3):
    """Smooth 2D value noise in 0..1."""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:h, 0:w]
    out = np.zeros((h, w))
    amp, total = 1.0, 0.0
    for o in range(octaves):
        p = max(2.0, period / (2 ** o))
        gw, gh = int(w / p) + 3, int(h / p) + 3
        v = rng.uniform(0, 1, (gh, gw))
        fx, fy = xx / p, yy / p
        x0, y0 = np.floor(fx).astype(int), np.floor(fy).astype(int)
        tx, ty = fx - x0, fy - y0
        tx, ty = tx * tx * (3 - 2 * tx), ty * ty * (3 - 2 * ty)
        out += amp * ((v[y0, x0] * (1 - tx) + v[y0, x0 + 1] * tx) * (1 - ty) + (v[y0 + 1, x0] * (1 - tx) + v[y0 + 1, x0 + 1] * tx) * ty)
        total += amp
        amp *= 0.5
    return out / total


def smooth(a, k):
    k = max(1, int(k))
    return np.convolve(np.pad(np.asarray(a, float), k, mode='edge'), np.ones(2 * k + 1) / (2 * k + 1), mode='valid')
