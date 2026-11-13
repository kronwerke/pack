# 080 immersive/connectors, thermoelectric
#area 101 177 132 202
fill 101 64 177 132 91 202 minecraft:air
fill 101 60 177 132 62 202 minecraft:stone
fill 101 63 177 132 63 202 minecraft:light_gray_concrete
fill 105 64 183 132 79 183 minecraft:light_gray_concrete
fill 105 64 183 105 79 196 minecraft:light_gray_concrete
setblock 106 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "080.1"}','{"text": "immersive"}','{"text": "connectors"}','{"text": ""}']}}
setblock 107 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "LV wires on"}','{"text": "posts, the"}','{"text": "accumulator,"}','{"text": "the generator"}']}}
setblock 108 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "between magma"}','{"text": "and blue ice, a"}','{"text": "transformer"}','{"text": "with LV and MV"}']}}
fill 117 64 183 117 79 196 minecraft:light_gray_concrete
setblock 108 64 188 immersiveengineering:capacitor_lv
setblock 114 64 188 immersiveengineering:capacitor_lv
fill 111 64 188 111 66 188 immersiveengineering:treated_fence
kw testworld use 108 64 188 up immersiveengineering:connector_lv
kw testworld use 114 64 188 up immersiveengineering:connector_lv
kw testworld use 111 66 188 up immersiveengineering:connector_lv_relay
kw testworld use 108 65 188 south immersiveengineering:wirecoil_copper
kw testworld use 111 67 188 south immersiveengineering:wirecoil_copper
kw testworld use 111 67 188 south immersiveengineering:wirecoil_copper
kw testworld use 114 65 188 south immersiveengineering:wirecoil_copper
setblock 118 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "080.2"}','{"text": "immersive"}','{"text": "thermoelectric"}','{"text": ""}']}}
setblock 119 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermoelektrischen"}','{"text": "Generator"}','{"text": ""}']}}
fill 127 64 183 127 79 196 minecraft:light_gray_concrete
setblock 121 64 188 minecraft:magma_block
setblock 122 64 188 immersiveengineering:thermoelectric_generator
setblock 123 64 188 minecraft:blue_ice
kw testworld use 122 64 188 up immersiveengineering:connector_lv
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
