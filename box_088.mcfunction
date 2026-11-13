# 088 botania_runes/thermalily
#area 137 143 156 168
fill 137 64 143 156 91 168 minecraft:air
fill 137 60 143 156 62 168 minecraft:stone
fill 137 63 143 156 63 168 minecraft:light_gray_concrete
fill 141 64 149 156 79 149 minecraft:light_gray_concrete
fill 141 64 149 141 79 162 minecraft:light_gray_concrete
setblock 142 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088"}','{"text": "botania_runes"}','{"text": "thermalily"}','{"text": ""}']}}
setblock 143 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a hose pulley"}','{"text": "feeding lava"}','{"text": "next to the"}','{"text": "lily"}']}}
fill 151 64 149 151 79 162 minecraft:light_gray_concrete
fill 144 63 153 148 63 155 minecraft:grass_block[snowy=false]
setblock 147 63 154 minecraft:lava
setblock 146 64 154 botania:thermalily
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
