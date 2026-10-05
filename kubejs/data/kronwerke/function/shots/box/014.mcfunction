# 014 farms/animals_thorn
fill 66 63 31 79 63 46 minecraft:light_gray_concrete
fill 66 64 31 79 71 31 minecraft:light_gray_concrete
fill 66 64 31 66 71 46 minecraft:light_gray_concrete
setblock 67 64 45 minecraft:air
setblock 67 64 45 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "014"}','{"text": "farms"}','{"text": "animals_thorn"}','{"text": ""}']}}
setblock 68 64 45 minecraft:air
setblock 68 64 45 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fenced pen with"}','{"text": "feeding trough,"}','{"text": "Dreadthorne,"}','{"text": "hopper floor,"}']}}
setblock 69 64 45 minecraft:air
setblock 69 64 45 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "mana pool"}','{"text": "nearby"}','{"text": ""}','{"text": ""}']}}
summon text_display 72.5 71 37.5 {text:'[{"text": "014  ", "color": "gold"}, {"text": "farms/animals_thorn", "color": "gray"}, {"text": "\\nPflanze einen Schreckdorn", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 68 64 33 minecraft:oak_fence
setblock 68 64 41 minecraft:oak_fence
setblock 69 64 33 minecraft:oak_fence
setblock 69 64 41 minecraft:oak_fence
setblock 70 64 33 minecraft:oak_fence
setblock 70 64 41 minecraft:oak_fence
setblock 71 64 33 minecraft:oak_fence
setblock 71 64 41 minecraft:oak_fence
setblock 72 64 33 minecraft:oak_fence
setblock 72 64 41 minecraft:oak_fence
setblock 73 64 33 minecraft:oak_fence
setblock 73 64 41 minecraft:oak_fence
setblock 74 64 33 minecraft:oak_fence
setblock 74 64 41 minecraft:oak_fence
setblock 75 64 33 minecraft:oak_fence
setblock 75 64 41 minecraft:oak_fence
setblock 76 64 33 minecraft:oak_fence
setblock 76 64 41 minecraft:oak_fence
setblock 68 64 33 minecraft:oak_fence
setblock 76 64 33 minecraft:oak_fence
setblock 68 64 34 minecraft:oak_fence
setblock 76 64 34 minecraft:oak_fence
setblock 68 64 35 minecraft:oak_fence
setblock 76 64 35 minecraft:oak_fence
setblock 68 64 36 minecraft:oak_fence
setblock 76 64 36 minecraft:oak_fence
setblock 68 64 37 minecraft:oak_fence
setblock 76 64 37 minecraft:oak_fence
setblock 68 64 38 minecraft:oak_fence
setblock 76 64 38 minecraft:oak_fence
setblock 68 64 39 minecraft:oak_fence
setblock 76 64 39 minecraft:oak_fence
setblock 68 64 40 minecraft:oak_fence
setblock 76 64 40 minecraft:oak_fence
setblock 68 64 41 minecraft:oak_fence
setblock 76 64 41 minecraft:oak_fence
fill 69 63 34 75 63 40 minecraft:hopper
setblock 72 64 37 botania:hopperhock
setblock 70 64 35 farmingforblockheads:feeding_trough
setblock 74 64 39 botania:mana_pool
summon minecraft:cow 70.5 64 38.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:sheep 71.5 64 38.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:pig 72.5 64 38.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:chicken 73.5 64 38.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 77 64 42 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:dreadthorne",count:1},{Slot:1b,id:"minecraft:wheat",count:32}]}
