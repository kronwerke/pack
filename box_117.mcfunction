# 117 enderio/smelter, cap_bank, soul_binder, vacuum_chest, enchanter
#area 150 233 210 258
fill 150 64 233 194 91 258 minecraft:air
fill 195 64 233 210 91 258 minecraft:air
fill 150 60 233 210 62 258 minecraft:stone
fill 150 63 233 210 63 258 minecraft:light_gray_concrete
fill 154 64 239 210 79 239 minecraft:light_gray_concrete
fill 154 64 239 154 79 252 minecraft:light_gray_concrete
setblock 155 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.1"}','{"text": "enderio"}','{"text": "smelter"}','{"text": ""}']}}
setblock 156 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmelze"}','{"text": ""}','{"text": ""}']}}
fill 165 64 239 165 79 252 minecraft:light_gray_concrete
setblock 158 64 244 enderio:alloy_smelter[facing=south,powered=true]
setblock 160 64 244 enderio:sag_mill[facing=south,powered=true]
setblock 162 64 244 minecraft:smooth_stone_slab
summon item_display 162.5 64.95 244.5 {item:{id:"enderio:basic_capacitor",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 166 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.2"}','{"text": "enderio"}','{"text": "cap_bank"}','{"text": ""}']}}
setblock 167 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Kondensatorbank"}','{"text": ""}','{"text": ""}']}}
fill 175 64 239 175 79 252 minecraft:light_gray_concrete
fill 169 64 244 171 66 244 enderio:basic_capacitor_bank
setblock 176 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.3"}','{"text": "enderio"}','{"text": "soul_binder"}','{"text": ""}']}}
setblock 177 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Seelenbinder"}','{"text": ""}','{"text": ""}']}}
fill 185 64 239 185 79 252 minecraft:light_gray_concrete
setblock 179 64 244 enderio:soul_binder[facing=south,powered=true]
setblock 181 64 244 minecraft:smooth_stone_slab
summon item_display 181.5 64.95 244.5 {item:{id:"enderio:soul_vial",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 186 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.4"}','{"text": "enderio"}','{"text": "vacuum_chest"}','{"text": ""}']}}
setblock 187 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Vakuumkiste auf"}','{"text": ""}','{"text": ""}']}}
fill 195 64 239 195 79 252 minecraft:light_gray_concrete
setblock 190 64 244 enderio:vacuum_chest
summon item 188.5 64.2 245.5 {Item:{id:"minecraft:rotten_flesh",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 192.5 64.2 245.5 {Item:{id:"minecraft:bone",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 189.5 64.2 246.5 {Item:{id:"minecraft:gunpowder",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 191.5 64.2 243.5 {Item:{id:"minecraft:string",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 196 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.5"}','{"text": "enderio"}','{"text": "enchanter"}','{"text": ""}']}}
setblock 197 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Verzauberer"}','{"text": ""}','{"text": ""}']}}
fill 205 64 239 205 79 252 minecraft:light_gray_concrete
setblock 200 64 244 enderio:enchanter[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
