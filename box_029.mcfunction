# 029 create_trains/unprocessed_sheet
#area 249 42 268 67
fill 249 64 42 268 91 67 minecraft:air
fill 249 60 42 268 62 67 minecraft:stone
fill 249 63 42 268 63 67 minecraft:light_gray_concrete
fill 253 64 48 268 79 48 minecraft:light_gray_concrete
fill 253 64 48 253 79 61 minecraft:light_gray_concrete
setblock 254 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "029"}','{"text": "create_trains"}','{"text": "unprocessed_sheet"}','{"text": ""}']}}
setblock 255 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spout pouring"}','{"text": "lava on"}','{"text": "powdered"}','{"text": "obsidian"}']}}
fill 263 64 48 263 79 61 minecraft:light_gray_concrete
setblock 258 64 53 create:depot
setblock 258 66 53 create:spout
setblock 258 67 53 create:fluid_tank[bottom=true,shape=window,top=true]
kw testworld use 258 64 53 up create:powdered_obsidian
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
