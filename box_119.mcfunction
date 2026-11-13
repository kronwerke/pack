# 119 list_gear/mek_jetpack, drilling, wyvern, sg_end
#area 253 336 302 361
fill 253 64 336 297 91 361 minecraft:air
fill 298 64 336 302 91 361 minecraft:air
fill 253 60 336 302 62 361 minecraft:stone
fill 253 63 336 302 63 361 minecraft:light_gray_concrete
fill 257 64 342 302 79 342 minecraft:light_gray_concrete
fill 257 64 342 257 79 355 minecraft:light_gray_concrete
setblock 258 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "119.1"}','{"text": "list_gear"}','{"text": "mek_jetpack"}','{"text": ""}']}}
setblock 259 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Flieg mit dem"}','{"text": "Jetpack"}','{"text": ""}','{"text": ""}']}}
fill 267 64 342 267 79 355 minecraft:light_gray_concrete
summon armor_stand 262.5 64 347.5 {ArmorItems:[{},{},{id:"mekanism:jetpack",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[20f,0f]}
setblock 268 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "119.2"}','{"text": "list_gear"}','{"text": "drilling"}','{"text": ""}']}}
setblock 269 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Bohrmaschine"}','{"text": "auf"}','{"text": ""}']}}
fill 277 64 342 277 79 355 minecraft:light_gray_concrete
setblock 272 64 347 createoreexcavation:drilling_machine[facing=south]
setblock 274 64 347 minecraft:smooth_stone_slab
summon item_display 274.5 64.95 347.5 {item:{id:"createoreexcavation:drill",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 278 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "119.3"}','{"text": "list_gear"}','{"text": "wyvern"}','{"text": ""}']}}
setblock 279 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Wyvern-Ausrüstung"}','{"text": ""}','{"text": ""}']}}
fill 287 64 342 287 79 355 minecraft:light_gray_concrete
summon armor_stand 281.5 64 347.5 {ArmorItems:[{},{},{id:"draconicevolution:wyvern_chestpiece",count:1},{}],HandItems:[{id:"draconicevolution:wyvern_sword",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon armor_stand 283.5 64 347.5 {ArmorItems:[{},{},{},{}],HandItems:[{id:"draconicevolution:wyvern_pickaxe",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 288 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "119.4"}','{"text": "list_gear"}','{"text": "sg_end"}','{"text": ""}']}}
setblock 289 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Azur-Elektrum"}','{"text": "und"}','{"text": "Tyrann-Stahl"}']}}
fill 297 64 342 297 79 355 minecraft:light_gray_concrete
fill 291 64 346 293 65 346 minecraft:end_stone
setblock 292 64 346 silentgear:azure_silver_ore
setblock 293 65 346 silentgear:azure_silver_ore
setblock 291 64 348 minecraft:smooth_stone_slab
summon item_display 291.5 64.95 348.5 {item:{id:"silentgear:azure_electrum_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 293 64 348 minecraft:smooth_stone_slab
summon item_display 293.5 64.95 348.5 {item:{id:"silentgear:tyrian_steel_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
