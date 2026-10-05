# 073 mekanism_advanced/turbine
fill 268 63 90 279 63 103 minecraft:light_gray_concrete
fill 268 64 90 279 71 90 minecraft:light_gray_concrete
fill 268 64 90 268 71 103 minecraft:light_gray_concrete
setblock 269 64 102 minecraft:air
setblock 269 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073"}','{"text": "mekanism_advanced"}','{"text": "turbine"}','{"text": ""}']}}
setblock 270 64 102 minecraft:air
setblock 270 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "turbine cutaway"}','{"text": "with rotors,"}','{"text": "dispersers,"}','{"text": "coils"}']}}
setblock 271 64 102 minecraft:air
setblock 271 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Rotorblätter"}','{"text": "auf die Rotoren"}','{"text": "setzen"}','{"text": ""}']}}
fill 271 64 93 275 72 97 mekanismgenerators:turbine_casing
fill 272 65 94 274 71 96 minecraft:air
fill 273 65 95 273 67 95 mekanismgenerators:turbine_rotor
setblock 273 68 95 mekanismgenerators:rotational_complex
fill 272 68 94 274 68 96 mekanism:pressure_disperser
setblock 273 68 95 mekanismgenerators:rotational_complex
fill 272 69 94 274 69 96 mekanismgenerators:electromagnetic_coil
setblock 273 69 95 mekanismgenerators:saturating_condenser
fill 271 65 97 275 71 97 mekanism:structural_glass
setblock 273 64 97 mekanismgenerators:turbine_valve
setblock 277 64 99 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"mekanismgenerators:turbine_blade",count:6}]}
