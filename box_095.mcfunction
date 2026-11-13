# 095 botania/manasteel_prep
#area 90 147 111 174
fill 90 64 147 111 91 174 minecraft:air
fill 90 60 147 111 62 174 minecraft:stone
fill 90 63 147 111 63 174 minecraft:light_gray_concrete
fill 94 64 153 111 79 153 minecraft:light_gray_concrete
fill 94 64 153 94 79 168 minecraft:light_gray_concrete
setblock 95 64 167 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095"}','{"text": "botania"}','{"text": "manasteel_prep"}','{"text": ""}']}}
setblock 96 64 167 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Nature\'s"}','{"text": "Aura ritual"}','{"text": "layout with"}','{"text": "gold powder and"}']}}
setblock 97 64 167 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stands"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 106 64 153 106 79 168 minecraft:light_gray_concrete
setblock 100 64 155 naturesaura:wood_stand
setblock 97 64 156 naturesaura:wood_stand
setblock 103 64 156 naturesaura:wood_stand
setblock 99 64 157 naturesaura:gold_powder
setblock 100 64 157 naturesaura:gold_powder
setblock 101 64 157 naturesaura:gold_powder
setblock 98 64 158 naturesaura:gold_powder
setblock 99 64 158 naturesaura:gold_powder
setblock 101 64 158 naturesaura:gold_powder
setblock 102 64 158 naturesaura:gold_powder
setblock 96 64 159 naturesaura:wood_stand
setblock 98 64 159 naturesaura:gold_powder
setblock 100 64 159 minecraft:oak_sapling
setblock 102 64 159 naturesaura:gold_powder
setblock 104 64 159 naturesaura:wood_stand
setblock 98 64 160 naturesaura:gold_powder
setblock 99 64 160 naturesaura:gold_powder
setblock 101 64 160 naturesaura:gold_powder
setblock 102 64 160 naturesaura:gold_powder
setblock 99 64 161 naturesaura:gold_powder
setblock 100 64 161 naturesaura:gold_powder
setblock 101 64 161 naturesaura:gold_powder
setblock 97 64 162 naturesaura:wood_stand
setblock 103 64 162 naturesaura:wood_stand
setblock 100 64 163 naturesaura:wood_stand
setblock 100 63 159 minecraft:grass_block
kw testworld use 100 64 155 up naturesaura:infused_iron
kw testworld use 97 64 156 up botania:livingwood_twig
kw testworld use 103 64 156 up naturesaura:infused_iron
kw testworld use 96 64 159 up botania:mana_diamond
kw testworld use 104 64 159 up naturesaura:gold_leaf
kw testworld use 97 64 162 up naturesaura:infused_iron
kw testworld use 103 64 162 up botania:livingwood_twig
kw testworld use 100 64 163 up naturesaura:infused_iron
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
