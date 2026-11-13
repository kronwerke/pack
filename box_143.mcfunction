# 143 quarries/first_dig, quarry, destroyer, coe_netherite
#area 67 317 116 342
fill 67 64 317 111 91 342 minecraft:air
fill 112 64 317 116 91 342 minecraft:air
fill 67 60 317 116 62 342 minecraft:stone
fill 67 63 317 116 63 342 minecraft:light_gray_concrete
fill 71 64 323 116 79 323 minecraft:light_gray_concrete
fill 71 64 323 71 79 336 minecraft:light_gray_concrete
setblock 72 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143.1"}','{"text": "quarries"}','{"text": "first_dig"}','{"text": ""}']}}
setblock 73 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass den"}','{"text": "Builder graben"}','{"text": ""}','{"text": ""}']}}
fill 81 64 323 81 79 336 minecraft:light_gray_concrete
setblock 76 64 328 rftoolsbuilder:builder[facing=south]
setblock 76 65 328 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 82 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143.2"}','{"text": "quarries"}','{"text": "quarry"}','{"text": ""}']}}
setblock 83 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Quarry Plus"}','{"text": ""}','{"text": ""}']}}
fill 91 64 323 91 79 336 minecraft:light_gray_concrete
setblock 85 64 329 quarryplus:quarry[facing=south,working=false]
setblock 86 64 329 quarryplus:marker[facing=up]
setblock 88 64 329 quarryplus:marker[facing=up]
setblock 86 64 327 quarryplus:marker[facing=up]
setblock 92 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143.3"}','{"text": "quarries"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 93 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Chunk"}','{"text": "Destroyer"}','{"text": ""}','{"text": ""}']}}
fill 101 64 323 101 79 336 minecraft:light_gray_concrete
setblock 95 64 328 quarryplus:adv_quarry[facing=south,working=false]
setblock 97 64 328 quarryplus:chunk_marker
setblock 102 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143.4"}','{"text": "quarries"}','{"text": "coe_netherite"}','{"text": ""}']}}
setblock 103 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Netheritbohrer"}','{"text": ""}','{"text": ""}']}}
fill 111 64 323 111 79 336 minecraft:light_gray_concrete
setblock 104 64 328 minecraft:smooth_stone_slab
summon item_display 104.5 64.95 328.5 {item:{id:"createoreexcavation:drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 106 64 328 minecraft:smooth_stone_slab
summon item_display 106.5 64.95 328.5 {item:{id:"createoreexcavation:diamond_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 108 64 328 minecraft:smooth_stone_slab
summon item_display 108.5 64.95 328.5 {item:{id:"createoreexcavation:netherite_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
