# 037 create_trains/unprocessed_sheet
#area 344 44 363 69
fill 344 64 44 363 91 69 minecraft:air
fill 344 60 44 363 62 69 minecraft:stone
fill 344 63 44 363 63 69 minecraft:light_gray_concrete
fill 348 64 50 363 79 50 minecraft:light_gray_concrete
fill 348 64 50 348 79 63 minecraft:light_gray_concrete
setblock 349 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "037"}','{"text": "create_trains"}','{"text": "unprocessed_sheet"}','{"text": ""}']}}
setblock 350 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spout pouring"}','{"text": "lava on"}','{"text": "powdered"}','{"text": "obsidian"}']}}
fill 358 64 50 358 79 63 minecraft:light_gray_concrete
setblock 353 64 55 create:depot
setblock 353 66 55 create:spout
setblock 353 67 55 create:fluid_tank[bottom=true,shape=window,top=true]
kw testworld use 353 64 55 up create:powdered_obsidian
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
