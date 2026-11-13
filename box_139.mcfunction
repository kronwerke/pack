# 139 flux_networks/dust
#area 58 307 77 332
fill 58 64 307 77 91 332 minecraft:air
fill 58 60 307 77 62 332 minecraft:stone
fill 58 63 307 77 63 332 minecraft:light_gray_concrete
fill 62 64 313 77 79 313 minecraft:light_gray_concrete
fill 62 64 313 62 79 326 minecraft:light_gray_concrete
setblock 63 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "139"}','{"text": "flux_networks"}','{"text": "dust"}','{"text": ""}']}}
setblock 64 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the bedrock gap"}','{"text": "with redstone"}','{"text": "and obsidian,"}','{"text": "left-clicking"}']}}
setblock 65 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the obsidian"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 72 64 313 72 79 326 minecraft:light_gray_concrete
setblock 67 64 318 minecraft:bedrock
summon item 67.5 65.1 318.5 {Item:{id:"minecraft:redstone",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 67 66 318 minecraft:obsidian
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
