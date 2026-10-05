# 073 mekanism_advanced/turbine
fill 268 63 108 279 63 121 minecraft:light_gray_concrete
fill 268 64 108 279 71 108 minecraft:light_gray_concrete
fill 268 64 108 268 71 121 minecraft:light_gray_concrete
setblock 269 64 120 minecraft:air
setblock 269 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073"}','{"text": "mekanism_advanced"}','{"text": "turbine"}','{"text": ""}']}}
setblock 270 64 120 minecraft:air
setblock 270 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "turbine cutaway"}','{"text": "with rotors,"}','{"text": "dispersers,"}','{"text": "coils"}']}}
setblock 271 64 120 minecraft:air
setblock 271 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Rotorblätter"}','{"text": "auf die Rotoren"}','{"text": "setzen"}','{"text": ""}']}}
summon text_display 273.5 71 113.5 {text:'[{"text": "073  ", "color": "gold"}, {"text": "mekanism_advanced/turbine", "color": "gray"}, {"text": "\\nSetz die Industrieturbine zusammen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 271 64 111 275 72 115 mekanismgenerators:turbine_casing
fill 272 65 112 274 71 114 minecraft:air
fill 273 65 113 273 67 113 mekanismgenerators:turbine_rotor
setblock 273 68 113 mekanismgenerators:rotational_complex
fill 272 68 112 274 68 114 mekanism:pressure_disperser
setblock 273 68 113 mekanismgenerators:rotational_complex
fill 272 69 112 274 69 114 mekanismgenerators:electromagnetic_coil
setblock 273 69 113 mekanismgenerators:saturating_condenser
fill 271 65 115 275 71 115 mekanism:structural_glass
setblock 273 64 115 mekanismgenerators:turbine_valve
setblock 277 64 117 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"mekanismgenerators:turbine_blade",count:6}]}
