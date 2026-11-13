# 084 alfheim/frame
#area 253 109 274 134
fill 253 64 109 274 91 134 minecraft:air
fill 253 60 109 274 62 134 minecraft:stone
fill 253 63 109 274 63 134 minecraft:light_gray_concrete
fill 257 64 115 274 79 115 minecraft:light_gray_concrete
fill 257 64 115 257 79 128 minecraft:light_gray_concrete
setblock 258 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084"}','{"text": "alfheim"}','{"text": "frame"}','{"text": ""}']}}
setblock 259 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "gateway with"}','{"text": "two pools and"}','{"text": "natura pylons"}']}}
fill 269 64 115 269 79 128 minecraft:light_gray_concrete
setblock 263 64 119 botania:elven_gateway_core
setblock 262 64 119 botania:livingwood_log[axis=x]
setblock 262 68 119 botania:livingwood_log[axis=x]
setblock 264 64 119 botania:livingwood_log[axis=x]
setblock 264 68 119 botania:livingwood_log[axis=x]
setblock 263 68 119 botania:glimmering_livingwood_log[axis=x]
setblock 261 65 119 botania:livingwood_log[axis=y]
setblock 261 66 119 botania:glimmering_livingwood_log[axis=y]
setblock 261 67 119 botania:livingwood_log[axis=y]
setblock 265 65 119 botania:livingwood_log[axis=y]
setblock 265 66 119 botania:glimmering_livingwood_log[axis=y]
setblock 265 67 119 botania:livingwood_log[axis=y]
setblock 259 64 121 botania:mana_pool{mana:1000000}
setblock 259 65 121 botania:natura_pylon
setblock 267 64 121 botania:mana_pool{mana:1000000}
setblock 267 65 121 botania:natura_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
