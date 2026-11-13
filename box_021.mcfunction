# 021 ars_nouveau/imbuement
#area -4 65 15 90
fill -4 64 65 15 91 90 minecraft:air
fill -4 60 65 15 62 90 minecraft:stone
fill -4 63 65 15 63 90 minecraft:light_gray_concrete
fill 0 64 71 15 79 71 minecraft:light_gray_concrete
fill 0 64 71 0 79 84 minecraft:light_gray_concrete
setblock 1 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "021"}','{"text": "ars_nouveau"}','{"text": "imbuement"}','{"text": ""}']}}
setblock 2 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the chamber"}','{"text": "with an"}','{"text": "amethyst shard,"}','{"text": "then with a"}']}}
setblock 3 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "finished gem"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 10 64 71 10 79 84 minecraft:light_gray_concrete
setblock 5 64 76 ars_nouveau:imbuement_chamber[facing=up]
kw testworld use 5 64 76 south minecraft:amethyst_shard
setblock 7 64 76 ars_nouveau:source_jar[fill=11]{source:10000}
