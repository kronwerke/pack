# 012 alfheim/open
#area 81 51 102 76
fill 81 64 51 102 91 76 minecraft:air
fill 81 60 51 102 62 76 minecraft:stone
fill 81 63 51 102 63 76 minecraft:light_gray_concrete
fill 85 64 57 102 79 57 minecraft:light_gray_concrete
fill 85 64 57 85 79 70 minecraft:light_gray_concrete
setblock 86 64 69 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "012"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 87 64 69 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
summon text_display 91.5 71 62.5 {text:'[{"text": "012  ", "color": "gold"}, {"text": "alfheim/open", "color": "gray"}, {"text": "\\nÖffne das Portal", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 97 64 57 97 79 66 minecraft:light_gray_concrete
setblock 91 64 61 botania:elven_gateway_core
setblock 90 64 61 botania:livingwood_log[axis=x]
setblock 90 68 61 botania:livingwood_log[axis=x]
setblock 92 64 61 botania:livingwood_log[axis=x]
setblock 92 68 61 botania:livingwood_log[axis=x]
setblock 91 68 61 botania:glimmering_livingwood_log[axis=x]
setblock 89 65 61 botania:livingwood_log[axis=y]
setblock 89 66 61 botania:glimmering_livingwood_log[axis=y]
setblock 89 67 61 botania:livingwood_log[axis=y]
setblock 93 65 61 botania:livingwood_log[axis=y]
setblock 93 66 61 botania:glimmering_livingwood_log[axis=y]
setblock 93 67 61 botania:livingwood_log[axis=y]
setblock 87 64 63 botania:mana_pool{mana:1000000}
setblock 87 65 63 botania:natura_pylon
setblock 95 64 63 botania:mana_pool{mana:1000000}
setblock 95 65 63 botania:natura_pylon
kw testworld use 91 64 61 south botania:wand_of_the_forest
execute unless block 91 65 61 minecraft:air
