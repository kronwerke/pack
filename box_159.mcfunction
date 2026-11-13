# 159 logistics/menril, programmer, counter, xnet_connectors, laser_node, mg_gadget
#area 164 298 234 323
fill 164 64 298 208 91 323 minecraft:air
fill 209 64 298 234 91 323 minecraft:air
fill 164 60 298 234 62 323 minecraft:stone
fill 164 63 298 234 63 323 minecraft:light_gray_concrete
fill 168 64 304 234 79 304 minecraft:light_gray_concrete
fill 168 64 304 168 79 317 minecraft:light_gray_concrete
setblock 169 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.1"}','{"text": "logistics"}','{"text": "menril"}','{"text": ""}']}}
setblock 170 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Press"}','{"text": "Menril-Harz"}','{"text": ""}','{"text": ""}']}}
fill 178 64 304 178 79 317 minecraft:light_gray_concrete
fill 171 64 308 171 66 308 integrateddynamics:menril_log[axis=y]
setblock 173 64 309 integrateddynamics:squeezer[axis=x,height=1]
setblock 174 64 309 integrateddynamics:drying_basin
setblock 179 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.2"}','{"text": "logistics"}','{"text": "programmer"}','{"text": ""}']}}
setblock 180 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schreib Karten"}','{"text": "im Logic"}','{"text": "Programmer"}','{"text": ""}']}}
fill 188 64 304 188 79 317 minecraft:light_gray_concrete
setblock 182 64 309 integrateddynamics:logic_programmer[facing=south]
setblock 184 64 309 integrateddynamics:variablestore[facing=south]
setblock 189 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.3"}','{"text": "logistics"}','{"text": "counter"}','{"text": ""}']}}
setblock 190 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Stahlzähler"}','{"text": ""}','{"text": ""}']}}
fill 198 64 304 198 79 317 minecraft:light_gray_concrete
setblock 192 64 309 minecraft:smooth_stone_slab
summon item_display 192.5 64.95 309.5 {item:{id:"integrateddynamics:part_inventory_reader",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 194 64 309 minecraft:smooth_stone_slab
summon item_display 194.5 64.95 309.5 {item:{id:"mekanism:ingot_steel",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 199 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.4"}','{"text": "logistics"}','{"text": "xnet_connectors"}','{"text": ""}']}}
setblock 200 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Connectors"}','{"text": "und Kabel"}','{"text": ""}','{"text": ""}']}}
fill 209 64 304 209 79 317 minecraft:light_gray_concrete
setblock 201 64 309 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 207 64 309 minecraft:furnace[facing=south,lit=false]
setblock 204 64 310 xnet:controller[facing=south,error=false]
kw testworld use 202 63 309 up xnet:connector_blue
kw testworld use 206 63 309 up xnet:connector_blue
kw testworld use 203 63 309 up xnet:netcable_blue
kw testworld use 204 63 309 up xnet:netcable_blue
kw testworld use 205 63 309 up xnet:netcable_blue
setblock 210 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.5"}','{"text": "logistics"}','{"text": "laser_node"}','{"text": ""}']}}
setblock 211 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Laser Nodes"}','{"text": ""}','{"text": ""}']}}
fill 219 64 304 219 79 317 minecraft:light_gray_concrete
setblock 212 64 309 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 212 65 309 laserio:laser_node
setblock 216 64 309 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 216 65 309 laserio:laser_node
kw testworld use 212 65 309 south laserio:laser_wrench
kw testworld use 216 65 309 south laserio:laser_wrench
setblock 220 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.6"}','{"text": "logistics"}','{"text": "mg_gadget"}','{"text": ""}']}}
setblock 221 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Mining Gadget"}','{"text": ""}','{"text": ""}']}}
fill 229 64 304 229 79 317 minecraft:light_gray_concrete
setblock 224 64 309 minecraft:smooth_stone_slab
summon item_display 224.5 65.4 309.5 {item:{id:"mininggadgets:mininggadget_simple",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
