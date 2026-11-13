#!/usr/bin/env python3
"""Builds the Kronwerke menus: draws the pixel art and writes the FancyMenu layouts.

    build.py [target]      target is the folder that holds `config` (default: the pack root)

Everything under config/fancymenu/customization and config/fancymenu/assets/kronwerke is
generated; change this script and the art scripts, not those files. The layouts are plain
FancyMenu 3.9 layout files, written by hand here instead of in the editor so that they can be
rebuilt and reviewed. The whole menu sits on a 480x270 grid (GUI scale 4 at 1920x1080, scaled
with the window), the same grid the artwork is drawn on.
"""
import json, os, sys, uuid

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'art'))
ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(HERE, '..', '..'))
FM = os.path.join(ROOT, 'config', 'fancymenu')
ASSETS = os.path.join(FM, 'assets', 'kronwerke')
LAYOUTS = os.path.join(FM, 'customization')
A = '[source:local]/config/fancymenu/assets/kronwerke/'

SERVER = 'kronwerke.net'
STATUS = 'https://kronwerke.com/api/status'
DISCORD = 'https://discord.gg/DZs3XyyHDj'
WEBSITE = 'https://kronwerke.com'
NIGHT_HOURS = '20,21,22,23,0,1,2,3,4,5'
DAY_HOURS = '6,7,8,9,10,11,12,13,14,15,16,17,18,19'
if os.environ.get('KW_MENU_FORCE') == 'night':        # for looking at the night pictures during the day
    NIGHT_HOURS, DAY_HOURS = ','.join(str(h) for h in range(24)), '99'
START_MS = 1800118800000        # 16.01.2027 18:00 Europe/Berlin, the season's start
STAMP = '1763000000000'
NS = uuid.UUID('6b726f6e-7765-726b-6500-000000000000')
NONE = '-2147483648'


_SEEN = {}


def uid(name):
    """An identifier in FancyMenu's form, uuid plus a time. The times rise in the order of first use: FancyMenu
    was seen to stack elements whose times are equal in an order of its own."""
    if name not in _SEEN:
        _SEEN[name] = len(_SEEN)
    return f'{uuid.uuid5(NS, name)}-{int(STAMP) + _SEEN[name]}'


def ph(name, **values):
    if not values:
        return '{"placeholder":"%s"}' % name
    return '{"placeholder":"%s","values":{%s}}' % (name, ','.join('"%s":"%s"' % kv for kv in values.items()))


def local(key):
    return ph('local', key='kwmenu.' + key)


def block(name, props):
    return name + ' {\n' + ''.join(f'  {k} = {v}\n' for k, v in props) + '}\n\n'


def requirement(name, hours=None, lines=None):
    """A requirement container: returns (container id, the property lines that define it)."""
    cid = uid(name + ':req')
    out, ids = [], []
    if hours:
        rid = uid(name + ':hours')
        ids.append(rid)
        out.append((f'[loading_requirement:fancymenu_visibility_requirement_is_realtime_hour][requirement_mode:if][req_id:{rid}]', hours))
    for i, (kind, mode, value) in enumerate(lines or []):
        rid = uid(f'{name}:r{i}')
        ids.append(rid)
        out.append((f'[loading_requirement:{kind}][requirement_mode:{mode}][req_id:{rid}]', value))
    meta = (f'[loading_requirement_container_meta:{cid}]', '[groups:][instances:%s]' % ''.join(i + ';' for i in ids))
    return cid, [meta] + out


def base(name, kind, anchor, x, y, w, h, req=None, opacity=1.0, parallax=None, anchor_el=None, ident=None, overlay='false', fade=None):
    cid, lines = req if req else requirement(name)
    p = [('element_type', kind), ('instance_identifier', ident or uid(name)),
         ('appearance_delay', 'no_delay'), ('disappearance_delay', 'no_delay'),
         ('fade_in_v2', fade or 'no_fading'), ('fade_out', 'no_fading'),
         ('auto_sizing', 'false'), ('auto_sizing_base_screen_width', '1920'), ('auto_sizing_base_screen_height', '1080'),
         ('sticky_anchor', 'false'), ('anchor_point', anchor)]
    if anchor_el:
        p.append(('anchor_point_element', anchor_el))
    p += [('x', x), ('y', y), ('width', w), ('height', h), ('stay_on_screen', 'false'),
          ('element_loading_requirement_container_identifier', cid)] + lines
    p += [('enable_parallax', 'true' if parallax else 'false'), ('invert_parallax', 'false'), ('animated_offset_x', 0), ('animated_offset_y', 0),
          ('load_once_per_session', 'false'), ('layer_hidden_in_editor', 'false'), ('advanced_rotation_mode', 'false'),
          ('advanced_vertical_tilt_mode', 'false'), ('advanced_horizontal_tilt_mode', 'false'),
          ('should_be_affected_by_decoration_overlays', overlay), ('in_editor_color', '#FFC800FF'),
          ('advanced_posx', NONE), ('advanced_posy', NONE), ('advanced_width', NONE), ('advanced_height', NONE),
          ('stretch_x', 'false'), ('stretch_y', 'false'), ('appearance_delay_seconds', '1.0'), ('disappearance_delay_seconds', '1.0'),
          ('fade_in_speed', '1.0'), ('fade_out_speed', '1.0'), ('base_opacity', opacity),
          ('parallax_intensity_x', parallax or 0.5), ('parallax_intensity_y', parallax or 0.5),
          ('rotation_degrees', '0.0'), ('advanced_rotation_degrees', '0.0'), ('vertical_tilt_degrees', '0.0'),
          ('advanced_vertical_tilt_degrees', '0.0'), ('horizontal_tilt_degrees', '0.0'), ('advanced_horizontal_tilt_degrees', '0.0')]
    return p


