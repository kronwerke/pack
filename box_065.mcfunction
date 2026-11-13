# 065 ars_nouveau/earth_essence
#area 58 122 77 147
fill 58 64 122 77 91 147 minecraft:air
fill 58 60 122 77 62 147 minecraft:stone
fill 58 63 122 77 63 147 minecraft:light_gray_concrete
fill 62 64 128 77 79 128 minecraft:light_gray_concrete
fill 62 64 128 62 79 141 minecraft:light_gray_concrete
setblock 63 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "065"}','{"text": "ars_nouveau"}','{"text": "earth_essence"}','{"text": ""}']}}
setblock 64 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "three pedestals"}','{"text": "next to it"}','{"text": ""}']}}
fill 72 64 128 72 79 141 minecraft:light_gray_concrete
setblock 67 64 133 ars_nouveau:imbuement_chamber[facing=up]
setblock 66 64 133 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 66 64 133 south minecraft:iron_ingot
setblock 68 64 133 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 68 64 133 south minecraft:wheat_seeds
setblock 67 64 132 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 67 64 132 south minecraft:dirt
kw testworld use 67 64 133 south ars_nouveau:source_gem
setblock 69 64 132 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
