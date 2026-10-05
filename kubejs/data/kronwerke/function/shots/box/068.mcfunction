# 068 mekanism_ores/foundry
fill 193 63 108 204 63 121 minecraft:light_gray_concrete
fill 193 64 108 204 71 108 minecraft:light_gray_concrete
fill 193 64 108 193 71 121 minecraft:light_gray_concrete
setblock 194 64 120 minecraft:air
setblock 194 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "068"}','{"text": "mekanism_ores"}','{"text": "foundry"}','{"text": ""}']}}
setblock 195 64 120 minecraft:air
setblock 195 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Metalworks"}','{"text": "foundry with"}','{"text": "raw ore going"}','{"text": "in and the"}']}}
setblock 196 64 120 minecraft:air
setblock 196 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ingot cast"}','{"text": "Gießerei"}','{"text": "formen, Erz"}','{"text": "hinein"}']}}
summon text_display 198.5 71 113.5 {text:'[{"text": "068  ", "color": "gold"}, {"text": "mekanism_ores/foundry", "color": "gray"}, {"text": "\\nSchmilz Erz in der Gießerei", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 195 64 111 productivemetalworks:gray_foundry_controller
setblock 197 64 111 productivemetalworks:gray_foundry_tank
setblock 199 64 111 productivemetalworks:casting_table
setblock 202 64 117 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"mekanism:raw_osmium",count:16}]}
