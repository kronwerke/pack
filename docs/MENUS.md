# Menus

The title screen, the pause screen, the server list, the loading screen while the game starts
and the background of every other menu are built with FancyMenu and Drippy Loading Screen.
Nothing is made in FancyMenu's editor: `tools/menus/build.py` draws the pixel art and writes
the layout files, so the menus can be rebuilt, compared and reviewed like code.

    python3 tools/menus/build.py            # into this repo
    python3 tools/menus/build.py <folder>   # into another game folder, for a test client

## What is generated

| Path | Content |
|---|---|
| `config/fancymenu/assets/kronwerke/` | artwork (dusk and night), logo, button plates, icons, bar, tips |
| `config/fancymenu/customization/kw_*.txt` | the layouts |
| `config/fancymenu/customizablemenus.txt` | the screens FancyMenu may touch |
| `config/fancymenu/options.txt` | pack mode, window title and icon |
| `kubejs/assets/kwmenu/lang/` | the menu's own texts, German and English |
| `kubejs/assets/minecraft/textures/gui/sprites/widget/` | the game's buttons and sliders in brass, for every screen |

Do not edit these by hand. Change `build.py` (layouts, texts, links) or the scripts in
`tools/menus/art/` (`scene.py` and `works.py` draw the picture, `ui.py` the logo and plates,
`px.py` is the small pixel toolkit) and run the build again.

## How it is put together

- Everything sits on a 480x270 grid: FancyMenu scales the layouts to GUI scale 4 at 1920x1080
  and with the window from there, and the artwork is drawn on the same grid, so one art pixel is
  one GUI pixel.
- The artwork is drawn by `scene.py` from shapes, ramps and patterns. Nothing is traced or
  taken from elsewhere. The night version uses the same drawing with a cooler palette and is
  shown from 20:00 to 06:00 (the player's clock), through two layouts with an hour requirement.
- The large button joins `kronwerke.net` directly. The line below it reads the player count
  from `https://kronwerke.com/api/status` and hides when there is no answer.
- The countdown in the lower left shows until the season starts (16.01.2027 18:00).
- The pause screen uses the same column on the right as the title screen, so the view and the
  texts other mods draw on the left stay free. Its quest book button sends
  `/ftbquests open_book` (the book has no key in the pack), the map button presses the map key.
- Widgets are addressed by FancyMenu's identifiers. Named ones (`mc_titlescreen_*`,
  `pause_*`) are stable. Unnamed ones are numbers made from the widget's position on a
  1000x1000 screen: `398348` is NeoForge's Mods button on the pause screen, `40` the "Game
  Menu" line, `376388` and `604388` the language and accessibility icons of the title screen.
- Buttons other mods add to these screens (the Aether's menu list, Create's and
  Supplementaries' config buttons) are switched off in those mods' configs, which the build
  writes as well.
- Joining and loading the world are not FancyMenu's: Core draws its own picture there
  (`JoinOverlay`, `TravelOverlay`).

## Looking at it

`tools/menus/fmrender.py` gives a rough offline preview of a layout. The real check is a
client: a small test client with only FancyMenu, Drippy, Konkrete, Melody and Core starts in
under a minute and is enough for the title, the lists and the loading screen. The pause screen
and anything other mods add must be looked at in the full pack.
