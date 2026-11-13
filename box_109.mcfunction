# 109 flux_networks/dust
#area 58 275 77 300
fill 58 64 275 77 91 300 minecraft:air
fill 58 60 275 77 62 300 minecraft:stone
fill 58 63 275 77 63 300 minecraft:light_gray_concrete
fill 62 64 281 77 79 281 minecraft:light_gray_concrete
fill 62 64 281 62 79 294 minecraft:light_gray_concrete
setblock 63 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "109"}','{"text": "flux_networks"}','{"text": "dust"}','{"text": ""}']}}
setblock 64 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the bedrock gap"}','{"text": "with redstone"}','{"text": "and obsidian,"}','{"text": "left-clicking"}']}}
setblock 65 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the obsidian"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 72 64 281 72 79 294 minecraft:light_gray_concrete
setblock 67 64 286 minecraft:bedrock
summon item 67.5 65.1 286.5 {Item:{id:"minecraft:redstone",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 67 66 286 minecraft:obsidian
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