def image(name, src, anchor, x, y, w, h, **kw):
    p = base(name, 'image', anchor, x, y, w, h, **kw)
    p += [('source', A + src), ('repeat_texture', 'false'), ('nine_slice_texture', 'false'), ('nine_slice_texture_border_x', 5),
          ('nine_slice_texture_border_y', 5), ('restart_animated_on_menu_load', 'false'), ('image_tint', '#FFFFFF'),
          ('rounding_radius_top_left', '0.0'), ('rounding_radius_top_right', '0.0'), ('rounding_radius_bottom_right', '0.0'),
          ('rounding_radius_bottom_left', '0.0')]
    return block('element', p)


def text(name, source, anchor, x, y, w, h, scale=1.0, color='#F2EDE3FF', shadow=True, **kw):
    head = [('interactable', 'false'), ('source', source), ('source_mode', 'direct'), ('shadow', 'true' if shadow else 'false'),
            ('enable_scrolling', 'false'), ('auto_line_wrapping', 'true'), ('remove_html_breaks', 'true'),
            ('code_block_single_color', '#737373FF'), ('code_block_multi_color', '#565656FF'), ('headline_line_color', '#A9A9A9FF'),
            ('separation_line_color', '#A9A9A9FF'), ('hyperlink_color', '#E5B451FF'), ('click_event_color', '#FFEA00'),
            ('hover_event_color', '#0771FCFF'), ('quote_color', '#818181FF'), ('quote_italic', 'false'),
            ('bullet_list_dot_color', '#A9A9A9FF'), ('parse_markdown', 'true'), ('table_show_header', 'true'),
            ('table_alternate_row_colors', 'true'), ('table_line_color', '#787878FF'), ('table_header_background_color', '#323232FF'),
            ('table_row_background_color', '#282828FF'), ('table_alternate_row_color', '#3C3C3CFF')]
    tail = [('base_color', color), ('scale', scale), ('text_border', 0), ('line_spacing', 2), ('quote_indent', '8.0'),
            ('bullet_list_indent', '8.0'), ('bullet_list_spacing', '3.0'), ('table_line_thickness', '1.0'), ('table_cell_padding', '8.0'),
            ('table_margin', '4.0')]
    return block('element', head + base(name, 'text_v2', anchor, x, y, w, h, **kw) + tail)


def widget(name, kind, anchor, x, y, w, h, normal=None, hover=None, label=None, actions=(), tip=None, hidden=None, ident=None, off=None, **kw):
    bid = uid(name + ':block')
    head = [('button_element_executable_block_identifier', bid)]
    aids = []
    for i, (atype, value) in enumerate(actions):
        aid = uid(f'{name}:a{i}')
        aids.append(aid)
        head.append((f'[executable_action_instance:{aid}][action_type:{atype}]', value))
    head.append((f'[executable_block:{bid}][type:generic]', '[executables:%s]' % ''.join(a + ';' for a in aids)))
    if normal:
        head += [('backgroundnormal', A + normal), ('backgroundhovered', A + (hover or normal))]
        if off:
            head.append(('background_texture_inactive', A + off))
    head += [('underline_label_on_hover', 'false'), ('transparent_background', 'false'), ('restartbackgroundanimations', 'true'),
             ('nine_slice_custom_background', 'false')]
    if tip:
        head.append(('description', tip))
    if label is not None:
        head.append(('label', label))
    acid, alines = requirement(name + ':active')
    head += [('navigatable', 'true'), ('widget_active_state_requirement_container_identifier', acid)] + alines
    head += [('is_template', 'false'), ('template_apply_width', 'false'), ('template_apply_height', 'false'), ('template_apply_posx', 'false'),
             ('template_apply_posy', 'false'), ('template_apply_opacity', 'false'), ('template_apply_visibility', 'false'),
             ('template_apply_label', 'false'), ('template_share_with', 'buttons'), ('nine_slice_slider_handle', 'false')]
    tail = [('label_scale', '1.0'), ('label_shadow', 'true'), ('nine_slice_border_x', 5), ('nine_slice_border_y', 5),
            ('nine_slice_slider_handle_border_x', 5), ('nine_slice_slider_handle_border_y', 5)]
    if kind == 'vanilla_button':
        tail += [('automated_button_clicks', 0), ('is_hidden', 'true' if hidden else 'false')]
    return block('vanilla_button' if kind == 'vanilla_button' else 'element', head + base(name, kind, anchor, x, y, w, h, ident=ident, overlay='true', **kw) + tail)


