# 056 alfheim/frame
#area 223 105 244 130
fill 223 64 105 244 91 130 minecraft:air
fill 223 60 105 244 62 130 minecraft:stone
fill 223 63 105 244 63 130 minecraft:light_gray_concrete
fill 227 64 111 244 79 111 minecraft:light_gray_concrete
fill 227 64 111 227 79 124 minecraft:light_gray_concrete
setblock 228 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "056"}','{"text": "alfheim"}','{"text": "frame"}','{"text": ""}']}}
setblock 229 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "gateway with"}','{"text": "two pools and"}','{"text": "natura pylons"}']}}
fill 239 64 111 239 79 124 minecraft:light_gray_concrete
setblock 233 64 115 botania:elven_gateway_core
setblock 232 64 115 botania:livingwood_log[axis=x]
setblock 232 68 115 botania:livingwood_log[axis=x]
setblock 234 64 115 botania:livingwood_log[axis=x]
setblock 234 68 115 botania:livingwood_log[axis=x]
setblock 233 68 115 botania:glimmering_livingwood_log[axis=x]
setblock 231 65 115 botania:livingwood_log[axis=y]
setblock 231 66 115 botania:glimmering_livingwood_log[axis=y]
setblock 231 67 115 botania:livingwood_log[axis=y]
setblock 235 65 115 botania:livingwood_log[axis=y]
setblock 235 66 115 botania:glimmering_livingwood_log[axis=y]
setblock 235 67 115 botania:livingwood_log[axis=y]
setblock 229 64 117 botania:mana_pool{mana:1000000}
setblock 229 65 117 botania:natura_pylon
setblock 237 64 117 botania:mana_pool{mana:1000000}
setblock 237 65 117 botania:natura_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
