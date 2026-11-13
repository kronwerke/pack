# 100 hexerei/cauldron
#area 264 146 283 171
fill 264 64 146 283 91 171 minecraft:air
fill 264 60 146 283 62 171 minecraft:stone
fill 264 63 146 283 63 171 minecraft:light_gray_concrete
fill 268 64 152 283 79 152 minecraft:light_gray_concrete
fill 268 64 152 268 79 165 minecraft:light_gray_concrete
setblock 269 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100"}','{"text": "hexerei"}','{"text": "cauldron"}','{"text": ""}']}}
setblock 270 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two mixing"}','{"text": "cauldrons, one"}','{"text": "heated over"}','{"text": "lava"}']}}
fill 278 64 152 278 79 165 minecraft:light_gray_concrete
setblock 272 64 157 hexerei:mixing_cauldron
setblock 274 63 157 minecraft:lava
setblock 274 64 157 hexerei:mixing_cauldron
kw testworld use 272 64 157 up minecraft:water_bucket
kw testworld use 274 64 157 up minecraft:water_bucket
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
