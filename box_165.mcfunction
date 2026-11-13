# 165 list_gear/mek_jetpack, drilling, wyvern, sg_end
#area 283 374 334 403
fill 283 64 374 321 91 403 minecraft:air
fill 322 64 374 334 91 403 minecraft:air
fill 283 60 374 334 62 403 minecraft:stone
fill 283 63 374 334 63 403 minecraft:light_gray_concrete
fill 287 64 380 334 79 380 minecraft:light_gray_concrete
fill 287 64 380 287 79 397 minecraft:light_gray_concrete
setblock 288 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.1"}','{"text": "list_gear"}','{"text": "mek_jetpack"}','{"text": ""}']}}
setblock 289 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Flieg mit dem"}','{"text": "Jetpack"}','{"text": ""}','{"text": ""}']}}
fill 297 64 380 297 79 397 minecraft:light_gray_concrete
summon armor_stand 292.5 64 385.5 {ArmorItems:[{},{},{id:"mekanism:jetpack",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[20f,0f]}
setblock 298 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.2"}','{"text": "list_gear"}','{"text": "drilling"}','{"text": ""}']}}
setblock 299 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Bohrmaschine"}','{"text": "auf"}','{"text": ""}']}}
fill 309 64 380 309 79 397 minecraft:light_gray_concrete
kw testworld place shots:createoreexcavation/drilling_machine 299 63 382 none
setblock 310 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.3"}','{"text": "list_gear"}','{"text": "wyvern"}','{"text": ""}']}}
setblock 311 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Wyvern-Ausrüstung"}','{"text": ""}','{"text": ""}']}}
fill 319 64 380 319 79 397 minecraft:light_gray_concrete
summon armor_stand 313.5 64 385.5 {ArmorItems:[{},{},{id:"draconicevolution:wyvern_chestpiece",count:1},{}],HandItems:[{id:"draconicevolution:wyvern_sword",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon armor_stand 315.5 64 385.5 {ArmorItems:[{},{},{},{}],HandItems:[{id:"draconicevolution:wyvern_pickaxe",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 320 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.4"}','{"text": "list_gear"}','{"text": "sg_end"}','{"text": ""}']}}
setblock 321 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Azur-Elektrum"}','{"text": "und"}','{"text": "Tyrann-Stahl"}']}}
fill 329 64 380 329 79 397 minecraft:light_gray_concrete
fill 323 64 384 325 65 384 minecraft:end_stone
setblock 324 64 384 silentgear:azure_silver_ore
setblock 325 65 384 silentgear:azure_silver_ore
setblock 323 64 386 minecraft:smooth_stone_slab
summon item_display 323.5 64.95 386.5 {item:{id:"silentgear:azure_electrum_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 325 64 386 minecraft:smooth_stone_slab
summon item_display 325.5 64.95 386.5 {item:{id:"silentgear:tyrian_steel_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
