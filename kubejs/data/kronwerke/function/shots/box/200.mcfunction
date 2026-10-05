# 200 flux_networks/setup_mek, setup_reactor, whole_base
fill 184 63 376 223 63 389 minecraft:light_gray_concrete
fill 184 64 376 223 71 376 minecraft:light_gray_concrete
fill 184 64 376 184 71 389 minecraft:light_gray_concrete
setblock 185 64 388 minecraft:air
setblock 185 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "200.1"}','{"text": "flux_networks"}','{"text": "setup_mek"}','{"text": ""}']}}
setblock 186 64 388 minecraft:air
setblock 186 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a factory row"}','{"text": "with points, a"}','{"text": "Powah reactor"}','{"text": "with a plug, a"}']}}
setblock 187 64 388 minecraft:air
setblock 187 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "machine hall"}','{"text": "without cables"}','{"text": ""}','{"text": ""}']}}
summon text_display 191.5 71 381.5 {text:'[{"text": "200.1  ", "color": "gold"}, {"text": "flux_networks/setup_mek", "color": "gray"}, {"text": "\\nFabrikreihe von Mekanism", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 187 64 381 mekanism:creative_energy_cube
setblock 188 64 381 fluxnetworks:flux_plug
setblock 194 64 381 fluxnetworks:flux_point
setblock 195 64 381 mekanism:enrichment_chamber
setblock 197 64 385 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"fluxnetworks:flux_configurator",count:1},{Slot:1b,id:"fluxnetworks:flux_controller",count:1}]}
setblock 199 64 388 minecraft:air
setblock 199 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "200.2"}','{"text": "flux_networks"}','{"text": "setup_reactor"}','{"text": ""}']}}
setblock 200 64 388 minecraft:air
setblock 200 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Reaktorstrom in"}','{"text": "die Ferne"}','{"text": ""}','{"text": ""}']}}
summon text_display 203.5 71 381.5 {text:'[{"text": "200.2  ", "color": "gold"}, {"text": "flux_networks/setup_reactor", "color": "gray"}, {"text": "\\nReaktorstrom in die Ferne", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 202 64 380 204 67 382 powah:reactor_starter
setblock 205 64 381 fluxnetworks:flux_plug
setblock 209 64 388 minecraft:air
setblock 209 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "200.3"}','{"text": "flux_networks"}','{"text": "whole_base"}','{"text": ""}']}}
setblock 210 64 388 minecraft:air
setblock 210 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Versorge die"}','{"text": "ganze Basis"}','{"text": ""}','{"text": ""}']}}
summon text_display 215.5 71 381.5 {text:'[{"text": "200.3  ", "color": "gold"}, {"text": "flux_networks/whole_base", "color": "gray"}, {"text": "\\nVersorge die ganze Basis", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 211 64 381 mekanism:creative_energy_cube
setblock 212 64 381 fluxnetworks:flux_plug
setblock 218 64 381 fluxnetworks:flux_point
setblock 219 64 381 mekanism:enrichment_chamber
setblock 221 64 385 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"fluxnetworks:flux_configurator",count:1},{Slot:1b,id:"fluxnetworks:flux_controller",count:1}]}
