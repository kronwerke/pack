# 061 ars_apprentice/turret
#area 150 88 169 113
fill 150 64 88 169 91 113 minecraft:air
fill 150 60 88 169 62 113 minecraft:stone
fill 150 63 88 169 63 113 minecraft:light_gray_concrete
fill 154 64 94 169 79 94 minecraft:light_gray_concrete
fill 154 64 94 154 79 107 minecraft:light_gray_concrete
setblock 155 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "061"}','{"text": "ars_apprentice"}','{"text": "turret"}','{"text": ""}']}}
setblock 156 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "turret in front"}','{"text": "of a"}','{"text": "cobblestone"}','{"text": "generator"}']}}
fill 164 64 94 164 79 107 minecraft:light_gray_concrete
setblock 159 64 100 ars_nouveau:basic_spell_turret
setblock 159 64 98 minecraft:cobblestone
setblock 158 64 98 minecraft:water
setblock 160 64 98 minecraft:lava
fill 157 64 97 161 64 97 minecraft:stone_bricks
setblock 157 64 98 minecraft:stone_bricks
setblock 161 64 98 minecraft:stone_bricks
setblock 158 64 99 minecraft:glass
setblock 160 64 99 minecraft:glass
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
