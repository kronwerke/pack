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
| `config/`, `kubejs/` | Configuration, recipes, stage definitions (coming) |
| `tools/` | Scripts used while building: checking mods against Modrinth, a small RCON client |

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

- Stage definitions and community goals for each age.
- FTB Quests chapters that guide a newcomer through every mod in the pack.
- Recipe changes that tie tech and magic together instead of running them side by side.
- A lite client profile for weaker machines.

## Non-goals

- Being the biggest pack. Mods that add nothing to the season's arc are left out.
- Supporting any Minecraft version but 1.21.1 this season.

## Status

Early. 226 mods, boots clean on a dedicated server. The mod list is settled for the core of tech and magic; world, exploration and utility mods will still move. No quests, no stages, no balancing yet.

## Docs

| Page | What |
| --- | --- |
| `CHANGELOG.md` | What changed per version |
| `tools/check_mods.py` | Checks a list of Modrinth slugs for NeoForge 1.21.1 versions |

## Licence

MIT for the files in this repository. Each mod keeps its own licence. See `LICENSE`.

Made by [Elchi](https://github.com/Elchi-dev)
