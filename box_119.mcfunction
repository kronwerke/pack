# 119 enderio/smelter, cap_bank, soul_binder, vacuum_chest, enchanter
#area 161 233 221 258
fill 161 64 233 205 91 258 minecraft:air
fill 206 64 233 221 91 258 minecraft:air
fill 161 60 233 221 62 258 minecraft:stone
fill 161 63 233 221 63 258 minecraft:light_gray_concrete
fill 165 64 239 221 79 239 minecraft:light_gray_concrete
fill 165 64 239 165 79 252 minecraft:light_gray_concrete
setblock 166 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "119.1"}','{"text": "enderio"}','{"text": "smelter"}','{"text": ""}']}}
setblock 167 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmelze"}','{"text": ""}','{"text": ""}']}}
fill 176 64 239 176 79 252 minecraft:light_gray_concrete
setblock 169 64 244 enderio:alloy_smelter[facing=south,powered=true]
setblock 171 64 244 enderio:sag_mill[facing=south,powered=true]
setblock 173 64 244 minecraft:smooth_stone_slab
summon item_display 173.5 64.95 244.5 {item:{id:"enderio:basic_capacitor",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 177 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "119.2"}','{"text": "enderio"}','{"text": "cap_bank"}','{"text": ""}']}}
setblock 178 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Kondensatorbank"}','{"text": ""}','{"text": ""}']}}
fill 186 64 239 186 79 252 minecraft:light_gray_concrete
fill 180 64 244 182 66 244 enderio:basic_capacitor_bank
setblock 187 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "119.3"}','{"text": "enderio"}','{"text": "soul_binder"}','{"text": ""}']}}
setblock 188 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Seelenbinder"}','{"text": ""}','{"text": ""}']}}
fill 196 64 239 196 79 252 minecraft:light_gray_concrete
setblock 190 64 244 enderio:soul_binder[facing=south,powered=true]
setblock 192 64 244 minecraft:smooth_stone_slab
summon item_display 192.5 64.95 244.5 {item:{id:"enderio:soul_vial",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 197 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "119.4"}','{"text": "enderio"}','{"text": "vacuum_chest"}','{"text": ""}']}}
setblock 198 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Vakuumkiste auf"}','{"text": ""}','{"text": ""}']}}
fill 206 64 239 206 79 252 minecraft:light_gray_concrete
setblock 201 64 244 enderio:vacuum_chest
summon item 199.5 64.2 245.5 {Item:{id:"minecraft:rotten_flesh",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 203.5 64.2 245.5 {Item:{id:"minecraft:bone",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 200.5 64.2 246.5 {Item:{id:"minecraft:gunpowder",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 202.5 64.2 243.5 {Item:{id:"minecraft:string",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 207 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "119.5"}','{"text": "enderio"}','{"text": "enchanter"}','{"text": ""}']}}
setblock 208 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Verzauberer"}','{"text": ""}','{"text": ""}']}}
fill 216 64 239 216 79 252 minecraft:light_gray_concrete
setblock 211 64 244 enderio:enchanter[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
