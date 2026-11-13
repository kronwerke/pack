# 081 botania_runes/terrasteel
#area 182 109 203 134
fill 182 64 109 203 91 134 minecraft:air
fill 182 60 109 203 62 134 minecraft:stone
fill 182 63 109 203 63 134 minecraft:light_gray_concrete
fill 186 64 115 203 79 115 minecraft:light_gray_concrete
fill 186 64 115 186 79 128 minecraft:light_gray_concrete
setblock 187 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 188 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 198 64 115 198 79 128 minecraft:light_gray_concrete
setblock 191 64 119 botania:livingrock
setblock 191 64 120 minecraft:lapis_block
setblock 191 64 121 botania:livingrock
setblock 192 64 119 minecraft:lapis_block
setblock 192 64 120 botania:livingrock
setblock 192 64 121 minecraft:lapis_block
setblock 193 64 119 botania:livingrock
setblock 193 64 120 minecraft:lapis_block
setblock 193 64 121 botania:livingrock
setblock 192 65 120 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 192.5 66.25 120.5 {Tags:["kw_shot"]}
setblock 188 64 120 botania:mana_pool{mana:1000000}
summon botania:mana_spark 188.5 65.25 120.5 {Tags:["kw_shot"]}
setblock 196 64 120 botania:mana_pool{mana:1000000}
summon botania:mana_spark 196.5 65.25 120.5 {Tags:["kw_shot"]}
summon item 192.5 65.3 120.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 120.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 120.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
