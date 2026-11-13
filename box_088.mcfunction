# 088 botania_runes/thermalily
#area 137 145 156 170
fill 137 64 145 156 91 170 minecraft:air
fill 137 60 145 156 62 170 minecraft:stone
fill 137 63 145 156 63 170 minecraft:light_gray_concrete
fill 141 64 151 156 79 151 minecraft:light_gray_concrete
fill 141 64 151 141 79 164 minecraft:light_gray_concrete
setblock 142 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088"}','{"text": "botania_runes"}','{"text": "thermalily"}','{"text": ""}']}}
setblock 143 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a hose pulley"}','{"text": "feeding lava"}','{"text": "next to the"}','{"text": "lily"}']}}
fill 151 64 151 151 79 164 minecraft:light_gray_concrete
fill 144 63 155 148 63 157 minecraft:grass_block[snowy=false]
setblock 147 63 156 minecraft:lava
setblock 146 64 156 botania:thermalily
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
