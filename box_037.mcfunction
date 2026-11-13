# 037 ars_nouveau/apparatus
#area 43 86 62 111
fill 43 64 86 62 91 111 minecraft:air
fill 43 60 86 62 62 111 minecraft:stone
fill 43 63 86 62 63 111 minecraft:light_gray_concrete
fill 47 64 92 62 79 92 minecraft:light_gray_concrete
fill 47 64 92 47 79 105 minecraft:light_gray_concrete
setblock 48 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "037"}','{"text": "ars_nouveau"}','{"text": "apparatus"}','{"text": ""}']}}
setblock 49 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "core, apparatus"}','{"text": "and pedestals"}','{"text": "in range"}','{"text": ""}']}}
fill 57 64 92 57 79 105 minecraft:light_gray_concrete
setblock 52 64 97 ars_nouveau:arcane_core[facing=up]
setblock 52 65 97 ars_nouveau:enchanting_apparatus[facing=up]
setblock 50 64 95 ars_nouveau:arcane_pedestal[facing=up]
setblock 52 64 94 ars_nouveau:arcane_pedestal[facing=up]
setblock 54 64 95 ars_nouveau:arcane_pedestal[facing=up]
setblock 49 64 97 ars_nouveau:arcane_pedestal[facing=up]
setblock 55 64 97 ars_nouveau:arcane_pedestal[facing=up]
setblock 50 64 99 ars_nouveau:arcane_pedestal[facing=up]
setblock 54 64 99 ars_nouveau:arcane_pedestal[facing=up]
setblock 55 64 94 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
