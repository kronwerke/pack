# 076 botania_runes/mana_pearl
#area 107 109 126 134
fill 107 64 109 126 91 134 minecraft:air
fill 107 60 109 126 62 134 minecraft:stone
fill 107 63 109 126 63 134 minecraft:light_gray_concrete
fill 111 64 115 126 79 115 minecraft:light_gray_concrete
fill 111 64 115 111 79 128 minecraft:light_gray_concrete
setblock 112 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076"}','{"text": "botania_runes"}','{"text": "mana_pearl"}','{"text": ""}']}}
setblock 113 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pool on a"}','{"text": "brass casing"}','{"text": "with a pearl in"}','{"text": "it"}']}}
fill 121 64 115 121 79 128 minecraft:light_gray_concrete
setblock 116 64 120 create:brass_casing
setblock 116 65 120 botania:mana_pool{mana:1000000}
summon item 116.5 66 120.5 {Item:{id:"minecraft:ender_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
