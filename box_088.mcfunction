# 088 botania_runes/thermalily
#area 137 139 156 164
fill 137 64 139 156 91 164 minecraft:air
fill 137 60 139 156 62 164 minecraft:stone
fill 137 63 139 156 63 164 minecraft:light_gray_concrete
fill 141 64 145 156 79 145 minecraft:light_gray_concrete
fill 141 64 145 141 79 158 minecraft:light_gray_concrete
setblock 142 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088"}','{"text": "botania_runes"}','{"text": "thermalily"}','{"text": ""}']}}
setblock 143 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a hose pulley"}','{"text": "feeding lava"}','{"text": "next to the"}','{"text": "lily"}']}}
fill 151 64 145 151 79 158 minecraft:light_gray_concrete
fill 144 63 149 148 63 151 minecraft:grass_block[snowy=false]
setblock 147 63 150 minecraft:lava
setblock 146 64 150 botania:thermalily
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
