# 139 logistics/menril, programmer, xnet_connectors, laser_node, mg_gadget
#area 164 290 224 315
fill 164 64 290 208 91 315 minecraft:air
fill 209 64 290 224 91 315 minecraft:air
fill 164 60 290 224 62 315 minecraft:stone
fill 164 63 290 224 63 315 minecraft:light_gray_concrete
fill 168 64 296 224 79 296 minecraft:light_gray_concrete
fill 168 64 296 168 79 309 minecraft:light_gray_concrete
setblock 169 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "139.1"}','{"text": "logistics"}','{"text": "menril"}','{"text": ""}']}}
setblock 170 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Press"}','{"text": "Menril-Harz"}','{"text": ""}','{"text": ""}']}}
fill 178 64 296 178 79 309 minecraft:light_gray_concrete
fill 171 64 300 171 66 300 integrateddynamics:menril_log[axis=y]
setblock 173 64 301 integrateddynamics:squeezer[axis=x,height=1]
setblock 174 64 301 integrateddynamics:drying_basin
setblock 179 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "139.2"}','{"text": "logistics"}','{"text": "programmer"}','{"text": ""}']}}
setblock 180 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schreib Karten"}','{"text": "im Logic"}','{"text": "Programmer"}','{"text": ""}']}}
fill 188 64 296 188 79 309 minecraft:light_gray_concrete
setblock 182 64 301 integrateddynamics:logic_programmer[facing=south]
setblock 184 64 301 integrateddynamics:variablestore[facing=south]
setblock 189 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "139.3"}','{"text": "logistics"}','{"text": "xnet_connectors"}','{"text": ""}']}}
setblock 190 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Connectors"}','{"text": "und Kabel"}','{"text": ""}','{"text": ""}']}}
fill 199 64 296 199 79 309 minecraft:light_gray_concrete
setblock 191 64 301 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 197 64 301 minecraft:furnace[facing=south,lit=false]
setblock 194 64 302 xnet:controller[facing=south,error=false]
kw testworld use 192 63 301 up xnet:connector_blue
kw testworld use 196 63 301 up xnet:connector_blue
kw testworld use 193 63 301 up xnet:netcable_blue
kw testworld use 194 63 301 up xnet:netcable_blue
kw testworld use 195 63 301 up xnet:netcable_blue
setblock 200 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "139.4"}','{"text": "logistics"}','{"text": "laser_node"}','{"text": ""}']}}
setblock 201 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Laser Nodes"}','{"text": ""}','{"text": ""}']}}
fill 209 64 296 209 79 309 minecraft:light_gray_concrete
setblock 202 64 301 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 202 65 301 laserio:laser_node
setblock 206 64 301 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 206 65 301 laserio:laser_node
kw testworld use 202 65 301 south laserio:laser_wrench
kw testworld use 206 65 301 south laserio:laser_wrench
setblock 210 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "139.5"}','{"text": "logistics"}','{"text": "mg_gadget"}','{"text": ""}']}}
setblock 211 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Mining Gadget"}','{"text": ""}','{"text": ""}']}}
fill 219 64 296 219 79 309 minecraft:light_gray_concrete
setblock 214 64 301 minecraft:smooth_stone_slab
summon item_display 214.5 64.95 301.5 {item:{id:"mininggadgets:mininggadget_simple",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
