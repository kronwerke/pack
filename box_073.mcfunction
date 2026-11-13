# 073 botania/manasteel_prep
#area 90 109 111 136
fill 90 64 109 111 91 136 minecraft:air
fill 90 60 109 111 62 136 minecraft:stone
fill 90 63 109 111 63 136 minecraft:light_gray_concrete
fill 94 64 115 111 79 115 minecraft:light_gray_concrete
fill 94 64 115 94 79 130 minecraft:light_gray_concrete
setblock 95 64 129 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073"}','{"text": "botania"}','{"text": "manasteel_prep"}','{"text": ""}']}}
setblock 96 64 129 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Nature\'s"}','{"text": "Aura ritual"}','{"text": "layout with"}','{"text": "gold powder and"}']}}
setblock 97 64 129 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stands"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 106 64 115 106 79 130 minecraft:light_gray_concrete
setblock 100 64 117 naturesaura:wood_stand
setblock 97 64 118 naturesaura:wood_stand
setblock 103 64 118 naturesaura:wood_stand
setblock 99 64 119 naturesaura:gold_powder
setblock 100 64 119 naturesaura:gold_powder
setblock 101 64 119 naturesaura:gold_powder
setblock 98 64 120 naturesaura:gold_powder
setblock 99 64 120 naturesaura:gold_powder
setblock 101 64 120 naturesaura:gold_powder
setblock 102 64 120 naturesaura:gold_powder
setblock 96 64 121 naturesaura:wood_stand
setblock 98 64 121 naturesaura:gold_powder
setblock 100 64 121 minecraft:oak_sapling
setblock 102 64 121 naturesaura:gold_powder
setblock 104 64 121 naturesaura:wood_stand
setblock 98 64 122 naturesaura:gold_powder
setblock 99 64 122 naturesaura:gold_powder
setblock 101 64 122 naturesaura:gold_powder
setblock 102 64 122 naturesaura:gold_powder
setblock 99 64 123 naturesaura:gold_powder
setblock 100 64 123 naturesaura:gold_powder
setblock 101 64 123 naturesaura:gold_powder
setblock 97 64 124 naturesaura:wood_stand
setblock 103 64 124 naturesaura:wood_stand
setblock 100 64 125 naturesaura:wood_stand
setblock 100 63 121 minecraft:grass_block
kw testworld use 100 64 117 up naturesaura:infused_iron
kw testworld use 97 64 118 up botania:livingwood_twig
kw testworld use 103 64 118 up naturesaura:infused_iron
kw testworld use 96 64 121 up botania:mana_diamond
kw testworld use 104 64 121 up naturesaura:gold_leaf
kw testworld use 97 64 124 up naturesaura:infused_iron
kw testworld use 103 64 124 up botania:livingwood_twig
kw testworld use 100 64 125 up naturesaura:infused_iron
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
