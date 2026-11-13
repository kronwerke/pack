# 068 botania_runes/terrasteel
#area 182 107 203 132
fill 182 64 107 203 91 132 minecraft:air
fill 182 60 107 203 62 132 minecraft:stone
fill 182 63 107 203 63 132 minecraft:light_gray_concrete
fill 186 64 113 203 79 113 minecraft:light_gray_concrete
fill 186 64 113 186 79 126 minecraft:light_gray_concrete
setblock 187 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "068"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 188 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 198 64 113 198 79 126 minecraft:light_gray_concrete
setblock 191 64 117 botania:livingrock
setblock 191 64 118 minecraft:lapis_block
setblock 191 64 119 botania:livingrock
setblock 192 64 117 minecraft:lapis_block
setblock 192 64 118 botania:livingrock
setblock 192 64 119 minecraft:lapis_block
setblock 193 64 117 botania:livingrock
setblock 193 64 118 minecraft:lapis_block
setblock 193 64 119 botania:livingrock
setblock 192 65 118 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 192.5 66.25 118.5 {Tags:["kw_shot"]}
setblock 188 64 118 botania:mana_pool{mana:1000000}
summon botania:mana_spark 188.5 65.25 118.5 {Tags:["kw_shot"]}
setblock 196 64 118 botania:mana_pool{mana:1000000}
summon botania:mana_spark 196.5 65.25 118.5 {Tags:["kw_shot"]}
summon item 192.5 65.3 118.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 118.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 118.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
