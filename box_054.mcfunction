# 054 ars_apprentice/source_motor
#area 150 88 169 113
fill 150 64 88 169 91 113 minecraft:air
fill 150 60 88 169 62 113 minecraft:stone
fill 150 63 88 169 63 113 minecraft:light_gray_concrete
fill 154 64 94 169 79 94 minecraft:light_gray_concrete
fill 154 64 94 154 79 107 minecraft:light_gray_concrete
setblock 155 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054"}','{"text": "ars_apprentice"}','{"text": "source_motor"}','{"text": ""}']}}
setblock 156 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "motor with a"}','{"text": "jar driving a"}','{"text": "Create shaft"}','{"text": ""}']}}
fill 164 64 94 164 79 107 minecraft:light_gray_concrete
setblock 158 64 99 ars_technica:source_motor[facing=east]
fill 159 64 99 161 64 99 create:shaft[axis=x]
setblock 158 64 98 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
