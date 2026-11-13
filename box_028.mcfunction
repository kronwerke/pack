# 028 ars_nouveau/imbuement
#area -4 67 15 92
fill -4 64 67 15 91 92 minecraft:air
fill -4 60 67 15 62 92 minecraft:stone
fill -4 63 67 15 63 92 minecraft:light_gray_concrete
fill 0 64 73 15 79 73 minecraft:light_gray_concrete
fill 0 64 73 0 79 86 minecraft:light_gray_concrete
setblock 1 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "028"}','{"text": "ars_nouveau"}','{"text": "imbuement"}','{"text": ""}']}}
setblock 2 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the chamber"}','{"text": "with an"}','{"text": "amethyst shard,"}','{"text": "then with a"}']}}
setblock 3 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "finished gem"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 10 64 73 10 79 86 minecraft:light_gray_concrete
setblock 5 64 78 ars_nouveau:imbuement_chamber[facing=up]
kw testworld use 5 64 78 south minecraft:amethyst_shard
setblock 7 64 78 ars_nouveau:source_jar[fill=11]{source:10000}
