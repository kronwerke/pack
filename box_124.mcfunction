# 124 immersive/bench
#area 91 217 111 242
fill 91 64 217 111 91 242 minecraft:air
fill 91 60 217 111 62 242 minecraft:stone
fill 91 63 217 111 63 242 minecraft:light_gray_concrete
fill 95 64 223 111 79 223 minecraft:light_gray_concrete
fill 95 64 223 95 79 236 minecraft:light_gray_concrete
setblock 96 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "124"}','{"text": "immersive"}','{"text": "bench"}','{"text": ""}']}}
setblock 97 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "engineer\'s"}','{"text": "workbench with"}','{"text": "the components"}','{"text": "blueprint"}']}}
fill 106 64 223 106 79 236 minecraft:light_gray_concrete
kw testworld use 100 63 228 up immersiveengineering:workbench
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
