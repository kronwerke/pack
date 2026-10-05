# 198 flux_networks/first_link
fill 118 63 376 133 63 389 minecraft:light_gray_concrete
fill 118 64 376 133 71 376 minecraft:light_gray_concrete
fill 118 64 376 118 71 389 minecraft:light_gray_concrete
setblock 119 64 388 minecraft:air
setblock 119 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "198"}','{"text": "flux_networks"}','{"text": "first_link"}','{"text": ""}']}}
setblock 120 64 388 minecraft:air
setblock 120 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a generator"}','{"text": "with a plug and"}','{"text": "a machine with"}','{"text": "a point, no"}']}}
setblock 121 64 388 minecraft:air
setblock 121 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 125.5 71 381.5 {text:'[{"text": "198  ", "color": "gold"}, {"text": "flux_networks/first_link", "color": "gray"}, {"text": "\\nSchließe die erste Maschine an", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 121 64 381 mekanism:creative_energy_cube
setblock 122 64 381 fluxnetworks:flux_plug
setblock 128 64 381 fluxnetworks:flux_point
setblock 129 64 381 mekanism:enrichment_chamber
setblock 131 64 385 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"fluxnetworks:flux_configurator",count:1},{Slot:1b,id:"fluxnetworks:flux_controller",count:1}]}
