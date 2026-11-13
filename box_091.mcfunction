# 091 botania_runes/gourmaryllis
#area 152 145 171 170
fill 152 64 145 171 91 170 minecraft:air
fill 152 60 145 171 62 170 minecraft:stone
fill 152 63 145 171 63 170 minecraft:light_gray_concrete
fill 156 64 151 171 79 151 minecraft:light_gray_concrete
fill 156 64 151 156 79 164 minecraft:light_gray_concrete
setblock 157 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091"}','{"text": "botania_runes"}','{"text": "gourmaryllis"}','{"text": ""}']}}
setblock 158 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt dropping"}','{"text": "varied food"}','{"text": ""}','{"text": ""}']}}
fill 166 64 151 166 79 164 minecraft:light_gray_concrete
fill 159 63 155 163 63 157 minecraft:grass_block[snowy=false]
setblock 161 64 156 botania:gourmaryllis
summon item 160.5 64.2 157.5 {Item:{id:"minecraft:bread",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 157.5 {Item:{id:"minecraft:cooked_beef",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 160.5 64.2 155.5 {Item:{id:"minecraft:apple",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 155.5 {Item:{id:"minecraft:baked_potato",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
