# 056 botania_runes/thermalily
#area 137 105 156 130
fill 137 64 105 156 91 130 minecraft:air
fill 137 60 105 156 62 130 minecraft:stone
fill 137 63 105 156 63 130 minecraft:light_gray_concrete
fill 141 64 111 156 79 111 minecraft:light_gray_concrete
fill 141 64 111 141 79 124 minecraft:light_gray_concrete
setblock 142 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "056"}','{"text": "botania_runes"}','{"text": "thermalily"}','{"text": ""}']}}
setblock 143 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a hose pulley"}','{"text": "feeding lava"}','{"text": "next to the"}','{"text": "lily"}']}}
fill 151 64 111 151 79 124 minecraft:light_gray_concrete
fill 144 63 115 148 63 117 minecraft:grass_block[snowy=false]
setblock 147 63 116 minecraft:lava
setblock 146 64 116 botania:thermalily
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
