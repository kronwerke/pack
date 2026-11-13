# 079 botania_runes/gourmaryllis
#area 152 109 171 134
fill 152 64 109 171 91 134 minecraft:air
fill 152 60 109 171 62 134 minecraft:stone
fill 152 63 109 171 63 134 minecraft:light_gray_concrete
fill 156 64 115 171 79 115 minecraft:light_gray_concrete
fill 156 64 115 156 79 128 minecraft:light_gray_concrete
setblock 157 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079"}','{"text": "botania_runes"}','{"text": "gourmaryllis"}','{"text": ""}']}}
setblock 158 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt dropping"}','{"text": "varied food"}','{"text": ""}','{"text": ""}']}}
fill 166 64 115 166 79 128 minecraft:light_gray_concrete
fill 159 63 119 163 63 121 minecraft:grass_block[snowy=false]
setblock 161 64 120 botania:gourmaryllis
summon item 160.5 64.2 121.5 {Item:{id:"minecraft:bread",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 121.5 {Item:{id:"minecraft:cooked_beef",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 160.5 64.2 119.5 {Item:{id:"minecraft:apple",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 119.5 {Item:{id:"minecraft:baked_potato",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
