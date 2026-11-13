# Menu research helpers

Small scripts used to study how other modpacks build their menus with FancyMenu
and Drippy Loading Screen. They only read; nothing here is part of the pack build.

- `mrpackscan.py <outdir> <limit> [offset]`: walks the most downloaded Modrinth
  modpacks and pulls only `config/fancymenu` and `config/drippyloadingscreen` out
  of each `.mrpack` with HTTP range requests, so no pack is downloaded whole.
- `fmlayout.py <layout.txt>...`: prints screen, background, element types,
  actions, requirements and placeholders of FancyMenu layout files.
- `fmrender.py <pack root> <layout.txt> <out.jpg> [gui scale]`: draws a rough
  preview of a layout on a 1920x1080 window. Vanilla widgets the layout does not
  touch, animations and requirements are not drawn.

Treat downloaded pack files as untrusted data and keep them outside the repo.
