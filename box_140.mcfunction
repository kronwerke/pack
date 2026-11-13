# 140 enderio/smelter, cap_bank, filter, soul_binder, vacuum_chest, enchanter
#area 211 275 281 300
fill 211 64 275 255 91 300 minecraft:air
fill 256 64 275 281 91 300 minecraft:air
fill 211 60 275 281 62 300 minecraft:stone
fill 211 63 275 281 63 300 minecraft:light_gray_concrete
fill 215 64 281 281 79 281 minecraft:light_gray_concrete
fill 215 64 281 215 79 294 minecraft:light_gray_concrete
setblock 216 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.1"}','{"text": "enderio"}','{"text": "smelter"}','{"text": ""}']}}
setblock 217 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmelze"}','{"text": ""}','{"text": ""}']}}
fill 226 64 281 226 79 294 minecraft:light_gray_concrete
setblock 219 64 286 enderio:alloy_smelter[facing=south,powered=true]
setblock 221 64 286 enderio:sag_mill[facing=south,powered=true]
setblock 223 64 286 minecraft:smooth_stone_slab
summon item_display 223.5 64.95 286.5 {item:{id:"enderio:basic_capacitor",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 227 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.2"}','{"text": "enderio"}','{"text": "cap_bank"}','{"text": ""}']}}
setblock 228 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Kondensatorbank"}','{"text": ""}','{"text": ""}']}}
fill 236 64 281 236 79 294 minecraft:light_gray_concrete
fill 230 64 286 232 66 286 enderio:basic_capacitor_bank
setblock 237 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.3"}','{"text": "enderio"}','{"text": "filter"}','{"text": ""}']}}
setblock 238 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Verbindung ein"}','{"text": ""}','{"text": ""}']}}
fill 246 64 281 246 79 294 minecraft:light_gray_concrete
setblock 240 64 286 minecraft:smooth_stone_slab
summon item_display 240.5 64.95 286.5 {item:{id:"enderio:yeta_wrench",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 242 64 286 minecraft:smooth_stone_slab
summon item_display 242.5 64.95 286.5 {item:{id:"enderio:basic_item_filter",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 247 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.4"}','{"text": "enderio"}','{"text": "soul_binder"}','{"text": ""}']}}
setblock 248 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Seelenbinder"}','{"text": ""}','{"text": ""}']}}
fill 256 64 281 256 79 294 minecraft:light_gray_concrete
setblock 250 64 286 enderio:soul_binder[facing=south,powered=true]
setblock 252 64 286 minecraft:smooth_stone_slab
summon item_display 252.5 64.95 286.5 {item:{id:"enderio:soul_vial",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 257 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.5"}','{"text": "enderio"}','{"text": "vacuum_chest"}','{"text": ""}']}}
setblock 258 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Vakuumkiste auf"}','{"text": ""}','{"text": ""}']}}
fill 266 64 281 266 79 294 minecraft:light_gray_concrete
setblock 261 64 286 enderio:vacuum_chest
summon item 259.5 64.2 287.5 {Item:{id:"minecraft:rotten_flesh",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 263.5 64.2 287.5 {Item:{id:"minecraft:bone",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 260.5 64.2 288.5 {Item:{id:"minecraft:gunpowder",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 262.5 64.2 285.5 {Item:{id:"minecraft:string",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 267 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.6"}','{"text": "enderio"}','{"text": "enchanter"}','{"text": ""}']}}
setblock 268 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Verzauberer"}','{"text": ""}','{"text": ""}']}}
fill 276 64 281 276 79 294 minecraft:light_gray_concrete
setblock 271 64 286 enderio:enchanter[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
