# 083 ars_master/wilden_ritual
#area 242 126 261 151
fill 242 64 126 261 91 151 minecraft:air
fill 242 60 126 261 62 151 minecraft:stone
fill 242 63 126 261 63 151 minecraft:light_gray_concrete
fill 246 64 132 261 79 132 minecraft:light_gray_concrete
fill 246 64 132 246 79 145 minecraft:light_gray_concrete
setblock 247 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083"}','{"text": "ars_master"}','{"text": "wilden_ritual"}','{"text": ""}']}}
setblock 248 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "brazier with"}','{"text": "spike, horn and"}','{"text": "wing"}','{"text": ""}']}}
fill 256 64 132 256 79 145 minecraft:light_gray_concrete
setblock 251 64 137 ars_nouveau:ritual_brazier
kw testworld use 251 64 137 up ars_nouveau:ritual_wilden_summon
setblock 249 64 137 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 249 64 137 south ars_nouveau:wilden_spike
setblock 253 64 137 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 253 64 137 south ars_nouveau:wilden_horn
setblock 251 64 135 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 251 64 135 south ars_nouveau:wilden_wing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
