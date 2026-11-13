# 091 enderio/smelter, cap_bank, soul_binder, vacuum_chest, enchanter
#area 140 231 200 256
fill 140 64 231 184 91 256 minecraft:air
fill 185 64 231 200 91 256 minecraft:air
fill 140 60 231 200 62 256 minecraft:stone
fill 140 63 231 200 63 256 minecraft:light_gray_concrete
fill 144 64 237 200 79 237 minecraft:light_gray_concrete
fill 144 64 237 144 79 250 minecraft:light_gray_concrete
setblock 145 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.1"}','{"text": "enderio"}','{"text": "smelter"}','{"text": ""}']}}
setblock 146 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmelze"}','{"text": ""}','{"text": ""}']}}
fill 155 64 237 155 79 250 minecraft:light_gray_concrete
setblock 148 64 242 enderio:alloy_smelter[facing=south,powered=true]
setblock 150 64 242 enderio:sag_mill[facing=south,powered=true]
setblock 152 64 242 minecraft:smooth_stone_slab
summon item_display 152.5 64.95 242.5 {item:{id:"enderio:basic_capacitor",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 156 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.2"}','{"text": "enderio"}','{"text": "cap_bank"}','{"text": ""}']}}
setblock 157 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Kondensatorbank"}','{"text": ""}','{"text": ""}']}}
fill 165 64 237 165 79 250 minecraft:light_gray_concrete
fill 159 64 242 161 66 242 enderio:basic_capacitor_bank
setblock 166 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.3"}','{"text": "enderio"}','{"text": "soul_binder"}','{"text": ""}']}}
setblock 167 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Seelenbinder"}','{"text": ""}','{"text": ""}']}}
fill 175 64 237 175 79 250 minecraft:light_gray_concrete
setblock 169 64 242 enderio:soul_binder[facing=south,powered=true]
setblock 171 64 242 minecraft:smooth_stone_slab
summon item_display 171.5 64.95 242.5 {item:{id:"enderio:soul_vial",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 176 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.4"}','{"text": "enderio"}','{"text": "vacuum_chest"}','{"text": ""}']}}
setblock 177 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Vakuumkiste auf"}','{"text": ""}','{"text": ""}']}}
fill 185 64 237 185 79 250 minecraft:light_gray_concrete
setblock 180 64 242 enderio:vacuum_chest
summon item 178.5 64.2 243.5 {Item:{id:"minecraft:rotten_flesh",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 182.5 64.2 243.5 {Item:{id:"minecraft:bone",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 179.5 64.2 244.5 {Item:{id:"minecraft:gunpowder",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 181.5 64.2 241.5 {Item:{id:"minecraft:string",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 186 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.5"}','{"text": "enderio"}','{"text": "enchanter"}','{"text": ""}']}}
setblock 187 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Verzauberer"}','{"text": ""}','{"text": ""}']}}
fill 195 64 237 195 79 250 minecraft:light_gray_concrete
setblock 190 64 242 enderio:enchanter[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
