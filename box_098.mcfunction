# 098 botania_runes/thermalily
#area 137 147 156 172
fill 137 64 147 156 91 172 minecraft:air
fill 137 60 147 156 62 172 minecraft:stone
fill 137 63 147 156 63 172 minecraft:light_gray_concrete
fill 141 64 153 156 79 153 minecraft:light_gray_concrete
fill 141 64 153 141 79 166 minecraft:light_gray_concrete
setblock 142 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098"}','{"text": "botania_runes"}','{"text": "thermalily"}','{"text": ""}']}}
setblock 143 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a hose pulley"}','{"text": "feeding lava"}','{"text": "next to the"}','{"text": "lily"}']}}
fill 151 64 153 151 79 166 minecraft:light_gray_concrete
fill 144 63 157 148 63 159 minecraft:grass_block[snowy=false]
setblock 147 63 158 minecraft:lava
setblock 146 64 158 botania:thermalily
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
