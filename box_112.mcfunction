# 112 immersive/connectors, thermoelectric, transformer
#area 132 181 173 206
fill 132 64 181 173 91 206 minecraft:air
fill 132 60 181 173 62 206 minecraft:stone
fill 132 63 181 173 63 206 minecraft:light_gray_concrete
fill 136 64 187 173 79 187 minecraft:light_gray_concrete
fill 136 64 187 136 79 200 minecraft:light_gray_concrete
setblock 137 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.1"}','{"text": "immersive"}','{"text": "connectors"}','{"text": ""}']}}
setblock 138 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "LV wires on"}','{"text": "posts, the"}','{"text": "accumulator,"}','{"text": "the generator"}']}}
setblock 139 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "between magma"}','{"text": "and blue ice, a"}','{"text": "transformer"}','{"text": "with LV and MV"}']}}
fill 148 64 187 148 79 200 minecraft:light_gray_concrete
setblock 139 64 192 immersiveengineering:capacitor_lv
setblock 145 64 192 immersiveengineering:capacitor_lv
fill 142 64 192 142 66 192 immersiveengineering:treated_fence
kw testworld use 139 64 192 up immersiveengineering:connector_lv
kw testworld use 145 64 192 up immersiveengineering:connector_lv
kw testworld use 142 66 192 up immersiveengineering:connector_lv_relay
kw testworld use 139 65 192 south immersiveengineering:wirecoil_copper
kw testworld use 142 67 192 south immersiveengineering:wirecoil_copper
kw testworld use 142 67 192 south immersiveengineering:wirecoil_copper
kw testworld use 145 65 192 south immersiveengineering:wirecoil_copper
setblock 149 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.2"}','{"text": "immersive"}','{"text": "thermoelectric"}','{"text": ""}']}}
setblock 150 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermoelektrischen"}','{"text": "Generator"}','{"text": ""}']}}
fill 158 64 187 158 79 200 minecraft:light_gray_concrete
setblock 152 64 192 minecraft:magma_block
setblock 153 64 192 immersiveengineering:thermoelectric_generator
setblock 154 64 192 minecraft:blue_ice
kw testworld use 153 64 192 up immersiveengineering:connector_lv
setblock 159 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.3"}','{"text": "immersive"}','{"text": "transformer"}','{"text": ""}']}}
setblock 160 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Trafo"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 168 64 187 168 79 200 minecraft:light_gray_concrete
setblock 161 64 192 immersiveengineering:capacitor_lv
kw testworld use 163 63 192 up immersiveengineering:transformer
setblock 165 64 192 immersiveengineering:capacitor_mv
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
