# 111 hexerei/sage_plate
#area 294 176 313 201
fill 294 64 176 313 91 201 minecraft:air
fill 294 60 176 313 62 201 minecraft:stone
fill 294 63 176 313 63 201 minecraft:light_gray_concrete
fill 298 64 182 313 79 182 minecraft:light_gray_concrete
fill 298 64 182 298 79 195 minecraft:light_gray_concrete
setblock 299 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "111"}','{"text": "hexerei"}','{"text": "sage_plate"}','{"text": ""}']}}
setblock 300 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "burning sage"}','{"text": "plate with the"}','{"text": "smoke ring"}','{"text": ""}']}}
fill 308 64 182 308 79 195 minecraft:light_gray_concrete
setblock 303 64 187 hexerei:sage_burning_plate[facing=south]
kw testworld use 303 64 187 up hexerei:dried_sage_bundle
kw testworld use 303 64 187 up minecraft:flint_and_steel
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
