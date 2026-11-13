# 144 quarries/first_dig, quarry, destroyer, coe_netherite
#area 52 319 101 344
fill 52 64 319 96 91 344 minecraft:air
fill 97 64 319 101 91 344 minecraft:air
fill 52 60 319 101 62 344 minecraft:stone
fill 52 63 319 101 63 344 minecraft:light_gray_concrete
fill 56 64 325 101 79 325 minecraft:light_gray_concrete
fill 56 64 325 56 79 338 minecraft:light_gray_concrete
setblock 57 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144.1"}','{"text": "quarries"}','{"text": "first_dig"}','{"text": ""}']}}
setblock 58 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass den"}','{"text": "Builder graben"}','{"text": ""}','{"text": ""}']}}
fill 66 64 325 66 79 338 minecraft:light_gray_concrete
setblock 61 64 330 rftoolsbuilder:builder[facing=south]
setblock 61 65 330 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 67 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144.2"}','{"text": "quarries"}','{"text": "quarry"}','{"text": ""}']}}
setblock 68 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Quarry Plus"}','{"text": ""}','{"text": ""}']}}
fill 76 64 325 76 79 338 minecraft:light_gray_concrete
setblock 70 64 331 quarryplus:quarry[facing=south,working=false]
setblock 71 64 331 quarryplus:marker[facing=up]
setblock 73 64 331 quarryplus:marker[facing=up]
setblock 71 64 329 quarryplus:marker[facing=up]
setblock 77 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144.3"}','{"text": "quarries"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 78 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Chunk"}','{"text": "Destroyer"}','{"text": ""}','{"text": ""}']}}
fill 86 64 325 86 79 338 minecraft:light_gray_concrete
setblock 80 64 330 quarryplus:adv_quarry[facing=south,working=false]
setblock 82 64 330 quarryplus:chunk_marker
setblock 87 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144.4"}','{"text": "quarries"}','{"text": "coe_netherite"}','{"text": ""}']}}
setblock 88 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Netheritbohrer"}','{"text": ""}','{"text": ""}']}}
fill 96 64 325 96 79 338 minecraft:light_gray_concrete
setblock 89 64 330 minecraft:smooth_stone_slab
summon item_display 89.5 64.95 330.5 {item:{id:"createoreexcavation:drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 91 64 330 minecraft:smooth_stone_slab
summon item_display 91.5 64.95 330.5 {item:{id:"createoreexcavation:diamond_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 93 64 330 minecraft:smooth_stone_slab
summon item_display 93.5 64.95 330.5 {item:{id:"createoreexcavation:netherite_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
