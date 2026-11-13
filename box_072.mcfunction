# 072 ars_apprentice/source_motor
#area 165 122 184 147
fill 165 64 122 184 91 147 minecraft:air
fill 165 60 122 184 62 147 minecraft:stone
fill 165 63 122 184 63 147 minecraft:light_gray_concrete
fill 169 64 128 184 79 128 minecraft:light_gray_concrete
fill 169 64 128 169 79 141 minecraft:light_gray_concrete
setblock 170 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072"}','{"text": "ars_apprentice"}','{"text": "source_motor"}','{"text": ""}']}}
setblock 171 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "motor with a"}','{"text": "jar driving a"}','{"text": "Create shaft"}','{"text": ""}']}}
fill 179 64 128 179 79 141 minecraft:light_gray_concrete
setblock 173 64 133 ars_technica:source_motor[facing=east]
fill 174 64 133 176 64 133 create:shaft[axis=x]
setblock 173 64 132 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