def button(name, label, anchor, x, y, w, h, normal, hover, actions, tip=None, **kw):
    return widget(name, 'custom_button', anchor, x, y, w, h, normal, hover, label, actions, tip, **kw)


def vanilla(ident, anchor='vanilla', x=0, y=0, w=20, h=20, normal=None, hover=None, label=None, hidden=False, off=None, layout='', **kw):
    return widget(f'{layout}:{ident}', 'vanilla_button', anchor, x, y, w, h, normal, hover, label, (), None, hidden, ident=ident, off=off, **kw)


def hide(layout, *idents):
    return ''.join(vanilla(i, hidden=True, layout=layout) for i in idents)


def layout(name, screen, body, background=None, behind=False, scale=4.0, req=None, keep=True, parallax=False, index=0, extra=''):
    cid, lines = req if req else requirement(name + ':layout')
    out = 'type = fancymenu_layout\n\n'
    out += block('layout-meta', [('identifier', screen), ('render_custom_elements_behind_vanilla', 'true' if behind else 'false'),
                                 ('last_edited_time', STAMP), ('is_enabled', 'true'), ('randommode', 'false'), ('randomgroup', 1),
                                 ('randomonlyfirsttime', 'false'), ('layout_index', index)] + lines)
    if scale:
        out += block('customization', [('action', 'setscale'), ('scale', scale)])
        out += block('customization', [('action', 'autoscale'), ('basewidth', 1920), ('baseheight', 1080)])
    if background:
        out += block('menu_background', [('instance_identifier', uid(name + ':bg')), ('background_type', 'image'), ('show_background', 'true'),
                                         ('image_path', A + background), ('fallback_path', ''), ('slide', 'false'), ('repeat_texture', 'false'),
                                         ('parallax', 'true' if parallax else 'false'), ('parallax_intensity_x', '0.015'),
                                         ('parallax_intensity_y', '0.015'), ('invert_parallax', 'false'),
                                         ('restart_animated_on_menu_load', 'false')])
    out += block('customization', [('action', 'backgroundoptions'), ('keepaspectratio', 'true' if keep else 'false')])
    out += block('scroll_list_customization', [('preserve_scroll_list_header_footer_aspect_ratio', 'true'),
                                               ('render_scroll_list_header_shadow', 'true'), ('render_scroll_list_footer_shadow', 'true'),
                                               ('show_scroll_list_header_footer_preview_in_editor', 'false'),
                                               ('repeat_scroll_list_header_texture', 'false'), ('repeat_scroll_list_footer_texture', 'false'),
                                               ('show_screen_background_overlay_on_custom_background', 'false'),
                                               ('apply_vanilla_background_blur', 'false')])
    out += extra
    out += 'layout_action_executable_blocks {\n}\n\n'
    return out + body


def centered(s):
    return '^^^%n%' + s + '%n%^^^'


def gold(s):
    return '%#E5B451%' + s + '%#%'


# ---------------------------------------------------------------------------------------------
# title screen
# ---------------------------------------------------------------------------------------------

TITLE_HIDDEN = ('minecraft_logo_widget', 'minecraft_splash_widget', 'minecraft_branding_widget',
                'minecraft_realms_notification_icons_widget', 'mc_titlescreen_realms_button',
                '376388', '604388', '376394', '604394', '376382', '604382')
COL = -164          # left edge of the button column, from the right screen edge
CW = 148


# The moving parts of the picture: cut-outs of the frames `art()` renders, laid over the still.
# name, region (x0, y0, x1, y1) on the 480x270 grid, frames, milliseconds per frame. Order is
# bottom to top: a later one lies over an earlier one where they overlap.
SPRITES = [
    ('slow', (0, 0, 480, 214), [0, 5, 10, 15], 500),           # stars, glitter on the water, the obelisk's beam, birds
    ('smoke', (66, 6, 186, 104), list(range(40)), 100),        # both chimneys
    ('train', (0, 164, 480, 246), list(range(161)), 100),      # in, wait, out; the last frame (empty track) stays 4 s
    ('gear_tower', (183, 78, 212, 107), list(range(8)), 100),
    ('gear_gate', (136, 120, 159, 143), list(range(8)), 100),
    ('gear_wheel', (224, 154, 249, 179), list(range(20)), 100),
]


