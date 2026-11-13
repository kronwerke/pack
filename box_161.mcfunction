# 161 list_gear/mek_jetpack, wyvern, sg_end
#area 253 370 292 395
fill 253 64 370 292 91 395 minecraft:air
fill 253 60 370 292 62 395 minecraft:stone
fill 253 63 370 292 63 395 minecraft:light_gray_concrete
fill 257 64 376 292 79 376 minecraft:light_gray_concrete
fill 257 64 376 257 79 389 minecraft:light_gray_concrete
setblock 258 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "161.1"}','{"text": "list_gear"}','{"text": "mek_jetpack"}','{"text": ""}']}}
setblock 259 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Flieg mit dem"}','{"text": "Jetpack"}','{"text": ""}','{"text": ""}']}}
fill 267 64 376 267 79 389 minecraft:light_gray_concrete
summon armor_stand 262.5 64 381.5 {ArmorItems:[{},{},{id:"mekanism:jetpack",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[20f,0f]}
setblock 268 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "161.2"}','{"text": "list_gear"}','{"text": "wyvern"}','{"text": ""}']}}
setblock 269 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Wyvern-Ausrüstung"}','{"text": ""}','{"text": ""}']}}
fill 277 64 376 277 79 389 minecraft:light_gray_concrete
summon armor_stand 271.5 64 381.5 {ArmorItems:[{},{},{id:"draconicevolution:wyvern_chestpiece",count:1},{}],HandItems:[{id:"draconicevolution:wyvern_sword",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon armor_stand 273.5 64 381.5 {ArmorItems:[{},{},{},{}],HandItems:[{id:"draconicevolution:wyvern_pickaxe",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 278 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "161.3"}','{"text": "list_gear"}','{"text": "sg_end"}','{"text": ""}']}}
setblock 279 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Azur-Elektrum"}','{"text": "und"}','{"text": "Tyrann-Stahl"}']}}
fill 287 64 376 287 79 389 minecraft:light_gray_concrete
fill 281 64 380 283 65 380 minecraft:end_stone
setblock 282 64 380 silentgear:azure_silver_ore
setblock 283 65 380 silentgear:azure_silver_ore
setblock 281 64 382 minecraft:smooth_stone_slab
summon item_display 281.5 64.95 382.5 {item:{id:"silentgear:azure_electrum_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 283 64 382 minecraft:smooth_stone_slab
summon item_display 283.5 64.95 382.5 {item:{id:"silentgear:tyrian_steel_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
