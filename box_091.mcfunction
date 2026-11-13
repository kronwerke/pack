# 091 botania_runes/terrasteel
#area 182 139 203 164
fill 182 64 139 203 91 164 minecraft:air
fill 182 60 139 203 62 164 minecraft:stone
fill 182 63 139 203 63 164 minecraft:light_gray_concrete
fill 186 64 145 203 79 145 minecraft:light_gray_concrete
fill 186 64 145 186 79 158 minecraft:light_gray_concrete
setblock 187 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 188 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 198 64 145 198 79 158 minecraft:light_gray_concrete
setblock 191 64 149 botania:livingrock
setblock 191 64 150 minecraft:lapis_block
setblock 191 64 151 botania:livingrock
setblock 192 64 149 minecraft:lapis_block
setblock 192 64 150 botania:livingrock
setblock 192 64 151 minecraft:lapis_block
setblock 193 64 149 botania:livingrock
setblock 193 64 150 minecraft:lapis_block
setblock 193 64 151 botania:livingrock
setblock 192 65 150 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 192.5 66.25 150.5 {Tags:["kw_shot"]}
setblock 188 64 150 botania:mana_pool{mana:1000000}
summon botania:mana_spark 188.5 65.25 150.5 {Tags:["kw_shot"]}
setblock 196 64 150 botania:mana_pool{mana:1000000}
summon botania:mana_spark 196.5 65.25 150.5 {Tags:["kw_shot"]}
summon item 192.5 65.3 150.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 150.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 150.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
