#!/usr/bin/env python3
"""The look of the quest book: FTB Quests reads a theme file (colours, textures, line
style) from assets/ftbquests/ftb_quests_theme.txt and the quest shapes from
assets/ftbquests/textures/shapes/<shape>/. KubeJS hands both to every client, so this
writes them into kubejs/assets and the quest book comes out in the Kronwerke colours.

The shape masks in shapes/ are the ones FTB Quests ships; the fill and the ring are drawn
here from them. FTB Quests tints both with the quest colour (locked, open, started,
done), so the textures are drawn in greys and the colours live in the theme file.
"""
import json
import os
import random

from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
SHAPES = ["circle", "hexagon", "gear", "diamond", "square", "rsquare"]

THEME = """[*]
background:          kronwerke:textures/gui/quests/background.png; color=#F4FFFFFF; tile_size=64
chapter_panel_background: hollow_rectangle:{{widget_border}}; round_edges + {{background}}; color=#FFFFFF; padding=1
key_reference_background: kronwerke:textures/gui/quests/background.png; color=#F4FFFFFF; tile_size=64
selected_chapter_highlight_1: #60d4a24a
selected_chapter_highlight_2: #28d4a24a

text_color:          #EDE6F5
hover_text_color:    #F6D68C
disabled_text_color: #9a90a8

widget_border:     #8a6420
widget_background: #B4141019
symbol_in:         #d4a24a
symbol_out:        #8a6420

button:                hollow_rectangle:{{widget_border}}
panel:                 {{container_slot}}
disabled_button:       hollow_rectangle:#3a3146
hover_button:          {{button}} + #C02c2438; padding=1
context_menu:          hollow_rectangle:{{widget_border}}; round_edges + {{background}}; color=#FFFFFF; padding=1
scroll_bar_background: {{widget_background}}
scroll_bar:            {{button}} + #FF3a3146; padding=1
container_slot:        {{button}}; padding=-1
text_box:              hollow_rectangle:{{widget_border}} + #FF0e0b12; padding=1

tasks_text_color:                   #9a6fd6
rewards_text_color:                 #d4a24a
quest_view_background:              {{context_menu}}
quest_view_border:                  {{widget_border}}
quest_view_title:                   #d4a24a
quest_completed_color:              #FFd4a24a
quest_started_color:                #FF9a6fd6
quest_not_started_color:            #FFEDE6F5
quest_locked_color:                 #FF6a6276
dependency_line_texture:            kronwerke:textures/gui/quests/dependency.png
dependency_line_completed_color:    #FFd4a24a
dependency_line_uncompleted_color:  #D2c0b6d2
dependency_line_unavailable_color:  #50807890
dependency_line_requires_color:     #FF5fd3d3
dependency_line_required_for_color: #FFf0c860
dependency_line_selected_speed:     1.0
dependency_line_unselected_speed:   0.0
dependency_line_thickness:          0.16
"""

BLUR = json.dumps({"texture": {"blur": True}}, indent=2)


def mask(shape):
    im = Image.open(os.path.join(HERE, "shapes", shape + ".png")).convert("RGBA")
    if shape == "square":
        return Image.new("L", im.size, 255)
    return im.getchannel("A")


def shape_textures(shape):
    """Fill and ring of a quest shape, in greys: a dark polished disc that gets a little
    lighter towards the centre, and a solid rim with a thin inner line."""
    m = mask(shape)
    w, h = m.size
    # fill: radial gradient, darker at the edge
    fill = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    px = fill.load()
    cx, cy = (w - 1) / 2, (h - 1) / 2
    r0 = w / 2
    for y in range(h):
        for x in range(w):
            a = m.getpixel((x, y))
            if a == 0:
                continue
            d = min(1.0, ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 / r0)
            g = round(92 - 44 * d)
            px[x, y] = (g, g, g, a)
    # a faint top light
    light = Image.new("L", (w, h), 0)
    ImageDraw.Draw(light).ellipse((w * 0.2, h * 0.08, w * 0.8, h * 0.5), fill=38)
    light = light.filter(ImageFilter.GaussianBlur(10))
    lp = light.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a:
                v = lp[x, y]
                px[x, y] = (min(255, r + v), min(255, g + v), min(255, b + v), a)

    # ring: the mask minus the mask shrunk by the rim width, plus a thin inner line. The
    # mask is padded first, so shapes that touch the edge of the texture shrink there too.
    def shrink(n):
        pad = Image.new("L", (w + 2 * n + 2, h + 2 * n + 2), 0)
        pad.paste(m, (n + 1, n + 1))
        return pad.filter(ImageFilter.MinFilter(2 * n + 1)).crop((n + 1, n + 1, n + 1 + w, n + 1 + h))

    rim = shrink(4)
    inner_a, inner_b = shrink(7), shrink(8)
    outline = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    op = outline.load()
    for y in range(h):
        for x in range(w):
            a = m.getpixel((x, y))
            if a == 0:
                continue
            ring = min(a, 255 - rim.getpixel((x, y)))
            line = min(a, inner_a.getpixel((x, y)) - inner_b.getpixel((x, y))) * 110 // 255
            v = max(ring, line)
            if v:
                op[x, y] = (255, 255, 255, v)
    return fill, outline


def background_tile(seed=7):
    """A 64 px dark stone tile with a little grain; the grain hides the seams."""
    rnd = random.Random(seed)
    im = Image.new("RGBA", (64, 64))
    px = im.load()
    for y in range(64):
        for x in range(64):
            n = rnd.randint(-5, 5)
            # a soft diagonal weave
            wv = 3 if (x + y) % 8 < 2 else 0
            px[x, y] = (20 + n + wv, 16 + n + wv, 25 + n + wv, 255)
    return im


def dependency():
    """A 64 px chevron for the dependency lines, softer than the stock one."""
    im = Image.new("RGBA", (64, 64), (255, 255, 255, 0))
    px = im.load()
    for y in range(64):
        for x in range(64):
            # distance to the chevron centre line, pointing right
            cy = 32 - (x - 32) if y >= 32 else 32 + (x - 32)
            d = abs(y - cy)
            if x < 8 or x > 56:
                a = 0
            else:
                a = max(0, 255 - d * 20)
            px[x, y] = (255, 255, 255, a)
    return im.filter(ImageFilter.GaussianBlur(0.6))


def write(assets_dir):
    q = os.path.join(assets_dir, "ftbquests")
    os.makedirs(q, exist_ok=True)
    with open(os.path.join(q, "ftb_quests_theme.txt"), "w") as f:
        f.write(THEME)
    for shape in SHAPES:
        d = os.path.join(q, "textures", "shapes", shape)
        os.makedirs(d, exist_ok=True)
        fill, outline = shape_textures(shape)
        fill.save(os.path.join(d, "background.png"), optimize=True)
        outline.save(os.path.join(d, "outline.png"), optimize=True)
        for n in ("background", "outline"):
            with open(os.path.join(d, n + ".png.mcmeta"), "w") as f:
                f.write(BLUR)
    g = os.path.join(assets_dir, "kronwerke", "textures", "gui", "quests")
    os.makedirs(g, exist_ok=True)
    background_tile().save(os.path.join(g, "background.png"), optimize=True)
    dependency().save(os.path.join(g, "dependency.png"), optimize=True)
    with open(os.path.join(g, "dependency.png.mcmeta"), "w") as f:
        f.write(BLUR)


if __name__ == "__main__":
    import sys
    write(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "kubejs", "assets"))
