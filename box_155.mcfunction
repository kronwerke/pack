# 155 enderio/smelter, cap_bank, conduits, filter, soul_binder, vacuum_chest, enchanter
#area 211 277 291 302
fill 211 64 277 255 91 302 minecraft:air
fill 256 64 277 291 91 302 minecraft:air
fill 211 60 277 291 62 302 minecraft:stone
fill 211 63 277 291 63 302 minecraft:light_gray_concrete
fill 215 64 283 291 79 283 minecraft:light_gray_concrete
fill 215 64 283 215 79 296 minecraft:light_gray_concrete
setblock 216 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.1"}','{"text": "enderio"}','{"text": "smelter"}','{"text": ""}']}}
setblock 217 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmelze"}','{"text": ""}','{"text": ""}']}}
fill 226 64 283 226 79 296 minecraft:light_gray_concrete
setblock 219 64 288 enderio:alloy_smelter[facing=south,powered=true]
setblock 221 64 288 enderio:sag_mill[facing=south,powered=true]
setblock 223 64 288 minecraft:smooth_stone_slab
summon item_display 223.5 64.95 288.5 {item:{id:"enderio:basic_capacitor",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 227 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.2"}','{"text": "enderio"}','{"text": "cap_bank"}','{"text": ""}']}}
setblock 228 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Kondensatorbank"}','{"text": ""}','{"text": ""}']}}
fill 236 64 283 236 79 296 minecraft:light_gray_concrete
fill 230 64 288 232 66 288 enderio:basic_capacitor_bank
setblock 237 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.3"}','{"text": "enderio"}','{"text": "conduits"}','{"text": ""}']}}
setblock 238 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Leitungen"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 246 64 283 246 79 296 minecraft:light_gray_concrete
setblock 241 64 288 minecraft:smooth_stone_slab
summon item_display 241.5 65.4 288.5 {item:{id:"enderio:conduit",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 247 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.4"}','{"text": "enderio"}','{"text": "filter"}','{"text": ""}']}}
setblock 248 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Verbindung ein"}','{"text": ""}','{"text": ""}']}}
fill 256 64 283 256 79 296 minecraft:light_gray_concrete
setblock 250 64 288 minecraft:smooth_stone_slab
summon item_display 250.5 64.95 288.5 {item:{id:"enderio:yeta_wrench",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 252 64 288 minecraft:smooth_stone_slab
summon item_display 252.5 64.95 288.5 {item:{id:"enderio:basic_item_filter",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 257 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.5"}','{"text": "enderio"}','{"text": "soul_binder"}','{"text": ""}']}}
setblock 258 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Seelenbinder"}','{"text": ""}','{"text": ""}']}}
fill 266 64 283 266 79 296 minecraft:light_gray_concrete
setblock 260 64 288 enderio:soul_binder[facing=south,powered=true]
setblock 262 64 288 minecraft:smooth_stone_slab
summon item_display 262.5 64.95 288.5 {item:{id:"enderio:soul_vial",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 267 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.6"}','{"text": "enderio"}','{"text": "vacuum_chest"}','{"text": ""}']}}
setblock 268 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Vakuumkiste auf"}','{"text": ""}','{"text": ""}']}}
fill 276 64 283 276 79 296 minecraft:light_gray_concrete
setblock 271 64 288 enderio:vacuum_chest
summon item 269.5 64.2 289.5 {Item:{id:"minecraft:rotten_flesh",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 273.5 64.2 289.5 {Item:{id:"minecraft:bone",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 270.5 64.2 290.5 {Item:{id:"minecraft:gunpowder",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 272.5 64.2 287.5 {Item:{id:"minecraft:string",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 277 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.7"}','{"text": "enderio"}','{"text": "enchanter"}','{"text": ""}']}}
setblock 278 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Verzauberer"}','{"text": ""}','{"text": ""}']}}
fill 286 64 283 286 79 296 minecraft:light_gray_concrete
setblock 281 64 288 enderio:enchanter[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
