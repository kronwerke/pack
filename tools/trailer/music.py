#!/usr/bin/env python3
"""The music of the trailer: thirty seconds, synthesised from nothing with numpy.

    music.py <out.wav> [stems]      writes the piece (44.1 kHz, stereo, 16 bit); with "stems"
                                    it also prints how loud every voice is

120 beats a minute, four to the bar, a bar is two seconds, fifteen bars. D minor, and D major
when the name comes. The cut of the pictures follows the bars (trailer.py):

    bars  1 -  2   the old works      a clock ticks, a music box finds the theme, a low drone
    bars  3 -  5   the valley         the theme whole, plucked chords, a pad, the train's steam
    bars  6 -  8   the obelisk        the drums come in, the theme climbs, a roll into the flash
    bars  9 - 13   the five stages    full band, one bar a stage: stone, brass, the hammer on
                                      the anvil, a bar of stars with the drums gone, then chaos
    bars 14 - 15   the name           the theme in major, two hits, and the clock goes on

Every sound is made here: bells and plucks from decaying partials, the lead a band limited
pulse wave (as an old console would), drums from sine sweeps and filtered noise, the room a
convolution with decaying noise. Same seed, same file.
"""
import math
import sys
import wave

import numpy as np
from scipy import signal

SR = 44100
BEAT = 0.5
BAR = 4 * BEAT
BARS = 15
LENGTH = BARS * BAR
N = int(LENGTH * SR)
RNG = np.random.default_rng(1601)

NOTE = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def hz(name):
    """'D5', 'Bb3', 'C#6' to a frequency."""
    step = NOTE[name[0]]
    rest = name[1:]
    while rest[0] in '#b':
        step += 1 if rest[0] == '#' else -1
        rest = rest[1:]
    midi = 12 * (int(rest) + 1) + step
    return 440.0 * 2 ** ((midi - 69) / 12.0)


def clock(dur):
    return np.arange(int(dur * SR)) / SR


def lowpass(x, f, order=2):
    return signal.sosfilt(signal.butter(order, f, 'low', fs=SR, output='sos'), x, axis=0)


def highpass(x, f, order=2):
    return signal.sosfilt(signal.butter(order, f, 'high', fs=SR, output='sos'), x, axis=0)


def bandpass(x, lo, hi, order=2):
    return signal.sosfilt(signal.butter(order, [lo, hi], 'band', fs=SR, output='sos'), x, axis=0)


def noise(dur):
    return RNG.uniform(-1, 1, int(dur * SR))


def fade(x, a=0.003, r=0.01):
    n = len(x)
    na, nr = min(n, int(a * SR)), min(n, int(r * SR))
    if na > 1:
        x[:na] *= np.linspace(0, 1, na)
    if nr > 1:
        x[-nr:] *= np.linspace(1, 0, nr)
    return x


class Bus:
    """One voice of the mix: a stereo buffer, a share that goes to the room."""

    def __init__(self, name, room=0.0):
        self.name = name
        self.room = room
        self.buf = np.zeros((N, 2))

    def add(self, sig, at, gain=1.0, pan=0.0):
        i = int(round(at * SR))
        if i >= N:
            return
        if i < 0:
            sig = sig[-i:]
            i = 0
        sig = sig[:N - i]
        left, right = math.cos((pan + 1) * math.pi / 4), math.sin((pan + 1) * math.pi / 4)
        self.buf[i:i + len(sig), 0] += sig * gain * left
        self.buf[i:i + len(sig), 1] += sig * gain * right


# ======================================================================================
# the instruments

def bell(f, dur):
    """A music box: a clear tone with a few partials that are not quite whole, each dying faster."""
    t = clock(dur)
    tau = 0.55 * (520.0 / f) ** 0.35
    out = np.zeros_like(t)
    for ratio, amp, life in ((1, 1.0, 1.0), (2, 0.42, 0.6), (3.01, 0.16, 0.38), (4.18, 0.1, 0.25), (5.43, 0.05, 0.16)):
        if f * ratio < 12000:
            out += amp * np.sin(2 * math.pi * f * ratio * t) * np.exp(-t / (tau * life))
    return fade(out, 0.002, 0.03)


