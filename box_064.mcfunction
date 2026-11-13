# 064 ars_nouveau/apparatus
#area 43 122 62 147
fill 43 64 122 62 91 147 minecraft:air
fill 43 60 122 62 62 147 minecraft:stone
fill 43 63 122 62 63 147 minecraft:light_gray_concrete
fill 47 64 128 62 79 128 minecraft:light_gray_concrete
fill 47 64 128 47 79 141 minecraft:light_gray_concrete
setblock 48 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "064"}','{"text": "ars_nouveau"}','{"text": "apparatus"}','{"text": ""}']}}
setblock 49 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "core, apparatus"}','{"text": "and pedestals"}','{"text": "in range"}','{"text": ""}']}}
fill 57 64 128 57 79 141 minecraft:light_gray_concrete
setblock 52 64 133 ars_nouveau:arcane_core[facing=up]
setblock 52 65 133 ars_nouveau:enchanting_apparatus[facing=up]
setblock 50 64 131 ars_nouveau:arcane_pedestal[facing=up]
setblock 52 64 130 ars_nouveau:arcane_pedestal[facing=up]
setblock 54 64 131 ars_nouveau:arcane_pedestal[facing=up]
setblock 49 64 133 ars_nouveau:arcane_pedestal[facing=up]
setblock 55 64 133 ars_nouveau:arcane_pedestal[facing=up]
setblock 50 64 135 ars_nouveau:arcane_pedestal[facing=up]
setblock 54 64 135 ars_nouveau:arcane_pedestal[facing=up]
setblock 55 64 130 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
