# 080 ars_apprentice/turret
#area 195 126 214 151
fill 195 64 126 214 91 151 minecraft:air
fill 195 60 126 214 62 151 minecraft:stone
fill 195 63 126 214 63 151 minecraft:light_gray_concrete
fill 199 64 132 214 79 132 minecraft:light_gray_concrete
fill 199 64 132 199 79 145 minecraft:light_gray_concrete
setblock 200 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "080"}','{"text": "ars_apprentice"}','{"text": "turret"}','{"text": ""}']}}
setblock 201 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "turret in front"}','{"text": "of a"}','{"text": "cobblestone"}','{"text": "generator"}']}}
fill 209 64 132 209 79 145 minecraft:light_gray_concrete
setblock 204 64 138 ars_nouveau:basic_spell_turret
setblock 204 64 136 minecraft:cobblestone
setblock 203 64 136 minecraft:water
setblock 205 64 136 minecraft:lava
fill 202 64 135 206 64 135 minecraft:stone_bricks
setblock 202 64 136 minecraft:stone_bricks
setblock 206 64 136 minecraft:stone_bricks
setblock 203 64 137 minecraft:glass
setblock 205 64 137 minecraft:glass
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
