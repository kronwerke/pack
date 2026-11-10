# Kronwerke override of Incendium 5.4.4 player/main, see the pack CHANGELOG 0.11.51.
# The item part (about forty checks of held and worn Incendium items) moved to player/kw_items and only runs
# for players who hold or wear an Incendium item, or still have state from one (a thrown trident, a bow
# being unloaded, a scroll tag, restless nature). Everything else runs for every player every tick as before.
# from: clocks/main
# @s: player tick

# say hello?
# no, I don't think I will :)

#> in.valid_player
#>   a non-invis player, non-creative, non-spectator player
#>   used extensively in custom mob targetting and more
tag @s remove in.valid_player
tag @s remove in.survival_player
tag @s[gamemode=survival] add in.survival_player
tag @s[gamemode=adventure] add in.survival_player
tag @s[tag=in.survival_player,tag=!in.invis] add in.valid_player

# check eid resets
execute unless score @s in.eid matches 0..32767 run function incendium:technical/entity_id/check

# are scores set?
execute unless entity @s[scores={in.cd_shield=-1..}] run scoreboard players add @s in.cd_shield 0
execute unless entity @s[scores={in.cd_charm=-1..}] run scoreboard players add @s in.cd_charm 0
execute unless entity @s[scores={in.cd_corrupt=-1..}] run scoreboard players add @s in.cd_corrupt 0

#function incendium:player/advancements/main

# shielding
scoreboard players set @s[advancements={incendium:technical/using/shield={requirement=false}}] in.shielding 0
execute if entity @s[advancements={incendium:technical/using/shield=true}] run function incendium:player/event/shielding

execute unless score @s in.wet matches -2147483647.. run scoreboard players set @s in.wet 0

# items
execute if items entity @s weapon.* *[minecraft:custom_data~{incendium:{}}] run return run function incendium:player/kw_main_tail_items
execute if items entity @s armor.head *[minecraft:custom_data~{incendium:{}}] run return run function incendium:player/kw_main_tail_items
execute if entity @s[scores={in.trident=1..}] run return run function incendium:player/kw_main_tail_items
execute if entity @s[scores={in.trailblazer=1..}] run return run function incendium:player/kw_main_tail_items
execute if entity @s[scores={in.ragnarok=1..}] run return run function incendium:player/kw_main_tail_items
execute if entity @s[scores={in.restless_nature=1..}] run return run function incendium:player/kw_main_tail_items
execute if entity @s[tag=in.scroll] run return run function incendium:player/kw_main_tail_items
execute if entity @s[tag=in.trailblazer_fix] run return run function incendium:player/kw_main_tail_items
execute if entity @s[tag=in.ragnarok_fix] run return run function incendium:player/kw_main_tail_items
function incendium:player/kw_tail
