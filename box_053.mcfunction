# 053 botania_runes/terrasteel
#area 152 105 173 130
fill 152 64 105 173 91 130 minecraft:air
fill 152 60 105 173 62 130 minecraft:stone
fill 152 63 105 173 63 130 minecraft:light_gray_concrete
fill 156 64 111 173 79 111 minecraft:light_gray_concrete
fill 156 64 111 156 79 124 minecraft:light_gray_concrete
setblock 157 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "053"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 158 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 168 64 111 168 79 124 minecraft:light_gray_concrete
setblock 161 64 115 botania:livingrock
setblock 161 64 116 minecraft:lapis_block
setblock 161 64 117 botania:livingrock
setblock 162 64 115 minecraft:lapis_block
setblock 162 64 116 botania:livingrock
setblock 162 64 117 minecraft:lapis_block
setblock 163 64 115 botania:livingrock
setblock 163 64 116 minecraft:lapis_block
setblock 163 64 117 botania:livingrock
setblock 162 65 116 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 162.5 66.25 116.5 {Tags:["kw_shot"]}
setblock 158 64 116 botania:mana_pool{mana:1000000}
summon botania:mana_spark 158.5 65.25 116.5 {Tags:["kw_shot"]}
setblock 166 64 116 botania:mana_pool{mana:1000000}
summon botania:mana_spark 166.5 65.25 116.5 {Tags:["kw_shot"]}
summon item 162.5 65.3 116.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 65.3 116.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 65.3 116.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
