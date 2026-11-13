# 033 create_trains/unprocessed_sheet
#area 329 42 348 67
fill 329 64 42 348 91 67 minecraft:air
fill 329 60 42 348 62 67 minecraft:stone
fill 329 63 42 348 63 67 minecraft:light_gray_concrete
fill 333 64 48 348 79 48 minecraft:light_gray_concrete
fill 333 64 48 333 79 61 minecraft:light_gray_concrete
setblock 334 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "033"}','{"text": "create_trains"}','{"text": "unprocessed_sheet"}','{"text": ""}']}}
setblock 335 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spout pouring"}','{"text": "lava on"}','{"text": "powdered"}','{"text": "obsidian"}']}}
fill 343 64 48 343 79 61 minecraft:light_gray_concrete
setblock 338 64 53 create:depot
setblock 338 66 53 create:spout
setblock 338 67 53 create:fluid_tank[bottom=true,shape=window,top=true]
kw testworld use 338 64 53 up create:powdered_obsidian
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