def pluck(f, dur):
    """A plucked string: the high harmonics go first."""
    t = clock(dur)
    out = np.zeros_like(t)
    for n in range(1, 9):
        if f * n < 9000:
            out += (1.0 / n) * np.sin(2 * math.pi * f * n * t + n * 0.7) * np.exp(-t * (2.6 + n * 1.9))
    return fade(out, 0.002, 0.02)


def pad(f, dur):
    """A soft string pad: three voices a little apart, slow to come and go; returns stereo."""
    t = clock(dur + 0.6)
    out = np.zeros((len(t), 2))
    for cents, pan in ((-7, -0.7), (0, 0.0), (7, 0.7)):
        ff = f * 2 ** (cents / 1200.0)
        v = np.zeros_like(t)
        for n in range(1, 7):
            v += (1.0 / n ** 1.4) * np.sin(2 * math.pi * ff * n * t + pan * n)
        left, right = math.cos((pan + 1) * math.pi / 4), math.sin((pan + 1) * math.pi / 4)
        out[:, 0] += v * left
        out[:, 1] += v * right
    env = np.minimum(1.0, t / 0.3) * np.minimum(1.0, np.maximum(0.0, (dur + 0.6 - t) / 0.6))
    trem = 1.0 + 0.06 * np.sin(2 * math.pi * 0.45 * t + f)
    return out * (env * trem)[:, None]


