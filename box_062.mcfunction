# 062 alfheim/frame
#area 253 105 274 130
fill 253 64 105 274 91 130 minecraft:air
fill 253 60 105 274 62 130 minecraft:stone
fill 253 63 105 274 63 130 minecraft:light_gray_concrete
fill 257 64 111 274 79 111 minecraft:light_gray_concrete
fill 257 64 111 257 79 124 minecraft:light_gray_concrete
setblock 258 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "062"}','{"text": "alfheim"}','{"text": "frame"}','{"text": ""}']}}
setblock 259 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "gateway with"}','{"text": "two pools and"}','{"text": "natura pylons"}']}}
fill 269 64 111 269 79 124 minecraft:light_gray_concrete
setblock 263 64 115 botania:elven_gateway_core
setblock 262 64 115 botania:livingwood_log[axis=x]
setblock 262 68 115 botania:livingwood_log[axis=x]
setblock 264 64 115 botania:livingwood_log[axis=x]
setblock 264 68 115 botania:livingwood_log[axis=x]
setblock 263 68 115 botania:glimmering_livingwood_log[axis=x]
setblock 261 65 115 botania:livingwood_log[axis=y]
setblock 261 66 115 botania:glimmering_livingwood_log[axis=y]
setblock 261 67 115 botania:livingwood_log[axis=y]
setblock 265 65 115 botania:livingwood_log[axis=y]
setblock 265 66 115 botania:glimmering_livingwood_log[axis=y]
setblock 265 67 115 botania:livingwood_log[axis=y]
setblock 259 64 117 botania:mana_pool{mana:1000000}
setblock 259 65 117 botania:natura_pylon
setblock 267 64 117 botania:mana_pool{mana:1000000}
setblock 267 65 117 botania:natura_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
