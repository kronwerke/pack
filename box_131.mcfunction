# 131 hexerei/sage_plate
#area 324 184 343 209
fill 324 64 184 343 91 209 minecraft:air
fill 324 60 184 343 62 209 minecraft:stone
fill 324 63 184 343 63 209 minecraft:light_gray_concrete
fill 328 64 190 343 79 190 minecraft:light_gray_concrete
fill 328 64 190 328 79 203 minecraft:light_gray_concrete
setblock 329 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131"}','{"text": "hexerei"}','{"text": "sage_plate"}','{"text": ""}']}}
setblock 330 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "burning sage"}','{"text": "plate with the"}','{"text": "smoke ring"}','{"text": ""}']}}
fill 338 64 190 338 79 203 minecraft:light_gray_concrete
setblock 333 64 195 hexerei:sage_burning_plate[facing=south]
kw testworld use 333 64 195 up hexerei:dried_sage_bundle
kw testworld use 333 64 195 up minecraft:flint_and_steel
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
