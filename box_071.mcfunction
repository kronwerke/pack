# 071 ars_apprentice/turret
#area 150 122 169 147
fill 150 64 122 169 91 147 minecraft:air
fill 150 60 122 169 62 147 minecraft:stone
fill 150 63 122 169 63 147 minecraft:light_gray_concrete
fill 154 64 128 169 79 128 minecraft:light_gray_concrete
fill 154 64 128 154 79 141 minecraft:light_gray_concrete
setblock 155 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071"}','{"text": "ars_apprentice"}','{"text": "turret"}','{"text": ""}']}}
setblock 156 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "turret in front"}','{"text": "of a"}','{"text": "cobblestone"}','{"text": "generator"}']}}
fill 164 64 128 164 79 141 minecraft:light_gray_concrete
setblock 159 64 134 ars_nouveau:basic_spell_turret
setblock 159 64 132 minecraft:cobblestone
setblock 158 64 132 minecraft:water
setblock 160 64 132 minecraft:lava
fill 157 64 131 161 64 131 minecraft:stone_bricks
setblock 157 64 132 minecraft:stone_bricks
setblock 161 64 132 minecraft:stone_bricks
setblock 158 64 133 minecraft:glass
setblock 160 64 133 minecraft:glass
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
