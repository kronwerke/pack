# 106 immersive/bench
#area 66 181 86 206
fill 66 64 181 86 91 206 minecraft:air
fill 66 60 181 86 62 206 minecraft:stone
fill 66 63 181 86 63 206 minecraft:light_gray_concrete
fill 70 64 187 86 79 187 minecraft:light_gray_concrete
fill 70 64 187 70 79 200 minecraft:light_gray_concrete
setblock 71 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "106"}','{"text": "immersive"}','{"text": "bench"}','{"text": ""}']}}
setblock 72 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "engineer\'s"}','{"text": "workbench with"}','{"text": "the components"}','{"text": "blueprint"}']}}
fill 81 64 187 81 79 200 minecraft:light_gray_concrete
kw testworld use 75 63 192 up immersiveengineering:workbench
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
