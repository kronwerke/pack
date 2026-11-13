# 035 create_trains/unprocessed_sheet
#area 344 42 363 67
fill 344 64 42 363 91 67 minecraft:air
fill 344 60 42 363 62 67 minecraft:stone
fill 344 63 42 363 63 67 minecraft:light_gray_concrete
fill 348 64 48 363 79 48 minecraft:light_gray_concrete
fill 348 64 48 348 79 61 minecraft:light_gray_concrete
setblock 349 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "035"}','{"text": "create_trains"}','{"text": "unprocessed_sheet"}','{"text": ""}']}}
setblock 350 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spout pouring"}','{"text": "lava on"}','{"text": "powdered"}','{"text": "obsidian"}']}}
fill 358 64 48 358 79 61 minecraft:light_gray_concrete
setblock 353 64 53 create:depot
setblock 353 66 53 create:spout
setblock 353 67 53 create:fluid_tank[bottom=true,shape=window,top=true]
kw testworld use 353 64 53 up create:powdered_obsidian
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
