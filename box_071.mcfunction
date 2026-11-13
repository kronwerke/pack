# 071 ars_master/wilden_ritual
#area 197 118 216 143
fill 197 64 118 216 91 143 minecraft:air
fill 197 60 118 216 62 143 minecraft:stone
fill 197 63 118 216 63 143 minecraft:light_gray_concrete
fill 201 64 124 216 79 124 minecraft:light_gray_concrete
fill 201 64 124 201 79 137 minecraft:light_gray_concrete
setblock 202 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071"}','{"text": "ars_master"}','{"text": "wilden_ritual"}','{"text": ""}']}}
setblock 203 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "brazier with"}','{"text": "spike, horn and"}','{"text": "wing"}','{"text": ""}']}}
fill 211 64 124 211 79 137 minecraft:light_gray_concrete
setblock 206 64 129 ars_nouveau:ritual_brazier
kw testworld use 206 64 129 up ars_nouveau:ritual_wilden_summon
setblock 204 64 129 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 204 64 129 south ars_nouveau:wilden_spike
setblock 208 64 129 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 208 64 129 south ars_nouveau:wilden_horn
setblock 206 64 127 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 206 64 127 south ars_nouveau:wilden_wing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
