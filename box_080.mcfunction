# 080 alfheim/frame
#area 253 107 274 132
fill 253 64 107 274 91 132 minecraft:air
fill 253 60 107 274 62 132 minecraft:stone
fill 253 63 107 274 63 132 minecraft:light_gray_concrete
fill 257 64 113 274 79 113 minecraft:light_gray_concrete
fill 257 64 113 257 79 126 minecraft:light_gray_concrete
setblock 258 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "080"}','{"text": "alfheim"}','{"text": "frame"}','{"text": ""}']}}
setblock 259 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "gateway with"}','{"text": "two pools and"}','{"text": "natura pylons"}']}}
fill 269 64 113 269 79 126 minecraft:light_gray_concrete
setblock 263 64 117 botania:elven_gateway_core
setblock 262 64 117 botania:livingwood_log[axis=x]
setblock 262 68 117 botania:livingwood_log[axis=x]
setblock 264 64 117 botania:livingwood_log[axis=x]
setblock 264 68 117 botania:livingwood_log[axis=x]
setblock 263 68 117 botania:glimmering_livingwood_log[axis=x]
setblock 261 65 117 botania:livingwood_log[axis=y]
setblock 261 66 117 botania:glimmering_livingwood_log[axis=y]
setblock 261 67 117 botania:livingwood_log[axis=y]
setblock 265 65 117 botania:livingwood_log[axis=y]
setblock 265 66 117 botania:glimmering_livingwood_log[axis=y]
setblock 265 67 117 botania:livingwood_log[axis=y]
setblock 259 64 119 botania:mana_pool{mana:1000000}
setblock 259 65 119 botania:natura_pylon
setblock 267 64 119 botania:mana_pool{mana:1000000}
setblock 267 65 119 botania:natura_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
