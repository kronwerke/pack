# 071 botania/manasteel_prep
#area 90 107 111 134
fill 90 64 107 111 91 134 minecraft:air
fill 90 60 107 111 62 134 minecraft:stone
fill 90 63 107 111 63 134 minecraft:light_gray_concrete
fill 94 64 113 111 79 113 minecraft:light_gray_concrete
fill 94 64 113 94 79 128 minecraft:light_gray_concrete
setblock 95 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071"}','{"text": "botania"}','{"text": "manasteel_prep"}','{"text": ""}']}}
setblock 96 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Nature\'s"}','{"text": "Aura ritual"}','{"text": "layout with"}','{"text": "gold powder and"}']}}
setblock 97 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stands"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 106 64 113 106 79 128 minecraft:light_gray_concrete
setblock 100 64 115 naturesaura:wood_stand
setblock 97 64 116 naturesaura:wood_stand
setblock 103 64 116 naturesaura:wood_stand
setblock 99 64 117 naturesaura:gold_powder
setblock 100 64 117 naturesaura:gold_powder
setblock 101 64 117 naturesaura:gold_powder
setblock 98 64 118 naturesaura:gold_powder
setblock 99 64 118 naturesaura:gold_powder
setblock 101 64 118 naturesaura:gold_powder
setblock 102 64 118 naturesaura:gold_powder
setblock 96 64 119 naturesaura:wood_stand
setblock 98 64 119 naturesaura:gold_powder
setblock 100 64 119 minecraft:oak_sapling
setblock 102 64 119 naturesaura:gold_powder
setblock 104 64 119 naturesaura:wood_stand
setblock 98 64 120 naturesaura:gold_powder
setblock 99 64 120 naturesaura:gold_powder
setblock 101 64 120 naturesaura:gold_powder
setblock 102 64 120 naturesaura:gold_powder
setblock 99 64 121 naturesaura:gold_powder
setblock 100 64 121 naturesaura:gold_powder
setblock 101 64 121 naturesaura:gold_powder
setblock 97 64 122 naturesaura:wood_stand
setblock 103 64 122 naturesaura:wood_stand
setblock 100 64 123 naturesaura:wood_stand
setblock 100 63 119 minecraft:grass_block
kw testworld use 100 64 115 up naturesaura:infused_iron
kw testworld use 97 64 116 up botania:livingwood_twig
kw testworld use 103 64 116 up naturesaura:infused_iron
kw testworld use 96 64 119 up botania:mana_diamond
kw testworld use 104 64 119 up naturesaura:gold_leaf
kw testworld use 97 64 122 up naturesaura:infused_iron
kw testworld use 103 64 122 up botania:livingwood_twig
kw testworld use 100 64 123 up naturesaura:infused_iron
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
