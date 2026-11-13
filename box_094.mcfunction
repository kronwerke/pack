# 094 logistics/menril, programmer, xnet_connectors
#area 126 252 166 277
fill 126 64 252 166 91 277 minecraft:air
fill 126 60 252 166 62 277 minecraft:stone
fill 126 63 252 166 63 277 minecraft:light_gray_concrete
fill 130 64 258 166 79 258 minecraft:light_gray_concrete
fill 130 64 258 130 79 271 minecraft:light_gray_concrete
setblock 131 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "094.1"}','{"text": "logistics"}','{"text": "menril"}','{"text": ""}']}}
setblock 132 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Press"}','{"text": "Menril-Harz"}','{"text": ""}','{"text": ""}']}}
fill 140 64 258 140 79 271 minecraft:light_gray_concrete
fill 133 64 262 133 66 262 integrateddynamics:menril_log[axis=y]
setblock 135 64 263 integrateddynamics:squeezer[axis=x,height=1]
setblock 136 64 263 integrateddynamics:drying_basin
setblock 141 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "094.2"}','{"text": "logistics"}','{"text": "programmer"}','{"text": ""}']}}
setblock 142 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schreib Karten"}','{"text": "im Logic"}','{"text": "Programmer"}','{"text": ""}']}}
fill 150 64 258 150 79 271 minecraft:light_gray_concrete
setblock 144 64 263 integrateddynamics:logic_programmer[facing=south]
setblock 146 64 263 integrateddynamics:variablestore[facing=south]
setblock 151 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "094.3"}','{"text": "logistics"}','{"text": "xnet_connectors"}','{"text": ""}']}}
setblock 152 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Connectors"}','{"text": "und Kabel"}','{"text": ""}','{"text": ""}']}}
fill 161 64 258 161 79 271 minecraft:light_gray_concrete
setblock 153 64 263 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 159 64 263 minecraft:furnace[facing=south,lit=false]
setblock 156 64 264 xnet:controller[facing=south,error=false]
kw testworld use 154 63 263 up xnet:connector_blue
kw testworld use 158 63 263 up xnet:connector_blue
kw testworld use 155 63 263 up xnet:netcable_blue
kw testworld use 156 63 263 up xnet:netcable_blue
kw testworld use 157 63 263 up xnet:netcable_blue
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
