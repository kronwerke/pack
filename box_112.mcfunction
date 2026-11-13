# 112 hexerei/cauldron
#area 264 176 283 201
fill 264 64 176 283 91 201 minecraft:air
fill 264 60 176 283 62 201 minecraft:stone
fill 264 63 176 283 63 201 minecraft:light_gray_concrete
fill 268 64 182 283 79 182 minecraft:light_gray_concrete
fill 268 64 182 268 79 195 minecraft:light_gray_concrete
setblock 269 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112"}','{"text": "hexerei"}','{"text": "cauldron"}','{"text": ""}']}}
setblock 270 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two mixing"}','{"text": "cauldrons, one"}','{"text": "heated over"}','{"text": "lava"}']}}
fill 278 64 182 278 79 195 minecraft:light_gray_concrete
setblock 272 64 187 hexerei:mixing_cauldron
setblock 274 63 187 minecraft:lava
setblock 274 64 187 hexerei:mixing_cauldron
kw testworld use 272 64 187 up minecraft:water_bucket
kw testworld use 274 64 187 up minecraft:water_bucket
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
