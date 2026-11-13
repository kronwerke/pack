# 023 ars_nouveau/earth_essence
#area 26 65 45 90
fill 26 64 65 45 91 90 minecraft:air
fill 26 60 65 45 62 90 minecraft:stone
fill 26 63 65 45 63 90 minecraft:light_gray_concrete
fill 30 64 71 45 79 71 minecraft:light_gray_concrete
fill 30 64 71 30 79 84 minecraft:light_gray_concrete
setblock 31 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "023"}','{"text": "ars_nouveau"}','{"text": "earth_essence"}','{"text": ""}']}}
setblock 32 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "three pedestals"}','{"text": "next to it"}','{"text": ""}']}}
fill 40 64 71 40 79 84 minecraft:light_gray_concrete
setblock 35 64 76 ars_nouveau:imbuement_chamber[facing=up]
setblock 34 64 76 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 34 64 76 south minecraft:iron_ingot
setblock 36 64 76 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 36 64 76 south minecraft:wheat_seeds
setblock 35 64 75 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 35 64 75 south minecraft:dirt
kw testworld use 35 64 76 south ars_nouveau:source_gem
setblock 37 64 75 ars_nouveau:source_jar[fill=11]{source:10000}
