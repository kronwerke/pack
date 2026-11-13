# 053 ars_apprentice/turret
#area 135 88 154 113
fill 135 64 88 154 91 113 minecraft:air
fill 135 60 88 154 62 113 minecraft:stone
fill 135 63 88 154 63 113 minecraft:light_gray_concrete
fill 139 64 94 154 79 94 minecraft:light_gray_concrete
fill 139 64 94 139 79 107 minecraft:light_gray_concrete
setblock 140 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "053"}','{"text": "ars_apprentice"}','{"text": "turret"}','{"text": ""}']}}
setblock 141 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "turret in front"}','{"text": "of a"}','{"text": "cobblestone"}','{"text": "generator"}']}}
fill 149 64 94 149 79 107 minecraft:light_gray_concrete
setblock 144 64 100 ars_nouveau:basic_spell_turret
setblock 144 64 98 minecraft:cobblestone
setblock 143 64 98 minecraft:water
setblock 145 64 98 minecraft:lava
fill 142 64 97 146 64 97 minecraft:stone_bricks
setblock 142 64 98 minecraft:stone_bricks
setblock 146 64 98 minecraft:stone_bricks
setblock 143 64 99 minecraft:glass
setblock 145 64 99 minecraft:glass
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
