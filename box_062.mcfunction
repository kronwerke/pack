# 062 ars_nouveau/earth_essence
#area 58 118 77 143
fill 58 64 118 77 91 143 minecraft:air
fill 58 60 118 77 62 143 minecraft:stone
fill 58 63 118 77 63 143 minecraft:light_gray_concrete
fill 62 64 124 77 79 124 minecraft:light_gray_concrete
fill 62 64 124 62 79 137 minecraft:light_gray_concrete
setblock 63 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "062"}','{"text": "ars_nouveau"}','{"text": "earth_essence"}','{"text": ""}']}}
setblock 64 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "three pedestals"}','{"text": "next to it"}','{"text": ""}']}}
fill 72 64 124 72 79 137 minecraft:light_gray_concrete
setblock 67 64 129 ars_nouveau:imbuement_chamber[facing=up]
setblock 66 64 129 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 66 64 129 south minecraft:iron_ingot
setblock 68 64 129 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 68 64 129 south minecraft:wheat_seeds
setblock 67 64 128 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 67 64 128 south minecraft:dirt
kw testworld use 67 64 129 south ars_nouveau:source_gem
setblock 69 64 128 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
