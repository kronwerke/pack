# 018 create_brass/crafter
#area 136 40 155 65
fill 136 64 40 155 91 65 minecraft:air
fill 136 60 40 155 62 65 minecraft:stone
fill 136 63 40 155 63 65 minecraft:light_gray_concrete
fill 140 64 46 155 79 46 minecraft:light_gray_concrete
fill 140 64 46 140 79 59 minecraft:light_gray_concrete
setblock 141 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "018"}','{"text": "create_brass"}','{"text": "crafter"}','{"text": ""}']}}
setblock 142 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3"}','{"text": "mechanical"}','{"text": "crafter grid"}','{"text": "with its arrows"}']}}
fill 150 64 46 150 79 59 minecraft:light_gray_concrete
setblock 144 64 51 create:mechanical_crafter[facing=south,pointing=right]
setblock 144 65 51 create:mechanical_crafter[facing=south,pointing=down]
setblock 144 66 51 create:mechanical_crafter[facing=south,pointing=down]
setblock 145 64 51 create:mechanical_crafter[facing=south,pointing=right]
setblock 145 65 51 create:mechanical_crafter[facing=south,pointing=down]
setblock 145 66 51 create:mechanical_crafter[facing=south,pointing=down]
setblock 146 64 51 create:mechanical_crafter[facing=south,pointing=right]
setblock 146 65 51 create:mechanical_crafter[facing=south,pointing=down]
setblock 146 66 51 create:mechanical_crafter[facing=south,pointing=down]
setblock 147 64 51 create:depot
setblock 143 64 51 create:cogwheel[axis=z]
fill 142 64 50 144 65 50 create:andesite_casing
setblock 143 64 50 create:andesite_encased_shaft[axis=z]
setblock 143 64 49 create:creative_motor[facing=south]{ScrollValue:32}
