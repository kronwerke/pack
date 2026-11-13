# 056 mekanism_elite/fusion
#area 225 95 248 122
fill 225 64 95 248 93 122 minecraft:air
fill 225 60 95 248 62 122 minecraft:stone
fill 225 63 95 248 63 122 minecraft:light_gray_concrete
fill 229 64 101 248 81 101 minecraft:light_gray_concrete
fill 229 64 101 229 81 116 minecraft:light_gray_concrete
setblock 230 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "056"}','{"text": "mekanism_elite"}','{"text": "fusion"}','{"text": ""}']}}
setblock 231 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fusion reactor"}','{"text": "with laser and"}','{"text": "amplifier"}','{"text": ""}']}}
fill 243 64 101 243 81 116 minecraft:light_gray_concrete
setblock 232 64 107 mekanismgenerators:fusion_reactor_frame
setblock 232 65 106 mekanismgenerators:fusion_reactor_frame
setblock 232 65 107 mekanismgenerators:reactor_glass
setblock 232 65 108 mekanismgenerators:fusion_reactor_frame
setblock 232 66 105 mekanismgenerators:fusion_reactor_frame
setblock 232 66 106 mekanismgenerators:reactor_glass
setblock 232 66 107 mekanismgenerators:fusion_reactor_port[active=false]
setblock 232 66 108 mekanismgenerators:reactor_glass
setblock 232 66 109 mekanismgenerators:fusion_reactor_frame
setblock 232 67 106 mekanismgenerators:fusion_reactor_frame
setblock 232 67 107 mekanismgenerators:reactor_glass
setblock 232 67 108 mekanismgenerators:fusion_reactor_frame
setblock 232 68 107 mekanismgenerators:fusion_reactor_frame
setblock 233 64 106 mekanismgenerators:fusion_reactor_frame
setblock 233 64 107 mekanismgenerators:reactor_glass
setblock 233 64 108 mekanismgenerators:fusion_reactor_frame
setblock 233 65 105 mekanismgenerators:fusion_reactor_frame
setblock 233 65 109 mekanismgenerators:fusion_reactor_frame
setblock 233 66 105 mekanismgenerators:reactor_glass
setblock 233 66 109 mekanismgenerators:reactor_glass
setblock 233 67 105 mekanismgenerators:fusion_reactor_frame
setblock 233 67 109 mekanismgenerators:fusion_reactor_frame
setblock 233 68 106 mekanismgenerators:fusion_reactor_frame
setblock 233 68 107 mekanismgenerators:reactor_glass
setblock 233 68 108 mekanismgenerators:fusion_reactor_frame
setblock 234 64 105 mekanismgenerators:fusion_reactor_frame
setblock 234 64 106 mekanismgenerators:reactor_glass
setblock 234 64 107 mekanismgenerators:fusion_reactor_port[active=true]
setblock 234 64 108 mekanismgenerators:reactor_glass
setblock 234 64 109 mekanismgenerators:fusion_reactor_frame
setblock 234 65 105 mekanismgenerators:reactor_glass
setblock 234 65 109 mekanismgenerators:reactor_glass
setblock 234 66 105 mekanismgenerators:reactor_glass
setblock 234 66 109 mekanismgenerators:reactor_glass
setblock 234 67 105 mekanismgenerators:reactor_glass
setblock 234 67 109 mekanismgenerators:reactor_glass
setblock 234 68 105 mekanismgenerators:fusion_reactor_frame
setblock 234 68 106 mekanismgenerators:reactor_glass
setblock 234 68 107 mekanismgenerators:fusion_reactor_controller[active=false]
setblock 234 68 108 mekanismgenerators:reactor_glass
setblock 234 68 109 mekanismgenerators:fusion_reactor_frame
setblock 235 64 106 mekanismgenerators:fusion_reactor_frame
setblock 235 64 107 mekanismgenerators:reactor_glass
setblock 235 64 108 mekanismgenerators:fusion_reactor_frame
setblock 235 65 105 mekanismgenerators:fusion_reactor_frame
setblock 235 65 109 mekanismgenerators:fusion_reactor_frame
setblock 235 66 105 mekanismgenerators:reactor_glass
setblock 235 66 109 mekanismgenerators:reactor_glass
setblock 235 67 105 mekanismgenerators:fusion_reactor_frame
setblock 235 67 109 mekanismgenerators:fusion_reactor_frame
setblock 235 68 106 mekanismgenerators:fusion_reactor_frame
setblock 235 68 107 mekanismgenerators:reactor_glass
setblock 235 68 108 mekanismgenerators:fusion_reactor_frame
setblock 236 64 107 mekanismgenerators:fusion_reactor_frame
setblock 236 65 106 mekanismgenerators:fusion_reactor_frame
setblock 236 65 107 mekanismgenerators:reactor_glass
setblock 236 65 108 mekanismgenerators:fusion_reactor_frame
setblock 236 66 105 mekanismgenerators:fusion_reactor_frame
setblock 236 66 106 mekanismgenerators:reactor_glass
setblock 236 66 107 mekanismgenerators:laser_focus_matrix
setblock 236 66 108 mekanismgenerators:reactor_glass
setblock 236 66 109 mekanismgenerators:fusion_reactor_frame
setblock 236 67 106 mekanismgenerators:fusion_reactor_frame
setblock 236 67 107 mekanismgenerators:reactor_glass
setblock 236 67 108 mekanismgenerators:fusion_reactor_frame
setblock 236 68 107 mekanismgenerators:fusion_reactor_frame
fill 238 64 107 238 65 107 mekanism:steel_casing
setblock 238 66 107 mekanism:laser_amplifier[facing=west]
fill 240 64 107 240 65 107 mekanism:steel_casing
setblock 240 66 107 mekanism:laser[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
