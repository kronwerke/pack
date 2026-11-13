# 105 logistics/menril, programmer, xnet_connectors, laser_node
#area 137 254 187 279
fill 137 64 254 181 91 279 minecraft:air
fill 182 64 254 187 91 279 minecraft:air
fill 137 60 254 187 62 279 minecraft:stone
fill 137 63 254 187 63 279 minecraft:light_gray_concrete
fill 141 64 260 187 79 260 minecraft:light_gray_concrete
fill 141 64 260 141 79 273 minecraft:light_gray_concrete
setblock 142 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "105.1"}','{"text": "logistics"}','{"text": "menril"}','{"text": ""}']}}
setblock 143 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Press"}','{"text": "Menril-Harz"}','{"text": ""}','{"text": ""}']}}
fill 151 64 260 151 79 273 minecraft:light_gray_concrete
fill 144 64 264 144 66 264 integrateddynamics:menril_log[axis=y]
setblock 146 64 265 integrateddynamics:squeezer[axis=x,height=1]
setblock 147 64 265 integrateddynamics:drying_basin
setblock 152 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "105.2"}','{"text": "logistics"}','{"text": "programmer"}','{"text": ""}']}}
setblock 153 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schreib Karten"}','{"text": "im Logic"}','{"text": "Programmer"}','{"text": ""}']}}
fill 161 64 260 161 79 273 minecraft:light_gray_concrete
setblock 155 64 265 integrateddynamics:logic_programmer[facing=south]
setblock 157 64 265 integrateddynamics:variablestore[facing=south]
setblock 162 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "105.3"}','{"text": "logistics"}','{"text": "xnet_connectors"}','{"text": ""}']}}
setblock 163 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Connectors"}','{"text": "und Kabel"}','{"text": ""}','{"text": ""}']}}
fill 172 64 260 172 79 273 minecraft:light_gray_concrete
setblock 164 64 265 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 170 64 265 minecraft:furnace[facing=south,lit=false]
setblock 167 64 266 xnet:controller[facing=south,error=false]
kw testworld use 165 63 265 up xnet:connector_blue
kw testworld use 169 63 265 up xnet:connector_blue
kw testworld use 166 63 265 up xnet:netcable_blue
kw testworld use 167 63 265 up xnet:netcable_blue
kw testworld use 168 63 265 up xnet:netcable_blue
setblock 173 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "105.4"}','{"text": "logistics"}','{"text": "laser_node"}','{"text": ""}']}}
setblock 174 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Laser Nodes"}','{"text": ""}','{"text": ""}']}}
fill 182 64 260 182 79 273 minecraft:light_gray_concrete
setblock 175 64 265 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 175 65 265 laserio:laser_node
setblock 179 64 265 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 179 65 265 laserio:laser_node
kw testworld use 175 65 265 south laserio:laser_wrench
kw testworld use 179 65 265 south laserio:laser_wrench
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
