# 089 botania_runes/gourmaryllis
#area 152 139 171 164
fill 152 64 139 171 91 164 minecraft:air
fill 152 60 139 171 62 164 minecraft:stone
fill 152 63 139 171 63 164 minecraft:light_gray_concrete
fill 156 64 145 171 79 145 minecraft:light_gray_concrete
fill 156 64 145 156 79 158 minecraft:light_gray_concrete
setblock 157 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089"}','{"text": "botania_runes"}','{"text": "gourmaryllis"}','{"text": ""}']}}
setblock 158 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt dropping"}','{"text": "varied food"}','{"text": ""}','{"text": ""}']}}
fill 166 64 145 166 79 158 minecraft:light_gray_concrete
fill 159 63 149 163 63 151 minecraft:grass_block[snowy=false]
setblock 161 64 150 botania:gourmaryllis
summon item 160.5 64.2 151.5 {Item:{id:"minecraft:bread",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 151.5 {Item:{id:"minecraft:cooked_beef",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 160.5 64.2 149.5 {Item:{id:"minecraft:apple",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 149.5 {Item:{id:"minecraft:baked_potato",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
