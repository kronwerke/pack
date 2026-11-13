# 122 enderio/smelter, cap_bank, soul_binder, vacuum_chest, enchanter
#area 161 235 221 260
fill 161 64 235 205 91 260 minecraft:air
fill 206 64 235 221 91 260 minecraft:air
fill 161 60 235 221 62 260 minecraft:stone
fill 161 63 235 221 63 260 minecraft:light_gray_concrete
fill 165 64 241 221 79 241 minecraft:light_gray_concrete
fill 165 64 241 165 79 254 minecraft:light_gray_concrete
setblock 166 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.1"}','{"text": "enderio"}','{"text": "smelter"}','{"text": ""}']}}
setblock 167 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmelze"}','{"text": ""}','{"text": ""}']}}
fill 176 64 241 176 79 254 minecraft:light_gray_concrete
setblock 169 64 246 enderio:alloy_smelter[facing=south,powered=true]
setblock 171 64 246 enderio:sag_mill[facing=south,powered=true]
setblock 173 64 246 minecraft:smooth_stone_slab
summon item_display 173.5 64.95 246.5 {item:{id:"enderio:basic_capacitor",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 177 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.2"}','{"text": "enderio"}','{"text": "cap_bank"}','{"text": ""}']}}
setblock 178 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Kondensatorbank"}','{"text": ""}','{"text": ""}']}}
fill 186 64 241 186 79 254 minecraft:light_gray_concrete
fill 180 64 246 182 66 246 enderio:basic_capacitor_bank
setblock 187 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.3"}','{"text": "enderio"}','{"text": "soul_binder"}','{"text": ""}']}}
setblock 188 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Seelenbinder"}','{"text": ""}','{"text": ""}']}}
fill 196 64 241 196 79 254 minecraft:light_gray_concrete
setblock 190 64 246 enderio:soul_binder[facing=south,powered=true]
setblock 192 64 246 minecraft:smooth_stone_slab
summon item_display 192.5 64.95 246.5 {item:{id:"enderio:soul_vial",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 197 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.4"}','{"text": "enderio"}','{"text": "vacuum_chest"}','{"text": ""}']}}
setblock 198 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Vakuumkiste auf"}','{"text": ""}','{"text": ""}']}}
fill 206 64 241 206 79 254 minecraft:light_gray_concrete
setblock 201 64 246 enderio:vacuum_chest
summon item 199.5 64.2 247.5 {Item:{id:"minecraft:rotten_flesh",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 203.5 64.2 247.5 {Item:{id:"minecraft:bone",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 200.5 64.2 248.5 {Item:{id:"minecraft:gunpowder",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 202.5 64.2 245.5 {Item:{id:"minecraft:string",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 207 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.5"}','{"text": "enderio"}','{"text": "enchanter"}','{"text": ""}']}}
setblock 208 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Verzauberer"}','{"text": ""}','{"text": ""}']}}
fill 216 64 241 216 79 254 minecraft:light_gray_concrete
setblock 211 64 246 enderio:enchanter[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
