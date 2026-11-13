# 044 ars_nouveau/imbuement
#area -4 88 15 113
fill -4 64 88 15 91 113 minecraft:air
fill -4 60 88 15 62 113 minecraft:stone
fill -4 63 88 15 63 113 minecraft:light_gray_concrete
fill 0 64 94 15 79 94 minecraft:light_gray_concrete
fill 0 64 94 0 79 107 minecraft:light_gray_concrete
setblock 1 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "044"}','{"text": "ars_nouveau"}','{"text": "imbuement"}','{"text": ""}']}}
setblock 2 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the chamber"}','{"text": "with an"}','{"text": "amethyst shard,"}','{"text": "then with a"}']}}
setblock 3 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "finished gem"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 10 64 94 10 79 107 minecraft:light_gray_concrete
setblock 5 64 99 ars_nouveau:imbuement_chamber[facing=up]
kw testworld use 5 64 99 south minecraft:amethyst_shard
setblock 7 64 99 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
