# 102 quarries/first_dig, quarry, destroyer, coe_netherite
#area 52 296 104 321
fill 52 64 296 96 91 321 minecraft:air
fill 97 64 296 104 91 321 minecraft:air
fill 52 60 296 104 62 321 minecraft:stone
fill 52 63 296 104 63 321 minecraft:light_gray_concrete
fill 56 64 302 104 79 302 minecraft:light_gray_concrete
fill 56 64 302 56 79 315 minecraft:light_gray_concrete
setblock 57 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102.1"}','{"text": "quarries"}','{"text": "first_dig"}','{"text": ""}']}}
setblock 58 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass den"}','{"text": "Builder graben"}','{"text": ""}','{"text": ""}']}}
fill 66 64 302 66 79 315 minecraft:light_gray_concrete
setblock 61 64 307 rftoolsbuilder:builder[facing=south]
setblock 61 65 307 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 67 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102.2"}','{"text": "quarries"}','{"text": "quarry"}','{"text": ""}']}}
setblock 68 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Quarry Plus"}','{"text": ""}','{"text": ""}']}}
fill 78 64 302 78 79 315 minecraft:light_gray_concrete
setblock 69 64 309 quarryplus:quarry[facing=south,working=false]
setblock 70 64 309 quarryplus:marker[facing=up]
setblock 75 64 309 quarryplus:marker[facing=up]
setblock 70 64 305 quarryplus:marker[facing=up]
setblock 79 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102.3"}','{"text": "quarries"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 80 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Chunk"}','{"text": "Destroyer"}','{"text": ""}','{"text": ""}']}}
fill 88 64 302 88 79 315 minecraft:light_gray_concrete
setblock 82 64 307 quarryplus:adv_quarry[facing=south,working=false]
setblock 84 64 307 quarryplus:chunk_marker
setblock 89 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102.4"}','{"text": "quarries"}','{"text": "coe_netherite"}','{"text": ""}']}}
setblock 90 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Netheritbohrer"}','{"text": ""}','{"text": ""}']}}
fill 99 64 302 99 79 315 minecraft:light_gray_concrete
setblock 91 64 307 minecraft:smooth_stone_slab
summon item_display 91.5 64.95 307.5 {item:{id:"createoreexcavation:drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 93 64 307 minecraft:smooth_stone_slab
summon item_display 93.5 64.95 307.5 {item:{id:"createoreexcavation:diamond_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 95 64 307 minecraft:smooth_stone_slab
summon item_display 95.5 64.95 307.5 {item:{id:"createoreexcavation:netherite_drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 97 64 307 createoreexcavation:drilling_machine[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
