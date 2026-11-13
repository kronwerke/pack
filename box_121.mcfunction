# 121 occultism_afrit/iesnium
#area 142 184 161 209
fill 142 64 184 161 91 209 minecraft:air
fill 142 60 184 161 62 209 minecraft:stone
fill 142 63 184 161 63 209 minecraft:light_gray_concrete
fill 146 64 190 161 79 190 minecraft:light_gray_concrete
fill 146 64 190 146 79 203 minecraft:light_gray_concrete
setblock 147 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "121"}','{"text": "occultism_afrit"}','{"text": "iesnium"}','{"text": ""}']}}
setblock 148 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "divination rod"}','{"text": "highlight on"}','{"text": "iesnium ore in"}','{"text": "the Nether"}']}}
fill 156 64 190 156 79 203 minecraft:light_gray_concrete
fill 150 64 194 152 65 195 minecraft:netherrack
setblock 151 64 195 occultism:iesnium_ore
setblock 150 65 195 occultism:iesnium_ore
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
