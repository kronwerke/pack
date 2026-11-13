# 058 ars_nouveau/imbuement
#area -4 118 15 143
fill -4 64 118 15 91 143 minecraft:air
fill -4 60 118 15 62 143 minecraft:stone
fill -4 63 118 15 63 143 minecraft:light_gray_concrete
fill 0 64 124 15 79 124 minecraft:light_gray_concrete
fill 0 64 124 0 79 137 minecraft:light_gray_concrete
setblock 1 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "058"}','{"text": "ars_nouveau"}','{"text": "imbuement"}','{"text": ""}']}}
setblock 2 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the chamber"}','{"text": "with an"}','{"text": "amethyst shard,"}','{"text": "then with a"}']}}
setblock 3 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "finished gem"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 10 64 124 10 79 137 minecraft:light_gray_concrete
setblock 5 64 129 ars_nouveau:imbuement_chamber[facing=up]
kw testworld use 5 64 129 south minecraft:amethyst_shard
setblock 7 64 129 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
