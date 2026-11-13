# 069 immersive/connectors, capacitor, thermoelectric
#area 115 158 158 183
fill 115 64 158 158 91 183 minecraft:air
fill 115 60 158 158 62 183 minecraft:stone
fill 115 63 158 158 63 183 minecraft:light_gray_concrete
fill 119 64 164 158 79 164 minecraft:light_gray_concrete
fill 119 64 164 119 79 177 minecraft:light_gray_concrete
setblock 120 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069.1"}','{"text": "immersive"}','{"text": "connectors"}','{"text": ""}']}}
setblock 121 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "LV wires on"}','{"text": "posts, the"}','{"text": "accumulator,"}','{"text": "the generator"}']}}
setblock 122 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "between magma"}','{"text": "and blue ice, a"}','{"text": "transformer"}','{"text": "with LV and MV"}']}}
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
setblock 132 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069.2"}','{"text": "immersive"}','{"text": "capacitor"}','{"text": ""}']}}
setblock 133 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "LV-Kondensator"}','{"text": ""}','{"text": ""}']}}
fill 143 64 164 143 79 177 minecraft:light_gray_concrete
setblock 134 64 169 immersiveengineering:capacitor_lv
setblock 140 64 169 immersiveengineering:capacitor_lv
fill 137 64 169 137 66 169 immersiveengineering:treated_fence
kw testworld use 134 64 169 up immersiveengineering:connector_lv
kw testworld use 140 64 169 up immersiveengineering:connector_lv
kw testworld use 137 66 169 up immersiveengineering:connector_lv_relay
kw testworld use 134 65 169 south immersiveengineering:wirecoil_copper
kw testworld use 137 67 169 south immersiveengineering:wirecoil_copper
kw testworld use 137 67 169 south immersiveengineering:wirecoil_copper
kw testworld use 140 65 169 south immersiveengineering:wirecoil_copper
setblock 144 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069.3"}','{"text": "immersive"}','{"text": "thermoelectric"}','{"text": ""}']}}
setblock 145 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermoelektrischen"}','{"text": "Generator"}','{"text": ""}']}}
fill 153 64 164 153 79 177 minecraft:light_gray_concrete
setblock 147 64 169 minecraft:magma_block
setblock 148 64 169 immersiveengineering:thermoelectric_generator
setblock 149 64 169 minecraft:blue_ice
kw testworld use 148 64 169 up immersiveengineering:connector_lv
