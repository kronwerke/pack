# 102 occultism_afrit/iesnium
#area 127 176 146 201
fill 127 64 176 146 91 201 minecraft:air
fill 127 60 176 146 62 201 minecraft:stone
fill 127 63 176 146 63 201 minecraft:light_gray_concrete
fill 131 64 182 146 79 182 minecraft:light_gray_concrete
fill 131 64 182 131 79 195 minecraft:light_gray_concrete
setblock 132 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102"}','{"text": "occultism_afrit"}','{"text": "iesnium"}','{"text": ""}']}}
setblock 133 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "divination rod"}','{"text": "highlight on"}','{"text": "iesnium ore in"}','{"text": "the Nether"}']}}
fill 141 64 182 141 79 195 minecraft:light_gray_concrete
fill 135 64 186 137 65 187 minecraft:netherrack
setblock 136 64 187 occultism:iesnium_ore
setblock 135 65 187 occultism:iesnium_ore
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
