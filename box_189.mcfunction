# 189 list_gear/mek_jetpack, drilling, wyvern, sg_end
#area 293 407 344 436
fill 293 64 407 331 91 436 minecraft:air
fill 332 64 407 344 91 436 minecraft:air
fill 293 60 407 344 62 436 minecraft:stone
fill 293 63 407 344 63 436 minecraft:light_gray_concrete
fill 297 64 413 344 79 413 minecraft:light_gray_concrete
fill 297 64 413 297 79 430 minecraft:light_gray_concrete
setblock 298 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "189.1"}','{"text": "list_gear"}','{"text": "mek_jetpack"}','{"text": ""}']}}
setblock 299 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Flieg mit dem"}','{"text": "Jetpack"}','{"text": ""}','{"text": ""}']}}
fill 307 64 413 307 79 430 minecraft:light_gray_concrete
summon armor_stand 302.5 64 418.5 {ArmorItems:[{},{},{id:"mekanism:jetpack",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[20f,0f]}
setblock 308 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "189.2"}','{"text": "list_gear"}','{"text": "drilling"}','{"text": ""}']}}
setblock 309 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Bohrmaschine"}','{"text": "auf"}','{"text": ""}']}}
fill 319 64 413 319 79 430 minecraft:light_gray_concrete
kw testworld place shots:createoreexcavation/drilling_machine 309 63 415 none
setblock 320 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "189.3"}','{"text": "list_gear"}','{"text": "wyvern"}','{"text": ""}']}}
setblock 321 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Wyvern-Ausrüstung"}','{"text": ""}','{"text": ""}']}}
fill 329 64 413 329 79 430 minecraft:light_gray_concrete
summon armor_stand 323.5 64 418.5 {ArmorItems:[{},{},{id:"draconicevolution:wyvern_chestpiece",count:1},{}],HandItems:[{id:"draconicevolution:wyvern_sword",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon armor_stand 325.5 64 418.5 {ArmorItems:[{},{},{},{}],HandItems:[{id:"draconicevolution:wyvern_pickaxe",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 330 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "189.4"}','{"text": "list_gear"}','{"text": "sg_end"}','{"text": ""}']}}
setblock 331 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Azur-Elektrum"}','{"text": "und"}','{"text": "Tyrann-Stahl"}']}}
fill 339 64 413 339 79 430 minecraft:light_gray_concrete
fill 333 64 417 335 65 417 minecraft:end_stone
setblock 334 64 417 silentgear:azure_silver_ore
setblock 335 65 417 silentgear:azure_silver_ore
setblock 333 64 419 minecraft:smooth_stone_slab
summon item_display 333.5 64.95 419.5 {item:{id:"silentgear:azure_electrum_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 335 64 419 minecraft:smooth_stone_slab
summon item_display 335.5 64.95 419.5 {item:{id:"silentgear:tyrian_steel_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
