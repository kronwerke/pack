# 094 occultism_afrit/iesnium
#area 127 146 146 171
fill 127 64 146 146 91 171 minecraft:air
fill 127 60 146 146 62 171 minecraft:stone
fill 127 63 146 146 63 171 minecraft:light_gray_concrete
fill 131 64 152 146 79 152 minecraft:light_gray_concrete
fill 131 64 152 131 79 165 minecraft:light_gray_concrete
setblock 132 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "094"}','{"text": "occultism_afrit"}','{"text": "iesnium"}','{"text": ""}']}}
setblock 133 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "divination rod"}','{"text": "highlight on"}','{"text": "iesnium ore in"}','{"text": "the Nether"}']}}
fill 141 64 152 141 79 165 minecraft:light_gray_concrete
fill 135 64 156 137 65 157 minecraft:netherrack
setblock 136 64 157 occultism:iesnium_ore
setblock 135 65 157 occultism:iesnium_ore
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
