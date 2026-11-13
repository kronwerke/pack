# 091 botania_runes/terrasteel
#area 182 145 203 170
fill 182 64 145 203 91 170 minecraft:air
fill 182 60 145 203 62 170 minecraft:stone
fill 182 63 145 203 63 170 minecraft:light_gray_concrete
fill 186 64 151 203 79 151 minecraft:light_gray_concrete
fill 186 64 151 186 79 164 minecraft:light_gray_concrete
setblock 187 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 188 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 198 64 151 198 79 164 minecraft:light_gray_concrete
setblock 191 64 155 botania:livingrock
setblock 191 64 156 minecraft:lapis_block
setblock 191 64 157 botania:livingrock
setblock 192 64 155 minecraft:lapis_block
setblock 192 64 156 botania:livingrock
setblock 192 64 157 minecraft:lapis_block
setblock 193 64 155 botania:livingrock
setblock 193 64 156 minecraft:lapis_block
setblock 193 64 157 botania:livingrock
setblock 192 65 156 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 192.5 66.25 156.5 {Tags:["kw_shot"]}
setblock 188 64 156 botania:mana_pool{mana:1000000}
summon botania:mana_spark 188.5 65.25 156.5 {Tags:["kw_shot"]}
setblock 196 64 156 botania:mana_pool{mana:1000000}
summon botania:mana_spark 196.5 65.25 156.5 {Tags:["kw_shot"]}
summon item 192.5 65.3 156.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 156.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 156.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
