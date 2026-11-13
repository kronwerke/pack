# 115 hexerei/sage_plate
#area 294 180 313 205
fill 294 64 180 313 91 205 minecraft:air
fill 294 60 180 313 62 205 minecraft:stone
fill 294 63 180 313 63 205 minecraft:light_gray_concrete
fill 298 64 186 313 79 186 minecraft:light_gray_concrete
fill 298 64 186 298 79 199 minecraft:light_gray_concrete
setblock 299 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "115"}','{"text": "hexerei"}','{"text": "sage_plate"}','{"text": ""}']}}
setblock 300 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "burning sage"}','{"text": "plate with the"}','{"text": "smoke ring"}','{"text": ""}']}}
fill 308 64 186 308 79 199 minecraft:light_gray_concrete
setblock 303 64 191 hexerei:sage_burning_plate[facing=south]
kw testworld use 303 64 191 up hexerei:dried_sage_bundle
kw testworld use 303 64 191 up minecraft:flint_and_steel
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
