# 107 immersive/connectors, thermoelectric, transformer
#area 132 179 173 204
fill 132 64 179 173 91 204 minecraft:air
fill 132 60 179 173 62 204 minecraft:stone
fill 132 63 179 173 63 204 minecraft:light_gray_concrete
fill 136 64 185 173 79 185 minecraft:light_gray_concrete
fill 136 64 185 136 79 198 minecraft:light_gray_concrete
setblock 137 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "107.1"}','{"text": "immersive"}','{"text": "connectors"}','{"text": ""}']}}
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
setblock 149 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "107.2"}','{"text": "immersive"}','{"text": "thermoelectric"}','{"text": ""}']}}
setblock 150 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermoelektrischen"}','{"text": "Generator"}','{"text": ""}']}}
fill 158 64 185 158 79 198 minecraft:light_gray_concrete
setblock 152 64 190 minecraft:magma_block
setblock 153 64 190 immersiveengineering:thermoelectric_generator
setblock 154 64 190 minecraft:blue_ice
kw testworld use 153 64 190 up immersiveengineering:connector_lv
setblock 159 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "107.3"}','{"text": "immersive"}','{"text": "transformer"}','{"text": ""}']}}
setblock 160 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Trafo"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 168 64 185 168 79 198 minecraft:light_gray_concrete
setblock 161 64 190 immersiveengineering:capacitor_lv
kw testworld use 163 63 190 up immersiveengineering:transformer
setblock 165 64 190 immersiveengineering:capacitor_mv
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
