# 083 hexerei/cauldron
#area 202 144 221 169
fill 202 64 144 221 91 169 minecraft:air
fill 202 60 144 221 62 169 minecraft:stone
fill 202 63 144 221 63 169 minecraft:light_gray_concrete
fill 206 64 150 221 79 150 minecraft:light_gray_concrete
fill 206 64 150 206 79 163 minecraft:light_gray_concrete
setblock 207 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083"}','{"text": "hexerei"}','{"text": "cauldron"}','{"text": ""}']}}
setblock 208 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two mixing"}','{"text": "cauldrons, one"}','{"text": "heated over"}','{"text": "lava"}']}}
fill 216 64 150 216 79 163 minecraft:light_gray_concrete
setblock 210 64 155 hexerei:mixing_cauldron
setblock 212 63 155 minecraft:lava
setblock 212 64 155 hexerei:mixing_cauldron
kw testworld use 210 64 155 up minecraft:water_bucket
kw testworld use 212 64 155 up minecraft:water_bucket
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