def moving(L, mode):
    """The sprites, only where the picture sits exactly on the 480x270 grid (a 16:9 window)."""
    exact = [('fancymenu_visibility_requirement_is_number', 'if', '["mode":"equals","number":"%s","compare_with":"480"]$' % ph('guiwidth')),
             ('fancymenu_visibility_requirement_is_number', 'if', '["mode":"equals","number":"%s","compare_with":"270"]$' % ph('guiheight'))]
    b = ''
    for name, (x0, y0, x1, y1), _, _ in SPRITES:
        b += image(f'{L}:anim_{name}', f'anim_{mode}_{name}.apng', 'top-left', x0, y0, x1 - x0, y1 - y0,
                   req=requirement(f'{L}:anim_{name}', lines=exact))
    return b


def title(name, art, hours):
    L = name
    b = moving(L, 'night' if 'night' in name else 'dusk')
    b += image(L + ':logo', 'logo.png', 'top-right', COL - 8, 8, 163, 62)
    b += button(L + ':join', local('join'), 'top-right', COL, 78, CW, 32, 'btn_main.png', 'btn_main_hover.png',
                [('joinserver', SERVER)], tip=local('join.tip'))
    players = ph('json', source=STATUS, json_path='$.server.players')
    most = ph('json', source=STATUS, json_path='$.server.max')
    has_status = [('fancymenu_visibility_requirement_is_number', 'if', '["mode":"bigger-than-or-equals","number":"%s","compare_with":"0"]$' % players)]
    b += image(L + ':tag', 'tag.png', 'top-right', COL + 22, 109, 104, 14, req=requirement(L + ':tag', lines=has_status))
    b += text(L + ':status', centered(gold(local('status')) + ' ' + players + ' / ' + most), 'top-right', COL + 22, 110, 104, 16,
              req=requirement(L + ':status', lines=has_status))
    y = 128
    b += vanilla('mc_titlescreen_singleplayer_button', 'top-right', COL, y, CW, 20, 'btn_wide.png', 'btn_wide_hover.png', layout=L)
    b += vanilla('mc_titlescreen_multiplayer_button', 'top-right', COL, y + 24, CW, 20, 'btn_wide.png', 'btn_wide_hover.png',
                 label=local('servers'), layout=L)
    b += vanilla('mc_titlescreen_options_button', 'top-right', COL, y + 48, 72, 20, 'btn_half.png', 'btn_half_hover.png',
                 label=local('options'), layout=L)
    b += vanilla('forge_titlescreen_mods_button', 'top-right', COL + 76, y + 48, 72, 20, 'btn_half.png', 'btn_half_hover.png', layout=L)
    b += button(L + ':discord', '', 'top-right', COL, y + 72, 20, 20, 'icon_chat.png', 'icon_chat_hover.png', [('openlink', DISCORD)], tip=local('discord.tip'))
    b += button(L + ':web', '', 'top-right', COL + 24, y + 72, 20, 20, 'icon_home.png', 'icon_home_hover.png', [('openlink', WEBSITE)], tip=local('web.tip'))
    b += button(L + ':lang', '', 'top-right', COL + 48, y + 72, 20, 20, 'icon_globe.png', 'icon_globe_hover.png',
                [('opengui', 'language_select_screen')], tip=local('lang.tip'))
    b += vanilla('mc_titlescreen_quit_button', 'top-right', COL + 76, y + 72, 72, 20, 'btn_half.png', 'btn_half_hover.png',
                 label=local('quit'), layout=L)
    b += text(L + ':version', gold('Kronwerke') + ' Season 2%n%Minecraft ' + ph('mcversion') + ' · NeoForge', 'bottom-left', 4, -26, 220, 26)
    days = ph('calc', expression='(%d - %s) / 86400000 + 0.5' % (START_MS, ph('unix_time')), decimal='false')
    b += text(L + ':countdown', gold(local('countdown.a') + ' ' + days + ' ' + local('countdown.b')), 'bottom-left', 4, -41, 260, 15,
              req=requirement(L + ':countdown', lines=[('fancymenu_visibility_requirement_is_number', 'if',
                                                        '["mode":"smaller-than","number":"%s","compare_with":"%d"]$' % (ph('unix_time'), START_MS))]))
    b += hide(L, *TITLE_HIDDEN)
    extra = ''
    if 'night' in name:
        extra = block('decoration_overlay', [('overlay_type', 'fireflies'), ('instance_identifier', uid(name + ':fireflies')),
                                             ('show_decoration_overlay', 'true'), ('firefly_group_density', '0.6'),
                                             ('firefly_group_amount', '0.7'), ('firefly_group_size', '0.8'), ('firefly_scale', '1.0'),
                                             ('firefly_follow_mouse', 'true'), ('firefly_landing', 'true'), ('firefly_color_hex', '#FFE08A')])
    return layout(name, 'title_screen', b, background=art, behind=True, req=requirement(name + ':layout', hours=hours), extra=extra)


