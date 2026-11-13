# 125 logistics/menril, programmer, xnet_connectors, laser_node
#area 154 256 204 281
fill 154 64 256 198 91 281 minecraft:air
fill 199 64 256 204 91 281 minecraft:air
fill 154 60 256 204 62 281 minecraft:stone
fill 154 63 256 204 63 281 minecraft:light_gray_concrete
fill 158 64 262 204 79 262 minecraft:light_gray_concrete
fill 158 64 262 158 79 275 minecraft:light_gray_concrete
setblock 159 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.1"}','{"text": "logistics"}','{"text": "menril"}','{"text": ""}']}}
setblock 160 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Press"}','{"text": "Menril-Harz"}','{"text": ""}','{"text": ""}']}}
fill 168 64 262 168 79 275 minecraft:light_gray_concrete
fill 161 64 266 161 66 266 integrateddynamics:menril_log[axis=y]
setblock 163 64 267 integrateddynamics:squeezer[axis=x,height=1]
setblock 164 64 267 integrateddynamics:drying_basin
setblock 169 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.2"}','{"text": "logistics"}','{"text": "programmer"}','{"text": ""}']}}
setblock 170 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schreib Karten"}','{"text": "im Logic"}','{"text": "Programmer"}','{"text": ""}']}}
fill 178 64 262 178 79 275 minecraft:light_gray_concrete
setblock 172 64 267 integrateddynamics:logic_programmer[facing=south]
setblock 174 64 267 integrateddynamics:variablestore[facing=south]
setblock 179 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.3"}','{"text": "logistics"}','{"text": "xnet_connectors"}','{"text": ""}']}}
setblock 180 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Connectors"}','{"text": "und Kabel"}','{"text": ""}','{"text": ""}']}}
fill 189 64 262 189 79 275 minecraft:light_gray_concrete
setblock 181 64 267 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 187 64 267 minecraft:furnace[facing=south,lit=false]
setblock 184 64 268 xnet:controller[facing=south,error=false]
kw testworld use 182 63 267 up xnet:connector_blue
kw testworld use 186 63 267 up xnet:connector_blue
kw testworld use 183 63 267 up xnet:netcable_blue
kw testworld use 184 63 267 up xnet:netcable_blue
kw testworld use 185 63 267 up xnet:netcable_blue
setblock 190 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.4"}','{"text": "logistics"}','{"text": "laser_node"}','{"text": ""}']}}
setblock 191 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Laser Nodes"}','{"text": ""}','{"text": ""}']}}
fill 199 64 262 199 79 275 minecraft:light_gray_concrete
setblock 192 64 267 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 192 65 267 laserio:laser_node
setblock 196 64 267 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 196 65 267 laserio:laser_node
kw testworld use 192 65 267 south laserio:laser_wrench
kw testworld use 196 65 267 south laserio:laser_wrench
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
