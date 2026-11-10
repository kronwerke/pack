# Kronwerke: the end of Incendium 5.4.4 player/main (counters and resets), unchanged, see player/main.

# Kronwerke: from the restless nature block, reset after the item part read it.
scoreboard players set @s in.use_snowball 0

# decr scoreboards
scoreboard players remove @s[scores={in.cd_shield=1..}] in.cd_shield 1
scoreboard players remove @s[scores={in.cd_corrupt=1..}] in.cd_corrupt 1
scoreboard players remove @s[scores={in.cd_charm=1..}] in.cd_charm 1
scoreboard players remove @s[scores={in.cd_weapon=1..}] in.cd_weapon 1
scoreboard players remove @s[scores={in.cd_wrath=1..}] in.cd_wrath 1
scoreboard players remove @s[scores={in.immunity=1..}] in.immunity 1
scoreboard players remove @s[scores={in.wet=1..}] in.wet 1

scoreboard players operation @s in.old_health = @s in.health

# resets
scoreboard players set @s in.netherrack 0
scoreboard players set @s in.basalt 0
scoreboard players set @s in.blackstone 0
scoreboard players set @s in.prism 0
scoreboard players set @s in.use_map 0

scoreboard players set @s in.use_bow 0
scoreboard players set @s in.trident 0
