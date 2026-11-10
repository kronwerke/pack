# Server settings

The servers install the pack with packwiz, configs included. Every pack update writes the shipped config files again, so a value changed by hand in `config/` on a server is gone after the next update. The pack ships defaults; what a server changes lives in files the pack never contains.

## Kronwerke Core

`kronwerke/overrides.properties` in the server folder, next to `kronwerke/servers/`. One line per setting, the key is the config path from `config/kronwerke-common.toml`:

```
locks.machineLocks=false
slots.defaultSlots=6
spawn.radius=48
mobs.health=0.0, 0.2, 0.5, 0.9, 1.4
testing.testCommands=true
```

Core reads it at every start and on every config reload and puts it over the shipped file. Lists are written comma separated. A key that is no setting, or a value that does not fit, is named in the log and skipped. `/kw admin locks on|off` writes its value there by itself. The queue limit keeps its own file, `kronwerke/queue-limit.txt`.

## FTB Chunks

A copy of `config/ftbchunks-world.snbt` in `world/serverconfig/ftbchunks-world.snbt` wins over the shipped one and is never written by an update. Use it only for a value one server needs; everything the whole network needs goes into the pack.

## What the pack sets and why

| File | Setting | Why |
| --- | --- | --- |
| `ftbchunks-world.snbt` | 9 force loaded chunks per team (3 by 3), released after 7 days without a login; claims released after 30 days | Machines of players who stopped keep no chunks ticking for the rest of the season. |
| `ftbchunks-world.snbt` | Fire and fluid protection on | Lava or fire placed next to a claim does not burn into it. |
| `ftbchunks-world.snbt` | PvP per team, off in claims by default | A claim is safe unless its team turns PvP on. |
| `quarryplus.toml` | Chunk loader off, bedrock module off | Quarries load no chunks outside FTB Chunks' limits and open no holes to the void. |
| `voicechat-server.properties` | Recording off | Nobody records the voice chat, as the privacy page says. |
| `kronwerke-common.toml` | `streamersManageOwnSlots = false` | Places are given through the Discord bot, which checks the Discord membership. |
