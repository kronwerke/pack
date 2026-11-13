# 106 occultism_afrit/iesnium
#area 127 182 146 207
fill 127 64 182 146 91 207 minecraft:air
fill 127 60 182 146 62 207 minecraft:stone
fill 127 63 182 146 63 207 minecraft:light_gray_concrete
fill 131 64 188 146 79 188 minecraft:light_gray_concrete
fill 131 64 188 131 79 201 minecraft:light_gray_concrete
setblock 132 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "106"}','{"text": "occultism_afrit"}','{"text": "iesnium"}','{"text": ""}']}}
setblock 133 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "divination rod"}','{"text": "highlight on"}','{"text": "iesnium ore in"}','{"text": "the Nether"}']}}
fill 141 64 188 141 79 201 minecraft:light_gray_concrete
fill 135 64 192 137 65 193 minecraft:netherrack
setblock 136 64 193 occultism:iesnium_ore
setblock 135 65 193 occultism:iesnium_ore
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
