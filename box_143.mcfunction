# 143 flux_networks/dust
#area 58 311 77 336
fill 58 64 311 77 91 336 minecraft:air
fill 58 60 311 77 62 336 minecraft:stone
fill 58 63 311 77 63 336 minecraft:light_gray_concrete
fill 62 64 317 77 79 317 minecraft:light_gray_concrete
fill 62 64 317 62 79 330 minecraft:light_gray_concrete
setblock 63 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143"}','{"text": "flux_networks"}','{"text": "dust"}','{"text": ""}']}}
setblock 64 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the bedrock gap"}','{"text": "with redstone"}','{"text": "and obsidian,"}','{"text": "left-clicking"}']}}
setblock 65 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the obsidian"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 72 64 317 72 79 330 minecraft:light_gray_concrete
setblock 67 64 322 minecraft:bedrock
summon item 67.5 65.1 322.5 {Item:{id:"minecraft:redstone",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 67 66 322 minecraft:obsidian
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
