"""Pixel letters for the trailer: capitals, digits and signs on a 5 by 7 grid (umlauts 5 by 9, dots above)."""
import numpy as np

_G = {
    'A': '.XXX. X...X X...X XXXXX X...X X...X X...X', 'B': 'XXXX. X...X X...X XXXX. X...X X...X XXXX.',
    'C': '.XXX. X...X X.... X.... X.... X...X .XXX.', 'D': 'XXXX. X...X X...X X...X X...X X...X XXXX.',
    'E': 'XXXXX X.... X.... XXXX. X.... X.... XXXXX', 'F': 'XXXXX X.... X.... XXXX. X.... X.... X....',
    'G': '.XXX. X...X X.... X.XXX X...X X...X .XXX.', 'H': 'X...X X...X X...X XXXXX X...X X...X X...X',
    'I': 'XXX .X. .X. .X. .X. .X. XXX', 'J': '..XXX ...X. ...X. ...X. ...X. X..X. .XX..',
    'K': 'X...X X..X. X.X.. XX... X.X.. X..X. X...X', 'L': 'X.... X.... X.... X.... X.... X.... XXXXX',
    'M': 'X...X XX.XX X.X.X X.X.X X...X X...X X...X', 'N': 'X...X XX..X XX..X X.X.X X..XX X..XX X...X',
    'O': '.XXX. X...X X...X X...X X...X X...X .XXX.', 'P': 'XXXX. X...X X...X XXXX. X.... X.... X....',
    'Q': '.XXX. X...X X...X X...X X.X.X X..X. .XX.X', 'R': 'XXXX. X...X X...X XXXX. X.X.. X..X. X...X',
    'S': '.XXXX X.... X.... .XXX. ....X ....X XXXX.', 'T': 'XXXXX ..X.. ..X.. ..X.. ..X.. ..X.. ..X..',
    'U': 'X...X X...X X...X X...X X...X X...X .XXX.', 'V': 'X...X X...X X...X X...X X...X .X.X. ..X..',
    'W': 'X...X X...X X...X X.X.X X.X.X XX.XX X...X', 'X': 'X...X X...X .X.X. ..X.. .X.X. X...X X...X',
    'Y': 'X...X X...X .X.X. ..X.. ..X.. ..X.. ..X..', 'Z': 'XXXXX ....X ...X. ..X.. .X... X.... XXXXX',
    '0': '.XXX. X...X X..XX X.X.X XX..X X...X .XXX.', '1': '..X.. .XX.. ..X.. ..X.. ..X.. ..X.. .XXX.',
    '2': '.XXX. X...X ....X ...X. ..X.. .X... XXXXX', '3': 'XXXX. ....X ....X .XXX. ....X ....X XXXX.',
    '4': '...X. ..XX. .X.X. X..X. XXXXX ...X. ...X.', '5': 'XXXXX X.... XXXX. ....X ....X X...X .XXX.',
    '6': '.XXX. X.... X.... XXXX. X...X X...X .XXX.', '7': 'XXXXX ....X ...X. ..X.. ..X.. ..X.. ..X..',
    '8': '.XXX. X...X X...X .XXX. X...X X...X .XXX.', '9': '.XXX. X...X X...X .XXXX ....X ....X .XXX.',
    '.': '. . . . . . X', ',': '.. .. .. .. .. .X X.', ':': '. . X . . X .', '!': 'X X X X X . X', '?': '.XXX. X...X ....X ...X. ..X.. ..... ..X..',
    '%': 'XX..X XX..X ...X. ..X.. .X... X..XX X..XX', '+': '..... ..X.. ..X.. XXXXX ..X.. ..X.. .....',
    '-': '.... .... .... XXXX .... .... ....', ' ': '... ... ... ... ... ... ...', '/': '....X ....X ...X. ..X.. .X... X.... X....',
}
for base, um in (('A', 'Ä'), ('O', 'Ö'), ('U', 'Ü')):
    _G[um] = 'X...X ..... ' + _G[base]            # two rows on top: the dots and a gap


def width(text, k=1, gap=1):
    return sum(len(_G[ch].split()[0]) * k + gap * k for ch in text) - gap * k


def mask(shape, text, x, y, k=1, gap=1):
    """A boolean mask of the text with its top left at x, y (capitals; umlauts reach two rows higher)."""
    m = np.zeros(shape, bool)
    for ch in text:
        rows = _G[ch].split()
        top = y - (len(rows) - 7) * k
        for r, row in enumerate(rows):
            for q, v in enumerate(row):
                if v == 'X':
                    y0, x0 = top + r * k, x + q * k
                    m[max(0, y0):max(0, y0 + k), max(0, x0):max(0, x0 + k)] = True
        x += (len(rows[0]) + gap) * k
    return m


def draw(a, text, x, y, colour, k=1, shadow=(21, 18, 31), outline=True, gap=1):
    """Draws text into an RGB array: a dark outline (or just a shadow below), then the letters."""
    m = mask(a.shape[:2], text, x, y, k, gap)
    if shadow is not None:
        grow = np.zeros_like(m)
        offs = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (0, 2), (1, 2), (-1, 2)) if outline else ((0, 1), (1, 1))
        for dx, dy in offs:
            grow |= np.roll(np.roll(m, dy * 1, axis=0), dx * 1, axis=1)
        a[grow & ~m] = shadow
    a[m] = colour
    return m


def centred(a, text, cx, y, colour, k=1, **kw):
    return draw(a, text, cx - width(text, k) // 2, y, colour, k, **kw)
