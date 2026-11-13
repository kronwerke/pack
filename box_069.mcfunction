# 069 ars_apprentice/source_motor
#area 165 118 184 143
fill 165 64 118 184 91 143 minecraft:air
fill 165 60 118 184 62 143 minecraft:stone
fill 165 63 118 184 63 143 minecraft:light_gray_concrete
fill 169 64 124 184 79 124 minecraft:light_gray_concrete
fill 169 64 124 169 79 137 minecraft:light_gray_concrete
setblock 170 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069"}','{"text": "ars_apprentice"}','{"text": "source_motor"}','{"text": ""}']}}
setblock 171 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "motor with a"}','{"text": "jar driving a"}','{"text": "Create shaft"}','{"text": ""}']}}
fill 179 64 124 179 79 137 minecraft:light_gray_concrete
setblock 173 64 129 ars_technica:source_motor[facing=east]
fill 174 64 129 176 64 129 create:shaft[axis=x]
setblock 173 64 128 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
