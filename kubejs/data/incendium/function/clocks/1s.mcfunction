# Kronwerke override of Incendium 5.4.4 clocks/1s.
# clock: 1s

schedule function incendium:clocks/1s 1s replace

function incendium:castle/1s

execute as @a at @s run function incendium:player/1s

execute as @e[type=blaze,tag=in.dune_blaze] at @s run function incendium:entity/dune_blaze/1s
execute as @e[type=blaze,tag=in.sentry] at @s run function incendium:entity/sentry/1s

effect give @e[type=piglin,predicate=incendium:biome/toxic_heap] poison 10 1


scoreboard players remove @e[type=vex,tag=in.spirit] in.lifetime 1
scoreboard players remove @e[type=slime,tag=in.toxic_slime] in.lifetime 1

# Kronwerke: moved here from clocks/main, where it walked every mob every tick.
execute in minecraft:the_nether as @e[type=#incendium:mobs_no_player,tag=!in.ticking_entity,distance=0..] unless score @s in.eid matches 0..32767 run function incendium:technical/entity_id/check
