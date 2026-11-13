# 084 logistics/menril, programmer, xnet_connectors
#area 126 233 166 258
fill 126 64 233 166 91 258 minecraft:air
fill 126 60 233 166 62 258 minecraft:stone
fill 126 63 233 166 63 258 minecraft:light_gray_concrete
fill 130 64 239 166 79 239 minecraft:light_gray_concrete
fill 130 64 239 130 79 252 minecraft:light_gray_concrete
setblock 131 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084.1"}','{"text": "logistics"}','{"text": "menril"}','{"text": ""}']}}
setblock 132 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Press"}','{"text": "Menril-Harz"}','{"text": ""}','{"text": ""}']}}
fill 140 64 239 140 79 252 minecraft:light_gray_concrete
fill 133 64 243 133 66 243 integrateddynamics:menril_log[axis=y]
setblock 135 64 244 integrateddynamics:squeezer[axis=x,height=1]
setblock 136 64 244 integrateddynamics:drying_basin
setblock 141 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084.2"}','{"text": "logistics"}','{"text": "programmer"}','{"text": ""}']}}
setblock 142 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schreib Karten"}','{"text": "im Logic"}','{"text": "Programmer"}','{"text": ""}']}}
fill 150 64 239 150 79 252 minecraft:light_gray_concrete
setblock 144 64 244 integrateddynamics:logic_programmer[facing=south]
setblock 146 64 244 integrateddynamics:variablestore[facing=south]
setblock 151 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084.3"}','{"text": "logistics"}','{"text": "xnet_connectors"}','{"text": ""}']}}
setblock 152 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Connectors"}','{"text": "und Kabel"}','{"text": ""}','{"text": ""}']}}
fill 161 64 239 161 79 252 minecraft:light_gray_concrete
setblock 153 64 244 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 159 64 244 minecraft:furnace[facing=south,lit=false]
setblock 156 64 245 xnet:controller[facing=south,error=false]
kw testworld use 154 63 244 up xnet:connector_blue
kw testworld use 158 63 244 up xnet:connector_blue
kw testworld use 155 63 244 up xnet:netcable_blue
kw testworld use 156 63 244 up xnet:netcable_blue
kw testworld use 157 63 244 up xnet:netcable_blue
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
