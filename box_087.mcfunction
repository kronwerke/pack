# 087 botania/manasteel_prep
#area 90 145 111 172
fill 90 64 145 111 91 172 minecraft:air
fill 90 60 145 111 62 172 minecraft:stone
fill 90 63 145 111 63 172 minecraft:light_gray_concrete
fill 94 64 151 111 79 151 minecraft:light_gray_concrete
fill 94 64 151 94 79 166 minecraft:light_gray_concrete
setblock 95 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "087"}','{"text": "botania"}','{"text": "manasteel_prep"}','{"text": ""}']}}
setblock 96 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Nature\'s"}','{"text": "Aura ritual"}','{"text": "layout with"}','{"text": "gold powder and"}']}}
setblock 97 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stands"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 106 64 151 106 79 166 minecraft:light_gray_concrete
setblock 100 64 153 naturesaura:wood_stand
setblock 97 64 154 naturesaura:wood_stand
setblock 103 64 154 naturesaura:wood_stand
setblock 99 64 155 naturesaura:gold_powder
setblock 100 64 155 naturesaura:gold_powder
setblock 101 64 155 naturesaura:gold_powder
setblock 98 64 156 naturesaura:gold_powder
setblock 99 64 156 naturesaura:gold_powder
setblock 101 64 156 naturesaura:gold_powder
setblock 102 64 156 naturesaura:gold_powder
setblock 96 64 157 naturesaura:wood_stand
setblock 98 64 157 naturesaura:gold_powder
setblock 100 64 157 minecraft:oak_sapling
setblock 102 64 157 naturesaura:gold_powder
setblock 104 64 157 naturesaura:wood_stand
setblock 98 64 158 naturesaura:gold_powder
setblock 99 64 158 naturesaura:gold_powder
setblock 101 64 158 naturesaura:gold_powder
setblock 102 64 158 naturesaura:gold_powder
setblock 99 64 159 naturesaura:gold_powder
setblock 100 64 159 naturesaura:gold_powder
setblock 101 64 159 naturesaura:gold_powder
setblock 97 64 160 naturesaura:wood_stand
setblock 103 64 160 naturesaura:wood_stand
setblock 100 64 161 naturesaura:wood_stand
setblock 100 63 157 minecraft:grass_block
kw testworld use 100 64 153 up naturesaura:infused_iron
kw testworld use 97 64 154 up botania:livingwood_twig
kw testworld use 103 64 154 up naturesaura:infused_iron
kw testworld use 96 64 157 up botania:mana_diamond
kw testworld use 104 64 157 up naturesaura:gold_leaf
kw testworld use 97 64 160 up naturesaura:infused_iron
kw testworld use 103 64 160 up botania:livingwood_twig
kw testworld use 100 64 161 up naturesaura:infused_iron
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
