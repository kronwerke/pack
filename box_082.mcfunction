# 082 botania/manasteel_prep
#area 90 139 111 166
fill 90 64 139 111 91 166 minecraft:air
fill 90 60 139 111 62 166 minecraft:stone
fill 90 63 139 111 63 166 minecraft:light_gray_concrete
fill 94 64 145 111 79 145 minecraft:light_gray_concrete
fill 94 64 145 94 79 160 minecraft:light_gray_concrete
setblock 95 64 159 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082"}','{"text": "botania"}','{"text": "manasteel_prep"}','{"text": ""}']}}
setblock 96 64 159 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Nature\'s"}','{"text": "Aura ritual"}','{"text": "layout with"}','{"text": "gold powder and"}']}}
setblock 97 64 159 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stands"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 106 64 145 106 79 160 minecraft:light_gray_concrete
setblock 100 64 147 naturesaura:wood_stand
setblock 97 64 148 naturesaura:wood_stand
setblock 103 64 148 naturesaura:wood_stand
setblock 99 64 149 naturesaura:gold_powder
setblock 100 64 149 naturesaura:gold_powder
setblock 101 64 149 naturesaura:gold_powder
setblock 98 64 150 naturesaura:gold_powder
setblock 99 64 150 naturesaura:gold_powder
setblock 101 64 150 naturesaura:gold_powder
setblock 102 64 150 naturesaura:gold_powder
setblock 96 64 151 naturesaura:wood_stand
setblock 98 64 151 naturesaura:gold_powder
setblock 100 64 151 minecraft:oak_sapling
setblock 102 64 151 naturesaura:gold_powder
setblock 104 64 151 naturesaura:wood_stand
setblock 98 64 152 naturesaura:gold_powder
setblock 99 64 152 naturesaura:gold_powder
setblock 101 64 152 naturesaura:gold_powder
setblock 102 64 152 naturesaura:gold_powder
setblock 99 64 153 naturesaura:gold_powder
setblock 100 64 153 naturesaura:gold_powder
setblock 101 64 153 naturesaura:gold_powder
setblock 97 64 154 naturesaura:wood_stand
setblock 103 64 154 naturesaura:wood_stand
setblock 100 64 155 naturesaura:wood_stand
setblock 100 63 151 minecraft:grass_block
kw testworld use 100 64 147 up naturesaura:infused_iron
kw testworld use 97 64 148 up botania:livingwood_twig
kw testworld use 103 64 148 up naturesaura:infused_iron
kw testworld use 96 64 151 up botania:mana_diamond
kw testworld use 104 64 151 up naturesaura:gold_leaf
kw testworld use 97 64 154 up naturesaura:infused_iron
kw testworld use 103 64 154 up botania:livingwood_twig
kw testworld use 100 64 155 up naturesaura:infused_iron
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
