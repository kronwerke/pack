# 148 flux_networks/dust
#area 58 317 77 342
fill 58 64 317 77 91 342 minecraft:air
fill 58 60 317 77 62 342 minecraft:stone
fill 58 63 317 77 63 342 minecraft:light_gray_concrete
fill 62 64 323 77 79 323 minecraft:light_gray_concrete
fill 62 64 323 62 79 336 minecraft:light_gray_concrete
setblock 63 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148"}','{"text": "flux_networks"}','{"text": "dust"}','{"text": ""}']}}
setblock 64 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the bedrock gap"}','{"text": "with redstone"}','{"text": "and obsidian,"}','{"text": "left-clicking"}']}}
setblock 65 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the obsidian"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 72 64 323 72 79 336 minecraft:light_gray_concrete
setblock 67 64 328 minecraft:bedrock
summon item 67.5 65.1 328.5 {Item:{id:"minecraft:redstone",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 67 66 328 minecraft:obsidian
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
