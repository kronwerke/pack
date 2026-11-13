# 130 flux_networks/dust
#area 58 277 77 302
fill 58 64 277 77 91 302 minecraft:air
fill 58 60 277 77 62 302 minecraft:stone
fill 58 63 277 77 63 302 minecraft:light_gray_concrete
fill 62 64 283 77 79 283 minecraft:light_gray_concrete
fill 62 64 283 62 79 296 minecraft:light_gray_concrete
setblock 63 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130"}','{"text": "flux_networks"}','{"text": "dust"}','{"text": ""}']}}
setblock 64 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the bedrock gap"}','{"text": "with redstone"}','{"text": "and obsidian,"}','{"text": "left-clicking"}']}}
setblock 65 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the obsidian"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 72 64 283 72 79 296 minecraft:light_gray_concrete
setblock 67 64 288 minecraft:bedrock
summon item 67.5 65.1 288.5 {Item:{id:"minecraft:redstone",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 67 66 288 minecraft:obsidian
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
