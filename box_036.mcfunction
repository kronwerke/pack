# 036 botania_runes/mana_pearl
#area 75 86 94 111
fill 75 64 86 94 91 111 minecraft:air
fill 75 60 86 94 62 111 minecraft:stone
fill 75 63 86 94 63 111 minecraft:light_gray_concrete
fill 79 64 92 94 79 92 minecraft:light_gray_concrete
fill 79 64 92 79 79 105 minecraft:light_gray_concrete
setblock 80 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "036"}','{"text": "botania_runes"}','{"text": "mana_pearl"}','{"text": ""}']}}
setblock 81 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pool on a"}','{"text": "brass casing"}','{"text": "with a pearl in"}','{"text": "it"}']}}
fill 89 64 92 89 79 105 minecraft:light_gray_concrete
setblock 84 64 97 create:brass_casing
setblock 84 65 97 botania:mana_pool{mana:1000000}
summon item 84.5 66 97.5 {Item:{id:"minecraft:ender_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
