# 034 ars_nouveau/earth_essence
#area 58 67 77 92
fill 58 64 67 77 91 92 minecraft:air
fill 58 60 67 77 62 92 minecraft:stone
fill 58 63 67 77 63 92 minecraft:light_gray_concrete
fill 62 64 73 77 79 73 minecraft:light_gray_concrete
fill 62 64 73 62 79 86 minecraft:light_gray_concrete
setblock 63 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "034"}','{"text": "ars_nouveau"}','{"text": "earth_essence"}','{"text": ""}']}}
setblock 64 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "three pedestals"}','{"text": "next to it"}','{"text": ""}']}}
fill 72 64 73 72 79 86 minecraft:light_gray_concrete
setblock 67 64 78 ars_nouveau:imbuement_chamber[facing=up]
setblock 66 64 78 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 66 64 78 south minecraft:iron_ingot
setblock 68 64 78 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 68 64 78 south minecraft:wheat_seeds
setblock 67 64 77 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 67 64 77 south minecraft:dirt
kw testworld use 67 64 78 south ars_nouveau:source_gem
setblock 69 64 77 ars_nouveau:source_jar[fill=11]{source:10000}
