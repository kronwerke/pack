# 113 hexerei/cauldron
#area 264 180 283 205
fill 264 64 180 283 91 205 minecraft:air
fill 264 60 180 283 62 205 minecraft:stone
fill 264 63 180 283 63 205 minecraft:light_gray_concrete
fill 268 64 186 283 79 186 minecraft:light_gray_concrete
fill 268 64 186 268 79 199 minecraft:light_gray_concrete
setblock 269 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "113"}','{"text": "hexerei"}','{"text": "cauldron"}','{"text": ""}']}}
setblock 270 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two mixing"}','{"text": "cauldrons, one"}','{"text": "heated over"}','{"text": "lava"}']}}
fill 278 64 186 278 79 199 minecraft:light_gray_concrete
setblock 272 64 191 hexerei:mixing_cauldron
setblock 274 63 191 minecraft:lava
setblock 274 64 191 hexerei:mixing_cauldron
kw testworld use 272 64 191 up minecraft:water_bucket
kw testworld use 274 64 191 up minecraft:water_bucket
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
