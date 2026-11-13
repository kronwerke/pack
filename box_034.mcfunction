# 034 create_trains/unprocessed_sheet
#area 327 42 346 67
fill 327 64 42 346 91 67 minecraft:air
fill 327 60 42 346 62 67 minecraft:stone
fill 327 63 42 346 63 67 minecraft:light_gray_concrete
fill 331 64 48 346 79 48 minecraft:light_gray_concrete
fill 331 64 48 331 79 61 minecraft:light_gray_concrete
setblock 332 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "034"}','{"text": "create_trains"}','{"text": "unprocessed_sheet"}','{"text": ""}']}}
setblock 333 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spout pouring"}','{"text": "lava on"}','{"text": "powdered"}','{"text": "obsidian"}']}}
fill 341 64 48 341 79 61 minecraft:light_gray_concrete
setblock 336 64 53 create:depot
setblock 336 66 53 create:spout
setblock 336 67 53 create:fluid_tank[bottom=true,shape=window,top=true]
kw testworld use 336 64 53 up create:powdered_obsidian
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
