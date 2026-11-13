# 059 botania_runes/terrasteel
#area 182 105 203 130
fill 182 64 105 203 91 130 minecraft:air
fill 182 60 105 203 62 130 minecraft:stone
fill 182 63 105 203 63 130 minecraft:light_gray_concrete
fill 186 64 111 203 79 111 minecraft:light_gray_concrete
fill 186 64 111 186 79 124 minecraft:light_gray_concrete
setblock 187 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "059"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 188 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 198 64 111 198 79 124 minecraft:light_gray_concrete
setblock 191 64 115 botania:livingrock
setblock 191 64 116 minecraft:lapis_block
setblock 191 64 117 botania:livingrock
setblock 192 64 115 minecraft:lapis_block
setblock 192 64 116 botania:livingrock
setblock 192 64 117 minecraft:lapis_block
setblock 193 64 115 botania:livingrock
setblock 193 64 116 minecraft:lapis_block
setblock 193 64 117 botania:livingrock
setblock 192 65 116 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 192.5 66.25 116.5 {Tags:["kw_shot"]}
setblock 188 64 116 botania:mana_pool{mana:1000000}
summon botania:mana_spark 188.5 65.25 116.5 {Tags:["kw_shot"]}
setblock 196 64 116 botania:mana_pool{mana:1000000}
summon botania:mana_spark 196.5 65.25 116.5 {Tags:["kw_shot"]}
summon item 192.5 65.3 116.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 116.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 116.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
