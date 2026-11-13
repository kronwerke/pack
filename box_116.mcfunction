# 116 hexerei/cauldron
#area 264 182 283 207
fill 264 64 182 283 91 207 minecraft:air
fill 264 60 182 283 62 207 minecraft:stone
fill 264 63 182 283 63 207 minecraft:light_gray_concrete
fill 268 64 188 283 79 188 minecraft:light_gray_concrete
fill 268 64 188 268 79 201 minecraft:light_gray_concrete
setblock 269 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116"}','{"text": "hexerei"}','{"text": "cauldron"}','{"text": ""}']}}
setblock 270 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two mixing"}','{"text": "cauldrons, one"}','{"text": "heated over"}','{"text": "lava"}']}}
fill 278 64 188 278 79 201 minecraft:light_gray_concrete
setblock 272 64 193 hexerei:mixing_cauldron
setblock 274 63 193 minecraft:lava
setblock 274 64 193 hexerei:mixing_cauldron
kw testworld use 272 64 193 up minecraft:water_bucket
kw testworld use 274 64 193 up minecraft:water_bucket
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
