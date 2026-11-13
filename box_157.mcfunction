# 157 quarries/first_dig, quarry, destroyer, coe_netherite
#area 62 349 111 374
fill 62 64 349 106 91 374 minecraft:air
fill 107 64 349 111 91 374 minecraft:air
fill 62 60 349 111 62 374 minecraft:stone
fill 62 63 349 111 63 374 minecraft:light_gray_concrete
fill 66 64 355 111 79 355 minecraft:light_gray_concrete
fill 66 64 355 66 79 368 minecraft:light_gray_concrete
setblock 67 64 367 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "157.1"}','{"text": "quarries"}','{"text": "first_dig"}','{"text": ""}']}}
setblock 68 64 367 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass den"}','{"text": "Builder graben"}','{"text": ""}','{"text": ""}']}}
fill 76 64 355 76 79 368 minecraft:light_gray_concrete
setblock 71 64 360 rftoolsbuilder:builder[facing=south]
setblock 71 65 360 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 77 64 367 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "157.2"}','{"text": "quarries"}','{"text": "quarry"}','{"text": ""}']}}
setblock 78 64 367 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Quarry Plus"}','{"text": ""}','{"text": ""}']}}
fill 86 64 355 86 79 368 minecraft:light_gray_concrete
setblock 80 64 361 quarryplus:quarry[facing=south,working=false]
setblock 81 64 361 quarryplus:marker[facing=up]
setblock 83 64 361 quarryplus:marker[facing=up]
setblock 81 64 359 quarryplus:marker[facing=up]
setblock 87 64 367 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "157.3"}','{"text": "quarries"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 88 64 367 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Chunk"}','{"text": "Destroyer"}','{"text": ""}','{"text": ""}']}}
fill 96 64 355 96 79 368 minecraft:light_gray_concrete
setblock 90 64 360 quarryplus:adv_quarry[facing=south,working=false]
setblock 92 64 360 quarryplus:chunk_marker
setblock 97 64 367 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "157.4"}','{"text": "quarries"}','{"text": "coe_netherite"}','{"text": ""}']}}
setblock 98 64 367 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Netheritbohrer"}','{"text": ""}','{"text": ""}']}}
fill 106 64 355 106 79 368 minecraft:light_gray_concrete
setblock 99 64 360 minecraft:smooth_stone_slab
summon item_display 99.5 64.95 360.5 {item:{id:"createoreexcavation:drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 101 64 360 minecraft:smooth_stone_slab
summon item_display 101.5 64.95 360.5 {item:{id:"createoreexcavation:diamond_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 103 64 360 minecraft:smooth_stone_slab
summon item_display 103.5 64.95 360.5 {item:{id:"createoreexcavation:netherite_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
