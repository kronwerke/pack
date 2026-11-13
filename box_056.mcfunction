# 056 mekanism_advanced/miner
#area 174 97 195 124
fill 174 64 97 195 91 124 minecraft:air
fill 174 60 97 195 62 124 minecraft:stone
fill 174 63 97 195 63 124 minecraft:light_gray_concrete
fill 178 64 103 195 79 103 minecraft:light_gray_concrete
fill 178 64 103 178 79 118 minecraft:light_gray_concrete
setblock 179 64 117 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "056"}','{"text": "mekanism_advanced"}','{"text": "miner"}','{"text": ""}']}}
setblock 180 64 117 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "digital miner"}','{"text": "GUI with"}','{"text": "filters and"}','{"text": "radius"}']}}
fill 190 64 103 190 79 118 minecraft:light_gray_concrete
setblock 184 64 109 mekanism:digital_miner[facing=south,active=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
