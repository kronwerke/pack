# 046 botania_runes/mana_pearl
#area 107 86 126 111
fill 107 64 86 126 91 111 minecraft:air
fill 107 60 86 126 62 111 minecraft:stone
fill 107 63 86 126 63 111 minecraft:light_gray_concrete
fill 111 64 92 126 79 92 minecraft:light_gray_concrete
fill 111 64 92 111 79 105 minecraft:light_gray_concrete
setblock 112 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "046"}','{"text": "botania_runes"}','{"text": "mana_pearl"}','{"text": ""}']}}
setblock 113 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pool on a"}','{"text": "brass casing"}','{"text": "with a pearl in"}','{"text": "it"}']}}
fill 121 64 92 121 79 105 minecraft:light_gray_concrete
setblock 116 64 97 create:brass_casing
setblock 116 65 97 botania:mana_pool{mana:1000000}
summon item 116.5 66 97.5 {Item:{id:"minecraft:ender_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
