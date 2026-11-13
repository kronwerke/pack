# 060 ars_apprentice/source_motor
#area 165 88 184 113
fill 165 64 88 184 91 113 minecraft:air
fill 165 60 88 184 62 113 minecraft:stone
fill 165 63 88 184 63 113 minecraft:light_gray_concrete
fill 169 64 94 184 79 94 minecraft:light_gray_concrete
fill 169 64 94 169 79 107 minecraft:light_gray_concrete
setblock 170 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "060"}','{"text": "ars_apprentice"}','{"text": "source_motor"}','{"text": ""}']}}
setblock 171 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "motor with a"}','{"text": "jar driving a"}','{"text": "Create shaft"}','{"text": ""}']}}
fill 179 64 94 179 79 107 minecraft:light_gray_concrete
setblock 173 64 99 ars_technica:source_motor[facing=east]
fill 174 64 99 176 64 99 create:shaft[axis=x]
setblock 173 64 98 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
