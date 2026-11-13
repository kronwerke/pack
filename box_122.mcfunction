# 122 immersive/connectors, thermoelectric, transformer
#area 132 211 173 236
fill 132 64 211 173 91 236 minecraft:air
fill 132 60 211 173 62 236 minecraft:stone
fill 132 63 211 173 63 236 minecraft:light_gray_concrete
fill 136 64 217 173 79 217 minecraft:light_gray_concrete
fill 136 64 217 136 79 230 minecraft:light_gray_concrete
setblock 137 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.1"}','{"text": "immersive"}','{"text": "connectors"}','{"text": ""}']}}
setblock 138 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "LV wires on"}','{"text": "posts, the"}','{"text": "accumulator,"}','{"text": "the generator"}']}}
setblock 139 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "between magma"}','{"text": "and blue ice, a"}','{"text": "transformer"}','{"text": "with LV and MV"}']}}
fill 148 64 217 148 79 230 minecraft:light_gray_concrete
setblock 139 64 222 immersiveengineering:capacitor_lv
setblock 145 64 222 immersiveengineering:capacitor_lv
fill 142 64 222 142 66 222 immersiveengineering:treated_fence
kw testworld use 139 64 222 up immersiveengineering:connector_lv
kw testworld use 145 64 222 up immersiveengineering:connector_lv
kw testworld use 142 66 222 up immersiveengineering:connector_lv_relay
kw testworld use 139 65 222 south immersiveengineering:wirecoil_copper
kw testworld use 142 67 222 south immersiveengineering:wirecoil_copper
kw testworld use 142 67 222 south immersiveengineering:wirecoil_copper
kw testworld use 145 65 222 south immersiveengineering:wirecoil_copper
setblock 149 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.2"}','{"text": "immersive"}','{"text": "thermoelectric"}','{"text": ""}']}}
setblock 150 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermoelektrischen"}','{"text": "Generator"}','{"text": ""}']}}
fill 158 64 217 158 79 230 minecraft:light_gray_concrete
setblock 152 64 222 minecraft:magma_block
setblock 153 64 222 immersiveengineering:thermoelectric_generator
setblock 154 64 222 minecraft:blue_ice
kw testworld use 153 64 222 up immersiveengineering:connector_lv
setblock 159 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.3"}','{"text": "immersive"}','{"text": "transformer"}','{"text": ""}']}}
setblock 160 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Trafo"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 168 64 217 168 79 230 minecraft:light_gray_concrete
setblock 161 64 222 immersiveengineering:capacitor_lv
kw testworld use 163 63 222 up immersiveengineering:transformer
setblock 165 64 222 immersiveengineering:capacitor_mv
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
