# 116 immersive/bench
#area 66 211 86 236
fill 66 64 211 86 91 236 minecraft:air
fill 66 60 211 86 62 236 minecraft:stone
fill 66 63 211 86 63 236 minecraft:light_gray_concrete
fill 70 64 217 86 79 217 minecraft:light_gray_concrete
fill 70 64 217 70 79 230 minecraft:light_gray_concrete
setblock 71 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116"}','{"text": "immersive"}','{"text": "bench"}','{"text": ""}']}}
setblock 72 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "engineer\'s"}','{"text": "workbench with"}','{"text": "the components"}','{"text": "blueprint"}']}}
fill 81 64 217 81 79 230 minecraft:light_gray_concrete
kw testworld use 75 63 222 up immersiveengineering:workbench
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
