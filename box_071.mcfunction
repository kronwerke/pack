# 071 immersive/connectors, capacitor, thermoelectric
#area 117 158 160 183
fill 117 64 158 160 91 183 minecraft:air
fill 117 60 158 160 62 183 minecraft:stone
fill 117 63 158 160 63 183 minecraft:light_gray_concrete
fill 121 64 164 160 79 164 minecraft:light_gray_concrete
fill 121 64 164 121 79 177 minecraft:light_gray_concrete
setblock 122 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.1"}','{"text": "immersive"}','{"text": "connectors"}','{"text": ""}']}}
setblock 123 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "LV wires on"}','{"text": "posts, the"}','{"text": "accumulator,"}','{"text": "the generator"}']}}
setblock 124 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "between magma"}','{"text": "and blue ice, a"}','{"text": "transformer"}','{"text": "with LV and MV"}']}}
fill 133 64 164 133 79 177 minecraft:light_gray_concrete
setblock 124 64 169 immersiveengineering:capacitor_lv
setblock 130 64 169 immersiveengineering:capacitor_lv
fill 127 64 169 127 66 169 immersiveengineering:treated_fence
kw testworld use 124 64 169 up immersiveengineering:connector_lv
kw testworld use 130 64 169 up immersiveengineering:connector_lv
kw testworld use 127 66 169 up immersiveengineering:connector_lv_relay
kw testworld use 124 65 169 south immersiveengineering:wirecoil_copper
kw testworld use 127 67 169 south immersiveengineering:wirecoil_copper
kw testworld use 127 67 169 south immersiveengineering:wirecoil_copper
kw testworld use 130 65 169 south immersiveengineering:wirecoil_copper
setblock 134 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.2"}','{"text": "immersive"}','{"text": "capacitor"}','{"text": ""}']}}
setblock 135 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "LV-Kondensator"}','{"text": ""}','{"text": ""}']}}
fill 145 64 164 145 79 177 minecraft:light_gray_concrete
setblock 136 64 169 immersiveengineering:capacitor_lv
setblock 142 64 169 immersiveengineering:capacitor_lv
fill 139 64 169 139 66 169 immersiveengineering:treated_fence
kw testworld use 136 64 169 up immersiveengineering:connector_lv
kw testworld use 142 64 169 up immersiveengineering:connector_lv
kw testworld use 139 66 169 up immersiveengineering:connector_lv_relay
kw testworld use 136 65 169 south immersiveengineering:wirecoil_copper
kw testworld use 139 67 169 south immersiveengineering:wirecoil_copper
kw testworld use 139 67 169 south immersiveengineering:wirecoil_copper
kw testworld use 142 65 169 south immersiveengineering:wirecoil_copper
setblock 146 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.3"}','{"text": "immersive"}','{"text": "thermoelectric"}','{"text": ""}']}}
setblock 147 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermoelektrischen"}','{"text": "Generator"}','{"text": ""}']}}
fill 155 64 164 155 79 177 minecraft:light_gray_concrete
setblock 149 64 169 minecraft:magma_block
setblock 150 64 169 immersiveengineering:thermoelectric_generator
setblock 151 64 169 minecraft:blue_ice
kw testworld use 150 64 169 up immersiveengineering:connector_lv
