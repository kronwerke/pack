# 143 flux_networks/dust
#area 58 313 77 338
fill 58 64 313 77 91 338 minecraft:air
fill 58 60 313 77 62 338 minecraft:stone
fill 58 63 313 77 63 338 minecraft:light_gray_concrete
fill 62 64 319 77 79 319 minecraft:light_gray_concrete
fill 62 64 319 62 79 332 minecraft:light_gray_concrete
setblock 63 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143"}','{"text": "flux_networks"}','{"text": "dust"}','{"text": ""}']}}
setblock 64 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the bedrock gap"}','{"text": "with redstone"}','{"text": "and obsidian,"}','{"text": "left-clicking"}']}}
setblock 65 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the obsidian"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 72 64 319 72 79 332 minecraft:light_gray_concrete
setblock 67 64 324 minecraft:bedrock
summon item 67.5 65.1 324.5 {Item:{id:"minecraft:redstone",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 67 66 324 minecraft:obsidian
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
