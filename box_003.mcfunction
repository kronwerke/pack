# 003 start_here/m_ritual
#area 32 -6 53 21
fill 32 64 -6 53 91 21 minecraft:air
fill 32 60 -6 53 62 21 minecraft:stone
fill 32 63 -6 53 63 21 minecraft:light_gray_concrete
fill 36 64 0 53 79 0 minecraft:light_gray_concrete
fill 36 64 0 36 79 15 minecraft:light_gray_concrete
setblock 37 64 14 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "003"}','{"text": "start_here"}','{"text": "m_ritual"}','{"text": ""}']}}
setblock 38 64 14 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the gold powder"}','{"text": "ring with"}','{"text": "wooden stands"}','{"text": "and a sapling"}']}}
setblock 39 64 14 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "in the middle"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 48 64 0 48 79 15 minecraft:light_gray_concrete
setblock 42 64 2 naturesaura:wood_stand
setblock 39 64 3 naturesaura:wood_stand
setblock 45 64 3 naturesaura:wood_stand
setblock 41 64 4 naturesaura:gold_powder
setblock 42 64 4 naturesaura:gold_powder
setblock 43 64 4 naturesaura:gold_powder
setblock 40 64 5 naturesaura:gold_powder
setblock 41 64 5 naturesaura:gold_powder
setblock 43 64 5 naturesaura:gold_powder
setblock 44 64 5 naturesaura:gold_powder
setblock 38 64 6 naturesaura:wood_stand
setblock 40 64 6 naturesaura:gold_powder
setblock 42 64 6 minecraft:oak_sapling
setblock 44 64 6 naturesaura:gold_powder
setblock 46 64 6 naturesaura:wood_stand
setblock 40 64 7 naturesaura:gold_powder
setblock 41 64 7 naturesaura:gold_powder
setblock 43 64 7 naturesaura:gold_powder
setblock 44 64 7 naturesaura:gold_powder
setblock 41 64 8 naturesaura:gold_powder
setblock 42 64 8 naturesaura:gold_powder
setblock 43 64 8 naturesaura:gold_powder
setblock 39 64 9 naturesaura:wood_stand
setblock 45 64 9 naturesaura:wood_stand
setblock 42 64 10 naturesaura:wood_stand
setblock 42 63 6 minecraft:grass_block
kw testworld use 42 64 2 up botania:livingrock
kw testworld use 46 64 6 up naturesaura:gold_leaf
kw testworld use 42 64 10 up minecraft:gold_ingot
kw testworld use 38 64 6 up naturesaura:token_joy
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
