# 139 draconic_chaos/crystals
#area 35 317 54 342
fill 35 64 317 54 91 342 minecraft:air
fill 35 60 317 54 62 342 minecraft:stone
fill 35 63 317 54 63 342 minecraft:light_gray_concrete
fill 39 64 323 54 79 323 minecraft:light_gray_concrete
fill 39 64 323 39 79 336 minecraft:light_gray_concrete
setblock 40 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "139"}','{"text": "draconic_chaos"}','{"text": "crystals"}','{"text": ""}']}}
setblock 41 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Brich einen"}','{"text": "Wächterkristall"}','{"text": ""}','{"text": ""}']}}
fill 49 64 323 49 79 336 minecraft:light_gray_concrete
summon draconicevolution:guardian_crystal 44.5 65 328.5 {Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
