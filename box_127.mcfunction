# 127 immersive/connectors, thermoelectric, transformer
#area 157 217 198 242
fill 157 64 217 198 91 242 minecraft:air
fill 157 60 217 198 62 242 minecraft:stone
fill 157 63 217 198 63 242 minecraft:light_gray_concrete
fill 161 64 223 198 79 223 minecraft:light_gray_concrete
fill 161 64 223 161 79 236 minecraft:light_gray_concrete
setblock 162 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127.1"}','{"text": "immersive"}','{"text": "connectors"}','{"text": ""}']}}
setblock 163 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "LV wires on"}','{"text": "posts, the"}','{"text": "accumulator,"}','{"text": "the generator"}']}}
setblock 164 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "between magma"}','{"text": "and blue ice, a"}','{"text": "transformer"}','{"text": "with LV and MV"}']}}
fill 173 64 223 173 79 236 minecraft:light_gray_concrete
setblock 164 64 228 immersiveengineering:capacitor_lv
setblock 170 64 228 immersiveengineering:capacitor_lv
fill 167 64 228 167 66 228 immersiveengineering:treated_fence
kw testworld use 164 64 228 up immersiveengineering:connector_lv
kw testworld use 170 64 228 up immersiveengineering:connector_lv
kw testworld use 167 66 228 up immersiveengineering:connector_lv_relay
kw testworld use 164 65 228 south immersiveengineering:wirecoil_copper
kw testworld use 167 67 228 south immersiveengineering:wirecoil_copper
kw testworld use 167 67 228 south immersiveengineering:wirecoil_copper
kw testworld use 170 65 228 south immersiveengineering:wirecoil_copper
setblock 174 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127.2"}','{"text": "immersive"}','{"text": "thermoelectric"}','{"text": ""}']}}
setblock 175 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermoelektrischen"}','{"text": "Generator"}','{"text": ""}']}}
fill 183 64 223 183 79 236 minecraft:light_gray_concrete
setblock 177 64 228 minecraft:magma_block
setblock 178 64 228 immersiveengineering:thermoelectric_generator
setblock 179 64 228 minecraft:blue_ice
kw testworld use 178 64 228 up immersiveengineering:connector_lv
setblock 184 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127.3"}','{"text": "immersive"}','{"text": "transformer"}','{"text": ""}']}}
setblock 185 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Trafo"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 193 64 223 193 79 236 minecraft:light_gray_concrete
setblock 186 64 228 immersiveengineering:capacitor_lv
kw testworld use 188 63 228 up immersiveengineering:transformer
setblock 190 64 228 immersiveengineering:capacitor_mv
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