# ---------------------------------------------------------------------------------------------
# every other menu outside a world: the dimmed artwork behind it
# ---------------------------------------------------------------------------------------------

def not_in_world(name):
    return requirement(name + ':layout', lines=[('fancymenu_loading_requirement_is_world_loaded', 'if_not', '')])


def universal():
    return layout('universal', '%fancymenu:universal_layout%', '', background='menu_dim.png', scale=None, req=not_in_world('universal'))


def multiplayer():
    L = 'multi'
    b = button(L + ':join', local('join'), 'top-centered', -74, 4, CW, 24, 'btn_join.png', 'btn_join_hover.png', [('joinserver', SERVER)],
               tip=local('join.tip'))
    players = ph('json', source=STATUS, json_path='$.server.players')
    most = ph('json', source=STATUS, json_path='$.server.max')
    has_status = [('fancymenu_visibility_requirement_is_number', 'if', '["mode":"bigger-than-or-equals","number":"%s","compare_with":"0"]$' % players)]
    b += image(L + ':tag', 'tag.png', 'top-centered', 78, 9, 104, 14, req=requirement(L + ':tag', lines=has_status))
    b += text(L + ':status', centered(gold(local('status')) + ' ' + players + ' / ' + most), 'top-centered', 78, 10, 104, 16,
              req=requirement(L + ':status', lines=has_status))
    return layout(L, 'join_multiplayer_screen', b, scale=None)


# ---------------------------------------------------------------------------------------------
# pause screen: the world stays visible, logo on top, one column
# ---------------------------------------------------------------------------------------------

def pause():
    """The same column as on the title screen, on the right, so the view and other mods' texts on the left stay free."""
    L = 'pause'
    x, y = COL, 80
    left, right = ('btn_80.png', 'btn_80_hover.png'), ('btn_64.png', 'btn_64_hover.png')     # 80 wide: "Advancements" must fit
    b = image(L + ':logo', 'logo.png', 'top-right', COL - 8, 8, 163, 62)
    b += vanilla('pause_return_to_game_button', 'top-right', x, y, CW, 20, 'btn_wide.png', 'btn_wide_hover.png', layout=L)
    b += button(L + ':quests', local('quests'), 'top-right', x, y + 24, 80, 20, *left,
                actions=[('closegui', ''), ('sendmessage', '/ftbquests open_book')])      # the book has no key in the pack
    b += button(L + ':map', local('map'), 'top-right', x + 84, y + 24, 64, 20, *right,
                actions=[('closegui', ''), ('mimic_keybind', 'key.ftbchunks.map|||false|||100')])
    b += vanilla('pause_advancements_button', 'top-right', x, y + 48, 80, 20, *left, layout=L)
    b += vanilla('pause_stats_button', 'top-right', x + 84, y + 48, 64, 20, *right, layout=L)
    b += vanilla('pause_options_button', 'top-right', x, y + 72, 80, 20, *left, label=local('options'), layout=L)
    b += vanilla('398348', 'top-right', x + 84, y + 72, 64, 20, *right, layout=L)                  # NeoForge's Mods button
    b += button(L + ':discord', '', 'top-right', x + 6, y + 96, 20, 20, 'icon_chat.png', 'icon_chat_hover.png', [('openlink', DISCORD)], tip=local('discord.tip'))
    b += button(L + ':web', '', 'top-right', x + 30, y + 96, 20, 20, 'icon_home.png', 'icon_home_hover.png', [('openlink', WEBSITE)], tip=local('web.tip'))
    b += button(L + ':status', '', 'top-right', x + 54, y + 96, 20, 20, 'icon_book.png', 'icon_book_hover.png', [('openlink', WEBSITE + '/status')], tip=local('status.tip'))
    b += vanilla('pause_disconnect_button', 'top-right', x + 84, y + 96, 64, 20, *right, label=local('leave'), layout=L)
    b += hide(L, 'pause_send_feedback_button', 'pause_report_bugs_button', 'pause_share_to_lan_button', '40')     # 40: the "Game Menu" line
    return layout(L, 'pause_screen', b)


# ---------------------------------------------------------------------------------------------
# the loading screen while the game starts (Drippy): same picture as the title, the bar where
# the big button will be, so the menu grows out of it
# ---------------------------------------------------------------------------------------------

