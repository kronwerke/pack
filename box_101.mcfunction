# 101 botania_runes/terrasteel
#area 182 147 203 172
fill 182 64 147 203 91 172 minecraft:air
fill 182 60 147 203 62 172 minecraft:stone
fill 182 63 147 203 63 172 minecraft:light_gray_concrete
fill 186 64 153 203 79 153 minecraft:light_gray_concrete
fill 186 64 153 186 79 166 minecraft:light_gray_concrete
setblock 187 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 188 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 198 64 153 198 79 166 minecraft:light_gray_concrete
setblock 191 64 157 botania:livingrock
setblock 191 64 158 minecraft:lapis_block
setblock 191 64 159 botania:livingrock
setblock 192 64 157 minecraft:lapis_block
setblock 192 64 158 botania:livingrock
setblock 192 64 159 minecraft:lapis_block
setblock 193 64 157 botania:livingrock
setblock 193 64 158 minecraft:lapis_block
setblock 193 64 159 botania:livingrock
setblock 192 65 158 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 192.5 66.25 158.5 {Tags:["kw_shot"]}
setblock 188 64 158 botania:mana_pool{mana:1000000}
summon botania:mana_spark 188.5 65.25 158.5 {Tags:["kw_shot"]}
setblock 196 64 158 botania:mana_pool{mana:1000000}
summon botania:mana_spark 196.5 65.25 158.5 {Tags:["kw_shot"]}
summon item 192.5 65.3 158.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 158.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 65.3 158.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
