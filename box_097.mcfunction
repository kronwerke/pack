# 097 hexerei/cauldron
#area 264 144 283 169
fill 264 64 144 283 91 169 minecraft:air
fill 264 60 144 283 62 169 minecraft:stone
fill 264 63 144 283 63 169 minecraft:light_gray_concrete
fill 268 64 150 283 79 150 minecraft:light_gray_concrete
fill 268 64 150 268 79 163 minecraft:light_gray_concrete
setblock 269 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097"}','{"text": "hexerei"}','{"text": "cauldron"}','{"text": ""}']}}
setblock 270 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two mixing"}','{"text": "cauldrons, one"}','{"text": "heated over"}','{"text": "lava"}']}}
fill 278 64 150 278 79 163 minecraft:light_gray_concrete
setblock 272 64 155 hexerei:mixing_cauldron
setblock 274 63 155 minecraft:lava
setblock 274 64 155 hexerei:mixing_cauldron
kw testworld use 272 64 155 up minecraft:water_bucket
kw testworld use 274 64 155 up minecraft:water_bucket
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
