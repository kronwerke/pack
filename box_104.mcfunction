# 104 hexerei/sage_plate
#area 294 146 313 171
fill 294 64 146 313 91 171 minecraft:air
fill 294 60 146 313 62 171 minecraft:stone
fill 294 63 146 313 63 171 minecraft:light_gray_concrete
fill 298 64 152 313 79 152 minecraft:light_gray_concrete
fill 298 64 152 298 79 165 minecraft:light_gray_concrete
setblock 299 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "104"}','{"text": "hexerei"}','{"text": "sage_plate"}','{"text": ""}']}}
setblock 300 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "burning sage"}','{"text": "plate with the"}','{"text": "smoke ring"}','{"text": ""}']}}
fill 308 64 152 308 79 165 minecraft:light_gray_concrete
setblock 303 64 157 hexerei:sage_burning_plate[facing=south]
kw testworld use 303 64 157 up hexerei:dried_sage_bundle
kw testworld use 303 64 157 up minecraft:flint_and_steel
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