def loading(name, art, hours):
    """Logo and bar in the middle, where the early window before it has them."""
    L = name
    b = image(L + ':logo', 'logo.png', 'mid-centered', -82, -50, 163, 62)
    b += image(L + ':frame', 'bar_frame.png', 'mid-centered', -74, 14, CW, 20)
    p = base(L + ':bar', 'progress_bar', 'mid-centered', -70, 18, CW - 8, 12)
    head = [('bar_color', '#E5B451FF'), ('bar_texture', A + 'bar_fill.png'), ('background_color', '#00000000'), ('direction', 'right'),
            ('progress_source', ph('game_loading_progress')), ('value_mode', 'percentage'), ('smooth_filling_animation', 'true')]
    b += block('element', head + p)
    for lang, mode in (('de', 'if'), ('en', 'if_not')):
        tip = ph('randomtext', source='/config/fancymenu/assets/kronwerke/tips_' + lang + '.txt', interval='6')
        b += image(L + ':tipbg_' + lang, 'tip.png', 'mid-centered', -110, 40, 220, 26,
                   req=requirement(L + ':tipbg_' + lang, lines=[('fancymenu_loading_requirement_is_language', mode, 'de_de')]))
        b += text(L + ':tip_' + lang, centered(tip), 'mid-centered', -106, 43, 212, 24,
                  req=requirement(L + ':tip_' + lang, lines=[('fancymenu_loading_requirement_is_language', mode, 'de_de')]))
    b += hide(L, 'progress_bar', 'mojang_logo')
    return layout(name, 'drippy_loading_overlay', b, background=art, req=requirement(name + ':layout', hours=hours))


LANG = {
    'de_de': {
        'join': '§e§lKronwerke betreten', 'join.tip': 'Verbindet dich direkt mit dem Kronwerke-Server.', 'status': 'Online:',
        'servers': 'Serverliste', 'options': 'Optionen', 'quit': 'Beenden', 'discord.tip': 'Zum Discord', 'web.tip': 'kronwerke.com',
        'lang.tip': 'Sprache', 'countdown.a': 'Season 2 startet in', 'countdown.b': 'Tagen', 'quests': 'Questbuch', 'map': 'Karte', 'leave': 'Verlassen', 'status.tip': 'Live-Status der Season',
    },
    'en_us': {
        'join': '§e§lEnter Kronwerke', 'join.tip': 'Connects you straight to the Kronwerke server.', 'status': 'Online:',
        'servers': 'Server list', 'options': 'Options', 'quit': 'Quit', 'discord.tip': 'Open Discord', 'web.tip': 'kronwerke.com',
        'lang.tip': 'Language', 'countdown.a': 'Season 2 starts in', 'countdown.b': 'days', 'quests': 'Quest book', 'map': 'Map', 'leave': 'Leave', 'status.tip': 'Live status of the season',
    },
}

SCREENS = ['net.minecraft.client.gui.screens.TitleScreen',
           'de.keksuccino.drippyloadingscreen.customization.DrippyOverlayScreen',
           'net.minecraft.client.gui.screens.PauseScreen',
           'net.minecraft.client.gui.screens.multiplayer.JoinMultiplayerScreen',
           'net.minecraft.client.gui.screens.multiplayer.SafetyScreen',
           'net.minecraft.client.gui.screens.DirectJoinServerScreen',
           'net.minecraft.client.gui.screens.EditServerScreen',
           'net.minecraft.client.gui.screens.worldselection.SelectWorldScreen',
           'net.minecraft.client.gui.screens.worldselection.CreateWorldScreen',
           'net.minecraft.client.gui.screens.options.OptionsScreen',
           'net.minecraft.client.gui.screens.options.LanguageSelectScreen',
           'net.minecraft.client.gui.screens.options.SoundOptionsScreen',
           'net.minecraft.client.gui.screens.options.controls.ControlsScreen',
           'net.minecraft.client.gui.screens.options.SkinCustomizationScreen',
           'net.minecraft.client.gui.screens.options.AccessibilityOptionsScreen',
           'net.minecraft.client.gui.screens.options.ChatOptionsScreen',
           'net.minecraft.client.gui.screens.options.OnlineOptionsScreen',
           'net.minecraft.client.gui.screens.options.VideoSettingsScreen',
           'net.minecraft.client.gui.screens.packs.PackSelectionScreen',
           'net.minecraft.client.gui.screens.DisconnectedScreen',
           'net.minecraft.client.gui.screens.ConfirmScreen',
           'net.neoforged.neoforge.client.gui.ModListScreen']

TIPS = {
    'de': ['Das Questbuch zeigt dir den Weg durch alle Stufen.', 'Mit M öffnest du die Karte, mit C darin deine Claims.',
           'Jede Stufe öffnet neue Mods und Dimensionen.', 'Der Obelisk sammelt, was alle gemeinsam einzahlen.',
           'Farmwelt, Nether und End erreichst du durch ihre Portale.', 'R und U in JEI zeigen Rezepte und Verwendungen.',
           'Auf kronwerke.com siehst du den Stand der Season live.'],
    'en': ['The quest book leads you through every stage.', 'M opens the map, C inside it shows your claims.',
           'Every stage unlocks new mods and dimensions.', 'The obelisk collects what everyone pays in together.',
           'The mining world, the Nether and the End are reached through their portals.', 'R and U in JEI show recipes and uses.',
           'kronwerke.com shows the state of the season live.'],
}


