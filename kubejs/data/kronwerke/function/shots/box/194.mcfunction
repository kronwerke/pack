# 194 refined_storage/
fill 321 63 355 332 63 368 minecraft:light_gray_concrete
fill 321 64 355 332 71 355 minecraft:light_gray_concrete
fill 321 64 355 321 71 368 minecraft:light_gray_concrete
setblock 322 64 367 minecraft:air
setblock 322 64 367 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "194"}','{"text": "refined_storage"}','{"text": ""}','{"text": ""}']}}
setblock 323 64 367 minecraft:air
setblock 323 64 367 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the network"}','{"text": "grid and the"}','{"text": "autocrafter"}','{"text": ""}']}}
summon text_display 326.5 71 360.5 {text:'[{"text": "194  ", "color": "gold"}, {"text": "refined_storage", "color": "gray"}, {"text": "\\n", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 323 64 360 refinedstorage:controller
fill 324 64 360 328 64 360 refinedstorage:cable
setblock 325 64 359 refinedstorage:disk_drive
setblock 327 64 361 refinedstorage:grid[direction=south]
setblock 329 64 360 refinedstorage:autocrafter[direction=south]
setblock 323 64 361 mekanism:creative_energy_cube
