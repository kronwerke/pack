# 131 enderio/smelter, cap_bank, soul_binder, vacuum_chest, enchanter
#area 161 265 221 290
fill 161 64 265 205 91 290 minecraft:air
fill 206 64 265 221 91 290 minecraft:air
fill 161 60 265 221 62 290 minecraft:stone
fill 161 63 265 221 63 290 minecraft:light_gray_concrete
fill 165 64 271 221 79 271 minecraft:light_gray_concrete
fill 165 64 271 165 79 284 minecraft:light_gray_concrete
setblock 166 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.1"}','{"text": "enderio"}','{"text": "smelter"}','{"text": ""}']}}
setblock 167 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmelze"}','{"text": ""}','{"text": ""}']}}
fill 176 64 271 176 79 284 minecraft:light_gray_concrete
setblock 169 64 276 enderio:alloy_smelter[facing=south,powered=true]
setblock 171 64 276 enderio:sag_mill[facing=south,powered=true]
setblock 173 64 276 minecraft:smooth_stone_slab
summon item_display 173.5 64.95 276.5 {item:{id:"enderio:basic_capacitor",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 177 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.2"}','{"text": "enderio"}','{"text": "cap_bank"}','{"text": ""}']}}
setblock 178 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Kondensatorbank"}','{"text": ""}','{"text": ""}']}}
fill 186 64 271 186 79 284 minecraft:light_gray_concrete
fill 180 64 276 182 66 276 enderio:basic_capacitor_bank
setblock 187 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.3"}','{"text": "enderio"}','{"text": "soul_binder"}','{"text": ""}']}}
setblock 188 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Seelenbinder"}','{"text": ""}','{"text": ""}']}}
fill 196 64 271 196 79 284 minecraft:light_gray_concrete
setblock 190 64 276 enderio:soul_binder[facing=south,powered=true]
setblock 192 64 276 minecraft:smooth_stone_slab
summon item_display 192.5 64.95 276.5 {item:{id:"enderio:soul_vial",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 197 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.4"}','{"text": "enderio"}','{"text": "vacuum_chest"}','{"text": ""}']}}
setblock 198 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Vakuumkiste auf"}','{"text": ""}','{"text": ""}']}}
fill 206 64 271 206 79 284 minecraft:light_gray_concrete
setblock 201 64 276 enderio:vacuum_chest
summon item 199.5 64.2 277.5 {Item:{id:"minecraft:rotten_flesh",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 203.5 64.2 277.5 {Item:{id:"minecraft:bone",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 200.5 64.2 278.5 {Item:{id:"minecraft:gunpowder",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 202.5 64.2 275.5 {Item:{id:"minecraft:string",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 207 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.5"}','{"text": "enderio"}','{"text": "enchanter"}','{"text": ""}']}}
setblock 208 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Verzauberer"}','{"text": ""}','{"text": ""}']}}
fill 216 64 271 216 79 284 minecraft:light_gray_concrete
setblock 211 64 276 enderio:enchanter[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
