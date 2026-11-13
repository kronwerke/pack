# 091 occultism_afrit/iesnium
#area 127 144 146 169
fill 127 64 144 146 91 169 minecraft:air
fill 127 60 144 146 62 169 minecraft:stone
fill 127 63 144 146 63 169 minecraft:light_gray_concrete
fill 131 64 150 146 79 150 minecraft:light_gray_concrete
fill 131 64 150 131 79 163 minecraft:light_gray_concrete
setblock 132 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091"}','{"text": "occultism_afrit"}','{"text": "iesnium"}','{"text": ""}']}}
setblock 133 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "divination rod"}','{"text": "highlight on"}','{"text": "iesnium ore in"}','{"text": "the Nether"}']}}
fill 141 64 150 141 79 163 minecraft:light_gray_concrete
fill 135 64 154 137 65 155 minecraft:netherrack
setblock 136 64 155 occultism:iesnium_ore
setblock 135 65 155 occultism:iesnium_ore
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
