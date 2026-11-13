# 074 immersive/connectors, capacitor, thermoelectric
#area 117 177 160 202
fill 117 64 177 160 91 202 minecraft:air
fill 117 60 177 160 62 202 minecraft:stone
fill 117 63 177 160 63 202 minecraft:light_gray_concrete
fill 121 64 183 160 79 183 minecraft:light_gray_concrete
fill 121 64 183 121 79 196 minecraft:light_gray_concrete
setblock 122 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.1"}','{"text": "immersive"}','{"text": "connectors"}','{"text": ""}']}}
setblock 123 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "LV wires on"}','{"text": "posts, the"}','{"text": "accumulator,"}','{"text": "the generator"}']}}
setblock 124 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "between magma"}','{"text": "and blue ice, a"}','{"text": "transformer"}','{"text": "with LV and MV"}']}}
fill 133 64 183 133 79 196 minecraft:light_gray_concrete
setblock 124 64 188 immersiveengineering:capacitor_lv
setblock 130 64 188 immersiveengineering:capacitor_lv
fill 127 64 188 127 66 188 immersiveengineering:treated_fence
kw testworld use 124 64 188 up immersiveengineering:connector_lv
kw testworld use 130 64 188 up immersiveengineering:connector_lv
kw testworld use 127 66 188 up immersiveengineering:connector_lv_relay
kw testworld use 124 65 188 south immersiveengineering:wirecoil_copper
kw testworld use 127 67 188 south immersiveengineering:wirecoil_copper
kw testworld use 127 67 188 south immersiveengineering:wirecoil_copper
kw testworld use 130 65 188 south immersiveengineering:wirecoil_copper
setblock 134 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.2"}','{"text": "immersive"}','{"text": "capacitor"}','{"text": ""}']}}
setblock 135 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "LV-Kondensator"}','{"text": ""}','{"text": ""}']}}
fill 145 64 183 145 79 196 minecraft:light_gray_concrete
setblock 136 64 188 immersiveengineering:capacitor_lv
setblock 142 64 188 immersiveengineering:capacitor_lv
fill 139 64 188 139 66 188 immersiveengineering:treated_fence
kw testworld use 136 64 188 up immersiveengineering:connector_lv
kw testworld use 142 64 188 up immersiveengineering:connector_lv
kw testworld use 139 66 188 up immersiveengineering:connector_lv_relay
kw testworld use 136 65 188 south immersiveengineering:wirecoil_copper
kw testworld use 139 67 188 south immersiveengineering:wirecoil_copper
kw testworld use 139 67 188 south immersiveengineering:wirecoil_copper
kw testworld use 142 65 188 south immersiveengineering:wirecoil_copper
setblock 146 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.3"}','{"text": "immersive"}','{"text": "thermoelectric"}','{"text": ""}']}}
setblock 147 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermoelektrischen"}','{"text": "Generator"}','{"text": ""}']}}
fill 155 64 183 155 79 196 minecraft:light_gray_concrete
setblock 149 64 188 minecraft:magma_block
setblock 150 64 188 immersiveengineering:thermoelectric_generator
setblock 151 64 188 minecraft:blue_ice
kw testworld use 150 64 188 up immersiveengineering:connector_lv
