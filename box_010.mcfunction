# 010 farms/animals_thorn
#area 60 21 79 46
fill 60 64 21 79 91 46 minecraft:air
fill 60 60 21 79 62 46 minecraft:stone
fill 60 63 21 79 63 46 minecraft:light_gray_concrete
fill 64 64 27 79 79 27 minecraft:light_gray_concrete
fill 64 64 27 64 79 40 minecraft:light_gray_concrete
setblock 65 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "010"}','{"text": "farms"}','{"text": "animals_thorn"}','{"text": ""}']}}
setblock 66 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fenced pen with"}','{"text": "feeding trough,"}','{"text": "Dreadthorne,"}','{"text": "hopper floor,"}']}}
setblock 67 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "mana pool"}','{"text": "nearby"}','{"text": ""}','{"text": ""}']}}
fill 74 64 27 74 79 40 minecraft:light_gray_concrete
fill 67 63 30 71 63 34 minecraft:grass_block[snowy=false]
setblock 67 64 30 minecraft:oak_fence
setblock 67 64 34 minecraft:oak_fence
setblock 68 64 30 minecraft:oak_fence
setblock 68 64 34 minecraft:oak_fence
setblock 69 64 30 minecraft:oak_fence
setblock 69 64 34 minecraft:oak_fence
setblock 70 64 30 minecraft:oak_fence
setblock 70 64 34 minecraft:oak_fence
setblock 71 64 30 minecraft:oak_fence
setblock 71 64 34 minecraft:oak_fence
setblock 67 64 31 minecraft:oak_fence
setblock 71 64 31 minecraft:oak_fence
setblock 67 64 32 minecraft:oak_fence
setblock 71 64 32 minecraft:oak_fence
setblock 67 64 33 minecraft:oak_fence
setblock 71 64 33 minecraft:oak_fence
setblock 69 64 32 botania:dreadthorne
summon minecraft:cow 68.5 64 33.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:cow 70.5 64 31.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],Age:-24000}
setblock 72 64 32 botania:mana_pool{mana:200000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
