# 024 botania_runes/terrasteel
#area 26 84 47 109
fill 26 64 84 47 91 109 minecraft:air
fill 26 60 84 47 62 109 minecraft:stone
fill 26 63 84 47 63 109 minecraft:light_gray_concrete
fill 30 64 90 47 79 90 minecraft:light_gray_concrete
fill 30 64 90 30 79 103 minecraft:light_gray_concrete
setblock 31 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "024"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 32 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 42 64 90 42 79 103 minecraft:light_gray_concrete
setblock 35 64 94 botania:livingrock
setblock 35 64 95 minecraft:lapis_block
setblock 35 64 96 botania:livingrock
setblock 36 64 94 minecraft:lapis_block
setblock 36 64 95 botania:livingrock
setblock 36 64 96 minecraft:lapis_block
setblock 37 64 94 botania:livingrock
setblock 37 64 95 minecraft:lapis_block
setblock 37 64 96 botania:livingrock
setblock 36 65 95 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 36.5 66.25 95.5 {Tags:["kw_shot"]}
setblock 32 64 95 botania:mana_pool{mana:1000000}
summon botania:mana_spark 32.5 65.25 95.5 {Tags:["kw_shot"]}
setblock 40 64 95 botania:mana_pool{mana:1000000}
summon botania:mana_spark 40.5 65.25 95.5 {Tags:["kw_shot"]}
summon item 36.5 65.3 95.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 36.5 65.3 95.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 36.5 65.3 95.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
