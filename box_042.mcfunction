# 042 ars_nouveau/earth_essence
#area 58 86 77 111
fill 58 64 86 77 91 111 minecraft:air
fill 58 60 86 77 62 111 minecraft:stone
fill 58 63 86 77 63 111 minecraft:light_gray_concrete
fill 62 64 92 77 79 92 minecraft:light_gray_concrete
fill 62 64 92 62 79 105 minecraft:light_gray_concrete
setblock 63 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "042"}','{"text": "ars_nouveau"}','{"text": "earth_essence"}','{"text": ""}']}}
setblock 64 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "three pedestals"}','{"text": "next to it"}','{"text": ""}']}}
fill 72 64 92 72 79 105 minecraft:light_gray_concrete
setblock 67 64 97 ars_nouveau:imbuement_chamber[facing=up]
setblock 66 64 97 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 66 64 97 south minecraft:iron_ingot
setblock 68 64 97 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 68 64 97 south minecraft:wheat_seeds
setblock 67 64 96 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 67 64 96 south minecraft:dirt
kw testworld use 67 64 97 south ars_nouveau:source_gem
setblock 69 64 96 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
