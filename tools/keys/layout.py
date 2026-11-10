"""The pack's key layout: every key a mod binds by default that clashes with another, moved to
a free key or a modifier combination, with vanilla's keys left where players expect them.

Input: a dump of every key mapping of the client (name, category, default key and modifier,
current key and modifier, conflict context), made by Kronwerke Core with
-Dkronwerke.dumpKeys=<file> on a client with the pack's mods. Output:

- config/defaultoptions/keybindings.txt: the whole layout, which Default Options writes into a
  new instance and uses as the defaults for "reset";
- the Core resource assets/kronwerke/keys.tsv: every key whose pack key differs from the mod's
  default, so Core moves it in instances that started before (only keys still on the mod's
  default).

    python3 tools/keys/layout.py keys-dump.tsv ../core/src/main/resources/assets/kronwerke/keys.tsv [old-keybindings.txt]

With the keybindings.txt of an earlier layout as third argument, keys that sit on that earlier
pack default are moved too (they were never chosen by the player either).

The script refuses to write while two keys that can be active at the same time share a key.
"""
import collections
import os
import sys

# bump when the layout changes, so Core applies it once more (only to keys still on a mod default)
VERSION = 1

U = "key.keyboard.unknown"


def k(key, mod="NONE"):
    return ("key.keyboard." + key if not key.startswith("key.") else key, mod)


A, C, S = "ALT", "CONTROL", "SHIFT"

# The layout of 0.11.30 (Samuel's choices of 2026-10-09 among them: sort and ping on the middle
# mouse button, pick block on mouse 5), kept as it was; see docs/KEYS.md
BASE = {
    "iris.keybind.reload": k("f6"),
    "iris.keybind.shaderPackSelection": k("o", A),
    "iris.keybind.toggleShaders": k("k", A),
    "key.aether.invisibility_toggle.desc": k("i", S),
    "key.ars_nouveau.head_curio_hotkey": k("h", A),
    "key.ars_nouveau.next_slot": k("x", C),
    "key.ars_nouveau.open_book": k("c", C),
    "key.ars_nouveau.previous_slot": k("z", C),
    "key.botania_corporea_request": k("n", C),
    "key.cataclysm.ability": k("v", S),
    "key.cataclysm.boots_ability": k("b", C),
    "key.cataclysm.chestplate_ability": k("y", C),
    "key.cataclysm.helmet_ability": k("y", A),
    "key.deeperdarker.boost": k("n", A),
    "key.deeperdarker.transmit": k("t", A),
    "key.disable_voice_chat": k(U),
    "key.draconicevolution.place_item": k("p", A),
    "key.draconicevolution.tool_config": k("c", A),
    "key.drawMahoujin": k("m", C),
    "key.enderio.toggle_magnet": k("m", S),
    "key.enderio.travel_staff": k("g", C),
    "key.gunDown": k("down", A),
    "key.gunUp": k("up", A),
    "key.hexerei.book_hovering_recipe": k("r", C),
    "key.hexerei.book_hovering_uses": k("u", A),
    "key.hexerei.broomActivate": k("j", A),
    "key.hexerei.glasses_zoom": k("h", C),
    "key.hide_icons": k(U),
    "key.hostilenetworks.open_deep_learner": k("d", A),
    "key.integratedterminals.terminal.portable.open": k("i", C),
    "key.inventorytweak.sort_inventory_key": ("key.mouse.middle", "NONE"),
    "key.irons_spellbooks.spellbook_cast": k("v", C),
    "key.kubejs.kubedex": k(U),
    "key.loadToolbarActivator": k(U),
    "key.mute_microphone": k(U),
    "key.neoorigins.skill_1": k("z"),
    "key.neoorigins.skill_2": k("x"),
    "key.neoorigins.skill_3": k("c"),
    "key.neoorigins.skill_4": k("r", A),
    "key.neoorigins.class_skill": k("h"),
    "key.occultism.backpack": k("g", A),
    "key.occultism.ender_bag": k("e", A),
    "key.occultism.storage_remote": k("s", A),
    "key.oritech.augment_screen": k("a", A),
    "key.saveToolbarActivator": k(U),
    "key.selectiveDisplacement": k("h", S),
    "key.sophisticatedbackpacks.inventory_interaction": k("i", A),
    "key.toastcontrol.clear": k(U),
    "key.voice_chat": k("v", A),
    "key.voice_chat_group": k("g", S),
    "pneumaticcraft.armor.options": k("u", C),
    "pneumaticcraft.boots.kick": k("j", C),
    "pneumaticcraft.chestplate.launcher": k("l", C),
    "pneumaticcraft.helmet.debugging.drone": k(U),
    "pneumaticcraft.helmet.hack": k("p", C),
    "simplemagnets.keys.toggle": k("m", A),
    "key.pingwheel.ping_location": ("key.mouse.middle", "NONE"),
    "key.pickItem": ("key.mouse.5", "NONE"),
}

