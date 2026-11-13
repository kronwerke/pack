# 071 botania_runes/mana_pearl
#area 107 107 126 132
fill 107 64 107 126 91 132 minecraft:air
fill 107 60 107 126 62 132 minecraft:stone
fill 107 63 107 126 63 132 minecraft:light_gray_concrete
fill 111 64 113 126 79 113 minecraft:light_gray_concrete
fill 111 64 113 111 79 126 minecraft:light_gray_concrete
setblock 112 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071"}','{"text": "botania_runes"}','{"text": "mana_pearl"}','{"text": ""}']}}
setblock 113 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pool on a"}','{"text": "brass casing"}','{"text": "with a pearl in"}','{"text": "it"}']}}
fill 121 64 113 121 79 126 minecraft:light_gray_concrete
setblock 116 64 118 create:brass_casing
setblock 116 65 118 botania:mana_pool{mana:1000000}
summon item 116.5 66 118.5 {Item:{id:"minecraft:ender_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
