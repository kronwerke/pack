# 098 flux_networks/dust
#area 58 273 77 298
fill 58 64 273 77 91 298 minecraft:air
fill 58 60 273 77 62 298 minecraft:stone
fill 58 63 273 77 63 298 minecraft:light_gray_concrete
fill 62 64 279 77 79 279 minecraft:light_gray_concrete
fill 62 64 279 62 79 292 minecraft:light_gray_concrete
setblock 63 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098"}','{"text": "flux_networks"}','{"text": "dust"}','{"text": ""}']}}
setblock 64 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the bedrock gap"}','{"text": "with redstone"}','{"text": "and obsidian,"}','{"text": "left-clicking"}']}}
setblock 65 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the obsidian"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 72 64 279 72 79 292 minecraft:light_gray_concrete
setblock 67 64 284 minecraft:bedrock
summon item 67.5 65.1 284.5 {Item:{id:"minecraft:redstone",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 67 66 284 minecraft:obsidian
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
