# 118 hexerei/sage_plate
#area 294 182 313 207
fill 294 64 182 313 91 207 minecraft:air
fill 294 60 182 313 62 207 minecraft:stone
fill 294 63 182 313 63 207 minecraft:light_gray_concrete
fill 298 64 188 313 79 188 minecraft:light_gray_concrete
fill 298 64 188 298 79 201 minecraft:light_gray_concrete
setblock 299 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118"}','{"text": "hexerei"}','{"text": "sage_plate"}','{"text": ""}']}}
setblock 300 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "burning sage"}','{"text": "plate with the"}','{"text": "smoke ring"}','{"text": ""}']}}
fill 308 64 188 308 79 201 minecraft:light_gray_concrete
setblock 303 64 193 hexerei:sage_burning_plate[facing=south]
kw testworld use 303 64 193 up hexerei:dried_sage_bundle
kw testworld use 303 64 193 up minecraft:flint_and_steel
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
