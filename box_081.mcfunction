# 081 enderio/smelter, cap_bank, soul_binder, vacuum_chest, enchanter
#area 140 212 200 237
fill 140 64 212 184 91 237 minecraft:air
fill 185 64 212 200 91 237 minecraft:air
fill 140 60 212 200 62 237 minecraft:stone
fill 140 63 212 200 63 237 minecraft:light_gray_concrete
fill 144 64 218 200 79 218 minecraft:light_gray_concrete
fill 144 64 218 144 79 231 minecraft:light_gray_concrete
setblock 145 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.1"}','{"text": "enderio"}','{"text": "smelter"}','{"text": ""}']}}
setblock 146 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmelze"}','{"text": ""}','{"text": ""}']}}
fill 155 64 218 155 79 231 minecraft:light_gray_concrete
setblock 148 64 223 enderio:alloy_smelter[facing=south,powered=true]
setblock 150 64 223 enderio:sag_mill[facing=south,powered=true]
setblock 152 64 223 minecraft:smooth_stone_slab
summon item_display 152.5 64.95 223.5 {item:{id:"enderio:basic_capacitor",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 156 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.2"}','{"text": "enderio"}','{"text": "cap_bank"}','{"text": ""}']}}
setblock 157 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Kondensatorbank"}','{"text": ""}','{"text": ""}']}}
fill 165 64 218 165 79 231 minecraft:light_gray_concrete
fill 159 64 223 161 66 223 enderio:basic_capacitor_bank
setblock 166 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.3"}','{"text": "enderio"}','{"text": "soul_binder"}','{"text": ""}']}}
setblock 167 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Seelenbinder"}','{"text": ""}','{"text": ""}']}}
fill 175 64 218 175 79 231 minecraft:light_gray_concrete
setblock 169 64 223 enderio:soul_binder[facing=south,powered=true]
setblock 171 64 223 minecraft:smooth_stone_slab
summon item_display 171.5 64.95 223.5 {item:{id:"enderio:soul_vial",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 176 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.4"}','{"text": "enderio"}','{"text": "vacuum_chest"}','{"text": ""}']}}
setblock 177 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Vakuumkiste auf"}','{"text": ""}','{"text": ""}']}}
fill 185 64 218 185 79 231 minecraft:light_gray_concrete
setblock 180 64 223 enderio:vacuum_chest
summon item 178.5 64.2 224.5 {Item:{id:"minecraft:rotten_flesh",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 182.5 64.2 224.5 {Item:{id:"minecraft:bone",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 179.5 64.2 225.5 {Item:{id:"minecraft:gunpowder",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 181.5 64.2 222.5 {Item:{id:"minecraft:string",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 186 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.5"}','{"text": "enderio"}','{"text": "enchanter"}','{"text": ""}']}}
setblock 187 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Verzauberer"}','{"text": ""}','{"text": ""}']}}
fill 195 64 218 195 79 231 minecraft:light_gray_concrete
setblock 190 64 223 enderio:enchanter[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
