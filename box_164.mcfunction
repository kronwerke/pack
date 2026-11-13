# 164 list_gear/mek_jetpack, drilling, wyvern, sg_end
#area 253 370 304 399
fill 253 64 370 291 91 399 minecraft:air
fill 292 64 370 304 91 399 minecraft:air
fill 253 60 370 304 62 399 minecraft:stone
fill 253 63 370 304 63 399 minecraft:light_gray_concrete
fill 257 64 376 304 79 376 minecraft:light_gray_concrete
fill 257 64 376 257 79 393 minecraft:light_gray_concrete
setblock 258 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "164.1"}','{"text": "list_gear"}','{"text": "mek_jetpack"}','{"text": ""}']}}
setblock 259 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Flieg mit dem"}','{"text": "Jetpack"}','{"text": ""}','{"text": ""}']}}
fill 267 64 376 267 79 393 minecraft:light_gray_concrete
summon armor_stand 262.5 64 381.5 {ArmorItems:[{},{},{id:"mekanism:jetpack",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[20f,0f]}
setblock 268 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "164.2"}','{"text": "list_gear"}','{"text": "drilling"}','{"text": ""}']}}
setblock 269 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Bohrmaschine"}','{"text": "auf"}','{"text": ""}']}}
fill 279 64 376 279 79 393 minecraft:light_gray_concrete
kw testworld place shots:createoreexcavation/drilling_machine 269 63 378 none
setblock 280 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "164.3"}','{"text": "list_gear"}','{"text": "wyvern"}','{"text": ""}']}}
setblock 281 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Wyvern-Ausrüstung"}','{"text": ""}','{"text": ""}']}}
fill 289 64 376 289 79 393 minecraft:light_gray_concrete
summon armor_stand 283.5 64 381.5 {ArmorItems:[{},{},{id:"draconicevolution:wyvern_chestpiece",count:1},{}],HandItems:[{id:"draconicevolution:wyvern_sword",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon armor_stand 285.5 64 381.5 {ArmorItems:[{},{},{},{}],HandItems:[{id:"draconicevolution:wyvern_pickaxe",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 290 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "164.4"}','{"text": "list_gear"}','{"text": "sg_end"}','{"text": ""}']}}
setblock 291 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Azur-Elektrum"}','{"text": "und"}','{"text": "Tyrann-Stahl"}']}}
fill 299 64 376 299 79 393 minecraft:light_gray_concrete
fill 293 64 380 295 65 380 minecraft:end_stone
setblock 294 64 380 silentgear:azure_silver_ore
setblock 295 65 380 silentgear:azure_silver_ore
setblock 293 64 382 minecraft:smooth_stone_slab
summon item_display 293.5 64.95 382.5 {item:{id:"silentgear:azure_electrum_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 295 64 382 minecraft:smooth_stone_slab
summon item_display 295.5 64.95 382.5 {item:{id:"silentgear:tyrian_steel_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
