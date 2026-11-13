# 021 create_brass/crafter
#area 153 42 172 67
fill 153 64 42 172 91 67 minecraft:air
fill 153 60 42 172 62 67 minecraft:stone
fill 153 63 42 172 63 67 minecraft:light_gray_concrete
fill 157 64 48 172 79 48 minecraft:light_gray_concrete
fill 157 64 48 157 79 61 minecraft:light_gray_concrete
setblock 158 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "021"}','{"text": "create_brass"}','{"text": "crafter"}','{"text": ""}']}}
setblock 159 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3"}','{"text": "mechanical"}','{"text": "crafter grid"}','{"text": "with its arrows"}']}}
fill 167 64 48 167 79 61 minecraft:light_gray_concrete
setblock 161 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 161 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 161 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 162 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 162 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 162 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 163 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 163 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 163 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 164 64 53 create:depot
setblock 160 64 53 create:cogwheel[axis=z]
fill 159 64 52 161 65 52 create:andesite_casing
setblock 160 64 52 create:andesite_encased_shaft[axis=z]
setblock 160 64 51 create:creative_motor[facing=south]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
