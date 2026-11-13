# 120 immersive/bench
#area 66 215 86 240
fill 66 64 215 86 91 240 minecraft:air
fill 66 60 215 86 62 240 minecraft:stone
fill 66 63 215 86 63 240 minecraft:light_gray_concrete
fill 70 64 221 86 79 221 minecraft:light_gray_concrete
fill 70 64 221 70 79 234 minecraft:light_gray_concrete
setblock 71 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "120"}','{"text": "immersive"}','{"text": "bench"}','{"text": ""}']}}
setblock 72 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "engineer\'s"}','{"text": "workbench with"}','{"text": "the components"}','{"text": "blueprint"}']}}
fill 81 64 221 81 79 234 minecraft:light_gray_concrete
kw testworld use 75 63 226 up immersiveengineering:workbench
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
