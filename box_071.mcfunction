# 071 ars_apprentice/turret
#area 150 118 169 143
fill 150 64 118 169 91 143 minecraft:air
fill 150 60 118 169 62 143 minecraft:stone
fill 150 63 118 169 63 143 minecraft:light_gray_concrete
fill 154 64 124 169 79 124 minecraft:light_gray_concrete
fill 154 64 124 154 79 137 minecraft:light_gray_concrete
setblock 155 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071"}','{"text": "ars_apprentice"}','{"text": "turret"}','{"text": ""}']}}
setblock 156 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "turret in front"}','{"text": "of a"}','{"text": "cobblestone"}','{"text": "generator"}']}}
fill 164 64 124 164 79 137 minecraft:light_gray_concrete
setblock 159 64 130 ars_nouveau:basic_spell_turret
setblock 159 64 128 minecraft:cobblestone
setblock 158 64 128 minecraft:water
setblock 160 64 128 minecraft:lava
fill 157 64 127 161 64 127 minecraft:stone_bricks
setblock 157 64 128 minecraft:stone_bricks
setblock 161 64 128 minecraft:stone_bricks
setblock 158 64 129 minecraft:glass
setblock 160 64 129 minecraft:glass
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
