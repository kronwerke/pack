# 142 immersive/connectors, thermoelectric, transformer
#area 157 219 198 244
fill 157 64 219 198 91 244 minecraft:air
fill 157 60 219 198 62 244 minecraft:stone
fill 157 63 219 198 63 244 minecraft:light_gray_concrete
fill 161 64 225 198 79 225 minecraft:light_gray_concrete
fill 161 64 225 161 79 238 minecraft:light_gray_concrete
setblock 162 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.1"}','{"text": "immersive"}','{"text": "connectors"}','{"text": ""}']}}
setblock 163 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "LV wires on"}','{"text": "posts, the"}','{"text": "accumulator,"}','{"text": "the generator"}']}}
setblock 164 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "between magma"}','{"text": "and blue ice, a"}','{"text": "transformer"}','{"text": "with LV and MV"}']}}
fill 173 64 225 173 79 238 minecraft:light_gray_concrete
setblock 164 64 230 immersiveengineering:capacitor_lv
setblock 170 64 230 immersiveengineering:capacitor_lv
fill 167 64 230 167 66 230 immersiveengineering:treated_fence
kw testworld use 164 64 230 up immersiveengineering:connector_lv
kw testworld use 170 64 230 up immersiveengineering:connector_lv
kw testworld use 167 66 230 up immersiveengineering:connector_lv_relay
kw testworld use 164 65 230 south immersiveengineering:wirecoil_copper
kw testworld use 167 67 230 south immersiveengineering:wirecoil_copper
kw testworld use 167 67 230 south immersiveengineering:wirecoil_copper
kw testworld use 170 65 230 south immersiveengineering:wirecoil_copper
setblock 174 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.2"}','{"text": "immersive"}','{"text": "thermoelectric"}','{"text": ""}']}}
setblock 175 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermoelektrischen"}','{"text": "Generator"}','{"text": ""}']}}
fill 183 64 225 183 79 238 minecraft:light_gray_concrete
setblock 177 64 230 minecraft:magma_block
setblock 178 64 230 immersiveengineering:thermoelectric_generator
setblock 179 64 230 minecraft:blue_ice
kw testworld use 178 64 230 up immersiveengineering:connector_lv
setblock 184 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.3"}','{"text": "immersive"}','{"text": "transformer"}','{"text": ""}']}}
setblock 185 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Trafo"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 193 64 225 193 79 238 minecraft:light_gray_concrete
setblock 186 64 230 immersiveengineering:capacitor_lv
kw testworld use 188 63 230 up immersiveengineering:transformer
setblock 190 64 230 immersiveengineering:capacitor_mv
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
