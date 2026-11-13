# 123 immersive/connectors, thermoelectric, transformer
#area 132 215 173 240
fill 132 64 215 173 91 240 minecraft:air
fill 132 60 215 173 62 240 minecraft:stone
fill 132 63 215 173 63 240 minecraft:light_gray_concrete
fill 136 64 221 173 79 221 minecraft:light_gray_concrete
fill 136 64 221 136 79 234 minecraft:light_gray_concrete
setblock 137 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "123.1"}','{"text": "immersive"}','{"text": "connectors"}','{"text": ""}']}}
setblock 138 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "LV wires on"}','{"text": "posts, the"}','{"text": "accumulator,"}','{"text": "the generator"}']}}
setblock 139 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "between magma"}','{"text": "and blue ice, a"}','{"text": "transformer"}','{"text": "with LV and MV"}']}}
fill 148 64 221 148 79 234 minecraft:light_gray_concrete
setblock 139 64 226 immersiveengineering:capacitor_lv
setblock 145 64 226 immersiveengineering:capacitor_lv
fill 142 64 226 142 66 226 immersiveengineering:treated_fence
kw testworld use 139 64 226 up immersiveengineering:connector_lv
kw testworld use 145 64 226 up immersiveengineering:connector_lv
kw testworld use 142 66 226 up immersiveengineering:connector_lv_relay
kw testworld use 139 65 226 south immersiveengineering:wirecoil_copper
kw testworld use 142 67 226 south immersiveengineering:wirecoil_copper
kw testworld use 142 67 226 south immersiveengineering:wirecoil_copper
kw testworld use 145 65 226 south immersiveengineering:wirecoil_copper
setblock 149 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "123.2"}','{"text": "immersive"}','{"text": "thermoelectric"}','{"text": ""}']}}
setblock 150 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermoelektrischen"}','{"text": "Generator"}','{"text": ""}']}}
fill 158 64 221 158 79 234 minecraft:light_gray_concrete
setblock 152 64 226 minecraft:magma_block
setblock 153 64 226 immersiveengineering:thermoelectric_generator
setblock 154 64 226 minecraft:blue_ice
kw testworld use 153 64 226 up immersiveengineering:connector_lv
setblock 159 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "123.3"}','{"text": "immersive"}','{"text": "transformer"}','{"text": ""}']}}
setblock 160 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Trafo"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 168 64 221 168 79 234 minecraft:light_gray_concrete
setblock 161 64 226 immersiveengineering:capacitor_lv
kw testworld use 163 63 226 up immersiveengineering:transformer
setblock 165 64 226 immersiveengineering:capacitor_mv
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
