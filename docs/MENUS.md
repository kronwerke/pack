# Menus

The title screen, the pause screen, the server list, the loading screen while the game starts
and the background of every other menu are built with FancyMenu and Drippy Loading Screen.
Nothing is made in FancyMenu's editor: `tools/menus/build.py` draws the pixel art and writes
the layout files, so the menus can be rebuilt, compared and reviewed like code.

    python3 tools/menus/build.py            # into this repo
    python3 tools/menus/build.py <folder>   # into another game folder, for a test client
    python3 tools/menus/build.py --layouts  # only the layout files (the pictures take minutes)

## What is generated

| Path | Content |
|---|---|
| `config/fancymenu/assets/kronwerke/` | artwork (dusk and night: `art_*.png` whole, `title_*.png` its middle enlarged), the moving parts as `anim_*.apng`, logo, button plates, icons, bar, tips |
| `config/fancymenu/customization/kw_*.txt` | the layouts |
| `config/fancymenu/customizablemenus.txt` | the screens FancyMenu may touch |
| `config/fancymenu/options.txt` | pack mode, window title and icon |
| `config/drippyloadingscreen/options.txt` | the early window (logo and bar before the game's own loading screen) |
| `kubejs/assets/kwmenu/lang/` | the menu's own texts, German and English |
| `kubejs/assets/minecraft/textures/gui/sprites/widget/` | the game's buttons and sliders in brass, for every screen |

Do not edit these by hand. Change `build.py` (layouts, texts, links) or the scripts in
`tools/menus/art/` (`scene.py` and `works.py` draw the picture, `ui.py` the logo and plates,
`px.py` is the small pixel toolkit) and run the build again.

## How it is put together

- The layouts set no scale of their own: they run at the game's GUI scale, which is a whole
  number, so one art pixel is a whole number of screen pixels in every window. (They used to
  force scale 4 and let FancyMenu scale that with the window: any window that was not 1920x1080
  got a stretched picture and uneven pixels, and the loading overlay applied the forced scale to
  the sizes but not to the positions, which threw logo, bar and tip across the screen.)
- The picture is painted 640x360 around its 480x270 middle (`scene.py`: `W, H` and the margin
  `OX, OY`) and laid into the middle of the screen as an element, one art pixel on one GUI
  pixel. At 1920x1080 and the automatic GUI scale the screen shows exactly the middle; a window
  of another shape or a smaller GUI scale shows more of the valley instead of a stretched
  picture. Where even 640x360 does not cover the GUI (somebody playing at GUI scale 2), a
  second element shows the same picture with two GUI pixels to the art pixel. Behind both lies
  the layout's own background, stretched, for the rare screen that is larger still.
- Buttons and texts hang on the screen's edges (top right, bottom left) and fit a GUI of
  384x240, the smallest the automatic scale gives a 16:10 window.
- The artwork is drawn by `scene.py` from shapes, ramps and patterns. Nothing is traced or
  taken from elsewhere. The night version uses the same drawing with a cooler palette and is
  shown from 20:00 to 06:00 (the player's clock), through two layouts with an hour requirement.
- The picture moves. `scene.build(mode, t)` draws frame `t` of a loop of 200 frames at 100 ms:
  the train comes in from the left, stands at the works and leaves to the right, smoke rises
  from the chimney and the engine, the gears in the tower, at the gate and the water wheel
  turn, stars and the lake glitter, birds cross. FancyMenu cannot play a full screen video
  cheaply, so only the parts that move are cut out as animated PNGs (`SPRITES` in `build.py`:
  region, frames, time per frame) and laid over the still picture. Every frame of such a file
  is a whole frame: FancyMenu draws each one on its own, and Pillow's writer stores only the
  changed part (`px.apng` writes them instead). The sprites are placed from the middle of the
  screen like the picture itself, so they move in every window. They lie under the game's buttons
  (`render_custom_elements_behind_vanilla`), and elements with the same time stamp in their id
  are stacked in no fixed order, which is why `uid()` counts the stamps up.
- Before the game's loading screen NeoForge shows its early window. The Drippy Early Loading
  Module (`mods/drippy-early-loading-module.pw.toml`) puts the dusk picture, the logo and a
  brass bar there. It places in absolute pixels and does not scale with the window, so logo
  and bar are centred, and the loading layout that follows is centred the same way (its logo
  is the same size only at GUI scale 4).
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
  (`JoinOverlay`, `TravelOverlay`). The music of the menus is Core's too (`MenuMusic`).

## Looking at it

`tools/menus/fmrender.py` gives a rough offline preview of a layout. The real check is a
client: a small test client with only FancyMenu, Drippy, Konkrete, Melody and Core starts in
under a minute and is enough for the title, the lists and the loading screen. The pause screen
and anything other mods add must be looked at in the full pack.
