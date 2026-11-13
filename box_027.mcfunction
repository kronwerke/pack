# 027 ars_nouveau/earth_essence
#area 41 67 60 92
fill 41 64 67 60 91 92 minecraft:air
fill 41 60 67 60 62 92 minecraft:stone
fill 41 63 67 60 63 92 minecraft:light_gray_concrete
fill 45 64 73 60 79 73 minecraft:light_gray_concrete
fill 45 64 73 45 79 86 minecraft:light_gray_concrete
setblock 46 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "027"}','{"text": "ars_nouveau"}','{"text": "earth_essence"}','{"text": ""}']}}
setblock 47 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "three pedestals"}','{"text": "next to it"}','{"text": ""}']}}
fill 55 64 73 55 79 86 minecraft:light_gray_concrete
setblock 50 64 78 ars_nouveau:imbuement_chamber[facing=up]
setblock 49 64 78 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 49 64 78 south minecraft:iron_ingot
setblock 51 64 78 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 51 64 78 south minecraft:wheat_seeds
setblock 50 64 77 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 50 64 77 south minecraft:dirt
kw testworld use 50 64 78 south ars_nouveau:source_gem
setblock 52 64 77 ars_nouveau:source_jar[fill=11]{source:10000}
