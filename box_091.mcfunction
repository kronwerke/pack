# 091 immersive/connectors, thermoelectric
#area 132 179 163 204
fill 132 64 179 163 91 204 minecraft:air
fill 132 60 179 163 62 204 minecraft:stone
fill 132 63 179 163 63 204 minecraft:light_gray_concrete
fill 136 64 185 163 79 185 minecraft:light_gray_concrete
fill 136 64 185 136 79 198 minecraft:light_gray_concrete
setblock 137 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.1"}','{"text": "immersive"}','{"text": "connectors"}','{"text": ""}']}}
setblock 138 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "LV wires on"}','{"text": "posts, the"}','{"text": "accumulator,"}','{"text": "the generator"}']}}
setblock 139 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "between magma"}','{"text": "and blue ice, a"}','{"text": "transformer"}','{"text": "with LV and MV"}']}}
fill 148 64 185 148 79 198 minecraft:light_gray_concrete
setblock 139 64 190 immersiveengineering:capacitor_lv
setblock 145 64 190 immersiveengineering:capacitor_lv
fill 142 64 190 142 66 190 immersiveengineering:treated_fence
kw testworld use 139 64 190 up immersiveengineering:connector_lv
kw testworld use 145 64 190 up immersiveengineering:connector_lv
kw testworld use 142 66 190 up immersiveengineering:connector_lv_relay
kw testworld use 139 65 190 south immersiveengineering:wirecoil_copper
kw testworld use 142 67 190 south immersiveengineering:wirecoil_copper
kw testworld use 142 67 190 south immersiveengineering:wirecoil_copper
kw testworld use 145 65 190 south immersiveengineering:wirecoil_copper
setblock 149 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.2"}','{"text": "immersive"}','{"text": "thermoelectric"}','{"text": ""}']}}
setblock 150 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermoelektrischen"}','{"text": "Generator"}','{"text": ""}']}}
fill 158 64 185 158 79 198 minecraft:light_gray_concrete
setblock 152 64 190 minecraft:magma_block
setblock 153 64 190 immersiveengineering:thermoelectric_generator
setblock 154 64 190 minecraft:blue_ice
kw testworld use 153 64 190 up immersiveengineering:connector_lv
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
