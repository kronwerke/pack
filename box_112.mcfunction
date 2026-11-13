# 112 quarries/first_dig, quarry, destroyer, coe_netherite
#area 52 315 104 340
fill 52 64 315 96 91 340 minecraft:air
fill 97 64 315 104 91 340 minecraft:air
fill 52 60 315 104 62 340 minecraft:stone
fill 52 63 315 104 63 340 minecraft:light_gray_concrete
fill 56 64 321 104 79 321 minecraft:light_gray_concrete
fill 56 64 321 56 79 334 minecraft:light_gray_concrete
setblock 57 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.1"}','{"text": "quarries"}','{"text": "first_dig"}','{"text": ""}']}}
setblock 58 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass den"}','{"text": "Builder graben"}','{"text": ""}','{"text": ""}']}}
fill 66 64 321 66 79 334 minecraft:light_gray_concrete
setblock 61 64 326 rftoolsbuilder:builder[facing=south]
setblock 61 65 326 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 67 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.2"}','{"text": "quarries"}','{"text": "quarry"}','{"text": ""}']}}
setblock 68 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Quarry Plus"}','{"text": ""}','{"text": ""}']}}
fill 78 64 321 78 79 334 minecraft:light_gray_concrete
setblock 69 64 328 quarryplus:quarry[facing=south,working=false]
setblock 70 64 328 quarryplus:marker[facing=up]
setblock 75 64 328 quarryplus:marker[facing=up]
setblock 70 64 324 quarryplus:marker[facing=up]
setblock 79 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.3"}','{"text": "quarries"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 80 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Chunk"}','{"text": "Destroyer"}','{"text": ""}','{"text": ""}']}}
fill 88 64 321 88 79 334 minecraft:light_gray_concrete
setblock 82 64 326 quarryplus:adv_quarry[facing=south,working=false]
setblock 84 64 326 quarryplus:chunk_marker
setblock 89 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.4"}','{"text": "quarries"}','{"text": "coe_netherite"}','{"text": ""}']}}
setblock 90 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Netheritbohrer"}','{"text": ""}','{"text": ""}']}}
fill 99 64 321 99 79 334 minecraft:light_gray_concrete
setblock 91 64 326 minecraft:smooth_stone_slab
summon item_display 91.5 64.95 326.5 {item:{id:"createoreexcavation:drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 93 64 326 minecraft:smooth_stone_slab
summon item_display 93.5 64.95 326.5 {item:{id:"createoreexcavation:diamond_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 95 64 326 minecraft:smooth_stone_slab
summon item_display 95.5 64.95 326.5 {item:{id:"createoreexcavation:netherite_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 97 64 326 createoreexcavation:drilling_machine[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
