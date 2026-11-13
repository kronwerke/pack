# 091 alfheim/frame
#area 253 139 274 164
fill 253 64 139 274 91 164 minecraft:air
fill 253 60 139 274 62 164 minecraft:stone
fill 253 63 139 274 63 164 minecraft:light_gray_concrete
fill 257 64 145 274 79 145 minecraft:light_gray_concrete
fill 257 64 145 257 79 158 minecraft:light_gray_concrete
setblock 258 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091"}','{"text": "alfheim"}','{"text": "frame"}','{"text": ""}']}}
setblock 259 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "gateway with"}','{"text": "two pools and"}','{"text": "natura pylons"}']}}
fill 269 64 145 269 79 158 minecraft:light_gray_concrete
setblock 263 64 149 botania:elven_gateway_core
setblock 262 64 149 botania:livingwood_log[axis=x]
setblock 262 68 149 botania:livingwood_log[axis=x]
setblock 264 64 149 botania:livingwood_log[axis=x]
setblock 264 68 149 botania:livingwood_log[axis=x]
setblock 263 68 149 botania:glimmering_livingwood_log[axis=x]
setblock 261 65 149 botania:livingwood_log[axis=y]
setblock 261 66 149 botania:glimmering_livingwood_log[axis=y]
setblock 261 67 149 botania:livingwood_log[axis=y]
setblock 265 65 149 botania:livingwood_log[axis=y]
setblock 265 66 149 botania:glimmering_livingwood_log[axis=y]
setblock 265 67 149 botania:livingwood_log[axis=y]
setblock 259 64 151 botania:mana_pool{mana:1000000}
setblock 259 65 151 botania:natura_pylon
setblock 267 64 151 botania:mana_pool{mana:1000000}
setblock 267 65 151 botania:natura_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
