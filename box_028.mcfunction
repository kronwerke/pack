# 028 botania_runes/mana_pearl
#area 56 84 75 109
fill 56 64 84 75 91 109 minecraft:air
fill 56 60 84 75 62 109 minecraft:stone
fill 56 63 84 75 63 109 minecraft:light_gray_concrete
fill 60 64 90 75 79 90 minecraft:light_gray_concrete
fill 60 64 90 60 79 103 minecraft:light_gray_concrete
setblock 61 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "028"}','{"text": "botania_runes"}','{"text": "mana_pearl"}','{"text": ""}']}}
setblock 62 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pool on a"}','{"text": "brass casing"}','{"text": "with a pearl in"}','{"text": "it"}']}}
fill 70 64 90 70 79 103 minecraft:light_gray_concrete
setblock 65 64 95 create:brass_casing
setblock 65 65 95 botania:mana_pool{mana:1000000}
summon item 65.5 66 95.5 {Item:{id:"minecraft:ender_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
