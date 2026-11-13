# 135 enderio/smelter, cap_bank, filter, soul_binder, vacuum_chest, enchanter
#area 161 269 231 294
fill 161 64 269 205 91 294 minecraft:air
fill 206 64 269 231 91 294 minecraft:air
fill 161 60 269 231 62 294 minecraft:stone
fill 161 63 269 231 63 294 minecraft:light_gray_concrete
fill 165 64 275 231 79 275 minecraft:light_gray_concrete
fill 165 64 275 165 79 288 minecraft:light_gray_concrete
setblock 166 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.1"}','{"text": "enderio"}','{"text": "smelter"}','{"text": ""}']}}
setblock 167 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmelze"}','{"text": ""}','{"text": ""}']}}
fill 176 64 275 176 79 288 minecraft:light_gray_concrete
setblock 169 64 280 enderio:alloy_smelter[facing=south,powered=true]
setblock 171 64 280 enderio:sag_mill[facing=south,powered=true]
setblock 173 64 280 minecraft:smooth_stone_slab
summon item_display 173.5 64.95 280.5 {item:{id:"enderio:basic_capacitor",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 177 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.2"}','{"text": "enderio"}','{"text": "cap_bank"}','{"text": ""}']}}
setblock 178 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Kondensatorbank"}','{"text": ""}','{"text": ""}']}}
fill 186 64 275 186 79 288 minecraft:light_gray_concrete
fill 180 64 280 182 66 280 enderio:basic_capacitor_bank
setblock 187 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.3"}','{"text": "enderio"}','{"text": "filter"}','{"text": ""}']}}
setblock 188 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Verbindung ein"}','{"text": ""}','{"text": ""}']}}
fill 196 64 275 196 79 288 minecraft:light_gray_concrete
setblock 190 64 280 minecraft:smooth_stone_slab
summon item_display 190.5 64.95 280.5 {item:{id:"enderio:yeta_wrench",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 192 64 280 minecraft:smooth_stone_slab
summon item_display 192.5 64.95 280.5 {item:{id:"enderio:basic_item_filter",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 197 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.4"}','{"text": "enderio"}','{"text": "soul_binder"}','{"text": ""}']}}
setblock 198 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Seelenbinder"}','{"text": ""}','{"text": ""}']}}
fill 206 64 275 206 79 288 minecraft:light_gray_concrete
setblock 200 64 280 enderio:soul_binder[facing=south,powered=true]
setblock 202 64 280 minecraft:smooth_stone_slab
summon item_display 202.5 64.95 280.5 {item:{id:"enderio:soul_vial",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 207 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.5"}','{"text": "enderio"}','{"text": "vacuum_chest"}','{"text": ""}']}}
setblock 208 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Vakuumkiste auf"}','{"text": ""}','{"text": ""}']}}
fill 216 64 275 216 79 288 minecraft:light_gray_concrete
setblock 211 64 280 enderio:vacuum_chest
summon item 209.5 64.2 281.5 {Item:{id:"minecraft:rotten_flesh",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 213.5 64.2 281.5 {Item:{id:"minecraft:bone",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 210.5 64.2 282.5 {Item:{id:"minecraft:gunpowder",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 212.5 64.2 279.5 {Item:{id:"minecraft:string",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 217 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.6"}','{"text": "enderio"}','{"text": "enchanter"}','{"text": ""}']}}
setblock 218 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Verzauberer"}','{"text": ""}','{"text": ""}']}}
fill 226 64 275 226 79 288 minecraft:light_gray_concrete
setblock 221 64 280 enderio:enchanter[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
