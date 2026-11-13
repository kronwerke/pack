# 054 immersive/connectors, capacitor, thermoelectric
#area 103 158 146 183
fill 103 64 158 146 91 183 minecraft:air
fill 103 60 158 146 62 183 minecraft:stone
fill 103 63 158 146 63 183 minecraft:light_gray_concrete
fill 107 64 164 146 79 164 minecraft:light_gray_concrete
fill 107 64 164 107 79 177 minecraft:light_gray_concrete
setblock 108 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054.1"}','{"text": "immersive"}','{"text": "connectors"}','{"text": ""}']}}
setblock 109 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "LV wires on"}','{"text": "posts, the"}','{"text": "accumulator,"}','{"text": "the generator"}']}}
setblock 110 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "between magma"}','{"text": "and blue ice, a"}','{"text": "transformer"}','{"text": "with LV and MV"}']}}
fill 119 64 164 119 79 177 minecraft:light_gray_concrete
setblock 110 64 169 immersiveengineering:capacitor_lv
setblock 116 64 169 immersiveengineering:capacitor_lv
fill 113 64 169 113 66 169 immersiveengineering:treated_fence
kw testworld use 110 64 169 up immersiveengineering:connector_lv
kw testworld use 116 64 169 up immersiveengineering:connector_lv
kw testworld use 113 66 169 up immersiveengineering:connector_lv_relay
kw testworld use 110 65 169 south immersiveengineering:wirecoil_copper
kw testworld use 113 67 169 south immersiveengineering:wirecoil_copper
kw testworld use 113 67 169 south immersiveengineering:wirecoil_copper
kw testworld use 116 65 169 south immersiveengineering:wirecoil_copper
setblock 120 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054.2"}','{"text": "immersive"}','{"text": "capacitor"}','{"text": ""}']}}
setblock 121 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "LV-Kondensator"}','{"text": ""}','{"text": ""}']}}
fill 131 64 164 131 79 177 minecraft:light_gray_concrete
setblock 122 64 169 immersiveengineering:capacitor_lv
setblock 128 64 169 immersiveengineering:capacitor_lv
fill 125 64 169 125 66 169 immersiveengineering:treated_fence
kw testworld use 122 64 169 up immersiveengineering:connector_lv
kw testworld use 128 64 169 up immersiveengineering:connector_lv
kw testworld use 125 66 169 up immersiveengineering:connector_lv_relay
kw testworld use 122 65 169 south immersiveengineering:wirecoil_copper
kw testworld use 125 67 169 south immersiveengineering:wirecoil_copper
kw testworld use 125 67 169 south immersiveengineering:wirecoil_copper
kw testworld use 128 65 169 south immersiveengineering:wirecoil_copper
setblock 132 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054.3"}','{"text": "immersive"}','{"text": "thermoelectric"}','{"text": ""}']}}
setblock 133 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermoelektrischen"}','{"text": "Generator"}','{"text": ""}']}}
fill 141 64 164 141 79 177 minecraft:light_gray_concrete
setblock 135 64 169 minecraft:magma_block
setblock 136 64 169 immersiveengineering:thermoelectric_generator
setblock 137 64 169 minecraft:blue_ice
kw testworld use 136 64 169 up immersiveengineering:connector_lv