OPTIONS = """##[customization]

B:show_customization_overlay = 'false';
B:modpack_mode = 'true';


##[window]

B:show_custom_window_icon = 'true';
S:custom_window_icon_32 = '/config/fancymenu/assets/kronwerke/icon_32.png';
S:custom_window_title = 'Kronwerke Season 2';
S:custom_window_icon_16 = '/config/fancymenu/assets/kronwerke/icon_16.png';
"""


# Buttons other mods put on the title and pause screens are switched off in those mods' own
# configs: Cumulus (the Aether's menu list, world preview, quick load), Create and
# Supplementaries (their config buttons). The mod list reaches all of them.
OTHER = {
    'cumulus_menus-client.toml': '[Menu]\n\t"Enable Menu API" = false\n\t"Active Menu" = "cumulus_menus:minecraft"\n\t"Enables menu selection button" = false\n\n'
                                 '["World Preview"]\n\t"Enables world preview" = false\n\t"Enables toggle world button" = false\n\t"Enables quick load button" = false\n',
    'create-client.toml': '[client]\n\tmainMenuConfigButtonRow = 0\n\tingameMenuConfigButtonRow = 0\n',
    'supplementaries-client.toml': '[general]\n\tconfigs_button = false\n',
}


# The early window (NeoForge's own, long before the game's loading screen) is the Drippy Early
# Loading Module's. It knows a background, a logo and a bar. Offsets are from the window's
# centre in the module's units (1920x1080): x offset, y offset, width, height.
# The module places in plain pixels and does not scale with the window, so logo and bar stay in
# the middle, where every window size shows them. Measured: at offset 0 the logo's centre sits
# 46 above the middle, and the bar hangs below the logo (its y offset is relative to the logo).
EARLY = {'logo': (0, -30, 652, 248), 'bar': (0, -30, 592, 80)}


def drippy_options():
    K = '/config/fancymenu/assets/kronwerke/'
    none = '/config/fancymenu/assets/some_image.png'
    early = {
        'S:early_loading_background_texture_path': K + 'title_dusk.png', 'B:early_loading_background_preserve_aspect_ratio': 'true',
        'S:early_loading_logo_texture_path': K + 'logo_big.png', 'I:early_loading_logo_width': EARLY['logo'][2], 'I:early_loading_logo_height': EARLY['logo'][3],
        'I:early_loading_logo_position_offset_x': EARLY['logo'][0], 'I:early_loading_logo_position_offset_y': EARLY['logo'][1], 'B:early_loading_hide_logo': 'false',
        'S:early_loading_bar_background_texture_path': K + 'bar_frame_big.png', 'S:early_loading_bar_progress_texture_path': K + 'bar_fill_early.png',
        'I:early_loading_bar_width': EARLY['bar'][2], 'I:early_loading_bar_height': EARLY['bar'][3],
        'I:early_loading_bar_position_offset_x': EARLY['bar'][0], 'I:early_loading_bar_position_offset_y': EARLY['bar'][1], 'B:early_loading_hide_bar': 'false',
        'B:early_loading_hide_logger': 'true', 'S:early_loading_window_title': 'Kronwerke Season 2',
        'I:early_loading_window_width': -1, 'I:early_loading_window_height': -1,
    }
    for corner in ('top_left', 'top_right', 'bottom_left', 'bottom_right'):
        early[f'S:early_loading_{corner}_watermark_texture_path'] = none
        early[f'I:early_loading_{corner}_watermark_width'] = 100
        early[f'I:early_loading_{corner}_watermark_height'] = 100
        early[f'I:early_loading_{corner}_watermark_position_offset_x'] = 0
        early[f'I:early_loading_{corner}_watermark_position_offset_y'] = 0
    out = "##[general]\n\nB:early_fade_out_elements = 'false';\nB:allow_universal_layouts = 'false';\nB:fade_out_loading_screen = 'true';\nB:wait_for_textures_in_loading = 'true';\n\n\n##[early_loading]\n\n"
    return out + ''.join(f"{k} = '{v}';\n" for k, v in early.items())


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)


def sprite_meta(w, h, border):
    return json.dumps({'gui': {'scaling': {'type': 'nine_slice', 'width': w, 'height': h, 'border': border}}}) + '\n'


