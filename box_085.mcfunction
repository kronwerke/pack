# 085 botania/manasteel_prep
#area 90 143 111 170
fill 90 64 143 111 91 170 minecraft:air
fill 90 60 143 111 62 170 minecraft:stone
fill 90 63 143 111 63 170 minecraft:light_gray_concrete
fill 94 64 149 111 79 149 minecraft:light_gray_concrete
fill 94 64 149 94 79 164 minecraft:light_gray_concrete
setblock 95 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "085"}','{"text": "botania"}','{"text": "manasteel_prep"}','{"text": ""}']}}
setblock 96 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Nature\'s"}','{"text": "Aura ritual"}','{"text": "layout with"}','{"text": "gold powder and"}']}}
setblock 97 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stands"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 106 64 149 106 79 164 minecraft:light_gray_concrete
setblock 100 64 151 naturesaura:wood_stand
setblock 97 64 152 naturesaura:wood_stand
setblock 103 64 152 naturesaura:wood_stand
setblock 99 64 153 naturesaura:gold_powder
setblock 100 64 153 naturesaura:gold_powder
setblock 101 64 153 naturesaura:gold_powder
setblock 98 64 154 naturesaura:gold_powder
setblock 99 64 154 naturesaura:gold_powder
setblock 101 64 154 naturesaura:gold_powder
setblock 102 64 154 naturesaura:gold_powder
setblock 96 64 155 naturesaura:wood_stand
setblock 98 64 155 naturesaura:gold_powder
setblock 100 64 155 minecraft:oak_sapling
setblock 102 64 155 naturesaura:gold_powder
setblock 104 64 155 naturesaura:wood_stand
setblock 98 64 156 naturesaura:gold_powder
setblock 99 64 156 naturesaura:gold_powder
setblock 101 64 156 naturesaura:gold_powder
setblock 102 64 156 naturesaura:gold_powder
setblock 99 64 157 naturesaura:gold_powder
setblock 100 64 157 naturesaura:gold_powder
setblock 101 64 157 naturesaura:gold_powder
setblock 97 64 158 naturesaura:wood_stand
setblock 103 64 158 naturesaura:wood_stand
setblock 100 64 159 naturesaura:wood_stand
setblock 100 63 155 minecraft:grass_block
kw testworld use 100 64 151 up naturesaura:infused_iron
kw testworld use 97 64 152 up botania:livingwood_twig
kw testworld use 103 64 152 up naturesaura:infused_iron
kw testworld use 96 64 155 up botania:mana_diamond
kw testworld use 104 64 155 up naturesaura:gold_leaf
kw testworld use 97 64 158 up naturesaura:infused_iron
kw testworld use 103 64 158 up botania:livingwood_twig
kw testworld use 100 64 159 up naturesaura:infused_iron
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
