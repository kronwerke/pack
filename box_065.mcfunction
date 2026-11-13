# 065 hexerei/cauldron
#area 202 123 221 148
fill 202 64 123 221 91 148 minecraft:air
fill 202 60 123 221 62 148 minecraft:stone
fill 202 63 123 221 63 148 minecraft:light_gray_concrete
fill 206 64 129 221 79 129 minecraft:light_gray_concrete
fill 206 64 129 206 79 142 minecraft:light_gray_concrete
setblock 207 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "065"}','{"text": "hexerei"}','{"text": "cauldron"}','{"text": ""}']}}
setblock 208 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two mixing"}','{"text": "cauldrons, one"}','{"text": "heated over"}','{"text": "lava"}']}}
fill 216 64 129 216 79 142 minecraft:light_gray_concrete
setblock 210 64 134 hexerei:mixing_cauldron
setblock 212 63 134 minecraft:lava
setblock 212 64 134 hexerei:mixing_cauldron
kw testworld use 210 64 134 up minecraft:water_bucket
kw testworld use 212 64 134 up minecraft:water_bucket
