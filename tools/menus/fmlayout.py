#!/usr/bin/env python3
"""Summarise FancyMenu layout files: screen, background, element types, actions, placeholders."""
import re, sys, collections, os

def blocks(text):
    out, name, cur, depth = [], None, None, 0
    for line in text.splitlines():
        s = line.strip()
        if cur is None:
            m = re.match(r'^([\w\-]+)\s*\{$', s)
            if m:
                name, cur = m.group(1), {}
            continue
        if s == '}':
            out.append((name, cur)); cur = None; continue
        if ' = ' in s:
            k, v = s.split(' = ', 1)
            cur[k] = v
        elif s.endswith(' ='):
            cur[s[:-2]] = ''
    return out

def summarise(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    bl = blocks(t)
    meta = next((b for n, b in bl if n == 'layout-meta'), {})
    print(f"--- {path}")
    print("  screen:", meta.get('identifier'), "| enabled:", meta.get('is_enabled', '?'),
          "| behind vanilla:", meta.get('render_custom_elements_behind_vanilla'),
          "| universal whitelist:", meta.get('universal_layout_whitelist', ''), meta.get('universal_layout_blacklist', ''))
    for n, b in bl:
        if n == 'menu_background':
            keys = {k: v for k, v in b.items() if k in ('background_type', 'image_path', 'panorama_name', 'slideshow_name', 'parallax', 'slide', 'source', 'video_path', 'color')}
            print("  background:", keys)
        if n == 'customization' and b.get('action') in ('setscale', 'autoscale', 'overridemenu', 'setopenaudio', 'setcloseaudio', 'forcegui_scale'):
            print("  customization:", b)
    types = collections.Counter(b.get('element_type', '?') for n, b in bl if n == 'element')
    print("  elements:", dict(types))
    van = [b for n, b in bl if n in ('vanilla_button',)]
    hidden = sum(1 for b in van if b.get('is_hidden') == 'true')
    print(f"  vanilla widgets touched: {len(van)}, hidden: {hidden}")
    acts = collections.Counter(re.findall(r'\[action_type:([\w\-]+)\]', t))
    print("  actions:", dict(acts))
    reqs = collections.Counter(re.findall(r'\[loading_requirement:([\w\-]+)\]', t))
    print("  requirements:", dict(reqs))
    ph = collections.Counter(re.findall(r'\{"placeholder":"([\w\-]+)"', t))
    print("  placeholders:", dict(ph))
    fades = sum(1 for n, b in bl if n == 'element' and b.get('fade_in_v2', 'no_fading') != 'no_fading')
    delay = sum(1 for n, b in bl if n == 'element' and b.get('appearance_delay', 'no_delay') != 'no_delay')
    par = sum(1 for n, b in bl if n == 'element' and b.get('enable_parallax') == 'true')
    print(f"  fade-in: {fades}, delayed: {delay}, parallax elements: {par}")

for p in sys.argv[1:]:
    summarise(p)
