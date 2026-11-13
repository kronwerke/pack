# 106 occultism_afrit/iesnium
#area 127 180 146 205
fill 127 64 180 146 91 205 minecraft:air
fill 127 60 180 146 62 205 minecraft:stone
fill 127 63 180 146 63 205 minecraft:light_gray_concrete
fill 131 64 186 146 79 186 minecraft:light_gray_concrete
fill 131 64 186 131 79 199 minecraft:light_gray_concrete
setblock 132 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "106"}','{"text": "occultism_afrit"}','{"text": "iesnium"}','{"text": ""}']}}
setblock 133 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "divination rod"}','{"text": "highlight on"}','{"text": "iesnium ore in"}','{"text": "the Nether"}']}}
fill 141 64 186 141 79 199 minecraft:light_gray_concrete
fill 135 64 190 137 65 191 minecraft:netherrack
setblock 136 64 191 occultism:iesnium_ore
setblock 135 65 191 occultism:iesnium_ore
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
