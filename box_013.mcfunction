# 013 create_brass/crafter
#area 121 21 140 46
fill 121 64 21 140 91 46 minecraft:air
fill 121 60 21 140 62 46 minecraft:stone
fill 121 63 21 140 63 46 minecraft:light_gray_concrete
fill 125 64 27 140 79 27 minecraft:light_gray_concrete
fill 125 64 27 125 79 40 minecraft:light_gray_concrete
setblock 126 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "013"}','{"text": "create_brass"}','{"text": "crafter"}','{"text": ""}']}}
setblock 127 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3"}','{"text": "mechanical"}','{"text": "crafter grid"}','{"text": "with its arrows"}']}}
fill 135 64 27 135 79 40 minecraft:light_gray_concrete
setblock 129 64 32 create:mechanical_crafter[facing=south,pointing=right]
setblock 129 65 32 create:mechanical_crafter[facing=south,pointing=down]
setblock 129 66 32 create:mechanical_crafter[facing=south,pointing=down]
setblock 130 64 32 create:mechanical_crafter[facing=south,pointing=right]
setblock 130 65 32 create:mechanical_crafter[facing=south,pointing=down]
setblock 130 66 32 create:mechanical_crafter[facing=south,pointing=down]
setblock 131 64 32 create:mechanical_crafter[facing=south,pointing=right]
setblock 131 65 32 create:mechanical_crafter[facing=south,pointing=down]
setblock 131 66 32 create:mechanical_crafter[facing=south,pointing=down]
setblock 132 64 32 create:depot
setblock 128 64 32 create:cogwheel[axis=z]
fill 127 64 31 129 65 31 create:andesite_casing
setblock 128 64 31 create:andesite_encased_shaft[axis=z]
setblock 128 64 30 create:creative_motor[facing=south]{ScrollValue:32}
