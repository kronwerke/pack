# 054 ars_nouveau/apparatus
#area 43 88 62 113
fill 43 64 88 62 91 113 minecraft:air
fill 43 60 88 62 62 113 minecraft:stone
fill 43 63 88 62 63 113 minecraft:light_gray_concrete
fill 47 64 94 62 79 94 minecraft:light_gray_concrete
fill 47 64 94 47 79 107 minecraft:light_gray_concrete
setblock 48 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054"}','{"text": "ars_nouveau"}','{"text": "apparatus"}','{"text": ""}']}}
setblock 49 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "core, apparatus"}','{"text": "and pedestals"}','{"text": "in range"}','{"text": ""}']}}
fill 57 64 94 57 79 107 minecraft:light_gray_concrete
setblock 52 64 99 ars_nouveau:arcane_core[facing=up]
setblock 52 65 99 ars_nouveau:enchanting_apparatus[facing=up]
setblock 50 64 97 ars_nouveau:arcane_pedestal[facing=up]
setblock 52 64 96 ars_nouveau:arcane_pedestal[facing=up]
setblock 54 64 97 ars_nouveau:arcane_pedestal[facing=up]
setblock 49 64 99 ars_nouveau:arcane_pedestal[facing=up]
setblock 55 64 99 ars_nouveau:arcane_pedestal[facing=up]
setblock 50 64 101 ars_nouveau:arcane_pedestal[facing=up]
setblock 54 64 101 ars_nouveau:arcane_pedestal[facing=up]
setblock 55 64 96 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
