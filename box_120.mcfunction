# 120 immersive/bench
#area 66 217 86 242
fill 66 64 217 86 91 242 minecraft:air
fill 66 60 217 86 62 242 minecraft:stone
fill 66 63 217 86 63 242 minecraft:light_gray_concrete
fill 70 64 223 86 79 223 minecraft:light_gray_concrete
fill 70 64 223 70 79 236 minecraft:light_gray_concrete
setblock 71 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "120"}','{"text": "immersive"}','{"text": "bench"}','{"text": ""}']}}
setblock 72 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "engineer\'s"}','{"text": "workbench with"}','{"text": "the components"}','{"text": "blueprint"}']}}
fill 81 64 223 81 79 236 minecraft:light_gray_concrete
kw testworld use 75 63 228 up immersiveengineering:workbench
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
