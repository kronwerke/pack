# 174 list_gear/mek_jetpack, drilling, wyvern, sg_end
#area 293 405 344 434
fill 293 64 405 331 91 434 minecraft:air
fill 332 64 405 344 91 434 minecraft:air
fill 293 60 405 344 62 434 minecraft:stone
fill 293 63 405 344 63 434 minecraft:light_gray_concrete
fill 297 64 411 344 79 411 minecraft:light_gray_concrete
fill 297 64 411 297 79 428 minecraft:light_gray_concrete
setblock 298 64 427 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "174.1"}','{"text": "list_gear"}','{"text": "mek_jetpack"}','{"text": ""}']}}
setblock 299 64 427 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Flieg mit dem"}','{"text": "Jetpack"}','{"text": ""}','{"text": ""}']}}
fill 307 64 411 307 79 428 minecraft:light_gray_concrete
summon armor_stand 302.5 64 416.5 {ArmorItems:[{},{},{id:"mekanism:jetpack",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[20f,0f]}
setblock 308 64 427 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "174.2"}','{"text": "list_gear"}','{"text": "drilling"}','{"text": ""}']}}
setblock 309 64 427 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Bohrmaschine"}','{"text": "auf"}','{"text": ""}']}}
fill 319 64 411 319 79 428 minecraft:light_gray_concrete
kw testworld place shots:createoreexcavation/drilling_machine 309 63 413 none
setblock 320 64 427 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "174.3"}','{"text": "list_gear"}','{"text": "wyvern"}','{"text": ""}']}}
setblock 321 64 427 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Wyvern-Ausrüstung"}','{"text": ""}','{"text": ""}']}}
fill 329 64 411 329 79 428 minecraft:light_gray_concrete
summon armor_stand 323.5 64 416.5 {ArmorItems:[{},{},{id:"draconicevolution:wyvern_chestpiece",count:1},{}],HandItems:[{id:"draconicevolution:wyvern_sword",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon armor_stand 325.5 64 416.5 {ArmorItems:[{},{},{},{}],HandItems:[{id:"draconicevolution:wyvern_pickaxe",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 330 64 427 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "174.4"}','{"text": "list_gear"}','{"text": "sg_end"}','{"text": ""}']}}
setblock 331 64 427 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Azur-Elektrum"}','{"text": "und"}','{"text": "Tyrann-Stahl"}']}}
fill 339 64 411 339 79 428 minecraft:light_gray_concrete
fill 333 64 415 335 65 415 minecraft:end_stone
setblock 334 64 415 silentgear:azure_silver_ore
setblock 335 65 415 silentgear:azure_silver_ore
setblock 333 64 417 minecraft:smooth_stone_slab
summon item_display 333.5 64.95 417.5 {item:{id:"silentgear:azure_electrum_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 335 64 417 minecraft:smooth_stone_slab
summon item_display 335.5 64.95 417.5 {item:{id:"silentgear:tyrian_steel_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
