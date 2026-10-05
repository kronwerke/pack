# 167 immersive/coke_oven, creosote, pump
fill 30 63 273 61 63 286 minecraft:light_gray_concrete
fill 30 64 273 61 71 273 minecraft:light_gray_concrete
fill 30 64 273 30 71 286 minecraft:light_gray_concrete
setblock 31 64 285 minecraft:air
setblock 31 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "167.1"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 32 64 285 minecraft:air
setblock 32 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 33 64 285 minecraft:air
setblock 33 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": "Mit dem Hammer"}','{"text": "formen"}','{"text": ""}']}}
summon text_display 35.5 71 278.5 {text:'[{"text": "167.1  ", "color": "gold"}, {"text": "immersive/coke_oven", "color": "gray"}, {"text": "\\nForm einen Koksofen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template immersiveengineering:multiblocks/coke_oven 32 64 275 none
setblock 39 64 282 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:hammer",count:1},{Slot:1b,id:"immersiveengineering:manual",count:1}]}
setblock 41 64 285 minecraft:air
setblock 41 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "167.2"}','{"text": "immersive"}','{"text": "creosote"}','{"text": ""}']}}
setblock 42 64 285 minecraft:air
setblock 42 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mit dem Hammer"}','{"text": "formen"}','{"text": ""}','{"text": ""}']}}
summon text_display 45.5 71 278.5 {text:'[{"text": "167.2  ", "color": "gold"}, {"text": "immersive/creosote", "color": "gray"}, {"text": "\\nZapf Kreosotöl ab", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template immersiveengineering:multiblocks/coke_oven 42 64 275 none
setblock 49 64 282 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:hammer",count:1},{Slot:1b,id:"immersiveengineering:manual",count:1}]}
setblock 51 64 285 minecraft:air
setblock 51 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "167.3"}','{"text": "immersive"}','{"text": "pump"}','{"text": ""}']}}
setblock 52 64 285 minecraft:air
setblock 52 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Pump das"}','{"text": "Kreosot ab"}','{"text": ""}','{"text": ""}']}}
summon text_display 55.5 71 278.5 {text:'[{"text": "167.3  ", "color": "gold"}, {"text": "immersive/pump", "color": "gray"}, {"text": "\\nPump das Kreosot ab", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 52 64 276 immersiveengineering:fluid_pump
setblock 54 64 276 immersiveengineering:fluid_pipe
