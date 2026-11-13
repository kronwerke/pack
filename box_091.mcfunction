# 091 botania_runes/terrasteel
#area 182 143 203 168
fill 182 64 143 203 91 168 minecraft:air
fill 182 60 143 203 62 168 minecraft:stone
fill 182 63 143 203 63 168 minecraft:light_gray_concrete
fill 186 64 149 203 79 149 minecraft:light_gray_concrete
fill 186 64 149 186 79 162 minecraft:light_gray_concrete
setblock 187 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 188 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 198 64 149 198 79 162 minecraft:light_gray_concrete
setblock 191 64 153 botania:livingrock
setblock 191 64 154 minecraft:lapis_block
setblock 191 64 155 botania:livingrock
setblock 192 64 153 minecraft:lapis_block
setblock 192 64 154 botania:livingrock
setblock 192 64 155 minecraft:lapis_block
setblock 193 64 153 botania:livingrock
setblock 193 64 154 minecraft:lapis_block
setblock 193 64 155 botania:livingrock
setblock 192 65 154 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 192.5 66.25 154.5 {Tags:["kw_shot"]}
setblock 188 64 154 botania:mana_pool{mana:1000000}
summon botania:mana_spark 188.5 65.25 154.5 {Tags:["kw_shot"]}
setblock 196 64 154 botania:mana_pool{mana:1000000}
summon botania:mana_spark 196.5 65.25 154.5 {Tags:["kw_shot"]}
summon item 192.5 65.3 154.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 154.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 154.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
