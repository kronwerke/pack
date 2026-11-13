# 072 ars_nouveau/earth_essence
#area 73 126 92 151
fill 73 64 126 92 91 151 minecraft:air
fill 73 60 126 92 62 151 minecraft:stone
fill 73 63 126 92 63 151 minecraft:light_gray_concrete
fill 77 64 132 92 79 132 minecraft:light_gray_concrete
fill 77 64 132 77 79 145 minecraft:light_gray_concrete
setblock 78 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072"}','{"text": "ars_nouveau"}','{"text": "earth_essence"}','{"text": ""}']}}
setblock 79 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "three pedestals"}','{"text": "next to it"}','{"text": ""}']}}
fill 87 64 132 87 79 145 minecraft:light_gray_concrete
setblock 82 64 137 ars_nouveau:imbuement_chamber[facing=up]
setblock 81 64 137 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 81 64 137 south minecraft:iron_ingot
setblock 83 64 137 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 83 64 137 south minecraft:wheat_seeds
setblock 82 64 136 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 82 64 136 south minecraft:dirt
kw testworld use 82 64 137 south ars_nouveau:source_gem
setblock 84 64 136 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
