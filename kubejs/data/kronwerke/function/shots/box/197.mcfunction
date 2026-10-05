# 197 flux_networks/dust
fill 103 63 376 114 63 389 minecraft:light_gray_concrete
fill 103 64 376 114 71 376 minecraft:light_gray_concrete
fill 103 64 376 103 71 389 minecraft:light_gray_concrete
setblock 104 64 388 minecraft:air
setblock 104 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "197"}','{"text": "flux_networks"}','{"text": "dust"}','{"text": ""}']}}
setblock 105 64 388 minecraft:air
setblock 105 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the bedrock gap"}','{"text": "with redstone"}','{"text": "and obsidian,"}','{"text": "left-clicking"}']}}
setblock 106 64 388 minecraft:air
setblock 106 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the obsidian"}','{"text": "Redstone in die"}','{"text": "Lücke, Obsidian"}','{"text": "anklicken"}']}}
summon text_display 108.5 71 381.5 {text:'[{"text": "197  ", "color": "gold"}, {"text": "flux_networks/dust", "color": "gray"}, {"text": "\\nMach Flux-Staub", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 108 64 381 minecraft:bedrock
setblock 108 66 381 minecraft:obsidian
setblock 112 64 385 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:redstone",count:64}]}
