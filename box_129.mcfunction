# 129 quarries/first_dig, quarry, destroyer, coe_netherite
#area 52 317 101 342
fill 52 64 317 96 91 342 minecraft:air
fill 97 64 317 101 91 342 minecraft:air
fill 52 60 317 101 62 342 minecraft:stone
fill 52 63 317 101 63 342 minecraft:light_gray_concrete
fill 56 64 323 101 79 323 minecraft:light_gray_concrete
fill 56 64 323 56 79 336 minecraft:light_gray_concrete
setblock 57 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.1"}','{"text": "quarries"}','{"text": "first_dig"}','{"text": ""}']}}
setblock 58 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass den"}','{"text": "Builder graben"}','{"text": ""}','{"text": ""}']}}
fill 66 64 323 66 79 336 minecraft:light_gray_concrete
setblock 61 64 328 rftoolsbuilder:builder[facing=south]
setblock 61 65 328 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 67 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.2"}','{"text": "quarries"}','{"text": "quarry"}','{"text": ""}']}}
setblock 68 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Quarry Plus"}','{"text": ""}','{"text": ""}']}}
fill 76 64 323 76 79 336 minecraft:light_gray_concrete
setblock 70 64 329 quarryplus:quarry[facing=south,working=false]
setblock 71 64 329 quarryplus:marker[facing=up]
setblock 73 64 329 quarryplus:marker[facing=up]
setblock 71 64 327 quarryplus:marker[facing=up]
setblock 77 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.3"}','{"text": "quarries"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 78 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Chunk"}','{"text": "Destroyer"}','{"text": ""}','{"text": ""}']}}
fill 86 64 323 86 79 336 minecraft:light_gray_concrete
setblock 80 64 328 quarryplus:adv_quarry[facing=south,working=false]
setblock 82 64 328 quarryplus:chunk_marker
setblock 87 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.4"}','{"text": "quarries"}','{"text": "coe_netherite"}','{"text": ""}']}}
setblock 88 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Netheritbohrer"}','{"text": ""}','{"text": ""}']}}
fill 96 64 323 96 79 336 minecraft:light_gray_concrete
setblock 89 64 328 minecraft:smooth_stone_slab
summon item_display 89.5 64.95 328.5 {item:{id:"createoreexcavation:drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 91 64 328 minecraft:smooth_stone_slab
summon item_display 91.5 64.95 328.5 {item:{id:"createoreexcavation:diamond_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 93 64 328 minecraft:smooth_stone_slab
summon item_display 93.5 64.95 328.5 {item:{id:"createoreexcavation:netherite_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
