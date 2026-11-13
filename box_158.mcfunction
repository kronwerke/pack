# 158 quarries/first_dig, quarry, destroyer, coe_netherite
#area 72 353 121 378
fill 72 64 353 116 91 378 minecraft:air
fill 117 64 353 121 91 378 minecraft:air
fill 72 60 353 121 62 378 minecraft:stone
fill 72 63 353 121 63 378 minecraft:light_gray_concrete
fill 76 64 359 121 79 359 minecraft:light_gray_concrete
fill 76 64 359 76 79 372 minecraft:light_gray_concrete
setblock 77 64 371 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.1"}','{"text": "quarries"}','{"text": "first_dig"}','{"text": ""}']}}
setblock 78 64 371 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass den"}','{"text": "Builder graben"}','{"text": ""}','{"text": ""}']}}
fill 86 64 359 86 79 372 minecraft:light_gray_concrete
setblock 81 64 364 rftoolsbuilder:builder[facing=south]
setblock 81 65 364 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 87 64 371 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.2"}','{"text": "quarries"}','{"text": "quarry"}','{"text": ""}']}}
setblock 88 64 371 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Quarry Plus"}','{"text": ""}','{"text": ""}']}}
fill 96 64 359 96 79 372 minecraft:light_gray_concrete
setblock 90 64 365 quarryplus:quarry[facing=south,working=false]
setblock 91 64 365 quarryplus:marker[facing=up]
setblock 93 64 365 quarryplus:marker[facing=up]
setblock 91 64 363 quarryplus:marker[facing=up]
setblock 97 64 371 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.3"}','{"text": "quarries"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 98 64 371 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Chunk"}','{"text": "Destroyer"}','{"text": ""}','{"text": ""}']}}
fill 106 64 359 106 79 372 minecraft:light_gray_concrete
setblock 100 64 364 quarryplus:adv_quarry[facing=south,working=false]
setblock 102 64 364 quarryplus:chunk_marker
setblock 107 64 371 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.4"}','{"text": "quarries"}','{"text": "coe_netherite"}','{"text": ""}']}}
setblock 108 64 371 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Netheritbohrer"}','{"text": ""}','{"text": ""}']}}
fill 116 64 359 116 79 372 minecraft:light_gray_concrete
setblock 109 64 364 minecraft:smooth_stone_slab
summon item_display 109.5 64.95 364.5 {item:{id:"createoreexcavation:drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 111 64 364 minecraft:smooth_stone_slab
summon item_display 111.5 64.95 364.5 {item:{id:"createoreexcavation:diamond_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 113 64 364 minecraft:smooth_stone_slab
summon item_display 113.5 64.95 364.5 {item:{id:"createoreexcavation:netherite_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
