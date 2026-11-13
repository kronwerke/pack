# 065 ars_nouveau/earth_essence
#area 58 124 77 149
fill 58 64 124 77 91 149 minecraft:air
fill 58 60 124 77 62 149 minecraft:stone
fill 58 63 124 77 63 149 minecraft:light_gray_concrete
fill 62 64 130 77 79 130 minecraft:light_gray_concrete
fill 62 64 130 62 79 143 minecraft:light_gray_concrete
setblock 63 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "065"}','{"text": "ars_nouveau"}','{"text": "earth_essence"}','{"text": ""}']}}
setblock 64 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "three pedestals"}','{"text": "next to it"}','{"text": ""}']}}
fill 72 64 130 72 79 143 minecraft:light_gray_concrete
setblock 67 64 135 ars_nouveau:imbuement_chamber[facing=up]
setblock 66 64 135 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 66 64 135 south minecraft:iron_ingot
setblock 68 64 135 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 68 64 135 south minecraft:wheat_seeds
setblock 67 64 134 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 67 64 134 south minecraft:dirt
kw testworld use 67 64 135 south ars_nouveau:source_gem
setblock 69 64 134 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
