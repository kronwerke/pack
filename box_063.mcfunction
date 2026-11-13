# 063 hexerei/sage_plate
#area 217 123 236 148
fill 217 64 123 236 91 148 minecraft:air
fill 217 60 123 236 62 148 minecraft:stone
fill 217 63 123 236 63 148 minecraft:light_gray_concrete
fill 221 64 129 236 79 129 minecraft:light_gray_concrete
fill 221 64 129 221 79 142 minecraft:light_gray_concrete
setblock 222 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "063"}','{"text": "hexerei"}','{"text": "sage_plate"}','{"text": ""}']}}
setblock 223 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "burning sage"}','{"text": "plate with the"}','{"text": "smoke ring"}','{"text": ""}']}}
fill 231 64 129 231 79 142 minecraft:light_gray_concrete
setblock 226 64 134 hexerei:sage_burning_plate[facing=south]
kw testworld use 226 64 134 up hexerei:dried_sage_bundle
kw testworld use 226 64 134 up minecraft:flint_and_steel
