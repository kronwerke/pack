# 054 ars_nouveau/earth_essence
#area 58 88 77 113
fill 58 64 88 77 91 113 minecraft:air
fill 58 60 88 77 62 113 minecraft:stone
fill 58 63 88 77 63 113 minecraft:light_gray_concrete
fill 62 64 94 77 79 94 minecraft:light_gray_concrete
fill 62 64 94 62 79 107 minecraft:light_gray_concrete
setblock 63 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054"}','{"text": "ars_nouveau"}','{"text": "earth_essence"}','{"text": ""}']}}
setblock 64 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "three pedestals"}','{"text": "next to it"}','{"text": ""}']}}
fill 72 64 94 72 79 107 minecraft:light_gray_concrete
setblock 67 64 99 ars_nouveau:imbuement_chamber[facing=up]
setblock 66 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 66 64 99 south minecraft:iron_ingot
setblock 68 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 68 64 99 south minecraft:wheat_seeds
setblock 67 64 98 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 67 64 98 south minecraft:dirt
kw testworld use 67 64 99 south ars_nouveau:source_gem
setblock 69 64 98 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
