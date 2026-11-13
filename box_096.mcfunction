# 096 botania_runes/mana_pearl
#area 107 147 126 172
fill 107 64 147 126 91 172 minecraft:air
fill 107 60 147 126 62 172 minecraft:stone
fill 107 63 147 126 63 172 minecraft:light_gray_concrete
fill 111 64 153 126 79 153 minecraft:light_gray_concrete
fill 111 64 153 111 79 166 minecraft:light_gray_concrete
setblock 112 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096"}','{"text": "botania_runes"}','{"text": "mana_pearl"}','{"text": ""}']}}
setblock 113 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pool on a"}','{"text": "brass casing"}','{"text": "with a pearl in"}','{"text": "it"}']}}
fill 121 64 153 121 79 166 minecraft:light_gray_concrete
setblock 116 64 158 create:brass_casing
setblock 116 65 158 botania:mana_pool{mana:1000000}
summon item 116.5 66 158.5 {Item:{id:"minecraft:ender_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
