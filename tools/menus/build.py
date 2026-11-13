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


def uid(name):
    return f'{uuid.uuid5(NS, name)}-{STAMP}'


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


def title(name, art, hours):
    L = name
    b = ''
    b += image(L + ':logo', 'logo.png', 'top-right', COL - 8, 8, 163, 62)
    b += button(L + ':join', local('join'), 'top-right', COL, 78, CW, 32, 'btn_main.png', 'btn_main_hover.png',
                [('joinserver', SERVER)], tip=local('join.tip'))
    players = ph('json', source=STATUS, json_path='$.server.players')
    most = ph('json', source=STATUS, json_path='$.server.max')
    b += text(L + ':status', centered(gold(local('status')) + ' ' + players + ' / ' + most), 'top-right', COL, 110, CW, 16,
              req=requirement(L + ':status', lines=[('fancymenu_visibility_requirement_is_number', 'if',
                                                     '["mode":"bigger-than-or-equals","number":"%s","compare_with":"0"]$' % players)]))
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
    return layout(name, 'title_screen', b, background=art, behind=False, req=requirement(name + ':layout', hours=hours), parallax=True)


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
    return layout(L, 'join_multiplayer_screen', b, scale=None)


# ---------------------------------------------------------------------------------------------
# pause screen: the world stays visible, logo on top, one column
# ---------------------------------------------------------------------------------------------

def pause():
    L = 'pause'
    x, y = -74, -52
    b = image(L + ':logo', 'logo.png', 'mid-centered', -82, y - 70, 163, 62)
    b += vanilla('mc_pausescreen_return_to_game_button', 'mid-centered', x, y, CW, 20, 'btn_wide.png', 'btn_wide_hover.png', layout=L)
    b += button(L + ':quests', local('quests'), 'mid-centered', x, y + 24, 72, 20, 'btn_half.png', 'btn_half_hover.png',
                [('closegui', ''), ('mimic_keybind', 'key.ftbquests.quests|||false|||100')])
    b += button(L + ':map', local('map'), 'mid-centered', x + 76, y + 24, 72, 20, 'btn_half.png', 'btn_half_hover.png',
                [('closegui', ''), ('mimic_keybind', 'key.ftbchunks.map|||false|||100')])
    b += vanilla('mc_pausescreen_advancements_button', 'mid-centered', x, y + 48, 72, 20, 'btn_half.png', 'btn_half_hover.png', layout=L)
    b += vanilla('mc_pausescreen_stats_button', 'mid-centered', x + 76, y + 48, 72, 20, 'btn_half.png', 'btn_half_hover.png', layout=L)
    b += vanilla('mc_pausescreen_options_button', 'mid-centered', x, y + 72, 72, 20, 'btn_half.png', 'btn_half_hover.png',
                 label=local('options'), layout=L)
    b += button(L + ':discord', '', 'mid-centered', x + 76, y + 72, 20, 20, 'icon_chat.png', 'icon_chat_hover.png', [('openlink', DISCORD)], tip=local('discord.tip'))
    b += button(L + ':web', '', 'mid-centered', x + 102, y + 72, 20, 20, 'icon_home.png', 'icon_home_hover.png', [('openlink', WEBSITE)], tip=local('web.tip'))
    b += button(L + ':status', '', 'mid-centered', x + 128, y + 72, 20, 20, 'icon_book.png', 'icon_book_hover.png', [('openlink', WEBSITE + '/status')], tip=local('status.tip'))
    b += vanilla('mc_pausescreen_disconnect_button', 'mid-centered', x, y + 96, CW, 20, 'btn_wide.png', 'btn_wide_hover.png', layout=L)
    b += hide(L, 'mc_pausescreen_feedback_button', 'mc_pausescreen_report_bugs_button', 'mc_pausescreen_lan_button')
    return layout(L, 'pause_screen', b)


# ---------------------------------------------------------------------------------------------
# the loading screen while the game starts (Drippy): same picture as the title, the bar where
# the big button will be, so the menu grows out of it
# ---------------------------------------------------------------------------------------------

def loading(name, art, hours):
    L = name
    b = image(L + ':logo', 'logo.png', 'top-right', COL - 8, 8, 163, 62)
    b += image(L + ':frame', 'bar_frame.png', 'top-right', COL, 84, CW, 20)
    p = base(L + ':bar', 'progress_bar', 'top-right', COL + 4, 88, CW - 8, 12)
    head = [('bar_color', '#E5B451FF'), ('bar_texture', A + 'bar_fill.png'), ('background_color', '#00000000'), ('direction', 'right'),
            ('progress_source', ph('game_loading_progress')), ('value_mode', 'percentage'), ('smooth_filling_animation', 'true')]
    b += block('element', head + p)
    for lang, mode in (('de', 'if'), ('en', 'if_not')):
        tip = ph('randomtext', source='/config/fancymenu/assets/kronwerke/tips_' + lang + '.txt', interval='6')
        b += text(L + ':tip_' + lang, centered(tip), 'top-right', COL - 20, 110, CW + 40, 40,
                  req=requirement(L + ':tip_' + lang, lines=[('fancymenu_loading_requirement_is_language', mode, 'de_de')]))
    b += hide(L, 'progress_bar', 'mojang_logo')
    return layout(name, 'drippy_loading_overlay', b, background=art, req=requirement(name + ':layout', hours=hours))


LANG = {
    'de_de': {
        'join': 'Kronwerke betreten', 'join.tip': 'Verbindet dich direkt mit dem Kronwerke-Server.', 'status': 'Online:',
        'servers': 'Serverliste', 'options': 'Optionen', 'quit': 'Beenden', 'discord.tip': 'Zum Discord', 'web.tip': 'kronwerke.com',
        'lang.tip': 'Sprache', 'countdown.a': 'Season 2 startet in', 'countdown.b': 'Tagen', 'quests': 'Questbuch', 'map': 'Karte', 'status.tip': 'Live-Status der Season',
    },
    'en_us': {
        'join': 'Enter Kronwerke', 'join.tip': 'Connects you straight to the Kronwerke server.', 'status': 'Online:',
        'servers': 'Server list', 'options': 'Options', 'quit': 'Quit', 'discord.tip': 'Open Discord', 'web.tip': 'kronwerke.com',
        'lang.tip': 'Language', 'countdown.a': 'Season 2 starts in', 'countdown.b': 'days', 'quests': 'Quest book', 'map': 'Map', 'status.tip': 'Live status of the season',
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
    dusk = None
    for mode in scene.PAL:
        c = scene.build(mode)
        c.image(4).save(os.path.join(ASSETS, f'title_{mode}.png'), optimize=True)
        if mode == 'dusk':
            dusk = c
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
    write(os.path.join(FM, 'customizablemenus.txt'), 'type = customizablemenus\n\n' + ''.join(s + ' {\n}\n\n' for s in SCREENS))
    for lang, table in LANG.items():
        write(os.path.join(ROOT, 'kubejs', 'assets', 'kwmenu', 'lang', lang + '.json'),
              json.dumps({'kwmenu.' + k: v for k, v in table.items()}, ensure_ascii=False, indent=2) + '\n')
    print('menus built into', ROOT)


if __name__ == '__main__':
    main()
