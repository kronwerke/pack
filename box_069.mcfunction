# 069 botania_runes/gourmaryllis
#area 152 107 171 132
fill 152 64 107 171 91 132 minecraft:air
fill 152 60 107 171 62 132 minecraft:stone
fill 152 63 107 171 63 132 minecraft:light_gray_concrete
fill 156 64 113 171 79 113 minecraft:light_gray_concrete
fill 156 64 113 156 79 126 minecraft:light_gray_concrete
setblock 157 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069"}','{"text": "botania_runes"}','{"text": "gourmaryllis"}','{"text": ""}']}}
setblock 158 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt dropping"}','{"text": "varied food"}','{"text": ""}','{"text": ""}']}}
fill 166 64 113 166 79 126 minecraft:light_gray_concrete
fill 159 63 117 163 63 119 minecraft:grass_block[snowy=false]
setblock 161 64 118 botania:gourmaryllis
summon item 160.5 64.2 119.5 {Item:{id:"minecraft:bread",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 119.5 {Item:{id:"minecraft:cooked_beef",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 160.5 64.2 117.5 {Item:{id:"minecraft:apple",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 117.5 {Item:{id:"minecraft:baked_potato",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
