# 073 ars_apprentice/source_motor
#area 165 124 184 149
fill 165 64 124 184 91 149 minecraft:air
fill 165 60 124 184 62 149 minecraft:stone
fill 165 63 124 184 63 149 minecraft:light_gray_concrete
fill 169 64 130 184 79 130 minecraft:light_gray_concrete
fill 169 64 130 169 79 143 minecraft:light_gray_concrete
setblock 170 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073"}','{"text": "ars_apprentice"}','{"text": "source_motor"}','{"text": ""}']}}
setblock 171 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "motor with a"}','{"text": "jar driving a"}','{"text": "Create shaft"}','{"text": ""}']}}
fill 179 64 130 179 79 143 minecraft:light_gray_concrete
setblock 173 64 135 ars_technica:source_motor[facing=east]
fill 174 64 135 176 64 135 create:shaft[axis=x]
setblock 173 64 134 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
