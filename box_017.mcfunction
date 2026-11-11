# 017 alfheim/open
#area 81 53 102 78
fill 81 64 53 102 91 78 minecraft:air
fill 81 60 53 102 62 78 minecraft:stone
fill 81 63 53 102 63 78 minecraft:light_gray_concrete
fill 85 64 59 102 79 59 minecraft:light_gray_concrete
fill 85 64 59 85 79 72 minecraft:light_gray_concrete
setblock 86 64 71 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "017"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 87 64 71 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
summon text_display 91.5 71 64.5 {text:'[{"text": "017  ", "color": "gold"}, {"text": "alfheim/open", "color": "gray"}, {"text": "\\nÖffne das Portal", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 97 64 59 97 79 72 minecraft:light_gray_concrete
setblock 91 64 63 botania:elven_gateway_core
setblock 90 64 63 botania:livingwood_log[axis=x]
setblock 90 68 63 botania:livingwood_log[axis=x]
setblock 92 64 63 botania:livingwood_log[axis=x]
setblock 92 68 63 botania:livingwood_log[axis=x]
setblock 91 68 63 botania:glimmering_livingwood_log[axis=x]
setblock 89 65 63 botania:livingwood_log[axis=y]
setblock 89 66 63 botania:glimmering_livingwood_log[axis=y]
setblock 89 67 63 botania:livingwood_log[axis=y]
setblock 93 65 63 botania:livingwood_log[axis=y]
setblock 93 66 63 botania:glimmering_livingwood_log[axis=y]
setblock 93 67 63 botania:livingwood_log[axis=y]
setblock 87 64 65 botania:mana_pool{mana:1000000}
setblock 87 65 65 botania:natura_pylon
setblock 95 64 65 botania:mana_pool{mana:1000000}
setblock 95 65 65 botania:natura_pylon
kw testworld use 91 64 63 south botania:wand_of_the_forest
execute unless block 91 64 63 botania:elven_gateway_core[state=off]
