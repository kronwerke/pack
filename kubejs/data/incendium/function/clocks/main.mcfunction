# Kronwerke override of Incendium 5.4.4 clocks/main, see the pack CHANGELOG 0.11.40.
# clock: 1t

schedule function incendium:clocks/main 1t replace

function incendium:technical/main
execute as @a at @s run function incendium:player/main
function incendium:castle/main

# mob init
# Kronwerke: mob init and mob ticking only look at the Nether (distance=0.. keeps the selector in the dimension of execute in).
# Every Incendium mob feature is tied to Nether biomes and structures; a selector without it walks every entity of every dimension.
execute in minecraft:the_nether as @e[type=#incendium:mobs_no_player, tag=!in.checked, distance=0..] at @s run function incendium:entity/mob/init

# Kronwerke: every tick only for Incendium's own ticking mobs; the full sweep over all mobs runs once a second in clocks/1s.
execute in minecraft:the_nether as @e[type=#incendium:mobs_no_player,tag=in.ticking_entity,distance=0..] unless score @s in.eid matches 0..32767 run function incendium:technical/entity_id/check
execute in minecraft:the_nether as @e[type=#incendium:mobs_no_player, tag=in.ticking_entity, distance=0..] at @s run function incendium:entity/mob/main

scoreboard players remove @e[type=#incendium:mobs,scores={in.frozen=1..}] in.frozen 1
execute at @e[type=#incendium:mobs,scores={in.frozen=1..},predicate=incendium:random/10] run particle minecraft:snowflake ~ ~1.6 ~ 0.1 0.05 0.1 .1 5 force

# other
execute as @e[type=#incendium:other, tag=!in.checked] at @s run function incendium:entity/other/init

execute as @e[type=#incendium:other, tag=in.ticking_entity] at @s run function incendium:entity/other/main

execute if entity @a[tag=nbs_borderofli] run function incendium:border_of_life/tick

# shield cloud effect clear
execute if entity @e[scores={in.cd_shield=1..},predicate=incendium:holding/radiation_shield] run effect clear @e[scores={in.cd_shield=1..},predicate=incendium:holding/radiation_shield] poison

execute if entity @e[scores={in.cd_shield=1..},predicate=incendium:holding/necrotic_shield] run effect clear @e[scores={in.cd_shield=1..},predicate=incendium:holding/necrotic_shield] wither
