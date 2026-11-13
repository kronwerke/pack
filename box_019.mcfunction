# 019 create_brass/crafter
#area 153 40 172 65
fill 153 64 40 172 91 65 minecraft:air
fill 153 60 40 172 62 65 minecraft:stone
fill 153 63 40 172 63 65 minecraft:light_gray_concrete
fill 157 64 46 172 79 46 minecraft:light_gray_concrete
fill 157 64 46 157 79 59 minecraft:light_gray_concrete
setblock 158 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "019"}','{"text": "create_brass"}','{"text": "crafter"}','{"text": ""}']}}
setblock 159 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3"}','{"text": "mechanical"}','{"text": "crafter grid"}','{"text": "with its arrows"}']}}
fill 167 64 46 167 79 59 minecraft:light_gray_concrete
setblock 161 64 51 create:mechanical_crafter[facing=south,pointing=right]
setblock 161 65 51 create:mechanical_crafter[facing=south,pointing=down]
setblock 161 66 51 create:mechanical_crafter[facing=south,pointing=down]
setblock 162 64 51 create:mechanical_crafter[facing=south,pointing=right]
setblock 162 65 51 create:mechanical_crafter[facing=south,pointing=down]
setblock 162 66 51 create:mechanical_crafter[facing=south,pointing=down]
setblock 163 64 51 create:mechanical_crafter[facing=south,pointing=right]
setblock 163 65 51 create:mechanical_crafter[facing=south,pointing=down]
setblock 163 66 51 create:mechanical_crafter[facing=south,pointing=down]
setblock 164 64 51 create:depot
setblock 160 64 51 create:cogwheel[axis=z]
fill 159 64 50 161 65 50 create:andesite_casing
setblock 160 64 50 create:andesite_encased_shaft[axis=z]
setblock 160 64 49 create:creative_motor[facing=south]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
