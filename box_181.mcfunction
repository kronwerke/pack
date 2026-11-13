# 181 quarries/first_dig, quarry, destroyer, coe_netherite
#area 87 386 136 411
fill 87 64 386 131 91 411 minecraft:air
fill 132 64 386 136 91 411 minecraft:air
fill 87 60 386 136 62 411 minecraft:stone
fill 87 63 386 136 63 411 minecraft:light_gray_concrete
fill 91 64 392 136 79 392 minecraft:light_gray_concrete
fill 91 64 392 91 79 405 minecraft:light_gray_concrete
setblock 92 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "181.1"}','{"text": "quarries"}','{"text": "first_dig"}','{"text": ""}']}}
setblock 93 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass den"}','{"text": "Builder graben"}','{"text": ""}','{"text": ""}']}}
fill 101 64 392 101 79 405 minecraft:light_gray_concrete
setblock 96 64 397 rftoolsbuilder:builder[facing=south]
setblock 96 65 397 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 102 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "181.2"}','{"text": "quarries"}','{"text": "quarry"}','{"text": ""}']}}
setblock 103 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Quarry Plus"}','{"text": ""}','{"text": ""}']}}
fill 111 64 392 111 79 405 minecraft:light_gray_concrete
setblock 105 64 398 quarryplus:quarry[facing=south,working=false]
setblock 106 64 398 quarryplus:marker[facing=up]
setblock 108 64 398 quarryplus:marker[facing=up]
setblock 106 64 396 quarryplus:marker[facing=up]
setblock 112 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "181.3"}','{"text": "quarries"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 113 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Chunk"}','{"text": "Destroyer"}','{"text": ""}','{"text": ""}']}}
fill 121 64 392 121 79 405 minecraft:light_gray_concrete
setblock 115 64 397 quarryplus:adv_quarry[facing=south,working=false]
setblock 117 64 397 quarryplus:chunk_marker
setblock 122 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "181.4"}','{"text": "quarries"}','{"text": "coe_netherite"}','{"text": ""}']}}
setblock 123 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Netheritbohrer"}','{"text": ""}','{"text": ""}']}}
fill 131 64 392 131 79 405 minecraft:light_gray_concrete
setblock 124 64 397 minecraft:smooth_stone_slab
summon item_display 124.5 64.95 397.5 {item:{id:"createoreexcavation:drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 126 64 397 minecraft:smooth_stone_slab
summon item_display 126.5 64.95 397.5 {item:{id:"createoreexcavation:diamond_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 128 64 397 minecraft:smooth_stone_slab
summon item_display 128.5 64.95 397.5 {item:{id:"createoreexcavation:netherite_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
