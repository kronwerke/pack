# 148 list_gear/mek_jetpack, wyvern, sg_end
#area 253 338 292 363
fill 253 64 338 292 91 363 minecraft:air
fill 253 60 338 292 62 363 minecraft:stone
fill 253 63 338 292 63 363 minecraft:light_gray_concrete
fill 257 64 344 292 79 344 minecraft:light_gray_concrete
fill 257 64 344 257 79 357 minecraft:light_gray_concrete
setblock 258 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.1"}','{"text": "list_gear"}','{"text": "mek_jetpack"}','{"text": ""}']}}
setblock 259 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Flieg mit dem"}','{"text": "Jetpack"}','{"text": ""}','{"text": ""}']}}
fill 267 64 344 267 79 357 minecraft:light_gray_concrete
summon armor_stand 262.5 64 349.5 {ArmorItems:[{},{},{id:"mekanism:jetpack",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[20f,0f]}
setblock 268 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.2"}','{"text": "list_gear"}','{"text": "wyvern"}','{"text": ""}']}}
setblock 269 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Wyvern-Ausrüstung"}','{"text": ""}','{"text": ""}']}}
fill 277 64 344 277 79 357 minecraft:light_gray_concrete
summon armor_stand 271.5 64 349.5 {ArmorItems:[{},{},{id:"draconicevolution:wyvern_chestpiece",count:1},{}],HandItems:[{id:"draconicevolution:wyvern_sword",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon armor_stand 273.5 64 349.5 {ArmorItems:[{},{},{},{}],HandItems:[{id:"draconicevolution:wyvern_pickaxe",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 278 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.3"}','{"text": "list_gear"}','{"text": "sg_end"}','{"text": ""}']}}
setblock 279 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Azur-Elektrum"}','{"text": "und"}','{"text": "Tyrann-Stahl"}']}}
fill 287 64 344 287 79 357 minecraft:light_gray_concrete
fill 281 64 348 283 65 348 minecraft:end_stone
setblock 282 64 348 silentgear:azure_silver_ore
setblock 283 65 348 silentgear:azure_silver_ore
setblock 281 64 350 minecraft:smooth_stone_slab
summon item_display 281.5 64.95 350.5 {item:{id:"silentgear:azure_electrum_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 283 64 350 minecraft:smooth_stone_slab
summon item_display 283.5 64.95 350.5 {item:{id:"silentgear:tyrian_steel_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