def pulse(f, dur, duty=0.25, vib=0.0015):
    """The lead: a pulse wave built from its harmonics so nothing folds back, a little vibrato late in the note."""
    t = clock(dur)
    depth = vib * np.clip((t - 0.14) / 0.2, 0, 1)
    phase = 2 * math.pi * f * (t + depth * np.sin(2 * math.pi * 5.6 * t) / (2 * math.pi * 5.6) * 2 * math.pi)
    out = np.zeros_like(t)
    top = int(min(40, 6500 // f))
    for n in range(1, top + 1):
        out += (2.0 / (n * math.pi)) * math.sin(n * math.pi * duty) * np.cos(n * phase)
    env = np.minimum(1.0, t / 0.008) * (0.72 + 0.28 * np.exp(-t / 0.09))
    return fade(out * env, 0.0, 0.05)


def bass(f, dur):
    t = clock(dur)
    out = np.sin(2 * math.pi * f * t) + 0.45 * np.sin(2 * math.pi * 2 * f * t) * np.exp(-t / 0.25) + 0.2 * np.sin(2 * math.pi * 3 * f * t) * np.exp(-t / 0.12)
    env = np.minimum(1.0, t / 0.005) * (0.7 + 0.3 * np.exp(-t / 0.15))
    return fade(out * env, 0.0, 0.04)


def kick():
    t = clock(0.4)
    f = 46 + 110 * np.exp(-t / 0.035)
    out = np.sin(2 * math.pi * np.cumsum(f) / SR) * np.exp(-t / 0.13)
    out[:int(0.004 * SR)] += highpass(noise(0.004), 2000) * 0.4
    return fade(out, 0.0005, 0.05)


def snare():
    t = clock(0.3)
    out = bandpass(noise(0.3), 900, 7000) * np.exp(-t / 0.065) + 0.5 * np.sin(2 * math.pi * 196 * t) * np.exp(-t / 0.05)
    return fade(out, 0.0005, 0.03)


def hat(open_=False):
    dur = 0.3 if open_ else 0.08
    t = clock(dur)
    return fade(highpass(noise(dur), 7500, 4) * np.exp(-t / (0.09 if open_ else 0.016)), 0.0005, 0.01)


def tick(high=True):
    """The clock: a dry click with a small wooden body; tick is higher than tock."""
    t = clock(0.12)
    f = 2300 if high else 1650
    out = np.sin(2 * math.pi * f * t) * np.exp(-t / 0.009)
    out += 0.5 * np.sin(2 * math.pi * (620 if high else 470) * t) * np.exp(-t / 0.022)
    out[:int(0.003 * SR)] += highpass(noise(0.003), 3000) * 0.8
    return fade(out, 0.0003, 0.02)


def anvil():
    """The steam hammer on the anvil: a hard click and a ring of partials that do not agree."""
    t = clock(0.7)
    out = np.zeros_like(t)
    for f, amp, life in ((1046, 1.0, 0.22), (1712, 0.6, 0.16), (2590, 0.5, 0.11), (3483, 0.3, 0.08), (4630, 0.2, 0.05), (410, 0.5, 0.05)):
        out += amp * np.sin(2 * math.pi * f * t) * np.exp(-t / life)
    out[:int(0.006 * SR)] += noise(0.006) * 1.2
    return fade(out, 0.0003, 0.05)


def impact():
    """A low blow for the cuts: a sine that falls, a short dull crash of noise."""
    t = clock(1.6)
    f = 34 + 70 * np.exp(-t / 0.08)
    out = np.sin(2 * math.pi * np.cumsum(f) / SR) * np.exp(-t / 0.45)
    out += lowpass(noise(1.6), 900) * np.exp(-t / 0.16) * 0.9
    return fade(out, 0.001, 0.2)


def crash():
    t = clock(2.4)
    out = highpass(noise(2.4), 3500) * np.exp(-t / 0.55)
    for f in (3120, 4370, 5830, 7410):
        out += 0.12 * np.sin(2 * math.pi * f * t + f) * np.exp(-t / 0.4)
    return fade(out, 0.001, 0.3)


def whoosh(dur=0.4):
    """Air drawn in before a cut: noise that swells and stops."""
    t = clock(dur)
    return fade(bandpass(noise(dur), 500, 5000) * (t / dur) ** 2.5, 0.01, 0.004)


def riser(dur):
    """Tension before a hit: noise and a tone, both climbing."""
    t = clock(dur)
    k = t / dur
    f = 180 * 2 ** (k * 3.0)
    tone = np.sin(2 * math.pi * np.cumsum(f) / SR) * 0.25
    hiss = highpass(noise(dur), 1500) * 0.6
    return fade((tone + hiss) * k ** 2.2, 0.01, 0.006)


def chuff():
    """One breath of the engine."""
    t = clock(0.22)
    env = np.minimum(1.0, t / 0.012) * np.exp(-t / 0.055)
    return fade(bandpass(noise(0.22), 350, 2600) * env, 0.001, 0.02)


def whistle(dur=0.9):
    """The train's whistle, far off: three pipes in the chord of the key, breathy, a little unsteady."""
    t = clock(dur)
    out = np.zeros_like(t)
    wob = 1 + 0.004 * np.sin(2 * math.pi * 6 * t)
    for f in (hz('D5'), hz('F5'), hz('A5')):
        out += np.sin(2 * math.pi * f * wob * t) + 0.3 * np.sin(2 * math.pi * 2 * f * wob * t)
    out += bandpass(noise(dur), 1500, 5000) * 0.5
    env = np.minimum(1.0, t / 0.06) * np.minimum(1.0, (dur - t) / 0.25)
    return out * env


def sparkle(f):
    t = clock(0.5)
    return fade((np.sin(2 * math.pi * f * t) + 0.3 * np.sin(2 * math.pi * 2.01 * f * t)) * np.exp(-t / 0.12), 0.001, 0.02)


# ======================================================================================
# the piece

CHORDS = {
    'Dm': ('D2', ('D3', 'A3', 'D4', 'F4', 'A4')),
    'Bb': ('Bb1', ('Bb2', 'F3', 'Bb3', 'D4', 'F4')),
    'F': ('F2', ('F3', 'C4', 'F4', 'A4')),
    'C': ('C2', ('C3', 'G3', 'C4', 'E4', 'G4')),
    'Gm': ('G2', ('G3', 'D4', 'G4', 'Bb4')),
    'A': ('A1', ('A2', 'E3', 'A3', 'C#4', 'E4')),
    'A7': ('A1', ('A2', 'E3', 'A3', 'C#4', 'E4', 'G4')),
    'D': ('D2', ('D3', 'A3', 'D4', 'F#4', 'A4')),
}
# per bar: (chord, from beat, beats)
HARMONY = (
    (('Dm', 0, 4),), (('Dm', 0, 4),),
    (('Dm', 0, 4),), (('Bb', 0, 4),), (('F', 0, 2), ('C', 2, 2)),
    (('Gm', 0, 4),), (('Bb', 0, 4),), (('C', 0, 2), ('A', 2, 2)),
    (('Dm', 0, 4),), (('F', 0, 4),), (('Gm', 0, 4),), (('Bb', 0, 4),), (('A7', 0, 4),),
    (('D', 0, 4),), (('D', 0, 4),),
)
# the melody per bar: (beat, note, beats)
THEME = (
    ((2, 'D5', 1), (3, 'A5', 1)),
    ((0, 'F5', 1.5), (1.5, 'E5', 0.5), (2, 'D5', 1.5), (3.5, 'A4', 0.5)),
    ((0, 'D5', 1), (1, 'F5', 0.5), (1.5, 'A5', 1.5), (3, 'G5', 0.5), (3.5, 'F5', 0.5)),
    ((0, 'D5', 1), (1, 'F5', 0.5), (1.5, 'Bb5', 1.5), (3, 'A5', 0.5), (3.5, 'G5', 0.5)),
    ((0, 'A5', 1.5), (1.5, 'G5', 0.5), (2, 'F5', 1), (3, 'E5', 0.5), (3.5, 'C5', 0.5)),
    ((0, 'G5', 1), (1, 'Bb5', 0.5), (1.5, 'D6', 1.5), (3, 'C6', 0.5), (3.5, 'Bb5', 0.5)),
    ((0, 'Bb5', 1), (1, 'D6', 0.5), (1.5, 'F6', 1.5), (3, 'E6', 0.5), (3.5, 'D6', 0.5)),
    ((0, 'G5', 0.5), (0.5, 'C6', 0.5), (1, 'E6', 1), (2, 'C#6', 0.5), (2.5, 'E6', 0.5), (3, 'A6', 1)),
    ((0, 'D5', 1), (1, 'F5', 0.5), (1.5, 'A5', 1.5), (3, 'G5', 0.5), (3.5, 'F5', 0.5)),
    ((0, 'C5', 1), (1, 'F5', 0.5), (1.5, 'A5', 1.5), (3, 'C6', 0.5), (3.5, 'A5', 0.5)),
    ((0, 'Bb5', 1), (1, 'A5', 0.5), (1.5, 'G5', 1.5), (3, 'Bb5', 0.5), (3.5, 'D6', 0.5)),
    ((0, 'D6', 1), (1, 'F6', 0.5), (1.5, 'D6', 1.5), (3, 'C6', 0.5), (3.5, 'Bb5', 0.5)),
    ((0, 'A5', 1), (1, 'C#6', 0.5), (1.5, 'E6', 1), (2.5, 'G6', 0.5), (3, 'A6', 1)),
    ((0, 'D6', 1), (1, 'F#6', 0.5), (1.5, 'A6', 1.5), (3, 'G6', 0.5), (3.5, 'F#6', 0.5)),
    ((0, 'D6', 4),),
)


def compose():
    b = {n: Bus(n, room) for n, room in (
        ('drone', 0.25), ('ticks', 0.12), ('bells', 0.45), ('pluck', 0.3), ('pad', 0.35), ('lead', 0.3), ('bass', 0.0),
        ('kick', 0.0), ('snare', 0.22), ('hats', 0.05), ('fx', 0.3), ('anvil', 0.3), ('steam', 0.4))}

    # the drone under the first bars: the key's root and fifth, and wind
    t = clock(5.0)
    dr = (np.sin(2 * math.pi * hz('D2') * t) + 0.5 * np.sin(2 * math.pi * hz('A2') * t) + 0.25 * np.sin(2 * math.pi * hz('D3') * t + 1))
    dr *= np.minimum(1.0, t / 1.5) * np.minimum(1.0, (5.0 - t) / 1.2) * (1 + 0.15 * np.sin(2 * math.pi * 0.5 * t))
    b['drone'].add(dr, 0.0, 0.13)
    wind = bandpass(noise(4.6), 250, 1100) * np.minimum(1.0, clock(4.6) / 2.0) * np.minimum(1.0, (4.6 - clock(4.6)) / 1.0)
    b['drone'].add(wind, 0.0, 0.1, -0.3)
    b['drone'].add(wind[::-1].copy(), 0.0, 0.1, 0.3)
    # the growl under the bar of chaos
    t = clock(2.2)
    gr = (np.sin(2 * math.pi * hz('A1') * t) + 0.6 * np.sin(2 * math.pi * hz('A1') * 1.5 * t) + 0.3 * np.sin(2 * math.pi * hz('Bb2') * t))
    gr *= (0.6 + 0.4 * np.sin(2 * math.pi * 8 * t)) * np.minimum(1.0, t / 0.1) * np.minimum(1.0, (2.2 - t) / 0.3)
    b['drone'].add(gr, 12 * BAR, 0.16)

    for bar in range(BARS):
        t0 = bar * BAR
        # ---- the clock: loud alone, under the music later, alone again at the end
        for beat in range(4):
            g = 0.34 if bar < 2 else (0.16 if bar < 5 else (0.3 if bar == 14 and beat > 0 else 0.0))
            if bar == 13:
                g = 0.0
            if g:
                b['ticks'].add(tick(beat % 2 == 0), t0 + beat * BEAT, g, -0.25 if beat % 2 == 0 else 0.25)
        # ---- harmony: pad, bass, plucked chords
        for name, at, beats in HARMONY[bar]:
            root, notes = CHORDS[name]
            ct = t0 + at * BEAT
            if bar >= 2:
                level = 0.026 if bar < 5 else (0.03 if bar < 8 else 0.034)
                if bar == 14:
                    level = 0.04
                for n in notes:
                    stereo = pad(hz(n), beats * BEAT if bar < 14 else 3.4)
                    i = int(ct * SR)
                    seg = stereo[:N - i]
                    b['pad'].buf[i:i + len(seg)] += seg * level
            # bass
            rf = hz(root)
            if rf < 60:
                rf *= 2
            if 2 <= bar < 5:
                b['bass'].add(bass(rf, beats * BEAT * 0.95), ct, 0.2)
            elif bar in (11, 14):
                b['bass'].add(bass(rf, beats * BEAT * (0.98 if bar == 11 else 1.6)), ct, 0.22)
            elif bar >= 5:
                for k in range(int(beats * 2)):
                    octave = 2 if (bar >= 8 and k % 8 in (2, 5, 7)) else 1
                    b['bass'].add(bass(rf * octave, BEAT * 0.5 * 0.9), ct + k * BEAT * 0.5, 0.22 if k % 2 == 0 else 0.17)
            # plucked chords: eighths going up and down the chord (bars 3 to 8), sixteenths above the band later
            if 2 <= bar < 8:
                seq = [notes[1], notes[2], notes[3], notes[-1], notes[3], notes[2], notes[-1], notes[3]]
                for k in range(int(beats * 2)):
                    f = hz(seq[k % 8]) * 2
                    b['pluck'].add(pluck(f, 0.6), ct + k * BEAT * 0.5, 0.15 if k % 2 == 0 else 0.115, ((k % 4) - 1.5) / 2.5)
            elif 8 <= bar < 14 and bar != 11:
                up = [notes[2], notes[3], notes[-1], notes[3]]
                for k in range(int(beats * 4)):
                    f = hz(up[k % 4]) * (4 if (k // 4) % 2 else 2)
                    b['pluck'].add(pluck(f, 0.3), ct + k * BEAT * 0.25, 0.075, 0.6 if k % 2 else -0.6)
        # ---- the melody
        for beat, note, beats in THEME[bar]:
            at = t0 + beat * BEAT
            f = hz(note)
            dur = beats * BEAT
            if bar < 5:
                b['bells'].add(bell(f, max(1.2, dur + 0.8)), at, 0.2 if bar < 2 else 0.17, 0.1)
                if bar >= 2:
                    b['bells'].add(bell(f * 2, 0.9), at, 0.045, -0.2)
            elif bar < 8:
                b['lead'].add(pulse(f / 2, dur * 0.94), at, 0.2)
                b['bells'].add(bell(f, dur + 0.7), at, 0.14, 0.15)
            elif bar < 13:
                if bar == 11:
                    b['bells'].add(bell(f, dur + 1.0), at, 0.2, 0.0)
                    b['bells'].add(bell(f * 2, 0.8), at, 0.06, 0.3)
                else:
                    b['lead'].add(pulse(f, dur * 0.94), at, 0.3)
                    b['lead'].add(pulse(f / 2, dur * 0.94, duty=0.5), at, 0.09)
                    b['bells'].add(bell(f, dur + 0.5), at, 0.07, 0.2)
            else:
                b['bells'].add(bell(f, max(1.5, dur + 1.2)), at, 0.2, 0.0)
                b['bells'].add(bell(f / 2, max(1.5, dur + 1.2)), at, 0.12, -0.15)
                if bar == 13:
                    b['lead'].add(pulse(f / 2, dur * 0.94), at, 0.17)
        # ---- drums
        if 2 <= bar < 5:
            for beat in (0, 2):
                b['kick'].add(kick(), t0 + beat * BEAT, 0.4)
            if bar >= 3:
                for k in range(8):
                    if k % 2:
                        b['hats'].add(hat(), t0 + k * BEAT * 0.5, 0.11, 0.3)
        elif 5 <= bar < 8:
            for beat in range(4):
                b['kick'].add(kick(), t0 + beat * BEAT, 0.6)
            for beat in (1, 3):
                if not (bar == 7 and beat == 3):
                    b['snare'].add(snare(), t0 + beat * BEAT, 0.36)
            for k in range(8):
                b['hats'].add(hat(), t0 + k * BEAT * 0.5, 0.16 if k % 2 else 0.1, 0.3)
            if bar == 7:                                    # a roll into the flash
                for k in range(8):
                    b['snare'].add(snare(), t0 + 2 * BEAT + k * BEAT * 0.25, 0.1 + 0.035 * k, -0.2 + 0.05 * k)
        elif bar in (8, 9, 10, 12, 13):
            pattern = (0, 1.5, 2, 3.5) if bar in (8, 10) else ((0, 1, 2, 3) if bar in (12, 13) else (0, 1.5, 2, 2.5))
            for beat in pattern:
                b['kick'].add(kick(), t0 + beat * BEAT, 0.72)
            for beat in (1, 3):
                if not (bar == 12 and beat == 3):
                    b['snare'].add(snare(), t0 + beat * BEAT, 0.45)
            for k in range(8):
                b['hats'].add(hat(k == 7), t0 + k * BEAT * 0.5, 0.18 if k % 2 else 0.11, 0.3)
            for k in range(16):
                if k % 2:
                    b['hats'].add(hat(), t0 + k * BEAT * 0.25, 0.06, -0.3)
            if bar == 12:                                   # the roll into the name
                for k in range(8):
                    b['snare'].add(snare(), t0 + 2 * BEAT + k * BEAT * 0.25, 0.12 + 0.04 * k, -0.2 + 0.05 * k)
        elif bar == 11:
            b['kick'].add(kick(), t0, 0.6)
            for k in range(16):                             # a bar of stars: high sparks of the chord
                n = CHORDS['Bb'][1][(k * 3) % 5]
                b['bells'].add(sparkle(hz(n) * (8 if k % 3 else 4)), t0 + k * BEAT * 0.25, 0.035, math.sin(k * 1.7))
        if bar == 10:                                       # the hammer falls on every beat
            for beat in range(4):
                b['anvil'].add(anvil(), t0 + beat * BEAT, 0.2, 0.35)
        # ---- the cuts
        if bar in (8, 13):
            b['fx'].add(impact(), t0, 0.42)
            b['fx'].add(crash(), t0, 0.16, -0.2)
        elif bar in (9, 10, 11, 12):
            b['fx'].add(impact(), t0, 0.2)
            b['fx'].add(whoosh(0.35), t0 - 0.35, 0.12)
        elif bar == 14:
            b['fx'].add(impact(), t0, 0.32)
            b['fx'].add(crash(), t0, 0.1, 0.2)
    # risers into the flash and into the name, air before them
    b['fx'].add(riser(2.0), 7 * BAR, 0.16)
    b['fx'].add(riser(1.5), 12 * BAR + 0.5, 0.16)
    b['fx'].add(whoosh(0.5), 8 * BAR - 0.5, 0.16)
    b['fx'].add(whoosh(0.5), 13 * BAR - 0.5, 0.16)
    b['fx'].add(whoosh(0.3), 2 * BAR - 0.3, 0.07)
    b['fx'].add(whoosh(0.3), 5 * BAR - 0.3, 0.09)
    # the train: its whistle from far off, its steam slowing down as it comes to a stop
    b['steam'].add(whistle(0.5), 2 * BAR + 0.5, 0.035, -0.5)
    b['steam'].add(whistle(1.0), 2 * BAR + 1.25, 0.04, -0.5)
    at, gap, pan, level = 2 * BAR, 0.25, -0.7, 0.11
    while at < 4.6 * BAR and level > 0.01:
        b['steam'].add(chuff(), at, level, pan)
        at += gap
        gap *= 1.07
        pan = min(0.2, pan + 0.06)
        level *= 0.955
    t = clock(1.2)                                           # and lets off steam when it stands
    hiss = highpass(noise(1.2), 2500) * np.minimum(1.0, t / 0.05) * np.exp(-t / 0.35)
    b['steam'].add(hiss, 4.6 * BAR + 0.1, 0.05, 0.1)
    # gifts at the obelisk: a rising run of small bells as the bar fills
    scale = ('D6', 'F6', 'G6', 'A6', 'C7', 'D7')
    for k in range(12):
        b['bells'].add(sparkle(hz(scale[k % 6]) * (1 if k < 6 else 1)), 7 * BAR + k * BEAT * 0.25 + 0.5, 0.02 + 0.004 * k, math.sin(k))
    return b


def room(send):
    """The hall: the send convolved with two seconds of decaying noise, different left and right."""
    t = clock(2.2)
    out = np.zeros((N, 2))
    for ch in (0, 1):
        ir = RNG.normal(0, 1, len(t)) * np.exp(-t / 0.42)
        ir[:int(0.012 * SR)] = 0
        ir = highpass(lowpass(ir, 6500), 280)
        ir /= np.sqrt((ir ** 2).sum())
        out[:, ch] = signal.fftconvolve(send[:, ch], ir)[:N]
    return out


def master(buses):
    dry = np.zeros((N, 2))
    send = np.zeros((N, 2))
    for bus in buses.values():
        dry += bus.buf
        send += bus.buf * bus.room
    # the lead sings twice: an echo three sixteenths later, softer, to the other side
    d = int(0.375 * SR)
    echo = np.zeros((N, 2))
    echo[d:, 0] = buses['lead'].buf[:-d, 1] * 0.22
    echo[d:, 1] = buses['lead'].buf[:-d, 0] * 0.22
    mix = dry + echo + room(send + echo) * 0.9
    mix = highpass(mix, 28)
    mix = np.tanh(mix * 1.5)
    peak = np.abs(mix).max()
    mix *= 0.8 / peak
    n = int(0.5 * SR)
    mix[-n:] *= np.linspace(1, 0, n)[:, None] ** 1.5
    return mix


def main():
    out = sys.argv[1]
    buses = compose()
    mix = master(buses)
    if len(sys.argv) > 2:
        for sec, (lo, hi) in (('intro', (0, 4)), ('valley', (4, 10)), ('obelisk', (10, 16)), ('stages', (16, 26)), ('name', (26, 30))):
            parts = []
            for bus in buses.values():
                seg = bus.buf[int(lo * SR):int(hi * SR)]
                rms = math.sqrt((seg ** 2).mean())
                if rms > 1e-5:
                    parts.append('%s %.0f' % (bus.name, 20 * math.log10(rms)))
            seg = mix[int(lo * SR):int(hi * SR)]
            print('%-8s mix %.1f dB rms, peak %.2f | %s' % (sec, 20 * math.log10(math.sqrt((seg ** 2).mean())), np.abs(seg).max(), ', '.join(parts)))
    pcm = (np.clip(mix, -1, 1) * 32767).astype('<i2')
    with wave.open(out, 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    print('ok', out, '%.1f s' % (len(pcm) / SR))


if __name__ == '__main__':
    main()
