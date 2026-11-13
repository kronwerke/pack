# 092 immersive/bench
#area 66 179 86 204
fill 66 64 179 86 91 204 minecraft:air
fill 66 60 179 86 62 204 minecraft:stone
fill 66 63 179 86 63 204 minecraft:light_gray_concrete
fill 70 64 185 86 79 185 minecraft:light_gray_concrete
fill 70 64 185 70 79 198 minecraft:light_gray_concrete
setblock 71 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092"}','{"text": "immersive"}','{"text": "bench"}','{"text": ""}']}}
setblock 72 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "engineer\'s"}','{"text": "workbench with"}','{"text": "the components"}','{"text": "blueprint"}']}}
fill 81 64 185 81 79 198 minecraft:light_gray_concrete
kw testworld use 75 63 190 up immersiveengineering:workbench
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
