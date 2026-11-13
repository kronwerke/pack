# 160 quarries/first_dig, quarry, destroyer, coe_netherite
#area 72 357 121 382
fill 72 64 357 116 91 382 minecraft:air
fill 117 64 357 121 91 382 minecraft:air
fill 72 60 357 121 62 382 minecraft:stone
fill 72 63 357 121 63 382 minecraft:light_gray_concrete
fill 76 64 363 121 79 363 minecraft:light_gray_concrete
fill 76 64 363 76 79 376 minecraft:light_gray_concrete
setblock 77 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.1"}','{"text": "quarries"}','{"text": "first_dig"}','{"text": ""}']}}
setblock 78 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass den"}','{"text": "Builder graben"}','{"text": ""}','{"text": ""}']}}
fill 86 64 363 86 79 376 minecraft:light_gray_concrete
setblock 81 64 368 rftoolsbuilder:builder[facing=south]
setblock 81 65 368 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 87 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.2"}','{"text": "quarries"}','{"text": "quarry"}','{"text": ""}']}}
setblock 88 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Quarry Plus"}','{"text": ""}','{"text": ""}']}}
fill 96 64 363 96 79 376 minecraft:light_gray_concrete
setblock 90 64 369 quarryplus:quarry[facing=south,working=false]
setblock 91 64 369 quarryplus:marker[facing=up]
setblock 93 64 369 quarryplus:marker[facing=up]
setblock 91 64 367 quarryplus:marker[facing=up]
setblock 97 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.3"}','{"text": "quarries"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 98 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Chunk"}','{"text": "Destroyer"}','{"text": ""}','{"text": ""}']}}
fill 106 64 363 106 79 376 minecraft:light_gray_concrete
setblock 100 64 368 quarryplus:adv_quarry[facing=south,working=false]
setblock 102 64 368 quarryplus:chunk_marker
setblock 107 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.4"}','{"text": "quarries"}','{"text": "coe_netherite"}','{"text": ""}']}}
setblock 108 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Netheritbohrer"}','{"text": ""}','{"text": ""}']}}
fill 116 64 363 116 79 376 minecraft:light_gray_concrete
setblock 109 64 368 minecraft:smooth_stone_slab
summon item_display 109.5 64.95 368.5 {item:{id:"createoreexcavation:drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 111 64 368 minecraft:smooth_stone_slab
summon item_display 111.5 64.95 368.5 {item:{id:"createoreexcavation:diamond_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 113 64 368 minecraft:smooth_stone_slab
summon item_display 113.5 64.95 368.5 {item:{id:"createoreexcavation:netherite_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
