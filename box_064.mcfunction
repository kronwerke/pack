# 064 ars_master/wilden_ritual
#area 197 88 216 113
fill 197 64 88 216 91 113 minecraft:air
fill 197 60 88 216 62 113 minecraft:stone
fill 197 63 88 216 63 113 minecraft:light_gray_concrete
fill 201 64 94 216 79 94 minecraft:light_gray_concrete
fill 201 64 94 201 79 107 minecraft:light_gray_concrete
setblock 202 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "064"}','{"text": "ars_master"}','{"text": "wilden_ritual"}','{"text": ""}']}}
setblock 203 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "brazier with"}','{"text": "spike, horn and"}','{"text": "wing"}','{"text": ""}']}}
fill 211 64 94 211 79 107 minecraft:light_gray_concrete
setblock 206 64 99 ars_nouveau:ritual_brazier
kw testworld use 206 64 99 up ars_nouveau:ritual_wilden_summon
setblock 204 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 204 64 99 south ars_nouveau:wilden_spike
setblock 208 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 208 64 99 south ars_nouveau:wilden_horn
setblock 206 64 97 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 206 64 97 south ars_nouveau:wilden_wing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
