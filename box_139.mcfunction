# 139 immersive/bench
#area 91 219 111 244
fill 91 64 219 111 91 244 minecraft:air
fill 91 60 219 111 62 244 minecraft:stone
fill 91 63 219 111 63 244 minecraft:light_gray_concrete
fill 95 64 225 111 79 225 minecraft:light_gray_concrete
fill 95 64 225 95 79 238 minecraft:light_gray_concrete
setblock 96 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "139"}','{"text": "immersive"}','{"text": "bench"}','{"text": ""}']}}
setblock 97 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "engineer\'s"}','{"text": "workbench with"}','{"text": "the components"}','{"text": "blueprint"}']}}
fill 106 64 225 106 79 238 minecraft:light_gray_concrete
kw testworld use 100 63 230 up immersiveengineering:workbench
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
