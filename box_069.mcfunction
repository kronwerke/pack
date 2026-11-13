# 069 hexerei/cauldron
#area 202 142 221 167
fill 202 64 142 221 91 167 minecraft:air
fill 202 60 142 221 62 167 minecraft:stone
fill 202 63 142 221 63 167 minecraft:light_gray_concrete
fill 206 64 148 221 79 148 minecraft:light_gray_concrete
fill 206 64 148 206 79 161 minecraft:light_gray_concrete
setblock 207 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069"}','{"text": "hexerei"}','{"text": "cauldron"}','{"text": ""}']}}
setblock 208 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two mixing"}','{"text": "cauldrons, one"}','{"text": "heated over"}','{"text": "lava"}']}}
fill 216 64 148 216 79 161 minecraft:light_gray_concrete
setblock 210 64 153 hexerei:mixing_cauldron
setblock 212 63 153 minecraft:lava
setblock 212 64 153 hexerei:mixing_cauldron
kw testworld use 210 64 153 up minecraft:water_bucket
kw testworld use 212 64 153 up minecraft:water_bucket
