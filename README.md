```
 _  __                                 _        
| |/ /_ __ ___  _ ____      _____ _ __| | _____ 
| ' /| '__/ _ \| '_ \ \ /\ / / _ \ '__| |/ / _ \
| . \| | | (_) | | | \ V  V /  __/ |  |   <  __/
|_|\_\_|  \___/|_| |_|\_/\_/ \___|_|  |_|\_\___|
                                                
                          p a c k
```

**The modpack for Kronwerke Season 2: tech and magic on NeoForge 1.21.1, built for a server where the whole community unlocks progression together.**

[![ci](https://github.com/kronwerke/pack/actions/workflows/ci.yml/badge.svg)](https://github.com/kronwerke/pack/actions/workflows/ci.yml)
![status](https://img.shields.io/badge/status-early-orange)
![minecraft](https://img.shields.io/badge/minecraft-1.21.1-blue)
![neoforge](https://img.shields.io/badge/neoforge-21.1.252-blue)
![licence](https://img.shields.io/badge/licence-MIT-green)
[![made by](https://img.shields.io/badge/made%20by-Elchi-black)](https://github.com/Elchi-dev)

## Overview

Big kitchen sink packs give experienced players a straight line to the endgame in a week while newcomers stand at spawn with no idea what to do. Kronwerke runs for one to two months with streamers and their viewers, and most of them have never played modded. The pack has to carry both.

## The trick

Progression is gated in stages and the gates open for everyone at once. Inside a stage, quests lead each player from "what is this" to "I built that". Between stages, the server needs the community to reach a goal.

```
  Stage 1 ──── community goal ────► Stage 2 ──── community goal ────► Stage 3 ...
  quests inside                      quests inside                      quests inside
```

The stage locks come from Chapters, the quests from FTB Quests, the goals from [Kronwerke Core](https://github.com/kronwerke/core).

## Parts

| Part | What |
| --- | --- |
| `pack.toml`, `index.toml`, `mods/` | The packwiz pack: every mod pinned to a version and a hash |
| `config/ftbquests/` | The quest book, generated from `tools/quests/` by CI on every push, never edited by hand |
| `tools/quests/` | Quest definitions in Python, the generator (`build.py`), `check_items.py` (every id exists in a jar) and `check_quest_stages.py` (no quest or crate hands out an item before its stage) |
| `kubejs/data/kronwerke/chapters/stages/` | What each stage unlocks, one file per stage, read by Chapters |
| `kubejs/server_scripts/` | Recipe changes: the tech and magic cross recipes, the Mining Dimension key |
| `config/kronwerke/goals.json` | The five community goals, read by Kronwerke Core |
| `docs/STAGES.md` | The design behind both: rules, timeline, numbers |
| `tools/` | Scripts used while building: checking mods against Modrinth, a small RCON client, `check_stages.py` |

## Quick look

Play: import the `.mrpack` from the releases into Prism Launcher or the Modrinth app. CurseForge users take the `.zip`.

Build:

```
go install github.com/packwiz/packwiz@latest
packwiz refresh
packwiz modrinth export
```

Test on a server: install NeoForge 21.1.252, then run `packwiz-installer-bootstrap.jar -g -s server <url to pack.toml>` in the server folder.

## Planned

- A screen for the obelisk (needs Kronwerke Core on clients). Depositing and feeders work since Core 0.3.0.
- A lite client profile for weaker machines.

## Non-goals

- Being the biggest pack. Mods that add nothing to the season's arc are left out.
- Supporting any Minecraft version but 1.21.1 this season.

## Status

Before the beta. 250 mod files, boots clean on a dedicated server. Stage locks, community goals with milestones and about a hundred recipe changes are in; the numbers are untested until the beta in December. The quest book covers all five stages: 61 chapters, about 1 640 quests, in German. Every id is checked against the jars and every item against the stage locks.

## Docs

| Page | What |
| --- | --- |
| `CHANGELOG.md` | What changed per version |
| `docs/STAGES.md` | Stage design: rules, timeline, goal numbers, tech and magic cross recipes |
| `tools/check_mods.py` | Checks a list of Modrinth slugs for NeoForge 1.21.1 versions |

## Licence

MIT for the files in this repository. Each mod keeps its own licence. See `LICENSE`.

Made by [Elchi](https://github.com/Elchi-dev)
