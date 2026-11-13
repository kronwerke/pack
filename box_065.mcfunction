# 065 botania_runes/thermalily
#area 137 107 156 132
fill 137 64 107 156 91 132 minecraft:air
fill 137 60 107 156 62 132 minecraft:stone
fill 137 63 107 156 63 132 minecraft:light_gray_concrete
fill 141 64 113 156 79 113 minecraft:light_gray_concrete
fill 141 64 113 141 79 126 minecraft:light_gray_concrete
setblock 142 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "065"}','{"text": "botania_runes"}','{"text": "thermalily"}','{"text": ""}']}}
setblock 143 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a hose pulley"}','{"text": "feeding lava"}','{"text": "next to the"}','{"text": "lily"}']}}
fill 151 64 113 151 79 126 minecraft:light_gray_concrete
fill 144 63 117 148 63 119 minecraft:grass_block[snowy=false]
setblock 147 63 118 minecraft:lava
setblock 146 64 118 botania:thermalily
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
