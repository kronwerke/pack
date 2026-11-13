# 072 ars_apprentice/turret
#area 150 124 169 149
fill 150 64 124 169 91 149 minecraft:air
fill 150 60 124 169 62 149 minecraft:stone
fill 150 63 124 169 63 149 minecraft:light_gray_concrete
fill 154 64 130 169 79 130 minecraft:light_gray_concrete
fill 154 64 130 154 79 143 minecraft:light_gray_concrete
setblock 155 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072"}','{"text": "ars_apprentice"}','{"text": "turret"}','{"text": ""}']}}
setblock 156 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "turret in front"}','{"text": "of a"}','{"text": "cobblestone"}','{"text": "generator"}']}}
fill 164 64 130 164 79 143 minecraft:light_gray_concrete
setblock 159 64 136 ars_nouveau:basic_spell_turret
setblock 159 64 134 minecraft:cobblestone
setblock 158 64 134 minecraft:water
setblock 160 64 134 minecraft:lava
fill 157 64 133 161 64 133 minecraft:stone_bricks
setblock 157 64 134 minecraft:stone_bricks
setblock 161 64 134 minecraft:stone_bricks
setblock 158 64 135 minecraft:glass
setblock 160 64 135 minecraft:glass
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
