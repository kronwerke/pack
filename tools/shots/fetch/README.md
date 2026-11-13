# Getting the camera's pictures off the server

These are the scripts of the machine that drives the camera (paths inside them are that
machine's). They are kept here so that they are not lost with it.

- `unsheet.py <shots-world sha> <tag> <prefix> <outdir> <since_ms>`: joins the fetched pieces
  of `/kw cam sheet <prefix>` into contact sheets of eight pictures, each lettered with its
  name. For looking at a run before anything is fetched in full.
- `unbundle5.py <tag> <outdir> <since_ms> <index file>`: joins the fetched pieces of
  `/kw cam bundle <prefix>` and cuts them by the bundle's own `index.json`. The names come
  from the server, so a stray picture with the same prefix cannot shift the rest.
- `takeshots.py <dir> [-x name ...]`: packs the pictures again without loss (a quarter
  smaller) and puts them into `kubejs/assets/kronwerke/textures/quests/shots`, all but the
  names after `-x` and the quests listed in `same.json`.
- `packbump.sh <core version|-> <pack version> "<subject>"`: bumps the pack, pushes, waits
  for the CI commit and prints its sha (the pack release goes on that commit).
