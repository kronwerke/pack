# 014 create_brass/crafter
#area 136 21 155 46
fill 136 64 21 155 91 46 minecraft:air
fill 136 60 21 155 62 46 minecraft:stone
fill 136 63 21 155 63 46 minecraft:light_gray_concrete
fill 140 64 27 155 79 27 minecraft:light_gray_concrete
fill 140 64 27 140 79 40 minecraft:light_gray_concrete
setblock 141 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "014"}','{"text": "create_brass"}','{"text": "crafter"}','{"text": ""}']}}
setblock 142 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3"}','{"text": "mechanical"}','{"text": "crafter grid"}','{"text": "with its arrows"}']}}
fill 150 64 27 150 79 40 minecraft:light_gray_concrete
setblock 144 64 32 create:mechanical_crafter[facing=south,pointing=right]
setblock 144 65 32 create:mechanical_crafter[facing=south,pointing=down]
setblock 144 66 32 create:mechanical_crafter[facing=south,pointing=down]
setblock 145 64 32 create:mechanical_crafter[facing=south,pointing=right]
setblock 145 65 32 create:mechanical_crafter[facing=south,pointing=down]
setblock 145 66 32 create:mechanical_crafter[facing=south,pointing=down]
setblock 146 64 32 create:mechanical_crafter[facing=south,pointing=right]
setblock 146 65 32 create:mechanical_crafter[facing=south,pointing=down]
setblock 146 66 32 create:mechanical_crafter[facing=south,pointing=down]
setblock 147 64 32 create:depot
setblock 143 64 32 create:cogwheel[axis=z]
fill 142 64 31 144 65 31 create:andesite_casing
setblock 143 64 31 create:andesite_encased_shaft[axis=z]
setblock 143 64 30 create:creative_motor[facing=south]{ScrollValue:32}
