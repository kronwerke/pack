# 088 flux_networks/dust
#area 58 254 77 279
fill 58 64 254 77 91 279 minecraft:air
fill 58 60 254 77 62 279 minecraft:stone
fill 58 63 254 77 63 279 minecraft:light_gray_concrete
fill 62 64 260 77 79 260 minecraft:light_gray_concrete
fill 62 64 260 62 79 273 minecraft:light_gray_concrete
setblock 63 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088"}','{"text": "flux_networks"}','{"text": "dust"}','{"text": ""}']}}
setblock 64 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the bedrock gap"}','{"text": "with redstone"}','{"text": "and obsidian,"}','{"text": "left-clicking"}']}}
setblock 65 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the obsidian"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 72 64 260 72 79 273 minecraft:light_gray_concrete
setblock 67 64 265 minecraft:bedrock
summon item 67.5 65.1 265.5 {Item:{id:"minecraft:redstone",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 67 66 265 minecraft:obsidian
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
