# 078 botania_runes/thermalily
#area 137 109 156 134
fill 137 64 109 156 91 134 minecraft:air
fill 137 60 109 156 62 134 minecraft:stone
fill 137 63 109 156 63 134 minecraft:light_gray_concrete
fill 141 64 115 156 79 115 minecraft:light_gray_concrete
fill 141 64 115 141 79 128 minecraft:light_gray_concrete
setblock 142 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078"}','{"text": "botania_runes"}','{"text": "thermalily"}','{"text": ""}']}}
setblock 143 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a hose pulley"}','{"text": "feeding lava"}','{"text": "next to the"}','{"text": "lily"}']}}
fill 151 64 115 151 79 128 minecraft:light_gray_concrete
fill 144 63 119 148 63 121 minecraft:grass_block[snowy=false]
setblock 147 63 120 minecraft:lava
setblock 146 64 120 botania:thermalily
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
