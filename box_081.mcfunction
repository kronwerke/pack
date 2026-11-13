# 081 ars_apprentice/source_motor
#area 210 126 229 151
fill 210 64 126 229 91 151 minecraft:air
fill 210 60 126 229 62 151 minecraft:stone
fill 210 63 126 229 63 151 minecraft:light_gray_concrete
fill 214 64 132 229 79 132 minecraft:light_gray_concrete
fill 214 64 132 214 79 145 minecraft:light_gray_concrete
setblock 215 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081"}','{"text": "ars_apprentice"}','{"text": "source_motor"}','{"text": ""}']}}
setblock 216 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "motor with a"}','{"text": "jar driving a"}','{"text": "Create shaft"}','{"text": ""}']}}
fill 224 64 132 224 79 145 minecraft:light_gray_concrete
setblock 218 64 137 ars_technica:source_motor[facing=east]
fill 219 64 137 221 64 137 create:shaft[axis=x]
setblock 218 64 136 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
