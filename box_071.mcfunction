# 071 ars_nouveau/apparatus
#area 58 126 77 151
fill 58 64 126 77 91 151 minecraft:air
fill 58 60 126 77 62 151 minecraft:stone
fill 58 63 126 77 63 151 minecraft:light_gray_concrete
fill 62 64 132 77 79 132 minecraft:light_gray_concrete
fill 62 64 132 62 79 145 minecraft:light_gray_concrete
setblock 63 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071"}','{"text": "ars_nouveau"}','{"text": "apparatus"}','{"text": ""}']}}
setblock 64 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "core, apparatus"}','{"text": "and pedestals"}','{"text": "in range"}','{"text": ""}']}}
fill 72 64 132 72 79 145 minecraft:light_gray_concrete
setblock 67 64 137 ars_nouveau:arcane_core[facing=up]
setblock 67 65 137 ars_nouveau:enchanting_apparatus[facing=up]
setblock 65 64 135 ars_nouveau:arcane_pedestal[facing=up]
setblock 67 64 134 ars_nouveau:arcane_pedestal[facing=up]
setblock 69 64 135 ars_nouveau:arcane_pedestal[facing=up]
setblock 64 64 137 ars_nouveau:arcane_pedestal[facing=up]
setblock 70 64 137 ars_nouveau:arcane_pedestal[facing=up]
setblock 65 64 139 ars_nouveau:arcane_pedestal[facing=up]
setblock 69 64 139 ars_nouveau:arcane_pedestal[facing=up]
setblock 70 64 134 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
