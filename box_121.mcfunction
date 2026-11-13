# 121 logistics/menril, programmer, xnet_connectors, laser_node
#area 154 254 204 279
fill 154 64 254 198 91 279 minecraft:air
fill 199 64 254 204 91 279 minecraft:air
fill 154 60 254 204 62 279 minecraft:stone
fill 154 63 254 204 63 279 minecraft:light_gray_concrete
fill 158 64 260 204 79 260 minecraft:light_gray_concrete
fill 158 64 260 158 79 273 minecraft:light_gray_concrete
setblock 159 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "121.1"}','{"text": "logistics"}','{"text": "menril"}','{"text": ""}']}}
setblock 160 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Press"}','{"text": "Menril-Harz"}','{"text": ""}','{"text": ""}']}}
fill 168 64 260 168 79 273 minecraft:light_gray_concrete
fill 161 64 264 161 66 264 integrateddynamics:menril_log[axis=y]
setblock 163 64 265 integrateddynamics:squeezer[axis=x,height=1]
setblock 164 64 265 integrateddynamics:drying_basin
setblock 169 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "121.2"}','{"text": "logistics"}','{"text": "programmer"}','{"text": ""}']}}
setblock 170 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schreib Karten"}','{"text": "im Logic"}','{"text": "Programmer"}','{"text": ""}']}}
fill 178 64 260 178 79 273 minecraft:light_gray_concrete
setblock 172 64 265 integrateddynamics:logic_programmer[facing=south]
setblock 174 64 265 integrateddynamics:variablestore[facing=south]
setblock 179 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "121.3"}','{"text": "logistics"}','{"text": "xnet_connectors"}','{"text": ""}']}}
setblock 180 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Connectors"}','{"text": "und Kabel"}','{"text": ""}','{"text": ""}']}}
fill 189 64 260 189 79 273 minecraft:light_gray_concrete
setblock 181 64 265 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 187 64 265 minecraft:furnace[facing=south,lit=false]
setblock 184 64 266 xnet:controller[facing=south,error=false]
kw testworld use 182 63 265 up xnet:connector_blue
kw testworld use 186 63 265 up xnet:connector_blue
kw testworld use 183 63 265 up xnet:netcable_blue
kw testworld use 184 63 265 up xnet:netcable_blue
kw testworld use 185 63 265 up xnet:netcable_blue
setblock 190 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "121.4"}','{"text": "logistics"}','{"text": "laser_node"}','{"text": ""}']}}
setblock 191 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Laser Nodes"}','{"text": ""}','{"text": ""}']}}
fill 199 64 260 199 79 273 minecraft:light_gray_concrete
setblock 192 64 265 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 192 65 265 laserio:laser_node
setblock 196 64 265 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 196 65 265 laserio:laser_node
kw testworld use 192 65 265 south laserio:laser_wrench
kw testworld use 196 65 265 south laserio:laser_wrench
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
