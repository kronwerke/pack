# 019 farms/s2_xp
fill 147 63 31 158 63 44 minecraft:light_gray_concrete
fill 147 64 31 158 71 31 minecraft:light_gray_concrete
fill 147 64 31 147 71 44 minecraft:light_gray_concrete
setblock 148 64 43 minecraft:air
setblock 148 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "019"}','{"text": "farms"}','{"text": "s2_xp"}','{"text": ""}']}}
setblock 149 64 43 minecraft:air
setblock 149 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "grindstone"}','{"text": "drain stack"}','{"text": "with experience"}','{"text": "hatch on a tank"}']}}
setblock 150 64 43 minecraft:air
setblock 150 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schleifstein-Abfluss"}','{"text": "auf den Tank"}','{"text": "setzen"}','{"text": ""}']}}
summon text_display 152.5 71 36.5 {text:'[{"text": "019  ", "color": "gold"}, {"text": "farms/s2_xp", "color": "gray"}, {"text": "\\nStufe 2: Erfahrung in Flaschen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 151 64 36 create:fluid_tank
setblock 151 65 36 create:fluid_tank
setblock 151 66 36 create_enchantment_industry:experience_hatch
setblock 153 64 36 create:millstone
setblock 155 64 39 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create_enchantment_industry:grindstone_drain",count:1},{Slot:1b,id:"create_enchantment_industry:experience_hatch",count:1}]}
