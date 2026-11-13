# 144 logistics/menril, programmer, xnet_connectors, laser_node, mg_gadget
#area 164 296 224 321
fill 164 64 296 208 91 321 minecraft:air
fill 209 64 296 224 91 321 minecraft:air
fill 164 60 296 224 62 321 minecraft:stone
fill 164 63 296 224 63 321 minecraft:light_gray_concrete
fill 168 64 302 224 79 302 minecraft:light_gray_concrete
fill 168 64 302 168 79 315 minecraft:light_gray_concrete
setblock 169 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144.1"}','{"text": "logistics"}','{"text": "menril"}','{"text": ""}']}}
setblock 170 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Press"}','{"text": "Menril-Harz"}','{"text": ""}','{"text": ""}']}}
fill 178 64 302 178 79 315 minecraft:light_gray_concrete
fill 171 64 306 171 66 306 integrateddynamics:menril_log[axis=y]
setblock 173 64 307 integrateddynamics:squeezer[axis=x,height=1]
setblock 174 64 307 integrateddynamics:drying_basin
setblock 179 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144.2"}','{"text": "logistics"}','{"text": "programmer"}','{"text": ""}']}}
setblock 180 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schreib Karten"}','{"text": "im Logic"}','{"text": "Programmer"}','{"text": ""}']}}
fill 188 64 302 188 79 315 minecraft:light_gray_concrete
setblock 182 64 307 integrateddynamics:logic_programmer[facing=south]
setblock 184 64 307 integrateddynamics:variablestore[facing=south]
setblock 189 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144.3"}','{"text": "logistics"}','{"text": "xnet_connectors"}','{"text": ""}']}}
setblock 190 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Connectors"}','{"text": "und Kabel"}','{"text": ""}','{"text": ""}']}}
fill 199 64 302 199 79 315 minecraft:light_gray_concrete
setblock 191 64 307 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 197 64 307 minecraft:furnace[facing=south,lit=false]
setblock 194 64 308 xnet:controller[facing=south,error=false]
kw testworld use 192 63 307 up xnet:connector_blue
kw testworld use 196 63 307 up xnet:connector_blue
kw testworld use 193 63 307 up xnet:netcable_blue
kw testworld use 194 63 307 up xnet:netcable_blue
kw testworld use 195 63 307 up xnet:netcable_blue
setblock 200 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144.4"}','{"text": "logistics"}','{"text": "laser_node"}','{"text": ""}']}}
setblock 201 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Laser Nodes"}','{"text": ""}','{"text": ""}']}}
fill 209 64 302 209 79 315 minecraft:light_gray_concrete
setblock 202 64 307 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 202 65 307 laserio:laser_node
setblock 206 64 307 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 206 65 307 laserio:laser_node
kw testworld use 202 65 307 south laserio:laser_wrench
kw testworld use 206 65 307 south laserio:laser_wrench
setblock 210 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144.5"}','{"text": "logistics"}','{"text": "mg_gadget"}','{"text": ""}']}}
setblock 211 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Mining Gadget"}','{"text": ""}','{"text": ""}']}}
fill 219 64 302 219 79 315 minecraft:light_gray_concrete
setblock 214 64 307 minecraft:smooth_stone_slab
summon item_display 214.5 65.4 307.5 {item:{id:"mininggadgets:mininggadget_simple",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
