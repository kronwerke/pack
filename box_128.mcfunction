# 128 hexerei/cauldron
#area 279 184 298 209
fill 279 64 184 298 91 209 minecraft:air
fill 279 60 184 298 62 209 minecraft:stone
fill 279 63 184 298 63 209 minecraft:light_gray_concrete
fill 283 64 190 298 79 190 minecraft:light_gray_concrete
fill 283 64 190 283 79 203 minecraft:light_gray_concrete
setblock 284 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "128"}','{"text": "hexerei"}','{"text": "cauldron"}','{"text": ""}']}}
setblock 285 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two mixing"}','{"text": "cauldrons, one"}','{"text": "heated over"}','{"text": "lava"}']}}
fill 293 64 190 293 79 203 minecraft:light_gray_concrete
setblock 287 64 195 hexerei:mixing_cauldron
setblock 289 63 195 minecraft:lava
setblock 289 64 195 hexerei:mixing_cauldron
kw testworld use 287 64 195 up minecraft:water_bucket
kw testworld use 289 64 195 up minecraft:water_bucket
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
