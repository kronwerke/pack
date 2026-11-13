# 107 alfheim/frame
#area 298 147 319 172
fill 298 64 147 319 91 172 minecraft:air
fill 298 60 147 319 62 172 minecraft:stone
fill 298 63 147 319 63 172 minecraft:light_gray_concrete
fill 302 64 153 319 79 153 minecraft:light_gray_concrete
fill 302 64 153 302 79 166 minecraft:light_gray_concrete
setblock 303 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "107"}','{"text": "alfheim"}','{"text": "frame"}','{"text": ""}']}}
setblock 304 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "gateway with"}','{"text": "two pools and"}','{"text": "natura pylons"}']}}
fill 314 64 153 314 79 166 minecraft:light_gray_concrete
setblock 308 64 157 botania:elven_gateway_core
setblock 307 64 157 botania:livingwood_log[axis=x]
setblock 307 68 157 botania:livingwood_log[axis=x]
setblock 309 64 157 botania:livingwood_log[axis=x]
setblock 309 68 157 botania:livingwood_log[axis=x]
setblock 308 68 157 botania:glimmering_livingwood_log[axis=x]
setblock 306 65 157 botania:livingwood_log[axis=y]
setblock 306 66 157 botania:glimmering_livingwood_log[axis=y]
setblock 306 67 157 botania:livingwood_log[axis=y]
setblock 310 65 157 botania:livingwood_log[axis=y]
setblock 310 66 157 botania:glimmering_livingwood_log[axis=y]
setblock 310 67 157 botania:livingwood_log[axis=y]
setblock 304 64 159 botania:mana_pool{mana:1000000}
setblock 304 65 159 botania:natura_pylon
setblock 312 64 159 botania:mana_pool{mana:1000000}
setblock 312 65 159 botania:natura_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