def art():
    import numpy as np
    from PIL import Image
    import scene, ui
    os.makedirs(ASSETS, exist_ok=True)
    import works, px
    dusk = None
    last = max(max(fr) for _, _, fr, _ in SPRITES)
    for mode in scene.PAL:
        frames = [scene.build(mode, t).a.copy() for t in range(last + 1)]
        still = scene.build(mode)
        still.image(4).save(os.path.join(ASSETS, f'title_{mode}.png'), optimize=True)
        if mode == 'dusk':
            dusk = still
        for name, (x0, y0, x1, y1), fr, ms in SPRITES:
            dur = [ms] * len(fr)
            if name == 'train':
                dur[-1] = (works.LOOP - last) * ms
            px.apng(os.path.join(ASSETS, f'anim_{mode}_{name}.apng'), [frames[t][y0:y1, x0:x1] for t in fr], dur)
    # the dimmed picture behind the other menus: darker, cooler, same pixels
    dim = (dusk.a.astype(float) * 0.34 + np.array([13, 11, 16], float) * 0.66).astype(np.uint8)
    Image.fromarray(dim, 'RGB').resize((1920, 1080), Image.NEAREST).save(os.path.join(ASSETS, 'menu_dim.png'), optimize=True)
    items = ui.build(os.path.join(ASSETS, '_tmp'))
    for k in items:
        os.replace(os.path.join(ASSETS, '_tmp', k + '.png'), os.path.join(ASSETS, k + '.png'))
    os.remove(os.path.join(ASSETS, '_tmp', 'ui_sheet.png'))
    os.rmdir(os.path.join(ASSETS, '_tmp'))
    # the game's own buttons and sliders, for every screen: sprites of the vanilla resource pack
    W = os.path.join(ROOT, 'kubejs', 'assets', 'minecraft', 'textures', 'gui', 'sprites', 'widget')
    os.makedirs(W, exist_ok=True)
    for sprite, c in (('button', ui.plate(200, 20)), ('button_highlighted', ui.plate(200, 20, hover=True)), ('button_disabled', ui.plate(200, 20, 'flat')),
                      ('slider', ui.plate(200, 20, 'flat')), ('slider_highlighted', ui.plate(200, 20, 'flat', hover=True)),
                      ('slider_handle', ui.plate(8, 20)), ('slider_handle_highlighted', ui.plate(8, 20, hover=True))):
        c.image(1, rgba=True).save(os.path.join(W, sprite + '.png'), optimize=True)
        w, h = c.w, c.h
        write(os.path.join(W, sprite + '.png.mcmeta'), sprite_meta(w, h, 4 if w > 20 else 3))
    # larger copies for the early window, which smooths its textures
    for k in ('logo', 'bar_frame', 'bar_fill'):
        im = Image.open(os.path.join(ASSETS, k + '.png'))
        im.resize((im.width * 4, im.height * 4), Image.NEAREST).save(os.path.join(ASSETS, k + '_big.png'), optimize=True)
    fill = Image.new('RGBA', (148, 20), (0, 0, 0, 0))
    fill.paste(ui.bar_fill(140, 12).image(1, rgba=True), (4, 4))
    fill.resize((592, 80), Image.NEAREST).save(os.path.join(ASSETS, 'bar_fill_early.png'), optimize=True)
    # window icons
    for size in (16, 32):
        ui.window_icon(size).image(1, rgba=True).save(os.path.join(ASSETS, f'icon_{size}.png'), optimize=True)
    for lang, lines in TIPS.items():
        write(os.path.join(ASSETS, f'tips_{lang}.txt'), '\n'.join(lines) + '\n')


def main():
    art()
    for f in os.listdir(LAYOUTS) if os.path.isdir(LAYOUTS) else []:
        if f.startswith('kw_'):
            os.remove(os.path.join(LAYOUTS, f))
    write(os.path.join(LAYOUTS, 'kw_title_day.txt'), title('title_day', 'title_dusk.png', DAY_HOURS))
    write(os.path.join(LAYOUTS, 'kw_title_night.txt'), title('title_night', 'title_night.png', NIGHT_HOURS))
    write(os.path.join(LAYOUTS, 'kw_loading_day.txt'), loading('loading_day', 'title_dusk.png', DAY_HOURS))
    write(os.path.join(LAYOUTS, 'kw_loading_night.txt'), loading('loading_night', 'title_night.png', NIGHT_HOURS))
    write(os.path.join(LAYOUTS, 'kw_universal.txt'), universal())
    write(os.path.join(LAYOUTS, 'kw_multiplayer.txt'), multiplayer())
    write(os.path.join(LAYOUTS, 'kw_pause.txt'), pause())
    write(os.path.join(FM, 'options.txt'), OPTIONS)
    write(os.path.join(ROOT, 'config', 'drippyloadingscreen', 'options.txt'), drippy_options())
    for name, content in OTHER.items():
        write(os.path.join(ROOT, 'config', name), content)
    write(os.path.join(FM, 'customizablemenus.txt'), 'type = customizablemenus\n\n' + ''.join(s + ' {\n}\n\n' for s in SCREENS))
    for lang, table in LANG.items():
        write(os.path.join(ROOT, 'kubejs', 'assets', 'kwmenu', 'lang', lang + '.json'),
              json.dumps({'kwmenu.' + k: v for k, v in table.items()}, ensure_ascii=False, indent=2) + '\n')
    print('menus built into', ROOT)


if __name__ == '__main__':
    main()