# keys the 0.11.30 layout did not cover, which still clashed with it or each other
EXTRA = {
    # Zume: zoom on the side button next to the ping; scrolling while zoomed changes how far
    "zume.zoom": ("key.mouse.4", "NONE"),
    "zume.zoom_in": k(U), "zume.zoom_out": k(U),
    # Mekanism's MekaSuit modes on ALT and the number of the armour piece, the HUD on ALT+0
    "key.mekanism.head_mode": k("1", A), "key.mekanism.chest_mode": k("2", A),
    "key.mekanism.legs_mode": k("3", A), "key.mekanism.feet_mode": k("4", A),
    "key.mekanism.key_hud": k("0", A),
    "key.mekanism.module_tweaker": k("backslash", A),
    "key.mekanismadditions.voice": k(U),
    # JourneyMap: the full map stays on J and the minimap on its own; the rest is in the map
    "key.journeymap.create_waypoint": k("b", S),
    "key.journeymap.fullscreen_waypoints": k(U), "key.journeymap.toggle_entity_names": k(U),
    "key.journeymap.minimap_preset": k(U), "key.journeymap.minimap_type": k(U),
    "key.journeymap.minimap_toggle_alt": k(U),
    "key.ftbchunks.minimap.zoomIn": k(U), "key.ftbchunks.minimap.zoomOut": k(U),
    # the Accessories screen on I, which the Aether's own key opened too
    "accessories.key.open_accessories_screen": k("i"),
    "key.aether.open_accessories.desc": k(U),
    # Iron Jetpacks
    "key.jetpack.toggle_active.description": k("j", S),
    "key.jetpack.toggle_hover.description": k("k", S),
    # gadgets, only while one is in hand
    "key.buildinggadgets2.settings_menu": k("b", A),
    "key.buildinggadgets2.anchor": k("a", C),
    "key.buildinggadgets2.range": k("r", S),
    "key.buildinggadgets2.undo": k("u", S),
    "justdirethings.key.toggle_tool": k("t", S),
    "key.immersiveengineering.magnetEquip": k("s", C),
    # carried things
    "supplementaries.keybind.quiver": k("q", A),
    "key.ars_elemental.open_pouch": k("p", S),
    # rare and accidental
    "key.evilcraft.fart": k(U), "key.evilcraft.exaltedCrafting": k(U),
    "key.unmountVehicle": k(U),
}

LAYOUT = {**BASE, **EXTRA}

# keys that are meant to sit on what they share: held modifiers and contextual movement keys
SHARED_OK = {"key.keyboard.left.shift", "key.keyboard.left.control", "key.keyboard.left.alt", "key.keyboard.space",
             "key.mouse.left", "key.mouse.right", "key.mouse.middle", U}
# conflict contexts that only matter in screens
SCREEN = ("GUI", "JEI", "net.p3pp3rf1y.sophisticatedcore.client.ClientEventHandler", "com.direwolf20.justdirethings.client.KeyBindings$KeyConflictContextConfigScreen")


# keys of a screen that registered them as universal: Power Grid's circuit editor, the search
# field of Refined Storage's grid
SCREEN_KEYS = {"powergrid.keyinfo.rotate_component", "powergrid.keyinfo.place_trace", "powergrid.keyinfo.delete_area",
               "powergrid.keyinfo.pick_component", "powergrid.keyinfo.switch_layer", "key.refinedstorage.focus_search_bar",
               "key.ponder.ponder"}


def screen_only(ctx, name):
    return ctx.startswith(SCREEN) or name in SCREEN_KEYS


def main(dump, tsv, old=None):
    rows = [l.rstrip("\n").split("\t") for l in open(dump) if l.strip()]
    names = {r[0] for r in rows}
    unknown = [n for n in LAYOUT if n not in names]
    if unknown:
        sys.exit(f"keys in the layout that the client does not have: {unknown}")
    final = {}
    for name, cat, dk, dm, ck, cm, ctx in rows:
        final[name] = (LAYOUT[name] if name in LAYOUT else (dk, dm), ctx, (dk, dm))
    clash = collections.defaultdict(list)
    for name, ((key, mod), ctx, _) in final.items():
        if key in SHARED_OK or screen_only(ctx, name):
            continue
        clash[(key, mod)].append(name)
    bad = {kk: v for kk, v in clash.items() if len(v) > 1}
    if bad:
        for kk, v in sorted(bad.items()):
            print("clash", kk, v)
        sys.exit(f"{len(bad)} keys still clash")

    here = os.path.dirname(os.path.abspath(__file__))
    opts = os.path.join(here, "..", "..", "config", "defaultoptions", "keybindings.txt")
    with open(opts, "w") as f:
        for name in sorted(final):
            (key, mod), _, _ = final[name]
            f.write(f"key_{name}:{key}:{mod}\n")
    earlier = {}
    if old:
        for line in open(old):
            line = line.strip()
            if line.startswith("key_") and line.count(":") >= 2:
                name, key, mod = line[4:].rsplit(":", 2)
                earlier[name] = (key, mod)
    moved = 0
    with open(tsv, "w") as f:
        f.write("# The pack's key layout, written by the pack's tools/keys/layout.py. name, mod default key and modifier, pack key and modifier.\n")
        f.write(f"version\t{VERSION}\n")
        for name in sorted(final):
            (key, mod), _, (dk, dm) = final[name]
            if (key, mod) != (dk, dm):
                f.write(f"{name}\t{dk}\t{dm}\t{key}\t{mod}\n")
                moved += 1
            e = earlier.get(name)
            if e and e != (key, mod) and e != (dk, dm):
                f.write(f"{name}\t{e[0]}\t{e[1]}\t{key}\t{mod}\n")
    print(f"{len(final)} keys, {moved} moved from their mod default, no clashes")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
