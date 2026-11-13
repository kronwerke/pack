# 061 ars_nouveau/apparatus
#area 43 118 62 143
fill 43 64 118 62 91 143 minecraft:air
fill 43 60 118 62 62 143 minecraft:stone
fill 43 63 118 62 63 143 minecraft:light_gray_concrete
fill 47 64 124 62 79 124 minecraft:light_gray_concrete
fill 47 64 124 47 79 137 minecraft:light_gray_concrete
setblock 48 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "061"}','{"text": "ars_nouveau"}','{"text": "apparatus"}','{"text": ""}']}}
setblock 49 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "core, apparatus"}','{"text": "and pedestals"}','{"text": "in range"}','{"text": ""}']}}
fill 57 64 124 57 79 137 minecraft:light_gray_concrete
setblock 52 64 129 ars_nouveau:arcane_core[facing=up]
setblock 52 65 129 ars_nouveau:enchanting_apparatus[facing=up]
setblock 50 64 127 ars_nouveau:arcane_pedestal[facing=up]
setblock 52 64 126 ars_nouveau:arcane_pedestal[facing=up]
setblock 54 64 127 ars_nouveau:arcane_pedestal[facing=up]
setblock 49 64 129 ars_nouveau:arcane_pedestal[facing=up]
setblock 55 64 129 ars_nouveau:arcane_pedestal[facing=up]
setblock 50 64 131 ars_nouveau:arcane_pedestal[facing=up]
setblock 54 64 131 ars_nouveau:arcane_pedestal[facing=up]
setblock 55 64 126 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
